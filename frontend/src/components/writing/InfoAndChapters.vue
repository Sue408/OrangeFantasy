<template>
    <div class="info-and-chapters-container" :class="{ hide: infoIsHide }">
        <!-- 信息设定 -->
        <div class="novel-info-wrapper">
            <!-- 基础信息区 -->
            <div class="basic-info-wrapper">
                <!-- 封面 -->
                <div class="avatar-wrapper">
                    <div class="avatar-box"  :class="{'have-avatar': novel.cover}">
                        <label for="set-cover"></label>
                        <img v-if="novel.cover" :src="novel.cover" alt="cover">
                        <div v-else  class="default-avatar">
                            <svg  xmlns="http://www.w3.org/2000/svg" width="42" height="42"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M8 6h9v2H8z"></path><path d="M20 2H6C4.35 2 3 3.35 3 5v14c0 1.65 1.35 3 3 3h15v-2H6c-.55 0-1-.45-1-1s.45-1 1-1h14c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1m-6 14H6c-.35 0-.69.07-1 .18V5c0-.55.45-1 1-1h13v12z"></path>
                            </svg>
                        </div>
                        <div class="mask">
                            <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="m5 17.41 3-3 1.29 1.29c.39.39 1.02.39 1.41 0l5.29-5.29 3 3V14h2V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H5zM19 5v5.59L16.71 8.3a.996.996 0 0 0-1.41 0l-5.29 5.29-1.29-1.29a.996.996 0 0 0-1.41 0l-2.29 2.29V5h14Z"></path><path d="M8.5 7a1.5 1.5 0 1 0 0 3 1.5 1.5 0 1 0 0-3m13.22 11.07-1.94-.86-.86-1.94a.46.46 0 0 0-.42-.28c-.19-.02-.35.1-.43.27l-.86 1.87-1.95.94c-.16.08-.27.25-.26.43 0 .18.11.35.28.42l1.94.86.86 1.94a.471.471 0 0 0 .86 0l.86-1.94 1.94-.86a.471.471 0 0 0 0-.86Z"></path>
                            </svg>
                        </div>
                        <input @change="setCover" ref="coverInputRef" id="set-cover" style="display: none;" type="file" accept="image/png, image/jpeg, image/jpg, image/webp">
                    </div>
                </div>

                <!-- 其余信息 (名称、类型、创建时间、更新时间) -->
                <div class="other-info-wrapper">
                    <div class="info-item">
                        <p class="label">
                            <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="m17.71 7.29-3-3a.996.996 0 0 0-1.41 0l-11.01 11A1 1 0 0 0 2 16v3c0 .55.45 1 1 1h3c.27 0 .52-.11.71-.29l11-11a.996.996 0 0 0 0-1.41ZM5.59 18H4v-1.59l7.5-7.5 1.59 1.59zm8.91-8.91L12.91 7.5 14 6.41 15.59 8zM11 18h11v2H11z"></path>
                            </svg>
                            作品名称:
                        </p>
                        <p class="value">{{ novel.name }}</p>
                    </div>

                    <div class="info-item">
                        <p class="label">
                            <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M21 3h-7c-.77 0-1.47.3-2 .78-.53-.48-1.23-.78-2-.78H3c-.55 0-1 .45-1 1v15c0 .55.45 1 1 1h5.76c.53 0 1.04.21 1.41.59l1.12 1.12s.02.01.03.02c.09.08.18.15.29.2.12.05.25.08.38.08s.26-.03.38-.08c.11-.05.21-.12.29-.2 0 0 .02-.01.03-.02l1.12-1.12c.37-.37.89-.59 1.41-.59h5.76c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1ZM8.76 18H4V5h6c.55 0 1 .45 1 1v12.69c-.66-.44-1.44-.69-2.24-.69M20 18h-4.76c-.8 0-1.58.25-2.24.69V6c0-.55.45-1 1-1h6z"></path>
                            </svg>
                            作品类型:
                        </p>
                        <p class="value">{{ novel.type === 'lang' ? '中/长篇' : '短篇' }}</p>
                    </div>

                    <div class="info-item">
                        <p class="label">
                            <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M12 2C6.58 2 2 6.58 2 12s4.58 10 10 10 10-4.58 10-10S17.42 2 12 2m0 18c-4.34 0-8-3.66-8-8s3.66-8 8-8 8 3.66 8 8-3.66 8-8 8"></path><path d="M13 7h-2v6h6v-2h-4z"></path>
                            </svg>
                            创建时间:
                        </p>
                        <p class="value">{{ formatDate(novel.created_at) }}</p>
                    </div>

                    <div class="info-item">
                        <p class="label">
                            <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M19.07 4.93a9.9 9.9 0 0 0-3.18-2.14A9.95 9.95 0 0 0 12 2v2c1.08 0 2.13.21 3.11.63.95.4 1.81.98 2.54 1.71s1.31 1.59 1.72 2.54c.42.99.63 2.03.63 3.11s-.21 2.13-.63 3.11c-.4.95-.98 1.81-1.72 2.54-.17.17-.34.32-.52.48L15 15.99v6h6l-2.45-2.45c.18-.15.36-.31.52-.48.92-.92 1.64-1.99 2.14-3.18.52-1.23.79-2.54.79-3.89s-.26-2.66-.79-3.89a9.9 9.9 0 0 0-2.14-3.18ZM4.93 19.07c.92.92 1.99 1.64 3.18 2.14 1.23.52 2.54.79 3.89.79v-2a7.9 7.9 0 0 1-3.11-.63c-.95-.4-1.81-.98-2.54-1.71s-1.31-1.59-1.72-2.54c-.42-.99-.63-2.03-.63-3.11s.21-2.13.63-3.11c.4-.95.98-1.81 1.72-2.54.17-.17.34-.32.52-.48L9 8.01V2H3l2.45 2.45c-.18.15-.36.31-.52.48-.92.92-1.64 1.99-2.14 3.18C2.27 9.34 2 10.65 2 12s.26 2.66.79 3.89c.5 1.19 1.22 2.26 2.14 3.18"></path>
                            </svg>
                            更新时间:
                        </p>
                        <p class="value">{{ formatDate(novel.updated_at) }}</p>
                    </div>
                </div>
            </div>

            <!-- 简介与概览区 -->
            <div class="introduce-wrapper" :class="{ 'is-short': novel.type === 'short' }">
                <p>
                    <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M5 21h14c1.1 0 2-.9 2-2v-7h-2v7H5V5h7V3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2"></path><path d="M7 13v3c0 .55.45 1 1 1h3c.27 0 .52-.11.71-.29l9-9a.996.996 0 0 0 0-1.41l-3-3a.996.996 0 0 0-1.41 0l-9.01 8.99A1 1 0 0 0 7 13m10-7.59L18.59 7 17.5 8.09 15.91 6.5zm-8 8 5.5-5.5 1.59 1.59-5.5 5.5H9z"></path>
                    </svg>
                    作品简介
                </p>
                <div class="textarea-box">
                    <textarea disabled="true"></textarea>
                </div>
            </div>
        </div>

        <!-- 收缩按钮容器 (兼收缩状态的作品名展示) -->
        <div class="hide-btn-wrapper" v-if="novel.type === 'lang'">
            <div>
                <h3>
                    <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M21 3h-7c-.77 0-1.47.3-2 .78-.53-.48-1.23-.78-2-.78H3c-.55 0-1 .45-1 1v15c0 .55.45 1 1 1h5.76c.53 0 1.04.21 1.41.59l1.12 1.12s.02.01.03.02c.09.08.18.15.29.2.12.05.25.08.38.08s.26-.03.38-.08c.11-.05.21-.12.29-.2 0 0 .02-.01.03-.02l1.12-1.12c.37-.37.89-.59 1.41-.59h5.76c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1ZM8.76 18H4V5h6c.55 0 1 .45 1 1v12.69c-.66-.44-1.44-.69-2.24-.69M20 18h-4.76c-.8 0-1.58.25-2.24.69V6c0-.55.45-1 1-1h6z"></path>
                    </svg>
                    {{ novel.name }}
                </h3>
                <button @click="$emit('toggleInfoHide')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M6.65 16h10.69c.64 0 .99-.76.56-1.24l-5.35-6.11a.753.753 0 0 0-1.13 0l-5.35 6.11c-.42.48-.08 1.24.56 1.24Z"></path>
                    </svg>
                </button>
            </div>
        </div>

        <!-- 章节设定 -->
        <div class="chapters-wrapper" v-if="novel.type === 'lang'">
            <!-- 控制栏 -->
            <div class="control-bar">
                <div class="control-item" @click="createChapter()">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M13 6h-2v3H8v2h3v3h2v-3h3V9h-3z"></path><path d="M18 2H6c-1.1 0-2 .9-2 2v17c0 .36.19.69.5.86.31.18.69.18 1 0l6.5-3.72 6.5 3.72c.15.09.32.13.5.13s.35-.04.5-.14a1 1 0 0 0 .5-.86V4c0-1.1-.9-2-2-2m0 8v9.28l-5.5-3.15a.98.98 0 0 0-.99 0l-5.5 3.15V4h12v6Z"></path>
                    </svg>
                </div>
                <div class="control-item" :class="{ active: isDeleteModal }" @click="toggleDeleteModal">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M17 6V4c0-1.1-.9-2-2-2H9c-1.1 0-2 .9-2 2v2H2v2h2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8h2V6zM9 4h6v2H9zM6 20V8h12v12z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path>
                    </svg>
                </div>
            </div>
            <!-- 章节内容与操作栏容器 -->
            <div class="chapters-and-btn">
                <div class="chapters-box">
                    <div class="chapter-item" :class="{ active: currentChapterId === chapter.id, select: checkChapterState(chapter.id) }" v-for="(chapter, index) in novel.chapters" :key="chapter.id" @click="ClickChapterElement(chapter.id)">
                        <p class="label">第{{ index + 1 }}章</p>
                        <p class="value">{{ chapter.name }}</p>
                        <button v-if="isDeleteModal" class="delete-select">
                        </button>
                    </div>
                    <div class="chapter-item add-chapter-btn" @click="createChapter()">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="18" height="18"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M13 6h-2v3H8v2h3v3h2v-3h3V9h-3z"></path><path d="M18 2H6c-1.1 0-2 .9-2 2v17c0 .36.19.69.5.86.31.18.69.18 1 0l6.5-3.72 6.5 3.72c.15.09.32.13.5.13s.35-.04.5-.14a1 1 0 0 0 .5-.86V4c0-1.1-.9-2-2-2m0 8v9.28l-5.5-3.15a.98.98 0 0 0-.99 0l-5.5 3.15V4h12v6Z"></path>
                        </svg>
                        <p>创建新章节</p>
                    </div>
                </div>
                <!-- 删除确认按钮容器 -->
                <div class="delete-confirm-box" :class="{ active: isDeleteModal }" @click="deleteChapters">
                    <p>确认删除</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { inject, ref, type Ref } from 'vue'
    import type { NovelMeta } from '@/types/novelTypes.ts'
    import fileToBase64 from '@/utils/imgToBase64'
    import useNovelStore from '@/stores/novelStore'
    import formatDate from '@/utils/formatData'
    import { showDialog } from '@/utils/showDoalog'

    const novelStore = useNovelStore()
    const props = defineProps<{
        novel: NovelMeta
        infoIsHide: boolean
    }>()

    // ========= 打开已有chapter =========
    const openChapterMethod = inject('open-chapter') as Function
    const currentChapterId = inject('current-chapter-id') as Ref<number | null>
    /**
     * 点击章节元素的回调
     * @param chapterId <number> - 点击指定id的章节 (delete模式为选择删除/正常模式为打开章节)
     */
    const ClickChapterElement = (chapterId: number) => {
        if (isDeleteModal.value) {
            // 如果选中则移除
            if (checkChapterState(chapterId)) {
                deleteChapterIds.value = deleteChapterIds.value.filter(id => id !== chapterId)
            } else {
                // 否则添加到待删除列表
                deleteChapterIds.value.push(chapterId)
            }
            
        } else {
            // 默认点击打开章节
            openChapterMethod(chapterId)
        }
    }

    // ========= 创建新chapter ==========
    const createChapterMethod = inject('create-chapter') as Function
    /**
     * 创建新章节方法
     */
    const createChapter = async () => {
        // 删除模式禁止创建新章节
        if (isDeleteModal.value) return
        try {
            await createChapterMethod()
        } catch(error) {
            return Promise.reject(error)
        }
    }

    // ========= 删除chapter =========
    const isDeleteModal = ref<boolean>(false)
    const deleteChapterIds = ref<number[]>([])
    const deleteChapterMethod = inject('delete-chapters') as Function // 删除chapter核心方法
    /**
     * 切换删除模式
     */
    const toggleDeleteModal = () => {
        isDeleteModal.value = !isDeleteModal.value

        // 自动关闭当前章节
        currentChapterId.value = null

        // 自动清空待删除的章节数组
        deleteChapterIds.value = []
    }

    /**
     * 判断当前章节是否被选中
     * @param chapterId <number> - 章节id
     */
    const checkChapterState = (chapterId: number): boolean => {
        if (deleteChapterIds.value.includes(chapterId)) return true
        return false
    }

    /**
     * 删除chapters方法
     */
    const deleteChapters = async () => {
        // 显示确认弹窗
        showDialog({
            context: '确认删除这些章节内容吗？',
            onConfirm: async () => {
                try {
                    if (deleteChapterIds.value.length === 0) return
                    await deleteChapterMethod(deleteChapterIds.value)
                } catch(error) {
                    return Promise.reject(error)
                } finally {
                    toggleDeleteModal()
                }
            }
        })
    }

    // ========= 设置封面方法 =========
    /**
     * 选择封面方法
     */
    const setCover = async (event: Event) => {
        const input = event.target as HTMLInputElement
        const file = input.files?.[0]
        if (!file) return

        // 转成DataURL并上传，接着重新显示
        try {
            const cover = await fileToBase64(file)

            await novelStore.updateNovel(props.novel.id, {cover})

            await novelStore.getNovels()
        } catch(error) {
            return Promise.reject(error)
        }
    }
