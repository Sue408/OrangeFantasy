<template>
    <div class="info-container">
        <!-- 用户昵称 -->
        <div class="nickname-wrapper">
            <div class="nickname-context">
                <p v-if="!isEditModal" @click="openEditModal">{{ userStore.userInfo?.nickname || '未知' }}</p>
                <input v-else type="text" ref="inputRef" v-model="editNickname" @keydown.enter="uploadNickname">
            </div>
            <transition name="fade" mode="out-in">
                <div v-if="isEditModal" class="btn-wrapper">
                    <button class="confirm-btn btn" @click="uploadNickname">√</button>
                    <button class="cancel-btn btn" @click="closeEditModal">x</button>
                </div>
            </transition>
        </div>

        <!-- 其他基本信息 -->
        <div class="other-info-wrapper">
            <!-- 邮箱 -->
            <div class="item">
                <p>{{ userStore.userInfo?.email || 'unknown' }}</p>
            </div>

            <!-- 注册时间 -->
            <div class="item">
                <p>{{ userStore.userInfo?.created_at ? formatDate(userStore.userInfo?.created_at) : 'unknown' }}</p>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { ref, nextTick } from 'vue'
    import useUserStore from '@/stores/userSotre'
    import formatDate from '@/utils/formatData'

    const userStore = useUserStore()

    const isEditModal = ref<boolean>(false)
    const editNickname = ref<string>('')
    const inputRef = ref<HTMLInputElement | null>(null) // 绑定input对象
    /**
     * 进入编辑模式
     */
    const openEditModal = (event: MouseEvent) => {
        event.stopPropagation() // 阻止事件冒泡
        editNickname.value = userStore.userInfo?.nickname || ''
        isEditModal.value = true

        nextTick(() => {
            inputRef.value?.focus() // 自动聚焦输入框
            // 添加点击事件
            document.addEventListener('click', handleClickOutside)
        })
    }

    /**
     * 关闭编辑模式
     */
    const closeEditModal = () => {
        editNickname.value = ''
        isEditModal.value = false
        document.removeEventListener('click', handleClickOutside)
    }

    /**
     * 点击外部事件关闭
     */
    const handleClickOutside = (event: Event) => {
        if (!inputRef.value) return

        // 获取编辑区域相关的所有元素
        const inputElement = inputRef.value
        const btnWrapper = inputElement.closest('.nickname-wrapper')
        
        // 检查点击目标是否是编辑区域内部
        const isClickInside = btnWrapper?.contains(event.target as Node)
        
        // 如果点击了外部，关闭编辑模式
        if (!isClickInside) {
            closeEditModal()
        }
    }

    /**
     * 提交修改昵称方法 (绑定confirm按钮/enter事件)
     */
    const uploadNickname = async () => {
        if (!editNickname.value.trim()) return

        try {
            await userStore.updateUserInfo({nickname: editNickname.value})
            await userStore.getUserInfo()
        } catch(error) {
            return Promise.reject(error)
        } finally {
            closeEditModal()
        }
    }
</script>

<style scoped>
    .info-container {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        padding: 20px 0 0 0;
    }

    /* 昵称相关 */
    .nickname-wrapper {
        position: relative;
        height: 35px;
        width: 100%;
        padding-bottom: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        
    }

    .nickname-context {
        position: relative;
        border-bottom: 1px solid var(--primary-color);
        width: 50%;
        height: 100%;
        text-align: center;
        padding-bottom: 5px;
    }

    .nickname-context p {
        cursor: pointer;
        user-select: none;
        font-family: 'Btn-text';
        color: var(--text-color);
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .nickname-context input {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background: transparent;
        border: none;
        outline: none;
        text-align: center;
        color: var(--text-color);
    }

    .btn-wrapper {
        position: absolute;
        right: -5px;
        height: 100%;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .btn-wrapper .btn {
        width: 30px;
        height: 80%;
        background: var(--btn-bg-color);
        border: none;
        border-radius: var(--btn-border-radius);
        color: var(--btn-text-color);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: var(--btn-shadow);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .btn-wrapper .btn:hover {
        transform: scale(1.2);
        box-shadow: var(--btn-shadow-hover);
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.5s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    /* 基本信息 */
    .other-info-wrapper {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px;
        gap: 15px;
    }

    .other-info-wrapper .item {
        display: flex;
        gap: 10px;
        color: var(--text-color);
        font-family: 'Btn-text';
        font-size: 0.9rem;
    }

    .other-info-wrapper .item p {
        overflow: hidden;
        text-overflow: ellipsis;
    }
</style>