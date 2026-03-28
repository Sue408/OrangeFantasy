"""
password hasher定义
"""
import bcrypt

class PasswordHasher:
    """密码哈希管理"""
    @staticmethod
    def hash(password: str) -> str:
        """密码哈希"""
        return bcrypt.hashpw(
            password.encode(),
            salt=bcrypt.gensalt()
        ).decode()

    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        """验证密码"""
        return bcrypt.checkpw(
            password.encode(),
            hashed_password.encode())