import http from '@/http.ts'
import type {
    CreateNovelRequest,
    NovelsResponse,
    UpdateNovelRequest
} from '@/types/novelTypes.ts'

/**
 * 创建novel接口
 */
export const createNovelAPI = async (data: CreateNovelRequest): Promise<void> => {
    return await http.post<void>(`/novel`, data)
}

/**
 * 获取novels接口
 */
export const getNovelsAPI = async (): Promise<NovelsResponse> => {
    return await http.get<NovelsResponse>(`/novel`)
}

/**
 * 更新novel设定接口
 */
export const updateNovelAPI = async (novelId: number, data: UpdateNovelRequest): Promise<void> => {
    return await http.put<void>(`/novel/${novelId}`, data)
}

/**
 * 删除novel接口
 */
export const deleteNovelAPI = async (novelId: number): Promise<void> => {
    return await http.delete<void>(`/novel/${novelId}`)
}