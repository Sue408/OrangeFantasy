"""
novel API相关Pydantic模型定义
"""
from pydantic import BaseModel
from datetime import datetime

class CreateNovelRequest(BaseModel):
    """创建novel请求模型"""
    name: str
    cover: str | None = None
    type: str

class ChapterForNovelMeta(BaseModel):
    """chapter对novel响应的单元模型"""
    id: int
    name: str
    number: int
    step: str | None = None
    created_at: datetime
    updated_at: datetime

class NovelMeta(BaseModel):
    """novel单元模型"""
    id: int
    name: str
    cover: str | None = None
    type: str
    chapters: list[ChapterForNovelMeta]
    created_at: datetime
    updated_at: datetime

class NovelsResponse(BaseModel):
    """novels响应模型"""
    novels: list[NovelMeta]

class UpdateNovelRequest(BaseModel):
    """更新novel请求模型"""
    name: str | None = None
    cover: str | None = None