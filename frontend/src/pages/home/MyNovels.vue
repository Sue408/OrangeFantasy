<template>
    <div class="my-novels-container">
        <transition name="scale" mode="out-in">
            <div class="wrapper" v-if="!isCreateModal">
                <BookShelf @openCreateModal="isCreateModal = true" />
            </div>

            <div class="wrapper" v-else>
                <CreateNovel @closeCreateModal="isCreateModal = false" />
            </div>
        </transition>
    </div>
</template>

<script setup lang='ts'>
    import { ref } from 'vue'
    import BookShelf from '@/components/home/myNovels/BookShelf.vue'
    import CreateNovel from '@/components/home/myNovels/CreateNovel.vue'

    // ========= 创建novel模式切换 =========
    const isCreateModal = ref<boolean>(false)
</script>

<style scoped>
    .scale-enter-active,
    .scale-leave-active {
        transition: all 0.3s ease;
    }

    .scale-enter-from,
    .scale-leave-to {
        opacity: 0;
        transform: scale(0.2);
    }

    .my-novels-container {
        width: 100%;
        height: 100%;
    }

    .my-novels-container .wrapper {
        width: 100%;
        height: 100%;
    }
</style>