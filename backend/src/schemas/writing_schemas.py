"""
writing API相关Pydantic模型定义
"""
from pydantic import BaseModel

class WritingRequest(BaseModel):
    """writing请求模型"""
    msg: str