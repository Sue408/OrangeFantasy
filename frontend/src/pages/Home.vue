<template>
    <div class="home-container">
        <!-- 顶部栏 -->
        <div class="top-bar-wrapper float-card">
            <TopBar />
        </div>

        <!-- 内容区 -->
         <div class="main-content-wrapper">

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
        margin-bottom: 10px;
    }

    .main-content-wrapper {
        height: calc(100% - 50px - 10px);
    }
</style>