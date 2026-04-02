<template>
    <div class="home-container">
        <!-- 顶部栏 -->
        <div class="top-bar-wrapper float-card">
            <TopBar />
        </div>

        <!-- 内容区 -->
        <div class="main-content-wrapper">
            <router-view v-slot="{ Component }">
                <transition name="fade" mode="out-in">
                    <component :is="Component" />
                </transition>
            </router-view>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import TopBar from '@/components/home/TopBar.vue'

</script>

<style scoped>
    .home-container {
        height: 100%;
        width: 100%;
    }

    .top-bar-wrapper {
        height: 50px;
    }

    .main-content-wrapper {
        height: calc(100% - 50px);
        padding: 10px 5px 0;
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