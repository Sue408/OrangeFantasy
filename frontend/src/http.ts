import axios, { type AxiosRequestConfig } from 'axios'

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
    error => {
        return Promise.reject(error)
    }
)

// 泛型支持导出
const http = {
    async get<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
        return await request.get(url, config)
    },
    async post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
        return await request.post(url, data, config)
    },
    async put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
        return await request.put(url, data, config)
    },
    async delete<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
        return await request.delete(url, config)
    }
}
export default http