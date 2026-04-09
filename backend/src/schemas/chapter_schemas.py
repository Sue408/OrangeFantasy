"""
chapter API相关Pydantic模型定义
"""
from pydantic import BaseModel
from datetime import datetime

class ChapterResponse(BaseModel):
    """chapter响应模型"""
    id: int
    step: str | None
    number: int
    name: str
    content: str
    created_at: datetime
    updated_at: datetime

class UpdateChapterRequest(BaseModel):
    """更新chapter请求模型"""
    name: str | None = None
    content: str | None = None