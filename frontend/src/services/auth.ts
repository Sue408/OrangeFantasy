// auth API相关接口调用
import http from '@/http.ts'
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
    return await http.post<TokenResponse>(`/auth/register`, data)
}

/**
 * 登录接口
 */
export const loginAPI = async (data: LoginRequest): Promise<TokenResponse> => {
    return await http.post<TokenResponse>(`/auth/login`, data)
}

/**
 * 刷新token接口
 */
export const refreshAPI = async (data: RefreshRequest): Promise<RefreshResponse> => {
    return await http.post<RefreshResponse>(`/auth/refresh`, data)
}