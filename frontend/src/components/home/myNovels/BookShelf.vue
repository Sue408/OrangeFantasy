<template>
    <div class="book-shelf-container float-card">
        <!-- 顶部栏 -->
        <div class="top-control-bar">
            <div class="title">
                <h3>My Novels ({{ novelStore.novels.length }})</h3>
            </div>

            <button class="add-btn" @click="$emit('openCreateModal')">
                创建作品
            </button>
        </div>

        <!-- 网格布局面板 -->
        <div class="novels-wrapper">
            <!-- 作品项目 -->
            <div class="novel-item" v-for="novel in novelStore.novels" :key="novel.id">
                <!-- 封面 -->
                <div class="novel-cover" :class="{ 'have-cover': novel.cover }">
                    <img v-if="novel.cover" :src="novel.cover" alt="cover">
                    <div v-else class="default-cover">
                        <svg  xmlns="http://www.w3.org/2000/svg" width="64" height="64"  
                        fill="currentColor" viewBox="0 0 24 24" >
                        <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                        <path d="M8 6h9v2H8z"></path><path d="M20 2H6C4.35 2 3 3.35 3 5v14c0 1.65 1.35 3 3 3h15v-2H6c-.55 0-1-.45-1-1s.45-1 1-1h14c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1m-6 14H6c-.35 0-.69.07-1 .18V5c0-.55.45-1 1-1h13v12z"></path>
                        </svg>
                    </div>
                </div>
                <!-- 名称 -->
                 <p>{{ novel.name }}</p>
            </div>

            <!-- 内置添加作品快捷按钮 -->
            <div class="novel-item add-item" @click="$emit('openCreateModal')">
                <!-- 封面 -->
                <div class="novel-cover">
                    <svg  xmlns="http://www.w3.org/2000/svg" width="42" height="42"  
                    fill="currentColor" viewBox="0 0 24 24" >
                    <!--Boxicons v3.0.8 https://boxicons.com | License  https://docs.boxicons.com/free-->
                    <path d="M3 13h8v8h2v-8h8v-2h-8V3h-2v8H3z"></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import { onMounted } from 'vue'
    import useNovelStore from '@/stores/novelStore'

    const novelStore = useNovelStore()
    onMounted(async () => {
        await novelStore.getNovels()
    })
</script>

<style scoped>
    .book-shelf-container {
        height: 100%;
        width: 100%;
        color: var(--text-color);
    }

    .top-control-bar {
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid var(--supple-color);
        padding: 0 45px;
        user-select: none;
    }

    .top-control-bar .title {
        color: var(--primary-color);
        font-family: 'Title';
        letter-spacing: 0.1rem;
        font-size: 1rem;
    }

    .top-control-bar .add-btn {
        width: 108px;
        height: 32px;
        border-radius: 12px;
        background-color: var(--primary-color);
        border: none;
        color: var(--text-color);
        font-family: 'Btn-text';
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--btn-shadow);
    }

    .top-control-bar .add-btn:hover {
        transform: scale(1.1);
        box-shadow: var(--btn-shadow-hover);
    }

    .novels-wrapper {
        display: grid;
        grid-template-columns: repeat(auto-fill, 150px);
        grid-auto-rows: 250px;
        padding: 25px;
        gap: 25px;
        overflow-x: hidden;
        overflow-y: auto;
        height: calc(100% - 64px);
        justify-content: center;
    }

    .novels-wrapper::-webkit-scrollbar {
        width: 0;
    }

    .novel-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        cursor: pointer;
    }
    
    .novel-cover {
        width: 100%;
        height: 85%;
        background-color: rgba(25, 25, 25, 0.75);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-color);
        transition: all 0.3s ease;
    }

    .novel-cover img {
        width: 100%;
        height: 100%;
        border-radius: 12px;
        object-fit: cover;
    }

    .novel-item:not(.add-item) .novel-cover {
        border: 1px solid var(--primary-color);
        box-shadow: 1px 1px 5px rgba(255, 255, 255, 0.25);
    }

    .novel-item:not(.add-item) .novel-cover.have-cover {
        border: 2px solid var(--primary-color);
    }

    .novel-item:not(.add-item) .novel-cover:hover {
        transform: scale(1.1);
        box-shadow: var(--btn-shadow-hover);
    }

    .novel-item p {
        font-family: 'Btn-text';
    }

    .novel-item.add-item .novel-cover {
        background-color: rgba(25, 25, 25, 0.25);
    }

    .novel-item.add-item .novel-cover svg {
        transition: all 0.3s ease-in-out;
    }

    .novel-item.add-item .novel-cover:hover svg {
        transform: scale(1.2);
    }
</style>