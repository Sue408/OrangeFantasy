<template>
    <div class="auth-container">
        <div class="form-wrapper float-card">
            <!-- 滑动窗口 -->
            <div class="slip-card" :class="{ 'login-model': loginModel}">
                <div class="mask-card"></div>

                <div class="content-card">
                    <transition name="fade" mode="out-in">
                        <div v-if="loginModel">
                            <h3>还没有账号？</h3>
                            <button @click="toggle">去注册</button>
                        </div>
                        <div v-else>
                            <h3>已有账号？</h3>
                            <button @click="toggle">去登录</button>
                        </div>
                    </transition>
                </div>
            </div>

            <!-- 注册表单 -->
            <div class="register form-card" :class="{ 'login-model': loginModel}">
                <!-- 标题 -->
                <div class="title">
                    <h3>REGISTER</h3>
                </div>

                <!-- 表单内容 -->
                <form>
                    <!-- 账号 -->
                    <div class="form-group">
                        <label for="reg-username"></label>
                        <input id="reg-username" v-model="registerForm.username" type="text" placeholder="账号">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M12 12c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5m0-8c1.65 0 3 1.35 3 3s-1.35 3-3 3-3-1.35-3-3 1.35-3 3-3M4 22h16c.55 0 1-.45 1-1v-1c0-3.86-3.14-7-7-7h-4c-3.86 0-7 3.14-7 7v1c0 .55.45 1 1 1m6-7h4c2.76 0 5 2.24 5 5H5c0-2.76 2.24-5 5-5"></path>
                            </svg>
                        </span>
                    </div>

                    <!-- 邮箱 -->
                     <div class="form-group">
                        <label for="email"></label>
                        <input id="email" v-model="registerForm.email" type="text" placeholder="注册邮箱">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2m0 2v.51l-8 6.22-8-6.22V6zM4 18V9.04l7.39 5.74c.18.14.4.21.61.21s.43-.07.61-.21L20 9.03v8.96H4Z"></path>
                            </svg>
                        </span>
                    </div>

                    <!-- 密码 -->
                     <div class="form-group">
                        <label for="reg-password"></label>
                        <input id="reg-password" v-model="registerForm.password" type="password" placeholder="密码 (6位)">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M8 21c2.76 0 5-2.24 5-5 0-1.02-.31-1.96-.83-2.75l3.33-3.33 1.79 1.79 1.41-1.41-1.79-1.79L18 7.42l2.29 2.29L21.7 8.3l-2.29-2.29 1.29-1.29-1.41-1.41-8.54 8.54c-.79-.52-1.74-.83-2.75-.83-2.76 0-5 2.24-5 5s2.24 5 5 5Zm0-8c1.65 0 3 1.35 3 3s-1.35 3-3 3-3-1.35-3-3 1.35-3 3-3"></path>
                            </svg>
                        </span>
                    </div>

                    <!-- 确认密码 -->
                     <div class="form-group">
                        <label for="confirm-password"></label>
                        <input id="confirm-password" v-model="registerForm.confirmPassword" type="password" placeholder="确认密码">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M6 22h12c1.1 0 2-.9 2-2v-9c0-1.1-.9-2-2-2h-1V7c0-2.76-2.24-5-5-5S7 4.24 7 7v2H6c-1.1 0-2 .9-2 2v9c0 1.1.9 2 2 2M9 7c0-1.65 1.35-3 3-3s3 1.35 3 3v2H9zm-3 4h12v9h-5v-2.28c.59-.35 1-.99 1-1.72 0-1.1-.9-2-2-2s-2 .9-2 2a2 2 0 0 0 1 1.72V20H6z"></path>
                            </svg>
                        </span>
                    </div>

                    <!-- 验证码 -->
                     <div class="form-group">
                        <label for="verify-code"></label>
                        <input id="verify-code" v-model="registerForm.verifyCode" type="text" placeholder="邮箱验证码">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M19 9.09V6c0-.55-.45-1-1-1h-3.09L12.7 2.79a.996.996 0 0 0-1.41 0L9.08 5H5.99c-.55 0-1 .45-1 1v3.09L2.78 11.3a.996.996 0 0 0 0 1.41l2.21 2.21v3.09c0 .55.45 1 1 1h3.09l2.21 2.21c.2.2.45.29.71.29s.51-.1.71-.29l2.21-2.21h3.09c.55 0 1-.45 1-1v-3.09l2.21-2.21a.996.996 0 0 0 0-1.41l-2.21-2.21Zm-1.71 4.71a1 1 0 0 0-.29.71v2.5h-2.5c-.27 0-.52.11-.71.29L12 19.09l-1.79-1.79a1 1 0 0 0-.71-.29H7v-2.5c0-.27-.11-.52-.29-.71l-1.79-1.79 1.79-1.79A1 1 0 0 0 7 9.51v-2.5h2.5c.27 0 .52-.11.71-.29L12 4.93l1.79 1.79c.19.19.44.29.71.29H17v2.5c0 .27.11.52.29.71l1.79 1.79z"></path><path d="m11 12.59-1.29-1.3-1.42 1.42 2.71 2.7 4.71-4.7-1.42-1.42z"></path>
                            </svg>
                        </span>
                    </div>
                </form>

                <!-- 提交按钮 -->
                <button @click="handleRegister" :disabled="isLoading">{{ errorMessage || '注册' }}</button>
            </div>

            <!-- 登录表单 -->
            <div class="login form-card" :class="{ 'login-model': loginModel}">
                <!-- 标题 -->
                <div class="title">
                    <h3>LOGIN</h3>
                </div>

                <!-- 表单内容 -->
                <form>
                    <!-- 账号 -->
                    <div class="form-group">
                        <label for="login-username"></label>
                        <input id="login-username" v-model="loginForm.username" type="text" placeholder="账号">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M12 12c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5m0-8c1.65 0 3 1.35 3 3s-1.35 3-3 3-3-1.35-3-3 1.35-3 3-3M4 22h16c.55 0 1-.45 1-1v-1c0-3.86-3.14-7-7-7h-4c-3.86 0-7 3.14-7 7v1c0 .55.45 1 1 1m6-7h4c2.76 0 5 2.24 5 5H5c0-2.76 2.24-5 5-5"></path>
                            </svg>
                        </span>
                    </div>

                    <!-- 密码 -->
                    <div class="form-group">
                        <label for="login-password"></label>
                        <input id="login-password" v-model="loginForm.password" type="password" placeholder="密码">
                        <span>
                            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                            fill="currentColor" viewBox="0 0 24 24" >
                            <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                            <path d="M8 21c2.76 0 5-2.24 5-5 0-1.02-.31-1.96-.83-2.75l3.33-3.33 1.79 1.79 1.41-1.41-1.79-1.79L18 7.42l2.29 2.29L21.7 8.3l-2.29-2.29 1.29-1.29-1.41-1.41-8.54 8.54c-.79-.52-1.74-.83-2.75-.83-2.76 0-5 2.24-5 5s2.24 5 5 5Zm0-8c1.65 0 3 1.35 3 3s-1.35 3-3 3-3-1.35-3-3 1.35-3 3-3"></path>
                            </svg>
                        </span>
                    </div>
                </form>

                <!-- 第三方登录接口 -->
                <div class="third-card">
                    <div v-for="setting in thirdLoginSettings" class="item" v-html="setting.logo"></div>
                </div>

                <!-- 提交按钮 -->
                <button @click="handleLogin" :disabled="isLoading">{{ errorMessage || '登录' }}</button>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { reactive, ref, onUnmounted } from 'vue'
    import { useRouter } from 'vue-router'
    import useUserStore from '@/stores/userSotre'
    import errorParser from '@/utils/errorParser'
    import Background from '@/components/auth/Background.vue'

    // 实例化router, user store
    const router = useRouter()
    const userStore = useUserStore()

    // 表单数据
    // 1. 登录表单数据绑定
    const loginForm = reactive({
        username: '',
        password: ''
    })
    // 2. 注册表单数据绑定
    const registerForm = reactive({
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        verifyCode: ''
    })

    // 登录/注册模式切换功能
    const loginModel = ref<boolean>(true)
    const toggle = () => {
        loginModel.value = !loginModel.value
        errorMessage.value = ''
    }

    // 错误处理
    const errorMessage = ref<string>('')
    const isLoading = ref<boolean>(false)
    let errorTimer: ReturnType<typeof setTimeout> | null = null

    const showError = (msg: string) => {
        errorMessage.value = msg
        if (errorTimer) clearTimeout(errorTimer)
        errorTimer = setTimeout(() => {
            errorMessage.value = ''
        }, 1500) // 显示1.5s
    }

    // 表单验证逻辑 (兼容注册/登录逻辑)
    const validateForm = (isRegister: boolean): string | null => {
        if (isRegister) {
            if (!registerForm.username) return '账号不能为空'
            if (!registerForm.email) return '邮箱不能为空'
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(registerForm.email)) return '邮箱格式不正确'
            if (!registerForm.password) return '密码不能为空'
            if (registerForm.password.length < 6) return '密码至少6位'
            if (!registerForm.confirmPassword) return '确认密码不能为空'
            if (registerForm.password !== registerForm.confirmPassword) return '两次密码不一致'
            if (!registerForm.verifyCode) return '验证码不能为空'
        } else {
            if (!loginForm.username) return '账号不能为空'
            if (!loginForm.password) return '密码不能为空'
            if (loginForm.password.length < 6) return '密码至少6位'
        }
        return null
    }

    // 登录逻辑实现
    const handleLogin = async () => {
        // 执行登录表单验证
        const error = validateForm(false)
        if (error) {
            // 展示错误信息
            showError(error)
            return
        }

        // 设置loading状态
        isLoading.value = true
        try {
            // 调用登录接口并执行路由跳转
            await userStore.login(loginForm.username, loginForm.password)
            router.replace('/')
        } catch (error: any) {
            const msg = errorParser(error)
            showError(msg)
        } finally {
            // 移除loading状态
            isLoading.value = false
        }
    }

    // 注册逻辑实现
    const handleRegister = async () => {
        // 执行注册表单验证
        const error = validateForm(true)
        if (error) {
            showError(error)
            return
        }

        isLoading.value = true
        try {
            await userStore.register(registerForm.email, registerForm.username, registerForm.password)
            router.replace('/')
        } catch (err: any) {
            const msg = errorParser(error)
            showError(msg)
        } finally {
            isLoading.value = false
        }
    }

    // 组件卸载的时候自动删除定时器对象
    onUnmounted(() => {
        if (errorTimer) clearTimeout(errorTimer)
    })

    // 第三方登录设置
    interface ThirdLoginSetting {
        name: string,
        logo: string
    }
    const thirdLoginSettings: ThirdLoginSetting[] = [
        {
            name: 'phone',
            logo: `<svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M18.07 22h.35c.47-.02.9-.26 1.17-.64l2.14-3.09c.23-.33.32-.74.24-1.14s-.31-.74-.64-.97l-4.64-3.09a1.47 1.47 0 0 0-.83-.25c-.41 0-.81.16-1.1.48l-1.47 1.59c-.69-.43-1.61-1.07-2.36-1.82-.72-.72-1.37-1.64-1.82-2.36l1.59-1.47c.54-.5.64-1.32.23-1.93L7.84 2.67c-.22-.33-.57-.57-.97-.64a1.46 1.46 0 0 0-1.13.24L2.65 4.41c-.39.27-.62.7-.64 1.17-.03.69-.16 6.9 4.68 11.74 4.35 4.35 9.81 4.69 11.38 4.69ZM6.88 10.05c-.16.15-.21.39-.11.59.05.09 1.15 2.24 2.74 3.84 1.6 1.6 3.75 2.7 3.84 2.75.2.1.44.06.59-.11l1.99-2.15 3.86 2.57-1.7 2.46c-1.16 0-6.13-.24-9.99-4.1S4 7.06 4 5.91l2.46-1.7 2.57 3.86-2.15 1.99Z"></path>
                    </svg>`
        }
    ]
</script>

<style scoped>
    .auth-container {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .form-wrapper {
        position: relative;
        height: 60%;
        width: 60%;
        min-height: 300px;
        min-width: 450px;
        overflow: hidden;
        display: flex;
        z-index: 10;
    }

    /* 滑动窗口 */
    .slip-card {
        position: absolute;
        height: 100%;
        width: 100%;
        pointer-events: none;
        z-index: 1000;
    }

    .slip-card .mask-card {
        position: absolute;
        height: 100%;
        width: 200%;
        background: var(--supple-color);
        right: 50%;
        transition: all 1.2s ease-in-out;
    }

    .slip-card .content-card {
        position: absolute;
        height: 100%;
        width: 50%;
        right: 50%;
        transition: all 1.2s ease;
        transition-delay: 0.3s;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        pointer-events: auto;
    }

    .slip-card:not(.login-model) .mask-card {
        right: -150%;
    }

    .slip-card:not(.login-model) .content-card {
        right: 0;
    }

    .content-card div {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        color: var(--text-color);
        font-size: 1.4rem;
    }

    .content-card div h3 {
        user-select: none;
    }

    .content-card div button {
        background: transparent;
        border: none;
        cursor: pointer;
        font-family: 'Btn-Text';
        font-size: 1.25rem;
        color: var(--text-color);
        border-bottom: 1px solid #ccc;
        transition: var(--transition-smooth);
    }

    .content-card div button:hover {
        color: #fff;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.6s ease;
        transition-delay: 0.3s;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    /* 登录/注册表单 */
    .form-card {
        width: 100%;
        padding: 15px;
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 30px 45px;
        align-items: center;
        transition: opacity 0.3s ease;
    }

    .form-card.register.login-model {
        opacity: 0;
    }

    .form-card.login:not(.login-model) {
        opacity: 0;
    }

    .form-card .title {
        padding-bottom: 15px;
        margin-bottom: 30px;
        border-bottom: 1px solid #fff;
        user-select: none;
    }

    .form-card.login .title {
        margin-bottom: 60px;
    }

    .form-card .title h3 {
        font-family: 'Title';
        color: var(--primary-color);
        font-size: 2rem;
        letter-spacing: 0.25rem;
    }

    .form-card form {
        display: flex;
        width: 100%;
        flex-direction: column;
        gap: 15px;
        margin-bottom: 20px;
    }

    .form-card.login form {
        gap: 40px;
    }

    .form-card.login .third-card {
        margin-bottom: 20px;
    }

    form .form-group {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }

    form .form-group input {
        border-radius: var(--input-border-radius);
        height: 35px;
        width: 100%;
        outline: none;
        padding: 0 40px 0 10px;
        font-family: 'Btn-Text';
        color: var(--input-text-color);
        background: var(--input-bg-color);
        border: 2px solid var(--primary-color);
        transition: all 0.3s ease;
    }

    form .form-group input::placeholder {
        color: #999;
    }

    form .form-group input:focus {
        box-shadow: var(--input-box-shadow);
    }

    form .form-group span {
        color: var(--input-text-color);
        position: absolute;
        right: 15px;
        top: calc(50% - 12px)
    }

    /* 提交按钮 */
    .form-card button {
        width: 80%;
        height: 40px;
        border-radius: var(--btn-border-radius);
        background-color: var(--btn-bg-color-light);
        font-family: 'Btn-Text';
        font-size: 1.1rem;
        cursor: pointer;
        transition: var(--transition-smooth);
        color: var(--btn-text-color-light);
        border: none;
    }

    .form-card button:hover:not(:disabled) {
        transform: translateY(-1px);
        box-shadow: var(--input-box-shadow);
    }

    .form-card button:active:not(:disabled) {
        transform: translateY(0px);
        background-color: var(--btn-bg-active);
    }

    .form-card button:disabled {
        opacity: 0.7;
        cursor: not-allowed;
    }

    /* 第三方登录 */
    .third-card {
        display: flex;
        gap: 15px;
    }

    .third-card .item {
        width: 36px;
        height: 36px;
        background: var(--input-bg-color);
        border-radius: var(--input-border-radius);
        color: var(--input-text-color);
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>