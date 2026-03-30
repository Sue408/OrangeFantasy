// 错误信息格式化解析器
/**
 * 提取错误信息
 * @param error <any> - 错误内容
 */
const errorParser = (error: any): string => {
    if (typeof error === 'string') {
        return error
    }

    if (error.response?.data?.detail) {
        return error.response.data.detail
    }

    if (!error.response?.data) {
        return '网络错误'
    }

    return '未知错误'
}

export default errorParser