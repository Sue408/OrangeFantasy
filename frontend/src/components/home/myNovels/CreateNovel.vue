<template>
    <div class="create-novel-container float-card">
        <!-- 顶部栏 -->
        <div class="top-control-bar">
            <!-- 离开按钮 -->
            <button class="control-btn leave" @click="$emit('closeCreateModal')">
                <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M5 5h7V3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h7v-2H5z"></path><path d="m14 7-6 5 6 5v-4h7v-2h-7z"></path>
                </svg>
            </button>

            <!-- 切换按钮 -->
             <button class="control-btn toggle" :class="{ 'is-delicate-modal': isDelicateModal }" @click="toggleSettingModal">
                <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M12 2C6.49 2 2 6.49 2 12s4.49 10 10 10 10-4.49 10-10S17.51 2 12 2m0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8"></path><path d="M12 10.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 1 0 0-3m4.5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 1 0 0-3m-9 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 1 0 0-3"></path>
                </svg>
             </button>

             <!-- 提交按钮 -->
              <button class="control-btn" @click="createNovel">
                <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M9 15.59 4.71 11.3 3.3 12.71l5 5c.2.2.45.29.71.29s.51-.1.71-.29l11-11-1.41-1.41L9.02 15.59Z"></path>
                </svg>
              </button>
        </div>

        <!-- 内容区 -->
        <div class="main-content" :class="{ 'is-delicate-modal': isDelicateModal }">
            <!-- 基础设置 -->
            <div class="wrapper basic-setting">
                <!-- 封面/名称设置 -->
                <div class="cover-wrapper">
                    <div class="novel-cover" :class="{ 'have-cover': novelCover }">
                        <label for="set-cover"></label>
                        <img v-if="novelCover" :src="novelCover" alt="cover">
                        <svg v-else  xmlns="http://www.w3.org/2000/svg" width="64" height="64"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="m5 17.41 3-3 1.29 1.29c.39.39 1.02.39 1.41 0l5.29-5.29 3 3V14h2V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H5zM19 5v5.59L16.71 8.3a.996.996 0 0 0-1.41 0l-5.29 5.29-1.29-1.29a.996.996 0 0 0-1.41 0l-2.29 2.29V5h14Z"></path><path d="M8.5 7a1.5 1.5 0 1 0 0 3 1.5 1.5 0 1 0 0-3m13.22 11.07-1.94-.86-.86-1.94a.46.46 0 0 0-.42-.28c-.19-.02-.35.1-.43.27l-.86 1.87-1.95.94c-.16.08-.27.25-.26.43 0 .18.11.35.28.42l1.94.86.86 1.94a.471.471 0 0 0 .86 0l.86-1.94 1.94-.86a.471.471 0 0 0 0-.86Z"></path>
                        </svg>
                    </div>
                    <input v-model="novelName" type="text" class="novel-name" placeholder="请设置作品名"></input>
                    <input @change="setCover" ref="coverInputRef" id="set-cover" style="display: none;" type="file" accept="image/png, image/jpeg, image/jpg, image/webp">
                </div>

                <!-- Form表单 -->
                <div class="form-wrapper">
                    <!-- 作品类型选择 -->
                    <div class="type-select">
                        <p>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M21 3h-7c-.77 0-1.47.3-2 .78-.53-.48-1.23-.78-2-.78H3c-.55 0-1 .45-1 1v15c0 .55.45 1 1 1h5.76c.53 0 1.04.21 1.41.59l1.12 1.12s.02.01.03.02c.09.08.18.15.29.2.12.05.25.08.38.08s.26-.03.38-.08c.11-.05.21-.12.29-.2 0 0 .02-.01.03-.02l1.12-1.12c.37-.37.89-.59 1.41-.59h5.76c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1ZM8.76 18H4V5h6c.55 0 1 .45 1 1v12.69c-.66-.44-1.44-.69-2.24-.69M20 18h-4.76c-.8 0-1.58.25-2.24.69V6c0-.55.45-1 1-1h6z"></path>
                            </svg>
                            作品类型:
                        </p>
                        <div class="select-container">
                            <p @click="setType('short')">短篇</p>
                            <p @click="setType('lang')">中/长篇</p>
                            <div class="mask" :class="{ 'is-long': novelType === 'lang' }"></div>
                        </div>
                    </div>

                    <!-- 作品概述 -->
                    <div class="novel-overview">
                        <textarea placeholder="这里可以写下你的作品概述..."></textarea>
                    </div>
                </div>
            </div>

            <!-- 详细设置 -->
            <div class="wrapper delicate-setting">
                详细设置
            </div>
        </div>

        <!-- 提交动画 -->
        <div class="load-layer" v-if="isloading">
            <div class="orange-loader">
                <div class="loader-outer">
                    <div class="loader-inner"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { ref } from 'vue'
    import fileToBase64 from '@/utils/imgToBase64'
    import type { NovelType, CreateNovelRequest } from '@/types/novelTypes'
    import useNovelStore from '@/stores/novelStore'
    import { showDialog } from '@/utils/showDoalog'

    const novelStore = useNovelStore()
    const emit = defineEmits(['closeCreateModal'])

    const isDelicateModal = ref<boolean>(false)
    /**
     * 切换setting模式
     */
    const toggleSettingModal = () => {
        isDelicateModal.value = !isDelicateModal.value
    }

    // ========= 设置封面 =========
    const novelCover = ref<string>('')
    /**
     * 选择封面方法
     */
    const setCover = async (event: Event) => {
        const input = event.target as HTMLInputElement
        const file = input.files?.[0]
        if (!file) return

        // 转成DataURL并显示
        try {
            novelCover.value = await fileToBase64(file)
        } catch(error) {
            return Promise.reject(error)
        }
    }

    // ========= 设置类型 =========
    const novelType = ref<NovelType>('short')
    /**
     * 设置作品类型方法
     * @param type <string> - 作品类型 ('short'/'long')
     */
    const setType = (type: NovelType) => {
        novelType.value = type
    }

    // ========= 创建作品相关 =========
    const novelName = ref<string>('')
    const isloading = ref<boolean>(false)
    /**
     * 创建作品方法
     */
    const createNovel = async () => {
        // 检查是否设置作品名
        if (!novelName.value.trim()) {
            showDialog({context: '请设置作品名'})
            return
        }

        const data: CreateNovelRequest = {
            name: novelName.value,
            type: novelType.value
        }

        if (novelCover.value) {
            data.cover = novelCover.value
        }

        isloading.value = true
        try {
            await novelStore.createNovel(data)

            // 刷新作品
            await novelStore.getNovels()
        } catch(error) {
            return Promise.reject(error)
        } finally {
            isloading.value = false
            setTimeout(() => {
                emit('closeCreateModal') // 发出关闭事件
            }, 50)
            
        }
    }
