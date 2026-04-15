<template>
    <div class="writing-container">
        <!-- 左侧区域 -->
        <div class="left-wrapper float-card">
            <ControlPanel :novel="novel" />
        </div>

        <!-- 右侧区域 -->
        <div class="right-wrapper float-card">
            <div v-if="currentChapterId" class="writing-wrapper">
                <div class="top-bar">
                    <p class="chapter-name" v-if="novel.type === 'lang'" @click="isSetNameModal = true">
                        {{ getChapterName(currentChapterId) || '点击此处设置章节名称' }}
                        <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M17.87 2.99a2 2 0 0 0-2.82 0l-7.96 7.84c-.14.13-.23.3-.27.49L5.8 15.76 4 18.01h2.83l1.14-1.13 3.59-.83c.18-.04.35-.13.48-.26l7.95-7.83c.38-.38.59-.88.6-1.42 0-.54-.21-1.04-.59-1.42L17.88 3Zm.71 3.53-7.24 7.13-2.12-2.12 7.24-7.13zM4 20h16v2H4z"></path>
                        </svg>
                        
                    </p>
                    <p class="novel-name" v-else>{{ novel.name }}</p>
                    <p style="font-size: 1rem;">{{ content.trim().length }}</p>
                </div>
                <div v-if="chapter" class="writing-box">
                    <textarea class="text" v-model="content" placeholder="请在这里写下你的故事..." @input="debounceSaveContent"></textarea>
                    <div class="interact" ref="MsgWrapperRef">
                        <textarea v-model="msg" ref="MsgTextareaRef" @input="autoResize" @keydown.enter="sendMsgForEnter" placeholder="hello~"></textarea>
                        <div class="send-btn">
                            <button :class="{ active: sendMsgIsActive }" :disabled="!sendMsgIsActive" @click="sendMsg">
                                <svg  xmlns="http://www.w3.org/2000/svg" width="32" height="32"  
                                fill="currentColor" viewBox="0 0 24 24" >
                                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                                <path d="M20.56 3.17c-.29-.2-.67-.23-.99-.08l-17 8.01a.999.999 0 0 0 .03 1.82L8 15.28V22l5.84-4.17 4.76 2.08c.13.06.26.08.4.08.18 0 .36-.05.52-.15a.99.99 0 0 0 .48-.79l1-15c.02-.35-.14-.69-.43-.89Zm-2.47 14.34-5.21-2.28L16 9l-7.65 4.25-2.93-1.28 13.47-6.34-.79 11.89Z"></path>
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
                
                <div class="animated-box" v-else>
                    <div class="animated-circle"></div>
                    <p>正在加载内容...</p>
                </div>
            </div>

            <!-- 遮罩层 -->
            <div v-else class="placeholder-wrapper">
                <svg  xmlns="http://www.w3.org/2000/svg" width="72" height="72"  
                fill="currentColor" viewBox="0 0 24 24" @click="createChapter" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M13 6h-2v3H8v2h3v3h2v-3h3V9h-3z"></path><path d="M18 2H6c-1.1 0-2 .9-2 2v17c0 .36.19.69.5.86.31.18.69.18 1 0l6.5-3.72 6.5 3.72c.15.09.32.13.5.13s.35-.04.5-.14a1 1 0 0 0 .5-.86V4c0-1.1-.9-2-2-2m0 8v9.28l-5.5-3.15a.98.98 0 0 0-.99 0l-5.5 3.15V4h12v6Z"></path>
                </svg>
                <p v-if="novel.chapters.length === 0">还没有章节内容，点此创建第一个章节</p>
                <p v-else>打开已有章节，或点此创建新章节</p>
            </div>
        </div>

        <!-- 设置章节名称弹窗 -->
        <SetChapterName v-model:visible="isSetNameModal" :name="chapter?.name || null" :id="currentChapterId" />
    </div>
</template>

