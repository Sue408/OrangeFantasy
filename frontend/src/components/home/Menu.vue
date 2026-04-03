<template>
    <div class="menu-container">
        <div class="menu-wrapper float-card" @mouseenter="isOpen = true" @mouseleave="isOpen = false"  :class="{ open: isOpen }">
            <!-- 菜单图标 -->
            <div class="menu-icon">
                <svg  xmlns="http://www.w3.org/2000/svg" width="32" height="32"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M3 5h18v2H3zm0 6h18v2H3zm0 6h18v2H3z"></path>
                </svg>
            </div>
            <!-- 导航项目 -->
            <div class="menu-item-wrapper">
                <!-- 用户中心 -->
                <div class="menu-item" :class="{ active: isActiveRoute('UserCenter') }" @click="routerLeap('UserCenter')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="28" height="28"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M12 7c-2 0-3.5 1.5-3.5 3.5S10 14 12 14s3.5-1.5 3.5-3.5S14 7 12 7m0 5c-.88 0-1.5-.62-1.5-1.5S11.12 9 12 9s1.5.62 1.5 1.5S12.88 12 12 12"></path><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2M8.18 19c.41-1.16 1.51-2 2.82-2h2c1.3 0 2.4.84 2.82 2H8.19Zm9.71 0a5 5 0 0 0-4.9-4h-2c-2.41 0-4.43 1.72-4.9 4h-1.1V5h14v14z"></path>
                    </svg>
                </div>

                <!-- 我的作品 -->
                <div class="menu-item" :class="{ active: isActiveRoute('MyNovels') }" @click="routerLeap('MyNovels')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="28" height="28"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M9 3h2v18H9zm11.71 17.23-3.8-8.15-3.81-8.16-.9.42-.91.43 3.8 8.15 3.81 8.16.9-.42zM6 3h2v18H6zM3 3h2v18H3z"></path>
                    </svg>
                </div>

                <!-- 个人设置 -->
                <div class="menu-item" @click="routerLeap('UserCenter')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="28" height="28"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4m0 6c-1.08 0-2-.92-2-2s.92-2 2-2 2 .92 2 2-.92 2-2 2"></path><path d="m20.42 13.4-.51-.29c.05-.37.08-.74.08-1.11s-.03-.74-.08-1.11l.51-.29c.96-.55 1.28-1.78.73-2.73l-1-1.73a2.006 2.006 0 0 0-2.73-.73l-.53.31c-.58-.46-1.22-.83-1.9-1.11v-.6c0-1.1-.9-2-2-2h-2c-1.1 0-2 .9-2 2v.6c-.67.28-1.31.66-1.9 1.11l-.53-.31c-.96-.55-2.18-.22-2.73.73l-1 1.73c-.55.96-.22 2.18.73 2.73l.51.29c-.05.37-.08.74-.08 1.11s.03.74.08 1.11l-.51.29c-.96.55-1.28 1.78-.73 2.73l1 1.73c.55.95 1.77 1.28 2.73.73l.53-.31c.58.46 1.22.83 1.9 1.11v.6c0 1.1.9 2 2 2h2c1.1 0 2-.9 2-2v-.6a8.7 8.7 0 0 0 1.9-1.11l.53.31c.95.55 2.18.22 2.73-.73l1-1.73c.55-.96.22-2.18-.73-2.73m-2.59-2.78c.11.45.17.92.17 1.38s-.06.92-.17 1.38a1 1 0 0 0 .47 1.11l1.12.65-1 1.73-1.14-.66c-.38-.22-.87-.16-1.19.14-.68.65-1.51 1.13-2.38 1.4-.42.13-.71.52-.71.96v1.3h-2v-1.3c0-.44-.29-.83-.71-.96-.88-.27-1.7-.75-2.38-1.4a1.01 1.01 0 0 0-1.19-.15l-1.14.66-1-1.73 1.12-.65c.39-.22.58-.68.47-1.11-.11-.45-.17-.92-.17-1.38s.06-.93.17-1.38A1 1 0 0 0 5.7 9.5l-1.12-.65 1-1.73 1.14.66c.38.22.87.16 1.19-.14.68-.65 1.51-1.13 2.38-1.4.42-.13.71-.52.71-.96v-1.3h2v1.3c0 .44.29.83.71.96.88.27 1.7.75 2.38 1.4.32.31.81.36 1.19.14l1.14-.66 1 1.73-1.12.65c-.39.22-.58.68-.47 1.11Z"></path>
                    </svg>
                </div>

                <!-- 默认首页 -->
                <div class="menu-item" :class="{ active: isActiveRoute('Introduce') }" @click="routerLeap('Introduce')">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="28" height="28"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M3 13h1v7c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-7h1c.4 0 .77-.24.92-.62.15-.37.07-.8-.22-1.09l-8.99-9a.996.996 0 0 0-1.41 0l-9.01 9c-.29.29-.37.72-.22 1.09s.52.62.92.62Zm7 7v-5h4v5zm2-15.59 6 6V20h-2v-5c0-1.1-.9-2-2-2h-4c-1.1 0-2 .9-2 2v5H6v-9.59z"></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { computed, ref } from 'vue'
    import { useRoute, useRouter } from 'vue-router'

    const isOpen = ref<boolean>(false)
    const router = useRouter()
    const route = useRoute()

    const currentRouteName = computed(() => route.name || '')

    /**
     * 判断输入路由名称是否为当前路由
     * @param routeName - 需要判断的路由名称
     */
    const isActiveRoute = (routeName: string) => {
        return currentRouteName.value === routeName
    }

    /**
     * 页面跳转封装
     * @param name <string> - 路由名称
     */
    const routerLeap = (name: string): void => {
        if (name === 'Auth') {
            router.push({name})
        } else {
            router.replace({name})
        }
    }
</script>

<style scoped>
    .menu-container {
        width: 100%;
        height: 100%;
        position: relative;
    }

    .menu-wrapper {
        width: 48px;
        height: 48px;
        display: flex;
        flex-direction: column;
        position: relative;
        color: var(--text-color);
        overflow: hidden;
        transition: all 0.3s ease;
        margin-top: 20px;
        margin-left: 10px;
        border: 1px solid var(--primary-color);
    }

    .menu-wrapper.open {
        height: 250px;
        border: none;
    }

    .menu-icon {
        position: absolute;
        top: 0;
        left: 0;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .menu-item-wrapper {
        position: absolute;
        top: 48px;
        height: 100%;
        width: 100%;
        padding-top: 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        border-top: 2px solid var(--supple-color);
    }

    .menu-item {
        transition: all 0.3s ease;
        position: relative;  /* 给光晕一个定位的家 */
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .menu-item:not(.active) {
        cursor: pointer;
    }

    .menu-item:not(.active):hover {
        color: var(--primary-color);
        transform: scale(1.2);
    }

    .menu-item.active {
        transform: scale(1.25);
    }

    .menu-item.active::after {
        content: '';  /* 伪元素必须有的“存在证明” */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 40px; 
        height: 40px;
        border-radius: 50%;
        background: radial-gradient(
            circle at center,
            var(--primary-color) 0%,
            transparent 70%
        );
        opacity: 0.9;
        z-index: -1;
    }
</style>