</script>

<style scoped>
    .info-and-chapters-container {
        width: 100%;
        height: 100%;
        border-top-right-radius: 24px;
        border-bottom-right-radius: 24px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .novel-info-wrapper {
        width: 100%;
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        transition: all 0.3s ease;
    }

    .hide-btn-wrapper {
        width: 100%;
        height: 50px;
        display: flex;
        justify-content: center;
    }

    .chapters-wrapper {
        width: 100%;
        flex: 1;
        display: flex;
        flex-direction: column;
        min-height: 0;
        padding: 0 25px 25px;
        transition: all 0.3s ease;
        overflow: hidden;
    }

    /* novel info 区域 */
    .info-and-chapters-container.hide .novel-info-wrapper {
        flex: 0;
        opacity: 0;
        min-height: 0;
    }

    .info-and-chapters-container.hide .chapters-wrapper {
        flex: 1;
    }

    /* 隐藏按钮区域 */
    .info-and-chapters-container.hide .hide-btn-wrapper {
        height: 75px;
    }

    .hide-btn-wrapper div {
        height: 100%;
        width: 90%;
        padding: 0 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .hide-btn-wrapper div h3 {
        color: var(--primary-color);
        font-family: 'Btn-text';
        font-size: 1.1rem;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 200px;
        opacity: 0;
        transition: opacity 0.3s ease;
        letter-spacing: 0.1rem;
        white-space: nowrap;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .hide-btn-wrapper div h3 svg {
        color: var(--text-color);
    }

    .info-and-chapters-container.hide .hide-btn-wrapper div h3 {
        opacity: 1;
     }

    .hide-btn-wrapper button {
        height: 24px;
        width: 24px;
        background-color: var(--btn-bg-color);
        border: 1px solid var(--supple-color);
        color: var(--text-color);
        border-radius: 50%;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: var(--btn-shadow);
    }

    .hide-btn-wrapper button:hover {
        transform: scale(1.1);
        box-shadow: var(--btn-shadow-hover);
    }

    .info-and-chapters-container.hide .hide-btn-wrapper button {
        transform: rotate(180deg);
    }

    /* avatar区域设计 */
    .basic-info-wrapper {
        width: 100%;
        height: 200px;
        display: flex;
    }

    .basic-info-wrapper .avatar-wrapper {
        flex: 1 1 40%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box {
        height: 160px;
        width: 112px;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--supple-color);
        box-shadow: var(--btn-shadow);
        transition: all 0.3s ease;
        position: relative;
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box label {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        cursor: pointer;
        z-index: 1;
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box .mask {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        z-index: 0;
        background-color: rgba(35, 35, 35, 0.75);
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box.have-avatar {
        border: 2px solid var(--supple-color);   
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box:hover {
        transform: scale(1.05);
        box-shadow: var(--btn-shadow-hover);
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box:hover .mask {
        opacity: 1;
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .basic-info-wrapper .avatar-wrapper .avatar-box .default-avatar {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
    }

    /* 其他info设计 */
    .basic-info-wrapper .other-info-wrapper {
        flex: 1 1 60%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 20px;
    }

    .basic-info-wrapper .other-info-wrapper .info-item {
        font-family: 'Btn-text';
        font-size: 0.8rem;
        display: flex;
        gap: 10px;
        align-items: center;
        color: var(--text-color);
    }

    .basic-info-wrapper .other-info-wrapper .info-item p.label {
        font-size: 0.9rem;
        color: var(--primary-color);
        border-bottom: 1px solid var(--supple-color);
        user-select: none;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .basic-info-wrapper .other-info-wrapper .info-item p.value {
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }

    .introduce-wrapper {
        width: 100%;
        height: calc(100% - 200px);
        padding: 5px 25px 0;
    }

    .introduce-wrapper.is-short {
        max-height: 40%;
    }

    .introduce-wrapper p {
        height: 40px;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        padding: 0 10px;
        font-family: 'Btn-text';
        user-select: none;

    }

    .textarea-box {
        width: 100%;
        height: calc(100% - 40px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px;
        background-color: rgba(35, 35, 35, 0.25);
        border: 1px solid var(--supple-color);
        border-radius: 12px;
    }

    .introduce-wrapper textarea {
        width: 100%;
        height: 100%;
        outline: none;
        resize: none;
        background-color: transparent;
        border: none;
        color: var(--text-color);
        font-size: 0.9rem;
        font-family: 'Btn-text';
    }

    .introduce-wrapper textarea::-webkit-scrollbar {
        width: 3px;
    }

    .introduce-wrapper textarea::-webkit-scrollbar-thumb {
        background-color: rgba(110, 110, 110, 0.5);
    }

    /* chapter control-bar设计 */
    .control-bar {
        height: 50px;
        display: flex;
        align-items: center;
        padding: 0 10px;
        border-top: 1px solid #ddd;
        border-bottom: 1px solid #ddd;
        gap: 25px;
    }

    .control-bar .control-item {
        color: var(--text-color);
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .control-bar .control-item.active {
        color: var(--supple-color);
    }

    .control-bar .control-item:hover {
        color: var(--primary-color);
        transform: scale(1.1);
    }

    .info-and-chapters-container.hide .control-bar {
        height: 50px;
    }
   
    /* chapters-and-btn容器设计 */
    .chapters-and-btn {
        width: 100%;
        height: calc(100% - 50px);
        display: flex;
        flex-direction: column;
    }

    /* chapters容器设计 */
    .chapters-box {
        flex: 1;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 10px;
        overflow-y: auto;
        overflow-x: hidden;
        user-select: none;
        margin: 20px 0 0;
    }

    .info-and-chapters-container.hide .chapters-box {
        height: calc(100% - 50px);
    }

    .chapters-box::-webkit-scrollbar {
        width: 6px;
    }

    .chapters-box::-webkit-scrollbar-thumb {
        background-color: rgba(35, 35, 35, 0.75);
        border-radius: 4px;
    }

    .chapters-box .chapter-item {
        width: 90%;
        height: 50px;
        min-height: 30px;
        border-radius: 8px;
        background-color: var(--btn-bg-color);
        border: 1px solid var(--supple-color);
        display: flex;
        color: var(--text-color);
        font-family: 'Btn-text';
        align-items: center;
        transition: all 0.15s ease;
        cursor: pointer;
        gap: 5px;
        position: relative;
    }

    .chapters-box .chapter-item .delete-select {
        position: absolute;
        height: 20px;
        width: 20px;
        border-radius: 50%;
        right: 15px;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: rgba(220, 220, 220, 0.75);
    }

    .chapters-box .chapter-item.select {
        background-color: rgba(120, 0, 0, 0.5);
    }

    .chapters-box .chapter-item.active {
        background-color: rgba(236, 96, 26, 0.5);
    }

    .chapters-box .chapter-item:not(.add-chapter-btn):hover {
        box-shadow: var(--btn-shadow-hover);
        transform: translateX(5px);
    }

    .chapters-box .chapter-item.add-chapter-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: rgba(35, 35, 35, 0.5);
        font-size: 0.9rem;
        transition: all 0.2s ease;
    }

    .chapters-box .chapter-item.add-chapter-btn:hover {
        background-color: rgba(35, 35, 35, 0.3);
    }

    .chapters-box .chapter-item p.label {
        height: 100%;
        width: 25%;
        font-size: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }

    .chapters-box .chapter-item p.value {
        height: 100%;
        flex: 1;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }

    /* delete-confirm-box设计 */
    .delete-confirm-box {
        width: 100%;
        height: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        box-shadow: var(--btn-shadow);
        background-color: var(--supple-color);
        border-radius: 12px;
        transition: all 0.2s ease;
        color: var(--text-color);
        font-size: 1.1rem;
        font-family: 'Btn-text';
        user-select: none;
        cursor: pointer;
    }

    .delete-confirm-box:hover {
        box-shadow: var(--btn-shadow-hover);
    }

    .delete-confirm-box.active {
        margin-top: 15px;
        height: 35px;
    }
</style>