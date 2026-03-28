"""
JWT Manager定义

- create_access_token: 创建access token
- create_refresh_token: 创建refresh token
- verify_token: 验证token
"""
from typing import Literal
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
import jwt

from ..config import config

class JWTManager:
    """JWT Manager定义"""
    @staticmethod
    def _create_token(
            user_id: int,
            token_type: Literal['access', 'refresh'],
            expires_delta: timedelta
    ) -> str:
        """统一的token创建方法"""
        # 计算失效时间
        expire: datetime = datetime.now(timezone.utc) + expires_delta

        return jwt.encode(
            {
                "sub": str(user_id),
                "exp": expire,
                "type": token_type,
                "iat": datetime.now(timezone.utc)
            },
            key=config.security.key,
            algorithm=config.security.algorithm
        )

    @staticmethod
    def create_access_token(user_id: int) -> str:
        """创建access token"""
        return JWTManager._create_token(
            user_id=user_id,
            token_type='access',
            expires_delta=timedelta(minutes=config.security.access_token_expires_minutes)
        )

    @staticmethod
    def create_refresh_token(user_id: int) -> str:
        """创建refresh token"""
        return JWTManager._create_token(
            user_id=user_id,
            token_type='refresh',
            expires_delta=timedelta(days=config.security.refresh_token_expires_days)
        )

    @staticmethod
    def verify_token(token: str) -> tuple[int, str]:
        """验证token有效性并返回user id、token type"""
        try:
            # 解码获取payload
            payload = jwt.decode(
                token,
                key=config.security.key,
                algorithms=[config.security.algorithm]
            )

            # 读取user id并验证
            return int(payload['sub']), payload['type']

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="token已过期",
                headers={"WWW-Authenticate": "Bearer"}
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="无效的token",
                headers={"WWW-Authenticate": "Bearer"}
            )
