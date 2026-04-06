<template>
    <div class="avatar-container">
        <!-- 头像展示层 -->
        <div class="avatar-display">
            <img v-if="userStore.userInfo?.avatar" :src="userStore.userInfo.avatar" :alt="userStore.userInfo.nickname || 'avatar'" class="avatar-img" />
            <div v-else class="avatar-placeholder">{{ userStore.userInfo?.nickname?.charAt(0) || 'U' }}</div>
        </div>

        <!-- 上传遮罩层 -->
        <div class="upload-overlay" :class="{ disabled: isUploading }">
            <label for="upload-avatar">
                <svg  xmlns="http://www.w3.org/2000/svg" width="42" height="42"  
                fill="currentColor" viewBox="0 0 24 24" >
                <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                <path d="M12 9c-2.17 0-4 1.83-4 4s1.83 4 4 4 4-1.83 4-4-1.83-4-4-4m0 6c-1.07 0-2-.93-2-2s.93-2 2-2 2 .93 2 2-.93 2-2 2"></path><path d="M20 5h-3.15l-2.23-1.78c-.18-.14-.4-.22-.62-.22h-4c-.23 0-.45.08-.62.22L7.15 5H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2m0 14H4V7h3.5c.23 0 .45-.08.62-.22L10.35 5h3.3l2.23 1.78c.18.14.4.22.62.22H20z"></path><path d="M18 8a1 1 0 1 0 0 2 1 1 0 1 0 0-2"></path>
                </svg>
            </label>
            <input type="file" id="upload-avatar" accept="image/png, image/jpeg, image/jpg, image/webp" @change="uploadAvatar" :disabled="isUploading">
        </div>

        <!-- 加载动画层 -->
        <div v-if="isUploading" class="loading-layer">
            <div class="spinner-wrapper">
                <div class="loading-spinner"></div>
            </div>
        </div>
    </div>
</template>

<script setup lang=ts>
    import { ref } from 'vue'
    import useUserStore from '@/stores/userSotre'
    import fileToBase64 from '@/utils/imgToBase64'

    const userStore = useUserStore()
    const isUploading = ref<boolean>(false)
    /**
     * 头像更新方法
     */
    const uploadAvatar = async (event: Event) => {
        const input = event.target as HTMLInputElement
        const file = input.files?.[0]
        if (file) {
            // 设置为上传状态
            isUploading.value = true
            try {
                const avatar = await fileToBase64(file) // 将头像文件转换为base64编码
                userStore.updateUserInfo({avatar})
                userStore.getUserInfo()
            } catch(error) {
                return Promise.reject(error)
            } finally {
                isUploading.value = false
            }
        }
    }
</script>

<style scoped>
    .avatar-container {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }

    /* 展示层 */
    .avatar-display {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 108px;
        height: 108px;
        border-radius: 50%;
        background: #222;
        border: 1px solid rgba(194, 87, 34, 0.3);
        overflow: hidden;
        user-select: none;
        box-shadow: 0 0 30px rgba(194, 87, 34, 0.5);
    }

    .avatar-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .avatar-placeholder {
        font-size: 2rem;
        font-weight: 600;
        color: var(--primary-color);
        text-transform: uppercase;
    }

    /* 遮罩层 */
    .upload-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .upload-overlay input {
        display: none;
    }

    .upload-overlay label {
        color: #fff;
        opacity: 0;
        width: 108px;
        height: 108px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(240, 110, 45, 0.5);
        cursor: pointer;
    }

    .upload-overlay label svg {
        transform: scale(0.1);
        transition: all 0.3s ease;
    }

    .upload-overlay:not(.disabled) label:hover {
        opacity: 1;
        background-color: rgba(0, 0, 0, 0.2);
        
    }

    .upload-overlay:not(.disabled) label:hover svg {
        transform: scale(1);
    }

    .loading-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .spinner-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 108px;
        height: 108px;
        border-radius: 50%;
        background-color: rgba(0, 0, 0, 0.8);
    }

    .loading-spinner {
        width: 56px;
        height: 56px;
        border: 4px solid rgba(255, 255, 255,0.3);
        border-radius: 50%;
        border-top-color: var(--primary-color);
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }
</style>