"""
数据库连接与get_db方法定义
"""
from typing import Any, Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from ..config import config

# 初始化数据库engine对象
engine = create_engine(
    f"{config.database.name}:///{config.database.host}",
    connect_args={"check_same_thread": False} if config.database.name == "sqlite" else {}
)
# 初始化会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 初始化ORM基类
Base = declarative_base()

# 获取数据库会话方法
def get_db() -> Generator[Session, Any, None]:
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
