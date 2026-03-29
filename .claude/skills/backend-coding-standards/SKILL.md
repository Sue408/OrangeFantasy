---
name: backend-coding-standards
description: FastAPI + Python后端开发规范。用于编写符合项目风格的后端代码，包括模型定义、API路由、数据验证、错误处理和依赖注入。
---

# 后端代码开发规范

## 文件组织

- **models/**: SQLAlchemy ORM模型，使用Mapped类型注解
- **schemas/**: Pydantic验证模型，用于API输入/输出
- **api/**: 路由定义，按功能模块分离（auth.py, user.py等）
- **utils/**: 工具函数（JWT、密码哈希等）
- **db/**: 数据库连接和会话管理

## 模型定义

使用Mapped类型注解，明确字段类型：

```python
id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
avatar: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

# 关系定义
novels = relationship("Novel", back_populates="user")
```

## API路由

- 使用APIRouter，通过app.include_router()注册
- 统一前缀 `/api/{module}`
- 明确指定status_code和response_model
- 在responses参数中文档化错误响应
- 使用Depends()进行依赖注入

```python
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
    responses={"400": {"description": "邮箱或账号已被注册"}}
)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """接口文档"""
```

## 数据验证

- 所有API输入使用Pydantic schemas
- 在路由处理前进行验证
- 返回标准HTTP状态码和结构化错误响应

## 错误处理

```python
if not user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="账号或密码错误"
    )
```

## 命名约定

- 模型类：PascalCase（User, Novel, Chapter）
- 数据库表：snake_case（users, novels, chapters）
- 函数/方法：snake_case
- 常量：UPPER_SNAKE_CASE
- 私有属性：_leading_underscore

## 类型注解

- 使用Python 3.10+的联合类型语法：`str | None`
- 函数参数和返回值必须有类型注解
- 使用Mapped进行ORM字段类型注解