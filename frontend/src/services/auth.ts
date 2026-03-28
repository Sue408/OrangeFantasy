// auth API相关接口调用
import http from '@/http.ts'
import config from '@/config.ts'
import type { 
    RegisterRequest,
    TokenResponse,
    LoginRequest,
    RefreshRequest,
    RefreshResponse } from '@/types/authTypes'

/**
 * 注册接口
 */
export const registerAPI = async (data: RegisterRequest): Promise<TokenResponse> => {
    return http.post<TokenResponse>(`${config.baseUrl}/auth/register`, data)
}

/**
 * 登录接口
 */
export const LoginAPI = async (data: LoginRequest): Promise<TokenResponse> => {
    return http.post<TokenResponse>(`${config.baseUrl}/auth/login`, data)
}

/**
 * 刷新token接口
 */
export const refreshAPI = async (data: RefreshRequest): Promise<RefreshResponse> => {
    return http.post<RefreshResponse>(`${config.baseUrl}/auth/refresh`, data)
}