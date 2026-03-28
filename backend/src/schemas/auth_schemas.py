"""
auth API相关Pydantic模型定义
"""
from pydantic import BaseModel

class RegisterRequest(BaseModel):
    """注册请求"""
    email: str
    username: str
    password: str

class TokenResponse(BaseModel):
    """token响应"""
    access_token: str
    refresh_token: str

class LoginRequest(BaseModel):
    """登录请求"""
    username: str
    password: str

class RefreshRequest(BaseModel):
    """刷新请求"""
    refresh_token: str

class RefreshResponse(BaseModel):
    """刷新响应"""
    access_token: str