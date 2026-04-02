// user Store定义
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { registerAPI, loginAPI, refreshAPI } from '@/services/auth'
import { getUserInfoAPI, updateUserInfoAPI } from '@/services/user'

const useUserStore = defineStore('user', () => {
    // ========= 基础属性 =========
    // 1. token信息
    const token = ref<{
        accessToken: string,
        refreshToken: string
        } | null>(null)

    // 2. 用户信息
    const userInfo = ref<{
        nickname: string | null,
        username: string,
        email: string,
        avatar: string | null,
        created_at: string
    } | null>(null)
    
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
            const response = await registerAPI({email, username, password})

            // 保存token到store
            token.value = {
                accessToken: response.access_token,
                refreshToken: response.refresh_token
            }

            // 保存token到localStorge
            localStorage.setItem('accessToken', response.access_token)
            localStorage.setItem('refreshToken', response.refresh_token)
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
            const response = await loginAPI({username, password})

            // 保存token到store
            token.value = {
                accessToken: response.access_token,
                refreshToken: response.refresh_token
            }

            // 保存token到localStorge
            localStorage.setItem('accessToken', response.access_token)
            localStorage.setItem('refreshToken', response.refresh_token)
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
            const refreshToken = token.value?.refreshToken
            if (!refreshToken) return Promise.reject('未持有refresh token')

            // 调用刷新接口
            const response = await refreshAPI({refresh_token: refreshToken})

            // 储存新的access token
            token.value = {accessToken: response.access_token, refreshToken}
            localStorage.setItem('accessToken', response.access_token)
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 登出方法
     */
    const logout = async () => {
        // 清除token信息
        token.value = null
        localStorage.removeItem('accessToken')
        localStorage.removeItem('refreshToken')

        // 清除用户信息
        userInfo.value = null
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
    const updateUserInfo = async (data: { nickname?: string, avatar?: string }) => {
        try {
            const response = await updateUserInfoAPI(data)
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
     * 从localStorage加载token并获取用户信息
     */
    const loadUser = async () => {
        // 获取token信息
        const accessToken = localStorage.getItem('accessToken')
        const refreshToken = localStorage.getItem('refreshToken')
        
        // 检查是否存在token
        if (accessToken && refreshToken) {
            token.value = {accessToken, refreshToken}
            try {
                await getUserInfo()
            } catch(error) {
                return Promise.reject(error)
            }
        }
    }

    return {
        token,
        userInfo,
        isLogged,
        register,
        login,
        refresh,
        logout,
        getUserInfo,
        updateUserInfo,
        loadUser
    }
})

export default useUserStore