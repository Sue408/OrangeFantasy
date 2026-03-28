// auth API相关typescript类型定义

// 注册请求
export interface RegisterRequest {
    email: string
    username: string
    password: string
}

// token响应
export interface TokenResponse {
    access_token: string
    refresh_token: string
}

// 登录请求
export interface LoginRequest {
    username: string
    password: string
}

// 刷新token请求
export interface RefreshRequest {
    refresh_token: string
}

// 刷新token响应
export interface RefreshResponse {
    access_token: string
}