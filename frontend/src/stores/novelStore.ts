import { defineStore } from "pinia"
import  { ref } from 'vue'
import type {
    NovelMeta,
    CreateNovelRequest,
    UpdateNovelRequest
} from '@/types/novelTypes.ts'
import {
    getNovelsAPI,
    createNovelAPI,
    updateNovelAPI,
    deleteNovelAPI
} from '@/services/novel'

const useNovelStore = defineStore('novel', () => {
    // ========= 基础属性 =========
    const novels = ref<NovelMeta[]>([])

    // ========= 计算属性 =========

    // ========= 方法定义 =========
    /**
     * 获取novels方法
     */
    const getNovels = async () => {
        try {
            const response = await getNovelsAPI()
            novels.value = response.novels
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 创建novels方法
     * @param name <string> - novel名称
     * @param cover? <string> - 要设定的作品封面 (url/base64)
     * @param type <string> - 要设定的作品类型 ('short'/'long')
     */
    const createNovel = async (data: CreateNovelRequest) => {
        try {
            await createNovelAPI(data)

            // 重新获取novels
            await getNovels()
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 更新novel方法
     * @param novelId <number> - novel id
     * @param name? <string> - 更新后的novel名称
     * @param cover? <string> - 更新后的作品封面 (url/base64)
     */
    const updateNovel = async (novelId: number, data: UpdateNovelRequest) => {
        try {
            await updateNovelAPI(novelId, data)

            // 重新获取novels
            await getNovels()
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 删除novel方法
     * @param novelId <number> - novel id
     */
    const deleteNovel = async (novelId: number) => {
        try {
            await deleteNovelAPI(novelId)

            // 重新获取novels
            await getNovels()
        } catch(error) {
            return Promise.reject(error)
        }
    }

    return {
        novels,
        getNovels,
        createNovel,
        updateNovel,
        deleteNovel
    }
})
export default useNovelStore