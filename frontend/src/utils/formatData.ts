// 从ISO格式化提取日期方法定义
/**
 * 格式化日期，提取年月日
 * @param dateStr - ISO格式日期字符串
 * @returns 格式化的年月日字符串
 */
const formatDate = (dateStr: string | undefined): string => {
    if (!dateStr) return '未知注册时间'
    
    try {
        const date = new Date(dateStr)
        // 检查是否为有效日期
        if (isNaN(date.getTime())) return '未知注册时间'
        
        const year = date.getFullYear()
        const month = String(date.getMonth() + 1).padStart(2, '0')
        const day = String(date.getDate()).padStart(2, '0')
        
        return `${year}年${month}月${day}日`
    } catch {
        return '未知注册时间'
    }
}

export default formatDate