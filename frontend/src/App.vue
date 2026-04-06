<template>
    <div class="app-container" @contextmenu.prevent="console.log('打不开~')">
        <router-view v-slot="{ Component }">
            <transition name="app-fade" mode="out-in">
                <component :is="Component" />
            </transition>
        </router-view>
    </div>
</template>

<script setup lang="ts">
    import { onMounted, nextTick } from 'vue'
    import useUserStore from './stores/userSotre'

    onMounted(() => {
        nextTick(async () => {
            const userStore = useUserStore()
            try {
                await userStore.loadUser()
            } catch(error) {
                return Promise.reject(error)
            }
        })
    })
</script>

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .app-container {
        height: 100vh;
        width: 100vw;
        overflow: hidden;
        background: var(--bg-color);
        padding: 20px;
    }

    .float-card {
        background: var(--float-card-bg-color);
        border-radius: var(--float-card-border-radius);
        box-shadow: var(--float-card-shadow);
    }

    .small-btn {
        padding: 5px 10px;
        border-radius: 12px;
        border: none;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .app-fade-enter-active,
    .app-fade-leave-active {
    transition: opacity 0.5s ease;
    }

    .app-fade-enter-from,
    .app-fade-leave-to {
    opacity: 0;
    }

    @font-face {
        font-family: 'Title';
        src: url('fonts/title.ttf')
    }

    @font-face {
        font-family: 'Btn-Text';
        src: url('fonts/btn-text.otf')
    }
</style>