<script setup lang='ts'>
    import { computed, onBeforeMount, ref, watch, provide } from 'vue' 
    import useNovelStore from '@/stores/novelStore.ts'
    import ControlPanel from '@/components/writing/ControlPanel.vue'
    import type { NovelMeta } from '@/types/novelTypes.ts'
    import type { Chapter } from '@/types/chapterTypes.ts'
    import { getChapterAPI, createChapterAPI, deleteChapterAPI, updateChapterAPI } from '@/services/chapter.ts'
    import SetChapterName from '@/components/writing/SetChapterName.vue'
    import PostSSE from '@/utils/SSEReciver'

    const novelStore = useNovelStore()
    const props = defineProps<{
        id: string
    }>()
    const currentChapterId = ref<number | null>(null) // 当前章节id
    const chapter = ref<Chapter | null>(null) // 当前章节
    const content = ref<string>('') // 当前章节内容
    const novel = computed(() => novelStore.novels[Number(props.id)] as NovelMeta)

    // 监听chapter id变化异步获取数据，并管理自动保存逻辑
    watch(currentChapterId, async () => {
        if (currentChapterId.value) {
            try {
                chapter.value = null // 清空当前chapter记录
                content.value = '' // 清空当前的content记录

                const data = await getChapterAPI(currentChapterId.value)

                chapter.value = data
                content.value = data.content
                
                // 开启自动保存
                startAutoSave()
            } catch(error) {
                return Promise.reject(error)
            }
        } else {
            // 关闭章节则关闭自动保存
            stopAutoSave()
        }
    })

    // 在组件挂载之前的行为控制
    onBeforeMount(async () => {
        // 检查novels是否为空并选择性加载
        if (novelStore.novels.length === 0) {
            try {
                await novelStore.getNovels()
            } catch(error) {
                return Promise.reject(error)
            }
        }

        // 检查作品类似以自适应地打开章节内容
        if (novel.value.type === 'short') {
            currentChapterId.value = novel.value.chapters[0]?.id || null
        }
    })

    // ========= 消息输入事件与自动高度调节方法 =========
    const MsgTextareaRef = ref<HTMLTextAreaElement | null>(null)
    const MsgWrapperRef = ref<HTMLDivElement | null>(null)
    let resizeTimer: number | null = null
    
    const autoResize = () => {
        if (resizeTimer) {
            clearTimeout(resizeTimer)
        }

        resizeTimer = setTimeout(() => {
            if (MsgTextareaRef.value && MsgWrapperRef.value) {
                const msgHeight = MsgTextareaRef.value.scrollHeight // 获取textarea高度

                const MIN_MEIGHT = 150
                const MAX_HEIGHT = 400
                const clampedHeight = Math.min(MAX_HEIGHT, Math.max(MIN_MEIGHT, msgHeight))

                MsgWrapperRef.value.style.height = clampedHeight + 'px'
                
                console.log(`输入框高度: ${msgHeight}, 容器高度: ${MsgWrapperRef.value.style.height}`)
            }
        }, 5) 
    }

    // ========= 创建章节方法 =========
    /**
     * 创建章节方法
     */
    const createChapter = async () => {
        try {
            await createChapterAPI(novel.value.id)

            // 重新加载所有作品
            await novelStore.getNovels()

            // 自动进入指定章节
            currentChapterId.value = novel.value.chapters.at(-1)?.id || null
        } catch(error) {
            return Promise.reject(error)
        }
    }
    provide('create-chapter', createChapter)

    // ========= 打开已有章节方法 =========
    /**
     * 打开已有章节
     * @param chapterId <number> 指定的章节id
     */
    const openChapter = (chapterId: number) => {
        if (currentChapterId.value === chapterId) {
            currentChapterId.value = null
        } else {
            currentChapterId.value = chapterId
        }
    }
    provide('open-chapter', openChapter)
    provide('current-chapter-id', currentChapterId)

    // ========= 删除章节方法 =========
    /**
     * 删除已有章节
     * @param chapterIds <number[]> - 需要删除的chapterId列表
     */
    const deleteChapters = async (chapterIds: number[]) => {
        try {
            await deleteChapterAPI(chapterIds)
            // 如果删除对象中包括当前已打开的章节则自动关闭
            if (currentChapterId.value && chapterIds.includes(currentChapterId.value)) {
                currentChapterId.value = null
            }
            // 重新加载novels
            await novelStore.getNovels()
        } catch(error) {
            return Promise.reject(error)
        }
    }
    provide('delete-chapters', deleteChapters)

    // ========= 修改章节名称方法 =========
    const isSetNameModal = ref<boolean>(false)
    /**
     * 获取chapter的name
     * @param chapterId <number> - chapter id
     */
    const getChapterName = (chapterId: number | null): string => {
        if (!chapterId) return ''
        const searchChapter = novel.value.chapters.find(chapter => chapter.id === chapterId)
        if (searchChapter) {
            return searchChapter.name
        } else {
            return ''
        }
    }

    // ========= 自动保存内容方法 =========
    let saveTimer: any = null
    let debounceSaveTimer: number | null = null // 防抖保存计时器

    /**
     * 开启自动保存 (30s强制进行保存)
     */
    const startAutoSave = () => {
        saveTimer = setInterval(async () => {
            try {
                await saveContent()
            } catch(error) {
                return Promise.reject(error)
            }
            
        }, 30000)
    }

    /**
     * 关闭自动保存
     */
    const stopAutoSave = () => {
        if (saveTimer) {
            clearInterval(saveTimer)
            saveTimer = null
        }
    }

    /**
     * 文本内容保存方法
     */
    const saveContent = async () => {
        // 确保已打开章节内容
        if (!currentChapterId.value || !chapter.value) return

        // 检测是否对文本进行改动
        if (content.value.trim() === chapter.value.content.trim()) return

        // 调用API
        try {
            await updateChapterAPI(currentChapterId.value, {content: content.value})

            // 获取最新的当前章节数据
            const data = await getChapterAPI(currentChapterId.value)
            chapter.value = data

            console.log('保存成功')
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 防抖保存封装 (1s抖动范围)
     */
    const debounceSaveContent = () => {
        if (debounceSaveTimer) {
            clearTimeout(debounceSaveTimer)
        }
        debounceSaveTimer = setTimeout(async () => {
                try {
                    await saveContent()
                } catch(error) {
                    return Promise.reject(error)
                }
            }, 1000)
    }

    // ========= 简单交互方法 =========
    const msg = ref<string>('')
    const isSending = ref<boolean>(false)
    const sendMsgIsActive = computed((): boolean => {
        if (msg.value.trim() && !isSending.value) {
            return true
        }
        return false
    })

    /**
     * enter消息发送方法
     */
    const sendMsgForEnter = async (event: KeyboardEvent) => {
        // 检查是否按下shift
        if (event.shiftKey) return

        // 阻止默认事件
        event.preventDefault()

        // 检查内容是否存在
        if (!sendMsgIsActive.value) return

        // 执行默认发送事件
        try {
            await sendMsg()
        } catch(error) {
            return Promise.reject(error)
        }
    }

    /**
     * 消息发送方法
     */
    const sendMsg = async () => {
        // 标记为正在发送消息
        isSending.value = true

        // 初始化SSE连接对象
        const postSSE = new PostSSE<{msg: string}, {content: string}>(`/api/writing/${novel.value.id}`)

        // 启动SSE连接
        try {
            await postSSE.connect(
                {msg: msg.value},
                {
                    onMessage: (data) => {
                        content.value += data.content
                    }
                }
            )
        } catch(error) {
            return Promise.reject(error)
        } finally {
            isSending.value = false
            msg.value = '' // 清空输入框内容
        }
        
    }
</script>

<style scoped>
    .writing-container {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .left-wrapper {
        flex: 1 1 40%;
        height: 100%;
    }

    /* 右侧区域 */
    .right-wrapper {
        flex: 1 1 60%;
        height: 100%;
    }

    .right-wrapper .animated-box {
        width: 100%;
        height: calc(100% - 50px - 25px);
        display: flex;
        flex-direction: column;
        gap: 15px;
        color: var(--text-color);
        font-family: 'Btn-text';
        align-items: center;
        justify-content: center;
    }

    .right-wrapper .animated-box .animated-circle {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 5px solid rgba(110, 110, 110, 0.5);
        border-top: 5px solid var(--primary-color);
        animation: span 0.75s linear infinite;
    }

    @keyframes span {
        to {
            rotate: 360deg;
        }
    }

    .right-wrapper .writing-wrapper {
        height: 100%;
        width: 100%;
        padding: 0 25px 25px;
    }

    .right-wrapper .placeholder-wrapper {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        gap: 10px;
        font-size: 1.25rem;
        font-family: 'Btn-text';
        user-select: none;
    }

    .right-wrapper .placeholder-wrapper svg {
        color: var(--primary-color);
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .right-wrapper .placeholder-wrapper svg:hover {
        transform: scale(1.1);
    }

    .right-wrapper .top-bar {
        height: 50px;
        margin-bottom: 25px;
        border-bottom: 1px solid var(--primary-color);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 5px;
        user-select: none;
    }

    .right-wrapper .top-bar p {
        color: var(--supple-color);
        font-family: 'Btn-text';
        font-size: 1.25rem;
        max-width: 50%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .right-wrapper .top-bar p.chapter-name {
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 5px;
        position: relative;
    }

    .right-wrapper .top-bar p.chapter-name svg {
        opacity: 0;
        transition: opacity 0.2s ease;
    }

    .right-wrapper .top-bar p.chapter-name:hover svg {
        opacity: 1;
    }

    .right-wrapper .writing-box {
        width: 100%;
        height: calc(100% - 50px - 25px);
        display: flex;
        flex-direction: column;
        gap: 25px;
    }

    .right-wrapper textarea {
        width: 100%;
        resize: none;
        outline: none;
        border: none;
        color: var(--text-color);
        font-family: 'Btn-text';
        padding: 0 5px;
        background-color: transparent;
    }

    .right-wrapper textarea.text {
        flex: 1;
        font-size: 1rem;
    }

    .right-wrapper textarea.text::-webkit-scrollbar {
        width: 6px;
    }

    .right-wrapper textarea.text::-webkit-scrollbar-thumb {
        background-color: rgba(35, 35, 35, 0.75);
        border-radius: 6px;
    }

    .right-wrapper .interact {
        height: 150px;
        min-height: 0;
        overflow: hidden;
        padding: 15px;
        background-color: rgba(35, 35, 35, 0.75);
        margin: 0 15px;
        border-radius: 24px;
        border: 1px solid var(--primary-color);
        transition: all 0.2s ease;
        display: flex;
        gap: 5px;
    }

    .right-wrapper .interact textarea {
        height: 100%;
        flex: 1;
        font-size: 0.9rem;
    }

    .right-wrapper .interact .send-btn {
        height: 100%;
        width: 75px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        padding: 5px 0;   
    }

    .right-wrapper .interact .send-btn button {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        border: none;
        background-color: var(--supple-color);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.2 ease;
    }

    .right-wrapper .interact .send-btn button svg {
        color: rgba(220, 220, 220, 0.4);
    }

    .right-wrapper .interact .send-btn button.active svg {
        color: rgba(220, 220, 220, 1);
    }

    .right-wrapper .interact .send-btn button:hover {
        transform: scale(1.05);
    }

    .right-wrapper .interact textarea::-webkit-scrollbar {
        width: 4px;
    }

    .right-wrapper .interact textarea::-webkit-scrollbar-thumb {
        background-color: rgba(110, 110, 110, 0.9);
        border-radius: 6px;
    }

    .right-wrapper .interact:focus-within {
        box-shadow: 0 0 12px  var(--primary-color);
    }
</style>