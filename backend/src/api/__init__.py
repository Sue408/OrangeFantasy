"""
API定义与导出
- auth_router: auth相关路由
"""
from .auth import router as auth_router
from .user import router as user_router
from .novel import router as novel_router
from .chapter import router as chapter_router

__all__ = [
    "auth_router",
    "user_router",
    "novel_router",
    "chapter_router"
]