"""
novel API设计
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import desc
from sqlalchemy.orm import Session, subqueryload

from ..models import User, Novel
from ..utils import get_user_and_db
from ..schemas.novel_schemas import *

# ========= 初始化router对象 =========
router = APIRouter()

# ========= 定义API接口 =========
@router.get(
    "",
    response_model=NovelsResponse,
    status_code=status.HTTP_200_OK,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
async def get_novels(user_and_db: tuple[User, Session] = Depends(get_user_and_db)):
    """获取用户的所有novel信息"""
    user, db = user_and_db

    # 查询user的所有novel (预加载chapters)
    novels = db.query(Novel).options(
        subqueryload(Novel.chapters)
    ).filter_by(user_id=user.id).order_by(desc(Novel.updated_at)).all()

    # 构造响应模型
    novels_list: list[NovelMeta] = []
    for novel in novels:
        chapters_list: list[ChapterForNovelMeta] = [
            ChapterForNovelMeta(
                id=chapter.id,
                name=chapter.name,
                number=chapter.number,
                step=chapter.step,
                created_at=chapter.create_at,
                updated_at=chapter.update_at
            ) for chapter in novel.chapters
        ]
        # 按照章节序号进行排序
        chapters_list.sort(key=lambda chapter: chapter.number)
        # 构造novel meta对象
        novels_list.append(NovelMeta(
            id=novel.id, # noqa
            name=novel.name, # noqa
            cover=novel.cover, # noqa
            type=novel.type, # noqa
            chapters=chapters_list,
            created_at=novel.created_at, # noqa
            updated_at=novel.updated_at # noqa
        ))

    return NovelsResponse(novels=novels_list)

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用"}
    }
)
async def create_novel(
        request: CreateNovelRequest,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    创建novel接口

    - name: novel名称
    - cover?: novel封面 (URL/Base64)
    - type: novel类型 ('short'/'long')
    """
    user, db = user_and_db

    # 创建novel对象
    novel = Novel(
        user_id=user.id,
        name=request.name,
        cover=request.cover,
        type=request.type
    )

    # 提交数据库操作
    db.add(novel)
    db.commit()
    db.refresh(novel)

@router.put(
    "/{novel_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/作品不存在"}
    }
)
async def update_novel(
        request: UpdateNovelRequest,
        novel_id: int,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    更新novel设定

    - novel_id: novel id
    - name?: 名称
    - cover?: 封面 (URL/Base64)
    """
    _, db = user_and_db

    # 查询novel
    novel: Novel | None = db.query(Novel).get(novel_id)
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="作品不存在"
        )

    # 按需求修改novel的数据
    if request.name:
        novel.name = request.name
    if request.cover:
        novel.cover = request.cover

    # 提交数据库操作
    db.add(novel)
    db.commit()
    db.refresh(novel)

@router.delete(
    "/{novel_id}",
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        "401": {"description": "无效的token"},
        "404": {"description": "用户不存在或已被禁用/作品不存在"}
    }
)
async def delete_novel(
        novel_id: int,
        user_and_db: tuple[User, Session] = Depends(get_user_and_db)
    ):
    """
    删除指定的novel

    - novel_id: novel id
    """
    _, db = user_and_db

    # 查询novel
    novel: Novel | None = db.query(Novel).get(novel_id)
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="作品不存在"
        )

    # 删除指定novel并提交数据库操作
    db.delete(novel)
    db.commit()
    db.refresh(novel)
