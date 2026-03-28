// 配置项定义

/**
 * 定义config接口
 */
export interface Config {
    baseUrl: string,
    env: "dev" | "product"
}

/**
 * 获取启动环境配置
 */
const getEnv = (): Config['env'] => {
    const env = import.meta.env.VITE_ENV

    if (env === 'product') {
        return env
    }

    // 默认是开发环境
    return 'dev'
}

/**
 * 获取后端API基础路径
 */
const getBaseUrl = (env: Config['env']): string => {
    const urlMap = {
        dev: import.meta.env.VITE_DEV_API_URL || '/api',
        product: import.meta.env.VITE_PROD_API_URL || '/api'
    }

    return urlMap[env]
}

const config: Config = {
    env: getEnv(),
    baseUrl: getBaseUrl(getEnv())
}
export default config