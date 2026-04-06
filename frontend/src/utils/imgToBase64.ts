/**
 * Base64转换方法
 */
const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader()

        reader.onload = () => {
            resolve(reader.result as string)
        }

        reader.onerror = () => {
            reject('转换错误')
        }

        // 开始转换
        reader.readAsDataURL(file)
    })
}
export default fileToBase64