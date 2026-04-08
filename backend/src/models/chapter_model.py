"""
Chapter表定义
"""
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timezone

from ..db import Base

class Chapter(Base):
    """章节表定义"""
    # 表名
    __tablename__ = "chapters"

    # ========= 字段定义 =========
    # 主键
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # 外键: 绑定Novel主键
    novel_id: Mapped[int] = mapped_column(Integer, ForeignKey("novels.id"))
    # 章节名称
    name: Mapped[str] = mapped_column(String(255))
    # 章节序号
    number: Mapped[int] = mapped_column(Integer)
    # 章节所属卷名
    step: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    # 章节内容
    content: Mapped[str] = mapped_column(Text, default="")
    # 创建时间
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    # 更新时间
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    # ========= 关系定义 =========
    novel = relationship("Novel", back_populates="chapters")