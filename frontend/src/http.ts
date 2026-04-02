import axios, { AxiosError, type AxiosRequestConfig } from 'axios'
import useUserStore from './stores/userSotre'
import router from '@/router/index.ts'

// 实例化axios对象
const request = axios.create({
    baseURL: '/api',
    timeout: 15000,
    headers: {
        'Content-Type': 'application/json'
    }
})

// 配置请求拦截器
request.interceptors.request.use(
    config => {
        // 获取access token
        const accessToken = localStorage.getItem('accessToken')

        // 如果access token存在则添加到请求头
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`
        }

        return config
    },
    error => {
        return Promise.reject(error)
    }
)

// 配置响应拦截器
request.interceptors.response.use(
    config => {
        return config
    },
    async (error: AxiosError) => {
        
        // 获取响应状态码
        const statusCode = error.response?.status

        // 401错误自动进行重新验证
        if (statusCode === 401) {
            const userStore = useUserStore()

            // 判断是否为刷新请求或已经重试
            if (error.config?.url?.includes('auth/refresh')) {
                await userStore.logout()
                router.replace('/')
                return Promise.reject(error)
            }

            // 自动进行token刷新并重新发送请求
            
            try {
                await userStore.refresh()
                return request(error.config!)
            } catch(error) {
                // 刷新失败则自动跳转到介绍页面并返回错误
                await userStore.logout()
                router.replace('/')
                return Promise.reject(error)
            }
        }

        return Promise.reject(error)
    }
)

// 泛型支持导出
const http = {
    async get<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
        const response = await request.get<T>(url, config)
        return response.data
    },
    async post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
        const response = await request.post<T>(url, data, config)
        return response.data
    },
    async put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
        const response = await request.put<T>(url, data, config)
        return response.data
    },
    async delete<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
        const response = await request.delete<T>(url, config)
        return response.data
    }
}
export default http