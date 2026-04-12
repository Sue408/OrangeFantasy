<template>
    <div class="novel-settings-container">
        <!-- 安全相关设置 -->
        <div class="secuity-wrapper">
            <div class="top-bar">
                <h3>security</h3>
            </div>
            <button class="delete-btn" @click="deleteNovel">删除作品</button>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import type { NovelMeta } from '@/types/novelTypes'
    import useNovelStore from '@/stores/novelStore'
    import { useRouter } from 'vue-router'
    import { showDialog } from '@/utils/showDoalog'

    const novelStore = useNovelStore()
    const router = useRouter()
    const props = defineProps<{
        novel: NovelMeta
    }>()

    const deleteNovel = () => {
        showDialog(
            {
                context: '确认要删除本作品吗？',
                onConfirm: async () => {
                    try {
                        await novelStore.deleteNovel(props.novel.id)
                        // 重新加载novel
                        await novelStore.getNovels()

                        // 执行路径跳转
                        router.replace({ name: 'MyNovels' })
                    } catch(error) {
                        return Promise.reject(error)
                    }
                }
            }
        )
    }


</script>

<style scoped>
    .novel-settings-container {
        width: 100%;
        height: 100%;
        border-top-right-radius: 24px;
        border-bottom-right-radius: 24px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .secuity-wrapper {
        width: 100%;
        height: 200px;
        display: flex;
        align-items: center;
        flex-direction: column;
        gap: 25px;
    }

    .secuity-wrapper .top-bar {
        width: 100%;
        height: 50px;
        display: flex;
        align-items: center;
        padding: 0 30px;
    }

    .secuity-wrapper .top-bar h3 {
        font-family: 'Title';
        color: var(--primary-color);
        font-size: 1.75rem;
        user-select: none;
    }

    .secuity-wrapper .delete-btn {
        width: 80%;
        height: 30px;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-family: 'Btn-text';
        color: var(--text-color);
        background-color: rgba(175, 0, 0, 0.75);
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .secuity-wrapper .delete-btn:hover {
        transform: scale(1.05);
    }
</style>