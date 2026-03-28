// user API相关接口调用
import http from '@/http.ts'
import config from '@/config.ts'
import type {
    UserInfoResponse,
    UpdateUserInfoRequest } from '@/types/userTypes'

/**
 * 获取用户信息接口
 */
export const getUserInfoAPI = async (): Promise<UserInfoResponse> => {
    return http.get<UserInfoResponse>(`${config.baseUrl}/user`)
}

/**
 * 更新用户信息接口
 */
export const updateUserInfoAPI = async (data: UpdateUserInfoRequest): Promise<UserInfoResponse> => {
    return http.post<UserInfoResponse>(`${config.baseUrl}/user`, data)
}
