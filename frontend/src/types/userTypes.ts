// user API相关typescript类型定义

// 用户信息响应
export interface UserInfoResponse {
    email: string
    username: string
    nickname: string | null
    avatar: string | null
    created_at: string
}

// 更新用户信息请求
export interface UpdateUserInfoRequest {
    nickname?: string
    avatar?: string
}
