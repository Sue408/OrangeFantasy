"""
auth API定义
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from ..utils import JWTManager, PasswordHasher
from ..models import User
from ..schemas.auth_schemas import *

# ========= 初始化router对象 =========
router = APIRouter()

# ========= 定义API接口 =========
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
    responses={
        "400": {"description": "邮箱或账号已被注册/密码过短" },
    }
)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    注册接口

    - email: 邮箱
    - username: 账号
    - password: 密码 (至少6位)
    """
    # 检查电话号码是否已经被注册
    existing_user = db.query(User).filter(
        (User.email == request.email) | (User.username == request.username)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="邮箱或账号已被注册"
        )

    # 检查密码是否合法
    if len(request.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="密码长度不得少于6位"
        )

    # 创建新用户并写入数据库
    user: User = User(
        username=request.username,
        email=request.email,
        hashed_password=PasswordHasher.hash(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # 生成token并响应
    access_token: str = JWTManager.create_access_token(user.id)
    refresh_token: str = JWTManager.create_refresh_token(user.id)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
    responses={
        "404": {"description": "账户或密码错误"}
    }
)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    登录接口

    - username: 账户
    - password: 密码
    """
    # 检查用户是否存在
    user: User | None = db.query(User).filter(User.username == request.username).first()
    if not user or not PasswordHasher.verify(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="账号或密码错误"
        )

    # 生成token并响应
    access_token: str = JWTManager.create_access_token(user.id)
    refresh_token: str = JWTManager.create_refresh_token(user.id)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
    response_model=RefreshResponse,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
def refresh(request: RefreshRequest, db: Session = Depends(get_db)):
    """
    token刷新方法

    - refresh_token: refresh token
    """
    # 验证token
    user_id, token_type = JWTManager.verify_token(request.refresh_token)

    # 检查token type
    if token_type != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的token"
        )

    # 检查user id
    user: User | None = db.query(User).filter(User.id == user_id).first()
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在或已被禁用"
        )

    # 生成access token并响应
    access_token: str = JWTManager.create_access_token(user.id)
    return RefreshResponse(access_token=access_token)

