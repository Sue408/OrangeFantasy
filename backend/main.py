"""
程序入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import config, Base, engine
from src import auth_router, user_router, novel_router, chapter_router

# ========= 初始化数据库 =========
Base.metadata.create_all(bind=engine)

# ========= 实例化App对象 =========
app = FastAPI(
    title="OrangeFantasy API",
    version="1.0"
)

# ========= 配置CORS中间件 =========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========= 健康检查端点 =========
@app.get("/")
async def health_check():
    """健康检查"""
    return {"status": "connect success"}

# ========= 注册子路由对象 =========
# 1. auth router
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["auth"]
)

# 2. user router
app.include_router(
    user_router,
    prefix="/api/user",
    tags=["user"]
)

# 3. novel router
app.include_router(
    novel_router,
    prefix="/api/novel",
    tags=["novel"]
)

# 4. chapter router
app.include_router(
    chapter_router,
    prefix="/api/chapter",
    tags=["chapter"]
)

# ========= 程序入口 =========
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=config.host,
        port=config.port,
        reload=config.debug
    )