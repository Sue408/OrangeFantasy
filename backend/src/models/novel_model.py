"""
Novels表定义
"""
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timezone

from ..db import Base

class Novel(Base):
    """作品表定义"""
    # 表名
    __tablename__ = "novels"

    # ========= 字段定义 =========
    # 主键
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # 外键: 绑定User主键
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    # 作品名称
    name: Mapped[str] = mapped_column(String(255), index=True)
    # 封面
    cover: Mapped[str | None] = mapped_column(Text)
    # 作品类型: 枚举 ("short"/"long")
    type: Mapped[str] = mapped_column(String(50))
    # chapter计数器
    chapter_counter: Mapped[int] = mapped_column(Integer, default=0)
    # 创建时间
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    # 更新时间
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    # ========= 关系定义 =========
    user = relationship("User", back_populates="novels")
    chapters = relationship("Chapter", back_populates="novel")