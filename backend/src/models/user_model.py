"""
Users表定义
"""
from sqlalchemy import Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime, timezone

from ..db import Base

class User(Base):
    """用户表定义"""
    # 表名
    __tablename__ = "users"

    # ========= 字段定义 =========
    # 主键
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # 昵称
    nickname: Mapped[str] = mapped_column(String(255), nullable=True, default=None)
    # 账号
    username: Mapped[str] = mapped_column(String(255), unique=True)
    # 邮箱地址
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    # 密码哈希
    hashed_password: Mapped[str] = mapped_column(String(50))
    # 头像
    avatar: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
    # 是否激活
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    # 创建时间
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    # 更新时间
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    # ========= 关系定义 =========
    novels = relationship("Novel", back_populates="user")