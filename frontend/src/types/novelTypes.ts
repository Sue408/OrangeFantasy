// novel API相关typescript类型定义

// novel类型
export type NovelType = 'short' | 'lang'

// 创建novel请求
export interface CreateNovelRequest {
    name: string
    cover?: string
    type: NovelType
}

// chapter相对于novel的响应单元模型
export interface ChapterForNovelMeta {
    id: number
    name: string
    number: number
    step: string | null
    created_at: string
    updated_at: string
}

// novel响应单元类型
export interface NovelMeta {
    id: number
    name: string
    cover: string | null
    type: NovelType
    chapters: ChapterForNovelMeta[]
    created_at: string
    updated_at: string
}

// novels响应模型
export interface NovelsResponse {
    novels: NovelMeta[]
}

// 更新novel请求模型
export interface UpdateNovelRequest {
    name?: string
    cover?: string
}