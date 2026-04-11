<template>
    <Transition name="fade" mode="out-in">
        <div class="set-chapter-name-container" v-if="visible" @click.self="$emit('update:visible', false)">
            <div class="dialog-wrapper">
                <h3>
                    <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M17.87 2.99a2 2 0 0 0-2.82 0l-7.96 7.84c-.14.13-.23.3-.27.49L5.8 15.76 4 18.01h2.83l1.14-1.13 3.59-.83c.18-.04.35-.13.48-.26l7.95-7.83c.38-.38.59-.88.6-1.42 0-.54-.21-1.04-.59-1.42L17.88 3Zm.71 3.53-7.24 7.13-2.12-2.12 7.24-7.13zM4 20h16v2H4z"></path>
                    </svg>
                    设置章节名称
                </h3>
                <input type="text" v-model="setName" ref="inputRef">
                <div class="btn-box">
                    <button class="confirm-btn" @click="setChapterName">确认</button>
                    <button class="cancel-btn" @click="$emit('update:visible', false)">取消</button>
                </div>
            </div>
        </div>
    </Transition>
</template>

<script setup lang='ts'>
    import { ref, watch, nextTick } from 'vue'
    import { updateChapterAPI } from '@/services/chapter'
    import useNovelStore from '@/stores/novelStore'

    const novelStore = useNovelStore()
    const props = defineProps<{
        visible: boolean
        id: number | null
        name: string | null
    }>()

    const emits = defineEmits<{
        (e: 'update:visible', value: boolean): void
    }>()

    const inputRef = ref<HTMLInputElement | null>(null)

    // 设置chapter名称ref
    const setName = ref<string>('')
    watch(() => props.visible,async () => {
        setName.value = ''
        if (props.name && props.name !== '未命名') {
            setName.value = props.name
        }

        // 自动聚焦
        await nextTick()
        if (inputRef.value) {
            inputRef.value.focus()
        }
    })

    const setChapterName = async () => {
        try {
            if (props.id && setName.value.trim()) {
                await updateChapterAPI(props.id, { name: setName.value })

                // 刷新novels
                await novelStore.getNovels()
            }
        } catch(error) {
            return Promise.reject(error)
        } finally {
            emits('update:visible', false)
        }
    }
</script>

<style scoped>
    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.2s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    .set-chapter-name-container {
        position: fixed;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.75);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .dialog-wrapper {
        height: 200px;
        width: 350px;
        background: rgba(35, 35, 35, 0.95);
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 25px;
    }

    .dialog-wrapper h3 {
        color: var(--supple-color);
        font-family: 'Btn-text';
        margin-bottom: 5px;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .dialog-wrapper input[type='text'] {
        width: 90%;
        height: 20%;
        border: 1px solid var(--primary-color);
        outline: none;
        background-color: rgba(25, 25, 25, 0.75);
        border-radius: 8px;
        color: var(--text-color);
        padding: 0 10px;
        font-family: 'Btn-text';
        font-size: 1rem;
    }

    .dialog-wrapper input[type='text']:focus {
        box-shadow: 0 0 12px var(--primary-color);
    }

    .dialog-wrapper .btn-box {
        width: 100%;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 80px;
    }

    .dialog-wrapper .btn-box button {
        width: 64px;
        height: 32px;
        border-radius: 8px;
        border: none;
        background-color: var(--primary-color);
        color: var(--text-color);
        font-family: 'Btn-text';
        font-size: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .dialog-wrapper .btn-box button:hover {
        transform: scale(1.1);
    }
</style>