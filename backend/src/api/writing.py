"""
writing API定义
"""
from fastapi import APIRouter, Depends, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import asyncio
import json

from ..models import User
from ..utils import get_user_and_db

# ========= 初始化router对象 =========
router = APIRouter()

# ========= 定义API接口 =========
@router.post(
    "/{novel_id}",
    status_code=status.HTTP_200_OK,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
async def writing(
        novel_id: int,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    创作主接口 (SSE)
    """
    _, _ = user_and_db

    async def event_generator():
        """测试生成器用例"""
        for _str in "你好，我叫doro！":
            data = json.dumps({"content": _str})
            yield f"data: {data}\n\n"
            await asyncio.sleep(0.1)

        yield "event: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )