<template>
    <div class="user-center-container">
        <!-- 用户信息卡 -->
        <div class="user-card float-card">
            <!-- 头像 -->
            <div class="avatar-wrapper">
                <AvatarPanel />
            </div>

            <!-- 用户信息 (昵称/邮箱/注册时间) -->
            <div class="info-wrapper">
                <InfoWrapper />
            </div>
        </div>
        <!-- 其他配置卡片容器 -->
        <div class="other-wrapper">
            <!-- 个人设置卡 -->
            <div class="setting card float-card">
                <!-- 标题 -->
                <div class="top-bar">
                    <div class="title">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4m0 6c-1.08 0-2-.92-2-2s.92-2 2-2 2 .92 2 2-.92 2-2 2"></path><path d="m20.42 13.4-.51-.29c.05-.37.08-.74.08-1.11s-.03-.74-.08-1.11l.51-.29c.96-.55 1.28-1.78.73-2.73l-1-1.73a2.006 2.006 0 0 0-2.73-.73l-.53.31c-.58-.46-1.22-.83-1.9-1.11v-.6c0-1.1-.9-2-2-2h-2c-1.1 0-2 .9-2 2v.6c-.67.28-1.31.66-1.9 1.11l-.53-.31c-.96-.55-2.18-.22-2.73.73l-1 1.73c-.55.96-.22 2.18.73 2.73l.51.29c-.05.37-.08.74-.08 1.11s.03.74.08 1.11l-.51.29c-.96.55-1.28 1.78-.73 2.73l1 1.73c.55.95 1.77 1.28 2.73.73l.53-.31c.58.46 1.22.83 1.9 1.11v.6c0 1.1.9 2 2 2h2c1.1 0 2-.9 2-2v-.6a8.7 8.7 0 0 0 1.9-1.11l.53.31c.95.55 2.18.22 2.73-.73l1-1.73c.55-.96.22-2.18-.73-2.73m-2.59-2.78c.11.45.17.92.17 1.38s-.06.92-.17 1.38a1 1 0 0 0 .47 1.11l1.12.65-1 1.73-1.14-.66c-.38-.22-.87-.16-1.19.14-.68.65-1.51 1.13-2.38 1.4-.42.13-.71.52-.71.96v1.3h-2v-1.3c0-.44-.29-.83-.71-.96-.88-.27-1.7-.75-2.38-1.4a1.01 1.01 0 0 0-1.19-.15l-1.14.66-1-1.73 1.12-.65c.39-.22.58-.68.47-1.11-.11-.45-.17-.92-.17-1.38s.06-.93.17-1.38A1 1 0 0 0 5.7 9.5l-1.12-.65 1-1.73 1.14.66c.38.22.87.16 1.19-.14.68-.65 1.51-1.13 2.38-1.4.42-.13.71-.52.71-.96v-1.3h2v1.3c0 .44.29.83.71.96.88.27 1.7.75 2.38 1.4.32.31.81.36 1.19.14l1.14-.66 1 1.73-1.12.65c-.39.22-.58.68-.47 1.11Z"></path>
                        </svg>
                        <h3>设置中心</h3>
                    </div>
                </div>

                <!-- 内容 -->
                <div class="context">
                </div>
            </div>
            <!-- 安全中心卡 -->
            <div class="security card float-card">
                <!-- 标题 -->
                <div class="top-bar">
                    <div class="title">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="m20.42 6.11-7.97-4c-.28-.14-.62-.14-.9 0l-7.97 4c-.31.15-.51.45-.55.79-.01.11-.96 10.76 8.55 15.01a.98.98 0 0 0 .82 0C21.91 17.66 20.97 7 20.95 6.9a.98.98 0 0 0-.55-.79ZM12 19.9C5.26 16.63 4.94 9.64 5 7.64l7-3.51 7 3.51c.04 1.99-.33 9.02-7 12.26"></path><path d="m11 12.59-1.29-1.3-1.42 1.42 2.71 2.7 4.71-4.7-1.42-1.42z"></path>
                        </svg>
                        <h3>安全中心</h3>
                    </div>
                    <transition name="fade" mode="out-in">
                        <p v-if="itemName">{{ itemName }}</p>
                    </transition>
                </div>

                <!-- 内容 -->
                <div class="context">
                    <!-- 修改密码 -->
                    <div class="item" @mouseenter="displayName('修改密码')" @mouseleave="displayName(null)" @click="changePassword">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M7 7c-2.76 0-5 2.24-5 5s2.24 5 5 5c2.41 0 4.43-1.72 4.9-4H15v2h2v-2h2v3h2v-3h1v-2H11.9A5 5 0 0 0 7 7m0 8c-1.65 0-3-1.35-3-3s1.35-3 3-3 3 1.35 3 3-1.35 3-3 3"></path>
                        </svg>
                    </div>
                    <!-- 退出登录 -->
                    <div class="item" @mouseenter="displayName(' 退出登录')" @mouseleave="displayName(null)" @click="logoutFunc">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M15 11H8v2h7v4l6-5-6-5zM4 4h2v16H4z"></path>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import AvatarPanel from '@/components/home/userCenter/AvatarPanel.vue'
    import InfoWrapper from '@/components/home/userCenter/InfoWrapper.vue'
    import useUserStore from '@/stores/userSotre'
    import { showDialog } from '@/utils/showDoalog'

    const userStore = useUserStore()
    const router = useRouter()

    // ========= 安全中心相关 =========
    const itemName = ref<string | null>(null)
    /**
     * 修改要显示的item名称
     * @param name 显示的itme名称
     */
    const displayName = (name: string | null) => {
        itemName.value = name
    }
    
    /**
     * 退出登录方法
     */
    const logoutFunc = () => {
        showDialog({
            context: '确定要退出登录吗?',
            onConfirm: async () => {
                router.replace('/')
                userStore.logout()
            }
        })
    }

    /**
     * 修改密码方法
     */
    const changePassword = async () => {
        showDialog({
            context: '开发中'
        })
    }
