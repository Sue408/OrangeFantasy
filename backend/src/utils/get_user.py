"""
get_user依赖注入方法
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .jwt_manager import JWTManager
from ..db import get_db
from ..models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user_and_db(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
) -> tuple[User, Session]:
    """获取用户对象与数据库对话 (确保数据库session一致性)"""
    # 解析并验证token
    user_id, _ = JWTManager.verify_token(token)

    # 查询用户并验证用户是否有效
    user: User | None = db.query(User).get(user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="用户不存在或已被禁用"
        )
    return user, db




