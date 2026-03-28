// user Store定义
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { registerAPI, loginAPI, refreshAPI } from '@/services/auth'
import { getUserInfoAPI, updateUserInfoAPI } from '@/services/user'

const useUserStore = defineStore('user', () => {
    // ========= 基础属性 =========
    // 1. token信息
    const token = ref<{
        accessToken: string | null,
        refreshToken: string | null
        }>({
            accessToken: null,
            refreshToken: null
        })

    // 2. 用户信息
    const userInfo = ref<{
        nickname: string | null,
        username: string | null,
        email: string | null,
        avatar: string | null,
        created_at: string | null
    }>({
        nickname: null,
        username: null,
        email: null,
        avatar: null,
        created_at: null
    })
    
    // ========= 计算属性 =======
    // 1. 登录态
    const isLogged = computed(() => {
        return !!token.value
    })

    // ========= 方法定义 =========
    /**
     *  注册方法
     * @param email <string> - 邮箱地址
     * @param username <string> - 账号
     * @param password <string> - 密码
     */
    const register = async (
        email: string,
        username: string,
        password: string
    ) => {
        try {
            // 调用注册接口
            const tokenResponse = await registerAPI({email, username, password})

            // 保存token到store
            token.value = {
                accessToken: tokenResponse.access_token,
                refreshToken: tokenResponse.refresh_token
            }

            // 保存token到localStorge
            localStorage.setItem('accessToken', tokenResponse.access_token)
            localStorage.setItem('refreshToken', tokenResponse.refresh_token)

        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 登录方法
     * @param username <string> - 账号
     * @param password <string> - 密码
     */
    const login = async (
        username: string,
        password: string
    ) => {
        try {
            // 调用登录接口
            const tokenResponse = await loginAPI({username, password})

            // 保存token到store
            token.value = {
                accessToken: tokenResponse.access_token,
                refreshToken: tokenResponse.refresh_token
            }

            // 保存token到localStorge
            localStorage.setItem('accessToken', tokenResponse.access_token)
            localStorage.setItem('refreshToken', tokenResponse.refresh_token)

        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 刷新token方法
     */
    const refresh = async () => {
        try {
            // 检查refresh token
            const refreshToken = token.value.refreshToken
            if (!refreshToken) return Promise.reject('未持有refresh token')

            // 调用刷新接口
            const TokenResponse = await refreshAPI({refresh_token: refreshToken})

            // 储存新的access token
            token.value = {accessToken: TokenResponse.access_token, refreshToken}
            localStorage.setItem('accessToken', TokenResponse.access_token)
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 获取用户信息方法
     */
    const getUserInfo = async () => {
        try {
            // 调用接口
            const response = await getUserInfoAPI()
            userInfo.value = {
                nickname: response.nickname,
                username: response.username,
                email: response.email,
                avatar: response.avatar,
                created_at: response.created_at
            }
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 修改用户信息方法
     * @param nickname? <string> - 要修改的用户昵称
     * @param avatar? <string> - 要修改的用户头像(url/base64)
     */
    const updateUserInfo = async (nickname?: string, avatar?: string) => {
        try {
            const response = await updateUserInfoAPI({
                ...(nickname && { nickname }),
                ...(avatar && { avatar })
            })
            userInfo.value = {
                nickname: response.nickname,
                username: response.username,
                email: response.email,
                avatar: response.avatar,
                created_at: response.created_at
            }
        } catch(error) {
            return Promise.reject(error)
        }
    }

    return {
        token,
        userInfo,
        isLogged,
        register,
        login,
        refresh,
        getUserInfo,
        updateUserInfo
    }
})

export default useUserStore