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

        <!-- 菜单栏 -->
        <div class="menu-wrapper">
            <Menu />
        </div>
    </div>
</template>

<script setup lang='ts'>
    import TopBar from '@/components/home/TopBar.vue'
    import Menu from '@/components/home/Menu.vue'

</script>

<style scoped>
    .home-container {
        height: 100%;
        width: 100%;
        position: relative;
    }

    .top-bar-wrapper {
        height: 50px;
    }

    .main-content-wrapper {
        height: calc(100% - 50px);
        padding: 10px 75px 0;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.5s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    .menu-wrapper {
        position: absolute;
        bottom: 0;
        left: 0;
        height: calc(100% - 50px);
        padding: 10px 0 0;
    }
</style>