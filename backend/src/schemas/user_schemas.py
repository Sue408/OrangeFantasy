"""
user API相关Pydantic模型定义
"""
from datetime import datetime
from pydantic import BaseModel

class UserInfoResponse(BaseModel):
    """用户信息响应"""
    email: str
    username: str
    nickname: str | None = None
    avatar: str | None = None
    created_at: datetime | None = None

class UpdateUserInfoRequest(BaseModel):
    """更新用户信息请求"""
    nickname: str | None = None
    avatar: str | None = None
