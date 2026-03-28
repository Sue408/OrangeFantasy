# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

**OrangeFantasy** 是一个全托管式AI小说创作平台，采用"AI为主，用户为辅"的创作模式。核心目标是通过自动上下文管理、智能规划与记忆保持，降低小说创作门槛，保障作品连贯性。

**技术栈**：
- 后端：FastAPI (Python 3.10+) + PostgreSQL/SQLite + OpenAI SDK
- 前端：Vue3 + TypeScript + Pinia + Axios
- 环境管理：后端用uv，前端用npm

## 核心概念

### 作品结构
- **作品**：基本创作单位，包含完整故事内容、设定资料与创作历史
- **世界书**：作品的单一可信源，记录角色档案、世界设定、时间线、动态标签
- **大纲**：AI生成的动态创作导航图，实现"AI主动规划，用户轻量确认"
- **章节**：记录创作内容的最小单位
  - 短篇：单章节储存
  - 中长篇：卷-章节的层次化设计

### 创作模式
- **短篇模式**：快速、完整的创作流程，无章节管理
- **中长篇模式**：章节化、迭代式的创作流程，支持长期投入

## 项目结构

```
backend/
├── src/
│   ├── ai/           # AI业务模块
│   ├── api/          # API路由 (auth.py, user.py等)
│   ├── db/           # 数据库初始化
│   ├── models/       # SQLAlchemy ORM模型
│   ├── schemas/      # Pydantic验证模型
│   ├── utils/        # 工具函数 (JWT、密码哈希等)
│   └── config.py     # 核心配置类
└── main.py           # 程序入口

frontend/
├── src/
│   ├── components/   # Vue组件 (common/, home/, working/, creation/)
│   ├── pages/        # 页面 (Home.vue, Auth.vue, home/Working.vue等)
│   ├── router/       # 路由配置
│   ├── stores/       # Pinia状态管理 (userStore.ts)
│   ├── services/     # 后端API对接与封装
│   ├── utils/        # 工具函数
│   ├── http.ts       # Axios实例配置
│   ├── config.ts     # 前端配置
│   └── App.vue       # 根组件
└── public/           # 静态资源
```

## 后端依赖链

```
config.py (读取.env)
  ↓
db/database.py (数据库连接、Engine、SessionFactory、Base)
  ↓
models/ (ORM模型定义)
  ↓
schemas/ (Pydantic模型) + utils/ + ai/
  ↓
api/ (路由定义)
  ↓
main.py (启动)
```

## 数据库设计

### Users表
- id (主键)
- nickname (昵称/笔名)
- avatar (头像URL/Base64)
- phone (手机号，唯一)
- password_hash (密码哈希)
- 关系：一对多关联Novels

### Novels表
- id (主键)
- user_id (外键)
- name (作品名称)
- type (枚举："short"/"long")
- 关系：多对一关联Users，一对多关联Chapters

### Chapters表
- id (主键)
- novel_id (外键)
- name (章节名称)
- number (章节序号)
- step (卷名称，可空)
- content (文本内容，<30000字)
- 关系：多对一关联Novels

## 编码风格与偏好

### 前端
- **组件组织**：按功能域分组 (common/, home/, working/, creation/)
- **状态管理**：使用Pinia的组合式API风格 (`defineStore` + `ref/computed`)
- **HTTP请求**：通过 `http.ts` 的泛型包装器，支持 `get<T>/post<T>/put<T>/delete<T>`
- **路由**：使用动态导入 (`() => import(...)`) 实现代码分割
- **样式**：
  - 全局重置：`* { margin: 0; padding: 0; box-sizing: border-box; }`
  - 通用卡片样式：`.card { border-radius: 24px; background: rgba(99, 106, 108, 0.3); box-shadow: 1px 1px 1px rgba(255, 255, 255, 0.2); }`
  - 深色主题：背景 `#2f2f2f`，使用半透明白色阴影
  - 自定义字体：`Crystal-Light-2.ttf` 用于标题

### 后端
- **配置管理**：使用Pydantic的 `BaseSettings` 读取环境变量
- **数据验证**：所有API输入/输出使用Pydantic schemas
- **路由组织**：按功能模块分离 (auth.py, user.py等)，通过 `app.include_router()` 注册，统一前缀 `/api/{module}`
- **依赖注入**：使用FastAPI的 `Depends()` 注入数据库会话、认证信息等
- **错误处理**：返回标准HTTP状态码与结构化错误响应

## 开发命令

### 后端
```bash
# 安装依赖
cd backend
uv sync

# 运行开发服务器
uv run main.py

# 或使用uvicorn直接运行
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### 前端
```bash
# 安装依赖
cd frontend
npm install

# 开发服务器 (Vite)
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

## 关键实现细节

### 认证流程
- 使用pyjwt + OAuth2
- 密码通过 `utils/password_hasher.py` 进行哈希
- pyjwt管理由 `utils/jwt_manager.py` 负责
- 前端通过Pinia的userStore管理认证状态

### WebSocket支持
- 后端：FastAPI原生WebSocket支持
- 前端：原生WebSocket API
- 用途：流式生成AI内容、实时协作

### 数据库会话
- 后端通过 `utils/get_db.py` 提供数据库会话依赖
- 使用SQLAlchemy ORM，支持PostgreSQL (生产) / SQLite (开发)

## 重要约定

1. **环境变量**：后端 `.env` 由 `config.py` 读取，前端 `.env` 由 `config.ts` 读取
2. **API前缀**：所有API路由统一前缀 `/api`
3. **响应格式**：遵循RESTful规范，使用标准HTTP状态码
4. **类型安全**：前端使用TypeScript，后端使用Pydantic进行类型验证
5. **代码分割**：前端路由使用动态导入，减少初始包体积
