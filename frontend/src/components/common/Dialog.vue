<template>
    <Transition name="fade" mode="out-in">
        <div v-show="visible" class="popup-container" @click.self="onCancelFunc">
            <div class="popup-box">
                <!-- 内容 -->
                <div class="context-wrapper">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="32" height="32"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M11 7h2v4.5h-2zm0 6h2v2h-2z"></path><path d="M12 3C6.49 3 2 6.59 2 11c0 2.91 1.9 5.51 5 6.93V21c0 .38.21.72.55.89.14.07.29.11.45.11.21 0 .42-.07.6-.2l3.74-2.8c5.36-.14 9.66-3.67 9.66-8s-4.49-8-10-8m0 14c-.22 0-.43.07-.6.2L9 19v-1.73c0-.41-.25-.78-.64-.93C5.67 15.3 4 13.26 4 11c0-3.31 3.59-6 8-6s8 2.69 8 6-3.59 6-8 6"></path>
                    </svg>
                    <p>{{ context }}</p>
                </div>

                <div class="btn-wrapper">
                    <button class="btn confirm" @click="onConfirmFunc">
                        YES
                    </button>

                    <button class="btn cancel" @click="onCancelFunc">
                        NO
                    </button>
                </div>
            </div>
        </div>
    </Transition>
</template>

<script setup lang='ts'>
    const props = defineProps<{
        visible: boolean,
        onClose: Function, // 关闭事件
        context: string,
        onConfirm?: Function,
        onCancel?: Function
    }>()

    /**
     * 确认方法
     */
    const onConfirmFunc = async () => {
        try {
            if (props.onConfirm) {
                await props.onConfirm()
            }
        } catch(error) {
            return Promise.reject(error)
        } finally {
            props.onClose() // 关闭窗口
        }
    }

    /**
     * 取消方法
     */
    const onCancelFunc = async () => {
        try {
            if (props.onCancel) {
                await props.onCancel()
            }
        } catch(error) {
            return Promise.reject(error)
        } finally {
            props.onClose()
        }
    }
</script>

<style scoped>
    .popup-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.75);
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.2s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    .popup-box {
        height: 200px;
        width: 350px;
        background: rgba(35, 35, 35, 0.95);
        border-radius: 12px;
        display: flex;
        flex-direction: column;
    }

    .popup-box .context-wrapper {
        height: 60%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        font-size: 1.2rem;
        border-bottom: 2px solid var(--supple-color);
        font-family: 'Btn-text';
        gap: 15px;
    }

    .popup-box .context-wrapper svg {
        color: var(--primary-color);
    }

    .popup-box .btn-wrapper {
        flex: 1;
        display: flex;
        padding: 0 60px;
        align-items: center;
        justify-content: space-between;
    }

    .popup-box .btn-wrapper .btn {
        width: 70px;
        height: 35px;
        border-radius: 8px;
        border: none;
        background-color: rgba(75, 75, 75, 0.9);
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: var(--btn-shadow);
        color: var(--text-color);
    }

    .popup-box .btn-wrapper .btn:hover {
        transform: scale(1.2);
        box-shadow: var(--btn-shadow-hover);
    }
</style>