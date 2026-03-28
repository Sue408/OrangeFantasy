"""
API定义与导出
- auth_router: auth相关路由
"""
from .auth import router as auth_router

__all__ = [
    "auth_router"
]