</script>

<style scoped>
    .user-center-container {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    /* 用户卡片 */
    .user-card {
        width: 300px;
        height: 300px;
        display: flex;
        flex-direction: column;
        padding: 30px 15px 15px;
    }

    .user-card .avatar-wrapper {
        width: 100%;
    }

    .user-card .info-wrapper {
        width: 100%;
        flex: 1;
    }

    /* 其他配置卡片容器 */
    .other-wrapper {
        display: flex;
        flex-direction: column;
        height: 300px;
        width: 300px;
        gap: 15px;
    }

    /* 设置卡片 */
    .card {
        width: 100%;
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 0 5px;
    }

    .card .top-bar {
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 15px;
        font-size: 0.8rem;
        font-family: 'Btn-text';
        letter-spacing: 0.1rem;
        border-bottom: 1px solid var(--supple-color);
        position: relative;
        overflow-x: hidden;
        color: var(--primary-color);
    }

    .card .top-bar::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: -100%;  /* 初始位置在左边看不见的地方 */
        width: 100%;
        height: 2px;  /* 边框粗细 */
        background: linear-gradient(90deg, 
            transparent, 
            var(--primary-color), 
            transparent
        );
        animation: flowBorder 2s ease-in-out infinite;
    }
    
    @keyframes flowBorder {
        0% {
            left: -100%;
        }
        100% {
            left: 100%;
        }
    }
    
    .card .top-bar .title {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .card .top-bar p {
        color: var(--text-color);
    }

    .card .context {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        padding: 15px 15px;
        grid-auto-rows: auto;
    }

    .card .context .item {
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        height: 32px;
        width: 32px;
        color: var(--text-color);
        background: var(--btn-bg-color);
        border: 1px solid rgba(194, 87, 34, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .card .context .item:hover {
        transform: scale(1.2);
        box-shadow: var(--btn-shadow);
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.5s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }
</style>