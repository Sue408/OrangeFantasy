import useUserStore from "@/stores/userSotre"
const userSotre = useUserStore()

// 基于fetch的POST类型SSE请求发送类封装
interface Callbacks<T = object> {
    onMessage: (data: T) => void
}

class PostSSE<ReqData = object, ResData = object> {
    url: string
    controller: AbortController | null = null
    isClosed: boolean = false
    retry: boolean = false // 刷新标记

    // 对象初始化
    constructor(url: string) {
        this.url = url
    }

    // 连接主方法
    async connect(data: ReqData, callbacks: Callbacks<ResData>): Promise<any> {
        this.controller = new AbortController() // 初始化中止控制器
        try {
            // 获取响应对象
            const response = await fetch(this.url, {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('accessToken') || ''}`
                 },
                body: JSON.stringify(data),
                signal: this.controller.signal
            })

            // 检查响应状态
            if (!response.ok || !response.body) {
                // 检查401错误
                if (response.status === 401) {
                    // 检查是否已经刷新过
                    if (this.retry) return Promise.reject('达到最大刷新次数')

                    try {
                        // 尝试进行token刷新
                        await userSotre.refresh()

                        // 断开原来的SSE连接
                        this.controller.abort()
                        this.controller = new AbortController()

                        // 重新调用connect方法
                        return this.connect(data, callbacks)
                    } catch(error) {
                        return Promise.reject(`令牌刷新失败`)
                    }
                }

                return Promise.reject(`HTTP ${response.status}`)
            }

            // 获取读取连接对象
            const reader = response.body.getReader()
            const decoder = new TextDecoder()
            let buffer = '' // 缓冲区

            // 循环读取chunk
            while (!this.isClosed) {
                const { done, value } = await reader.read()

                // 如果TCP连接断开则退出循环
                if (done) {
                    break
                }

                // 解码chunk并加入到缓冲区
                buffer += decoder.decode(value, { stream: true })
                // 根据SSE协议拆分chunk
                const lines = buffer.split('\n\n')
                // 根据SSE协议循环解码chunk并按需处理
                for (const line of lines.slice(0, -1)) {
                    // 如果包含data字段的处理 (数据处理)
                    if (line.startsWith('data: ')) {
                        // 将json格式的内容转换为object
                        const data = JSON.parse(line.replace('data: ', ''))

                        // 调用回调
                        callbacks.onMessage(data)
                    
                    // 如果包含event字段的处理 (事件处理)
                    } else if (line.startsWith('event: ')) {
                        const event = line.replace('event: ', '') // 获取事件类型

                        // 针对[DONE]事件结束SSE连接
                        if ( event === '[DONE]' ) {
                            this.isClosed = true
                            this.controller.abort() // 触发AboutError手动中断连接

                            // 后续处理...
                        }

                        // 其他事件处理...
                    }
                }
                // 更新缓冲区
                buffer = lines[lines.length - 1] as string
            }
        } catch(error) {
            return Promise.reject(error)
        }
    }

    // 中断连接方法
    close() {
        // 如果已经关闭则直接退出逻辑
        if (this.isClosed) return

        this.isClosed = true
        if (this.controller) {
            this.controller.abort() // 触发'AboutError'
        }
    }
}

export default PostSSE