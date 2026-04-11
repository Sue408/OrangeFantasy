<template>
    <div class="control-panel-container">
        <!-- 导航栏 -->
        <div class="nav-bar">
            <!-- 头像 -->
            <div class="avatar-wrapper" @click="goToUserCenter">
                <img v-if="userStore.userInfo?.avatar" :src="userStore.userInfo.avatar" :alt="userStore.userInfo.nickname || 'avatar'" class="avatar-img" />
                <div v-else class="avatar-placeholder">{{ userStore.userInfo?.nickname?.charAt(0).toUpperCase() || 'U' }}</div>
            </div>

            <!-- 导航项目 -->
            <div class="nav-item-wrapper">
                <!-- 章节信息 -->
                <button class="nav-item" :class="{ active: controlModal === 'Chapters' }" @click="setControlModal('Chapters')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M21 3h-7c-.77 0-1.47.3-2 .78-.53-.48-1.23-.78-2-.78H3c-.55 0-1 .45-1 1v15c0 .55.45 1 1 1h5.76c.53 0 1.04.21 1.41.59l1.12 1.12s.02.01.03.02c.09.08.18.15.29.2.12.05.25.08.38.08s.26-.03.38-.08c.11-.05.21-.12.29-.2 0 0 .02-.01.03-.02l1.12-1.12c.37-.37.89-.59 1.41-.59h5.76c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1ZM8.76 18H4V5h6c.55 0 1 .45 1 1v12.69c-.66-.44-1.44-.69-2.24-.69M20 18h-4.76c-.8 0-1.58.25-2.24.69V6c0-.55.45-1 1-1h6z"></path>
                    </svg>
                </button>

                <button class="nav-item" :class="{ active: controlModal === 'B' }" @click="setControlModal('B')">

                </button>
                <button class="nav-item" :class="{ active: controlModal === 'C' }" @click="setControlModal('C')">

                </button>
            </div>

            <!-- 返回按钮 -->
            <button class="nav-item leave" @click="leaveFunc">
                <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M5 5h7V3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h7v-2H5z"></path><path d="m14 7-6 5 6 5v-4h7v-2h-7z"></path>
                </svg>
            </button>
        </div>

        <!-- 设置内容区 -->
        <div class="control-content">
            <transition name="fade" mode="out-in">
                <div v-if="controlModal === 'Chapters'" class="control-wrapper">
                    <InfoAndChapters :novel="novel" :infoIsHide="infoIsHide" @toggleInfoHide="infoIsHide = !infoIsHide" />
                </div>

                <div v-else-if="controlModal === 'B'" class="control-wrapper">
                    控制面板B
                </div>

                <div v-else class="control-wrapper">
                    控制面板C
                </div>
            </transition>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { ref } from 'vue'
    import useUserStore from '@/stores/userSotre'
    import { useRouter } from 'vue-router'
    import type { NovelMeta } from '@/types/novelTypes'
    import InfoAndChapters from './InfoAndChapters.vue'

    const userStore = useUserStore()
    const router = useRouter()
    // ========= props插槽 =========
    const props = defineProps<{
        novel: NovelMeta
    }>()

    // ========= 跳转方法 =========
    type ControlModal = 'Chapters' | 'B' | 'C'
    const controlModal = ref<ControlModal>('Chapters')
    /**
     * 修改当前control模式
     */
    const setControlModal = (modal: ControlModal) => {
        controlModal.value = modal
    }
    /**
     * 跳转到user-center页面
     */
    const goToUserCenter = () => {
        router.replace({name: 'UserCenter'})
    }
    /**
     * 返回my-novels页面
     */
    const leaveFunc = () => {
        router.replace({name: 'MyNovels'})
    }

    // ========= infoAndChapters组件折叠控制 =========
    const infoIsHide = ref<boolean>(false)
</script>

<style scoped>
    .control-panel-container {
        width: 100%;
        height: 100%;
        display: flex;
    }

    /* 导航栏 */
    .nav-bar {
        height: 100%;
        width: 75px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        border-right: 2px solid var(--supple-color);
        background-color: rgba(35, 35, 35, 0.5);
        padding: 15px 0;
    }

    .nav-bar .avatar-wrapper {
        width: 48px;
        height: 48px;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .nav-bar .avatar-wrapper:hover {
        transform: scale(1.1);
    }

    .nav-bar .avatar-wrapper img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
        border: 2px solid rgba(194, 87, 34, 0.5);
    }

    .nav-bar .avatar-wrapper .avatar-placeholder {
        background-color: #222;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 2px solid rgba(194, 87, 34, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        font-size: 1.25rem;
        font-weight: 600;
    }

    .nav-bar .nav-item {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        background-color: var(--btn-bg-color);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .nav-bar .nav-item.leave {
        border: 1px solid var(--primary-color);
    }

    .nav-bar .nav-item:hover {
        transform: scale(1.1);
        color: #fff;
        box-shadow: var(--btn-shadow-hover);
    }

    /* 导航子项容器 */
    .nav-bar .nav-item-wrapper {
        width: 100%;
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    .nav-bar .nav-item-wrapper .nav-item.active {
        background-color: rgba(194, 87, 34, 0.75);
        box-shadow: var(--btn-shadow);
    }

    /* 设置内容区 */
    .left-wrapper .control-content {
        flex: 1;
        height: 100%;
    }

    .left-wrapper .control-content .control-wrapper {
        width: 100%;
        height: 100%;

        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        font-size: 1.5rem;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.3s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }
</style>