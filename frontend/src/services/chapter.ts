import http from '@/http.ts'
import type {
    Chapter,
    UpdateChapterRequest
} from '@/types/chapterTypes.ts'


/**
 * 获取章节内容接口
 * @param chapterId <number> - 章节id
 */
export const getChapterAPI = async (chapterId: number): Promise<Chapter> => {
    return await http.get<Chapter>(`/chapter/${chapterId}`)
}

/**
 * 新建章节内容接口
 * @param novelId <number> - 作品id
 */
export const createChapterAPI = async (novelId: number): Promise<void> => {
    return await http.post<void>(`/chapter?novel_id=${novelId}`)
}

/**
 * 删除章节内容接口
 * @param chaptersId <number[]> - 章节id数组
 */
export const deleteChapterAPI = async (chaptersId: number[]): Promise<void> => {
    return await http.delete<void>(`/chapter?chapters_id=${chaptersId.join(',')}`)
}

/**
 * 更新章节信息接口
 * @param chapterId <number> - 章节id
 * @param name? <string> - 章节名称
 * @param content? <string> - 章节内容
 */
export const updateChapterAPI = async (chapterId: number, data: UpdateChapterRequest): Promise<void> => {
    return await http.put<void>(`/chapter/${chapterId}`, data)
}
