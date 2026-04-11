"""
chapter API定义
"""
from datetime import timezone
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import delete
from sqlalchemy.orm import Session, subqueryload

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
    获取特定章节接口
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

@router.get(
    "",
    response_model=ChaptersResponse,
    status_code=status.HTTP_200_OK,
responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/作品不存在"}
    }
)
async def get_chapters(
        novel_id: int = Query(..., description="novel id"),
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    获取指定作品所有章节的简略数据接口
    """
    _, db = user_and_db

    # 查询作品 (预加载chapters)
    novel: Novel | None = db.query(Novel).options(
        subqueryload(Novel.chapters)
    ).get(novel_id)
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="作品不存在"
        )

    # 封装返回对象
    return ChaptersResponse(
        chapters=[
            ChapterForNovelMeta(
                id=chapter.id,
                name=chapter.name,
                number=chapter.number,
                step=chapter.step,
                created_at=chapter.created_at,
                updated_at=chapter.updated_at
            ) for chapter in novel.chapters
        ]
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

    # 查询作品与已经存在的章节数量
    novel: Novel | None = db.query(Novel).get(novel_id)
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="作品不存在"
        )


    # 新建chapter ORM对象
    chapter = Chapter(
        novel_id=novel_id,
        name="未命名",
        number=novel.chapter_counter + 1
    )

    # 更新novel计数器
    novel.chapter_counter += 1

    # 提交数据库操作
    db.add(novel)
    db.add(chapter)
    db.commit()
    db.refresh(chapter)

@router.delete(
    "",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/章节不存在"}
    }
)
async def delete_chapter(
        chapters_id: str = Query(..., description="逗号分隔的chapter id列表"),
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    删除章节接口

    - chapters: 要删除的chapter id数组
    """
    _, db = user_and_db

    # 将chapters转换为list对象
    chapters_id = [int(_id.strip()) for _id in chapters_id.split(",") if _id.strip()]

    # 构建删除语句
    stmt = delete(Chapter).where(Chapter.id.in_(chapters_id))

    # 执行数据库操作并提交
    db.execute(stmt)
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

