// chapter API相关typescripts类型定义

// chapter响应模型
export interface Chapter {
    id: number
    step: string | null
    number: number
    name: string
    content: string
    created_at: string
    updated_at: string
}

// chapter更新请求模型
export interface UpdateChapterRequest {
    name?: string
    content?: string
}