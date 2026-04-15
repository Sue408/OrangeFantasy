"""
核心配置类定义

- debug: 调试模式
- host: 启动地址
- port: 端口
- database
    - host: 数据库地址
    - name: 数据库名称
- security
    - key: 密钥
    - algorithm: 加密算法
    - access_token_expires_minutes: access token有效时长 (分钟)
    - refresh_token_expires_days: refresh token有效时长 (天)
"""
from pydantic_settings import BaseSettings

class DatabaseSetting(BaseSettings):
    """"数据库配置"""
    host: str = '.test.db'
    name: str = 'sqlite'

class SecuritySetting(BaseSettings):
    """安全验证配置"""
    key: str = "11111111111111111111111111111111"
    algorithm: str = "HS256"
    access_token_expires_minutes: int = 30
    refresh_token_expires_days: int = 7

class Setting(BaseSettings):
    """核心配置类定义"""
    # ========= 后端服务配置 =========
    debug: bool = True
    host: str = "localhost"
    port: int = 8080

    # ========= 数据库配置 =========
    database: DatabaseSetting = DatabaseSetting()

    # ========= 安全验证配置 =========
    security: SecuritySetting = SecuritySetting()

    class Config:
        """读取配置"""
        env_file = [".env.local", ".env"]
        env_file_encoding = 'utf-8'

config: Setting = Setting()  # 实例化配置对象