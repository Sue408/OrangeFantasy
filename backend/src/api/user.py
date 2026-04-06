"""
user API定义
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..utils import get_user_and_db
from ..models import User
from ..schemas.user_schemas import *

# ========= 初始化router对象 =========
router = APIRouter()

# ========= 定义API接口 =========
@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=UserInfoResponse,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
def get_user_info(
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    获取用户信息接口
    """
    # 解包对象并返回
    user, _ = user_and_db
    return UserInfoResponse(
        email=user.email,
        username=user.username,
        nickname=user.nickname,
        avatar=user.avatar,
        created_at=user.created_at
    )

@router.post(
    "",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UserInfoResponse,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
def update_user_info(
        request: UpdateUserInfoRequest,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    更新用户信息接口

    - nickname?: 昵称
    - avatar?: 头像 (URL/Base64)
    """
    user, db = user_and_db

    # 更新用户信息
    if request.nickname:
        user.nickname = request.nickname
    if request.avatar:
        user.avatar = request.avatar

    # 提交数据库操作
    db.add(user)
    db.commit()
    db.refresh(user)

    return UserInfoResponse(
        email=user.email,
        username=user.username,
        nickname=user.nickname,
        avatar=user.avatar,
        created_at=user.created_at
    )