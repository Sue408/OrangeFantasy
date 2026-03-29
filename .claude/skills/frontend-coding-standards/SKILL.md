---
name: frontend-coding-standards
description: Vue3 + TypeScript前端开发规范。用于编写符合项目风格的前端代码，包括组件组织、状态管理、HTTP请求、路由配置和样式规范。
---

# 前端代码开发规范

## 文件组织

- **components/**: Vue组件，按功能域分组（common/, home/, working/, creation/）
- **pages/**: 页面级组件
- **stores/**: Pinia状态管理
- **services/**: 后端API对接与封装
- **router/**: 路由配置
- **types/**: TypeScript类型定义
- **http.ts**: Axios实例配置和拦截器

## 状态管理（Pinia）

使用组合式API风格，结构如下：

```typescript
const useUserStore = defineStore('user', () => {
    // 基础属性
    const token = ref<{ accessToken: string | null, refreshToken: string | null }>({
        accessToken: null,
        refreshToken: null
    })

    // 计算属性
    const isLogged = computed(() => !!token.value)

    // 方法
    const login = async (username: string, password: string) => {
        // 实现
    }

    return { token, isLogged, login }
})
```

## HTTP请求

### Axios配置
- baseURL: `/api`
- timeout: 15000ms
- 请求拦截器：自动添加Authorization header
- 响应拦截器：401自动刷新token并重试

### 泛型包装器
```typescript
const http = {
    async get<T>(url: string, config?: AxiosRequestConfig): Promise<T>
    async post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>
    async put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T>
    async delete<T>(url: string, config?: AxiosRequestConfig): Promise<T>
}
```

## 路由配置

使用动态导入实现代码分割：`() => import(...)`

## 样式规范

### 全局重置
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
```

### 通用卡片样式
```css
.card {
    border-radius: 24px;
    background: rgba(99, 106, 108, 0.3);
    box-shadow: 1px 1px 1px rgba(255, 255, 255, 0.2);
}
```

### 主题配色
- 背景色：#2f2f2f（深色主题）
- 阴影：半透明白色 rgba(255, 255, 255, 0.2)
- 自定义字体：Crystal-Light-2.ttf（标题）

## 命名约定

- 组件：PascalCase（UserProfile.vue）
- 函数/方法：camelCase
- 常量：UPPER_SNAKE_CASE
- 私有属性：_leading_underscore

## TypeScript

- 所有变量和函数参数必须有类型注解
- 使用联合类型：`string | null`
- 为API响应定义类型接口