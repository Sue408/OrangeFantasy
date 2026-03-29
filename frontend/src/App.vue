<template>
    <div class="app-container">
        <router-view />
    </div>
</template>

<script setup lang="ts"></script>

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

    @font-face {
        font-family: 'Title';
        src: url('fonts/title.ttf')
    }

    @font-face {
        font-family: 'Btn-Text';
        src: url('fonts/btn-text.otf')
    }
</style>