</script>

<style scoped>
    .create-novel-container {
        height: 100%;
        width: 100%;
    }

    .top-control-bar {
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-bottom: 1px solid var(--supple-color);
        padding: 0 45px;
        user-select: none;
        gap: 25px;
    }

    .control-btn {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: 1px solid var(--primary-color);
        box-shadow: var(--btn-shadow);
        background-color: var(--supple-color);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .control-btn:hover {
        transform: scale(1.1);
    }

    .control-btn.toggle {
        background-color: var(--btn-bg-color);
    }

    .control-btn.toggle.is-delicate-modal {
        background-color: var(--supple-color);
    }

    /* 主内容区域 */
    .main-content {
        height: calc(100% - 64px);
        width: 100%;
        overflow: hidden;
        position: relative;
    }

    .wrapper {
        position: absolute;
        height: 100%;
        width: 50%;
        top: 0;
        transition: all 0.3s ease-in-out;
    }

    .wrapper.basic-setting {
        left: 25%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .wrapper.delicate-setting {
        left: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: var(--text-color);
    }

    .main-content.is-delicate-modal .wrapper.basic-setting {
        left: 0;
    }

    .main-content.is-delicate-modal .wrapper.delicate-setting {
        left: 50%;
    }
    
    /* 设置封面 */
    .wrapper.basic-setting .cover-wrapper {
        height: 300px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 25px;
    }

    .wrapper.basic-setting .cover-wrapper .novel-cover {
        height: 212px;
        width: 150px;
        background-color: rgba(25, 25, 25, 0.75);
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        color: var(--text-color);
        transition: all 0.3s ease;
        border: 1px solid var(--supple-color);
        position: relative;
    }

    .wrapper.basic-setting .cover-wrapper .novel-name {
        height: 25px;
        width: 200px;
        outline: none;
        background: transparent;
        border: none;
        border-bottom: 2px solid var(--supple-color);
        color: var(--text-color);
        text-align: center;
        font-family: 'Btn-text';
        font-size: 1rem;
        padding: 0 10px 10px;
    }

    .wrapper.basic-setting .cover-wrapper .novel-cover.have-cover {
        border: 3px solid var(--supple-color);
    }

    .wrapper.basic-setting .cover-wrapper .novel-cover label {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        cursor: pointer;
    }

    .wrapper.basic-setting .cover-wrapper .novel-cover img {
        height: 100%;
        width: 100%;
        border-radius: 12px;
        object-fit: cover;
    }

    .wrapper.basic-setting .cover-wrapper .novel-cover:hover {
        box-shadow: var(--btn-shadow-hover);
        transform: scale(1.05);
    }

    /* form容器 */
    .form-wrapper {
        flex: 1;
        width: 100%;
        padding: 15px;
        display: flex;
        flex-direction: column;
        gap: 25px;
        align-items: center;
    }

    /* 类型选择器 */
    .form-wrapper .type-select {
        width: 100%;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        padding: 0 25px;
    }

    .form-wrapper .type-select p {
        color: var(--primary-color);
        font-family: 'Btn-text';
        font-size: 1rem;
        letter-spacing: 0.1rem;
        user-select: none;
        display: flex;
        gap: 10px;
        align-items: center;
        justify-content: center;
    }

    .form-wrapper .type-select .select-container {
        display: flex;
        width: 200px;
        height: 80%;
        position: relative;
        align-items: center;
        
    }

    .form-wrapper .type-select .select-container p {
        height: 100%;
        width: 50%;
        z-index: 1;
        color: var(--text-color);
        font-size: 0.9rem;
        cursor: pointer;
    }

    .form-wrapper .type-select .select-container .mask {
        position: absolute;
        top: 0;
        left: 0;
        width: 50%;
        height: 100%;
        border-radius: 8px;
        transition: all 0.2s ease;
        background: linear-gradient(0deg, rgba(236, 96, 26, 0.5), transparent);
    }

    .form-wrapper .type-select .select-container .mask.is-long {
        left: 50%;
    }

    /* 概述输入框 */
    .form-wrapper .novel-overview {
        width: 80%;
        height: calc(100% - 75px);
        padding: 15px;
        border: 1px solid var(--supple-color);
        border-radius: 12px;
        background-color: rgba(35, 35, 35, 0.75);
        transition: box-shadow 0.3s ease;
    }

    .form-wrapper .novel-overview:focus-within {
        box-shadow: 0 0 8px var(--primary-color);
    }

    .form-wrapper .novel-overview textarea {
        background: transparent;
        resize: none;
        width: 100%;
        height: 100%;
        border: none;
        outline: none;
        color: var(--text-color);
        font-size: 0.9rem;
        overflow-x: hidden;
        overflow-y: auto;
    }

    .form-wrapper .novel-overview textarea::-webkit-scrollbar {
        width: 6px;
        background-color: transparent;
    }

    .form-wrapper .novel-overview textarea::-webkit-scrollbar-thumb {
        background-color: rgba(35, 35, 35, 0.9);
        border-radius: 12px;
        
    }

    /* 提交加载动画 */
    .load-layer {
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 100vw;
        background-color: rgba(0, 0, 0, 0.75);
        z-index: 100;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .orange-loader {
        width: 100px;
        height: 100px;
        position: relative;
    }

    /* 外部轨道 - 顺时针旋转 */
    .loader-outer {
        width: 100%;
        height: 100%;
        border: 4px solid rgba(75, 75, 75, 0.5); /* 浅橙色背景 */
        border-top: 4px solid var(--primary-color); /* 橙色的轨道部分 */
        border-radius: 50%;
        animation: rotate-outer 1.2s linear infinite;
    }

    /* 内部轨道 - 逆时针旋转 */
    .loader-inner {
        position: absolute;
        top: 20px;  /* 内圈比外圈小 */
        left: 20px;
        width: 60px;
        height: 60px;
        border: 3px solid rgba(255, 255, 255, 0.3); /* 浅白色背景 */
        border-top: 3px solid #ddd; /* 白色的轨道部分 */
        border-radius: 50%;
        animation: rotate-inner 0.8s linear infinite;
    }

    /* 动画定义 */
    @keyframes rotate-outer {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes rotate-inner {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(-360deg); } /* 负值表示逆时针 */
    }
</style>