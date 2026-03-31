<template>
    <div class="top-bar-container">
        <!-- LOGO -->
        <div class="logo-wrapper" @click="routerLeap('Introduce')">
            <h3>OrangeFantasy</h3>
        </div>

        <!-- 用户头像 or 登录/注册按钮 -->
        <div class="user-wrapper">
            <!-- 用户头像 -->
            <div class="avatar-wrapper" v-if="userStore.isLogged" @click="routerLeap('UserCenter')">
                <img v-if="userStore.userInfo?.avatar" :src="userStore.userInfo.avatar" :alt="userStore.userInfo.nickname || 'avatar'" class="avatar-img" />
                <div v-else class="avatar-placeholder">{{ userStore.userInfo?.nickname?.charAt(0) || 'U' }}</div>
            </div>

            <!-- 登录按钮 -->
            <div class="auth-wrapper" v-else>
                <button class="auth-btn small-btn" @click="routerLeap('Auth')">登录/注册</button>
            </div>

        </div>
    </div>
</template>

<script setup lang='ts'>
    import { useRouter } from 'vue-router'
    import useUserStore from '@/stores/userSotre'

    const userStore = useUserStore()
    const router = useRouter()

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
    .top-bar-container {
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px 0 30px;
        user-select: none;
    }

    .logo-wrapper h3 {
        color: var(--primary-color);
        font-size: 1.25rem;
        font-weight: 1200;
        letter-spacing: 0.2rem;
        font-family: 'Title';
        cursor: pointer;
    }

    .user-wrapper {
        cursor: pointer;
    }

    /* 登录/注册按钮 */
    .auth-wrapper .auth-btn {
        border-radius: var(--btn-border-radius);
        background-color: var(--btn-bg-color);
        color: var(--btn-text-color);
        font-size: 0.82rem;
        font-family: 'Btn-Text';
        letter-spacing: 0.04rem;
        cursor: pointer;
        transition: var(--transition-smooth);
    }

    .auth-wrapper .auth-btn:hover {
        box-shadow: var(--btn-shadow-hover);
        transform: translateY(-1px);
    }

    .auth-wrapper .auth-btn:active {
        background-color: var(--btn-bg-active);
        box-shadow: none;
        transform: translateY(0);
    }

    /* 用户头像 */
    .avatar-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: #222;
        border: 1px solid rgba(194, 87, 34, 0.3);
        overflow: hidden;
    }

    .avatar-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .avatar-placeholder {
        font-size: 0.9rem;
        font-weight: 600;
        color: var(--primary-color);
        text-transform: uppercase;
    }
</style>