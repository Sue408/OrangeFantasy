"""
chapter API定义
"""
from datetime import timezone
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from .. import Novel
from ..models import User, Chapter
from ..schemas.chapter_schemas import *
from ..utils import get_user_and_db

# ========= 初始化router对象 =========
router = APIRouter()

# ========= 定义API接口 =========
@router.get(
    "/{chapter_id}",
    response_model=ChapterResponse,
    status_code=status.HTTP_200_OK,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/章节不存在"}
    }
)
async def get_chapter(
        chapter_id: int,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    获取章节内容接口
    """
    _, db = user_and_db

    # 查询对应章节数据
    chapter: Chapter | None = db.query(Chapter).get(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="章节不存在"
        )

    return ChapterResponse(
        id=chapter.id,
        step=chapter.step,
        number=chapter.number,
        name=chapter.name,
        content=chapter.content,
        created_at=chapter.created_at,
        updated_at=chapter.updated_at
    )

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/作品不存在"}
    }
)
async def create_chapter(
        novel_id: int = Query(..., description="novel id"),
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    新建章节接口
    """
    _, db = user_and_db

    # 查询已存在章节数量
    novel: Novel | None = db.query(Novel).get(novel_id)
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="作品不存在"
        )
    lens: int = len(novel.chapters)

    # 新建chapter ORM对象
    chapter = Chapter(
        novel_id=novel_id,
        name="未命名",
        number=lens + 1
    )

    # 提交数据库操作
    db.add(chapter)
    db.commit()
    db.refresh(chapter)

@router.delete(
    "/{chapter_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/章节不存在"}
    }
)
async def delete_chapter(
        chapter_id: int,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    删除章节接口
    """
    _, db = user_and_db

    # 查询chapter ORM对象
    chapter: Chapter | None = db.query(Chapter).get(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="章节不存在"
        )

    db.delete(chapter)
    db.commit()

@router.put(
    "/{chapter_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/作品不存在"}
    }
)
async def update_chapter(
        chapter_id: int,
        request: UpdateChapterRequest,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    更新章节信息接口

    - name?: 章节名称
    - content?: 章节内容
    """
    _, db = user_and_db

    # 查询chapter ORM对象
    chapter: Chapter | None = db.query(Chapter).get(chapter_id)
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="章节不存在"
        )

    # 按需更新chapter内容
    if request.name:
        chapter.name = request.name
    if request.content:
        chapter.content = request.content

    # 更新updated_at:
    chapter.updated_at = datetime.now(timezone.utc)

    # 提交数据库操作
    db.add(chapter)
    db.commit()
    db.refresh(chapter)

