<template>
  <!-- 🍊 橙子星空魔法背景 -->
  <div 
    class="orange-starry-sky"
    ref="starrySky"
    @mousemove="throttledCreateRipple"
    @click="createClickRipple"
  >
    <!-- 🌟 静态星空背景层 -->
    <div class="starry-background"></div>
    
    <!-- 🍊 四个角落的“果瓣涟漪发射器” -->
    <div class="orange-corner top-left">
      <div class="orange-ripple ripple-1"></div>
      <div class="orange-ripple ripple-2"></div>
      <div class="orange-ripple ripple-3"></div>
    </div>
    
    <div class="orange-corner top-right">
      <div class="orange-ripple ripple-1"></div>
      <div class="orange-ripple ripple-2"></div>
      <div class="orange-ripple ripple-3"></div>
    </div>
    
    <div class="orange-corner bottom-left">
      <div class="orange-ripple ripple-1"></div>
      <div class="orange-ripple ripple-2"></div>
      <div class="orange-ripple ripple-3"></div>
    </div>
    
    <div class="orange-corner bottom-right">
      <div class="orange-ripple ripple-1"></div>
      <div class="orange-ripple ripple-2"></div>
      <div class="orange-ripple ripple-3"></div>
    </div>
    
    <!-- 🖱️ 鼠标跟随涟漪（动态生成） -->
    <div 
      v-for="ripple in mouseRipples" 
      :key="ripple.id"
      class="mouse-orange-ripple"
      :style="{
        left: ripple.x + 'px',
        top: ripple.y + 'px',
        width: ripple.size + 'px',
        height: ripple.size + 'px',
        'animation-duration': ripple.duration + 's'
      }"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// 🍊 鼠标涟漪数据类型
interface MouseRipple {
  id: number
  x: number
  y: number
  size: number
  duration: number
  createdAt: number
}

// 🎨 星空配置
const starCount = 80 // 星星数量
const starrySky = ref<HTMLElement | null>(null)
const mouseRipples = ref<MouseRipple[]>([])
let rippleId = 0
let lastMouseMoveTime = 0
const MOUSE_MOVE_THROTTLE = 50 // 毫秒，控制涟漪生成频率

// ✨ 生成星空背景
const generateStars = () => {
  const stars: string[] = []
  for (let i = 0; i < starCount; i++) {
    const x = Math.random() * 100
    const y = Math.random() * 100
    const size = Math.random() * 3 + 1 // 1-4px
    const opacity = Math.random() * 0.8 + 0.2 // 0.2-1.0
    const hue = 30 + Math.random() * 20 // 橙色系：30-50度
    const saturation = 70 + Math.random() * 30 // 70-100%
    const lightness = 50 + Math.random() * 30 // 50-80%
    
    stars.push(
      `radial-gradient(${size}px ${size}px at ${x}% ${y}%, 
       hsla(${hue}, ${saturation}%, ${lightness}%, ${opacity}) 50%, 
       transparent 100%)`
    )
  }
  return stars.join(', ')
}

// 🍊 创建鼠标跟随涟漪
const createRipple = (event: MouseEvent) => {
  if (!starrySky.value) return
  
  const container = starrySky.value
  const rect = container.getBoundingClientRect()
  
  // 计算在容器内的位置
  const x = event.clientX - rect.left
  const y = event.clientY - rect.top
  
  // 随机大小和时长，增加自然感
  const size = Math.random() * 30 + 20 // 20-50px
  const duration = Math.random() * 1 + 2 // 2-3秒
  
  const newRipple: MouseRipple = {
    id: rippleId++,
    x,
    y,
    size,
    duration,
    createdAt: Date.now()
  }
  
  mouseRipples.value.push(newRipple)
  
  // 自动清理（动画结束后+额外缓冲）
  setTimeout(() => {
    mouseRipples.value = mouseRipples.value.filter(r => r.id !== newRipple.id)
  }, (duration + 0.5) * 1000) // 动画时长+0.5秒缓冲
}

// ⚡ 节流版本（避免鼠标移动过快时生成太多涟漪）
const throttledCreateRipple = (event: MouseEvent) => {
  const now = Date.now()
  if (now - lastMouseMoveTime < MOUSE_MOVE_THROTTLE) return
  
  lastMouseMoveTime = now
  createRipple(event)
}

// 🎯 点击时创建特殊涟漪（更大更亮）
const createClickRipple = (event: MouseEvent) => {
  if (!starrySky.value) return
  
  const container = starrySky.value
  const rect = container.getBoundingClientRect()
  const x = event.clientX - rect.left
  const y = event.clientY - rect.top
  
  // 点击涟漪更大更持久
  const clickRipple: MouseRipple = {
    id: rippleId++,
    x,
    y,
    size: 60, // 固定大小
    duration: 3.5, // 固定时长
    createdAt: Date.now()
  }
  
  mouseRipples.value.push(clickRipple)
  
  setTimeout(() => {
    mouseRipples.value = mouseRipples.value.filter(r => r.id !== clickRipple.id)
  }, 4000)
}

// 📦 清理过期涟漪（每5秒运行一次）
const cleanupOldRipples = () => {
  const now = Date.now()
  const maxAge = 4000 // 最长4秒（包含缓冲）
  
  mouseRipples.value = mouseRipples.value.filter(
    ripple => now - ripple.createdAt < maxAge
  )
}

// 🎪 初始化
onMounted(() => {
  // 设置动态星空背景
  const bgElement = document.querySelector('.starry-background') as HTMLElement
  if (bgElement) {
    bgElement.style.backgroundImage = generateStars()
  }
  
  // 启动定期清理
  setInterval(cleanupOldRipples, 5000)
})

// 🧹 组件卸载时清理
onUnmounted(() => {
  mouseRipples.value = []
})
</script>

<style scoped>
/* 🌌 橙子星空容器 */
.orange-starry-sky {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: auto;
  z-index: 0;
  overflow: hidden;
  cursor: none; /* 隐藏默认光标 */
}

/* ✨ 动态星空背景 */
.starry-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #0a0a0a;
  z-index: 1;
  pointer-events: none;
  transition: opacity 2s ease;
}

/* 🎆 星星闪烁动画 */
@keyframes star-twinkle {
  0%, 100% {
    opacity: 0.3;
    filter: brightness(0.8) blur(0.5px);
  }
  20%, 60% {
    opacity: 0.8;
    filter: brightness(1.3) blur(0px);
  }
  40% {
    opacity: 1;
    filter: brightness(1.8) blur(0px);
  }
  80% {
    opacity: 0.6;
    filter: brightness(1.1) blur(0.2px);
  }
}

.starry-background {
  animation: star-twinkle 7s infinite alternate ease-in-out;
}

/* 🍊 四个角落的定位 */
.orange-corner {
  position: absolute;
  width: 200px;
  height: 200px;
  pointer-events: none;
  z-index: 2;
}

.top-left { top: -50px; left: -50px; }
.top-right { top: -50px; right: -50px; }
.bottom-left { bottom: -50px; left: -50px; }
.bottom-right { bottom: -50px; right: -50px; }

/* 🍊 角落橙子瓣涟漪 */
.orange-ripple {
  position: absolute;
  width: 100px;
  height: 100px;
  border-radius: 40% 60% 60% 40% / 50% 40% 60% 50%;
  background: linear-gradient(
    135deg,
    rgba(255, 165, 0, 0.6) 0%,
    rgba(255, 140, 0, 0.4) 33%,
    rgba(255, 69, 0, 0.2) 66%,
    rgba(255, 69, 0, 0.05) 100%
  );
  filter: blur(3px) drop-shadow(0 0 6px rgba(255, 140, 0, 0.3));
  pointer-events: none;
  transform-origin: center;
}

/* 🎵 角落涟漪动画编排 */
@keyframes corner-ripple-dance {
  0% {
    transform: scale(0.3) rotate(0deg);
    opacity: 0.8;
    border-radius: 40% 60% 60% 40% / 50% 40% 60% 50%;
  }
  50% {
    transform: scale(1.5) rotate(180deg);
    opacity: 0.4;
    border-radius: 50% 40% 60% 50% / 40% 50% 50% 60%;
  }
  100% {
    transform: scale(3) rotate(360deg);
    opacity: 0;
    border-radius: 60% 40% 40% 60% / 50% 60% 40% 50%;
  }
}

/* 左上角：轻快节奏 */
.top-left .ripple-1 { animation: corner-ripple-dance 4s ease-out infinite; }
.top-left .ripple-2 { animation: corner-ripple-dance 4s ease-out infinite 1.3s; }
.top-left .ripple-3 { animation: corner-ripple-dance 4s ease-out infinite 2.6s; }

/* 右上角：优雅节奏 */
.top-right .ripple-1 { animation: corner-ripple-dance 4.5s ease-in-out infinite 0.5s; }
.top-right .ripple-2 { animation: corner-ripple-dance 4.5s ease-in-out infinite 2s; }
.top-right .ripple-3 { animation: corner-ripple-dance 4.5s ease-in-out infinite 3.5s; }

/* 左下角：活泼节奏 */
.bottom-left .ripple-1 { animation: corner-ripple-dance 3.8s ease-out infinite 0.8s; }
.bottom-left .ripple-2 { animation: corner-ripple-dance 3.8s ease-out infinite 2.4s; }
.bottom-left .ripple-3 { animation: corner-ripple-dance 3.8s ease-out infinite 4s; }

/* 右下角：缓慢节奏 */
.bottom-right .ripple-1 { animation: corner-ripple-dance 5s ease-in infinite 1s; }
.bottom-right .ripple-2 { animation: corner-ripple-dance 5s ease-in infinite 3s; }
.bottom-right .ripple-3 { animation: corner-ripple-dance 5s ease-in infinite 5s; }

/* 🖱️ 鼠标跟随涟漪 */
.mouse-orange-ripple {
  position: absolute;
  border-radius: 50% 40% 50% 40%;
  background: radial-gradient(
    circle at center,
    rgba(255, 220, 120, 0.9) 0%,
    rgba(255, 180, 80, 0.7) 30%,
    rgba(255, 140, 0, 0.4) 60%,
    transparent 100%
  );
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 10;
  filter: blur(1px) 
         drop-shadow(0 0 8px rgba(255, 200, 100, 0.6))
         drop-shadow(0 0 12px rgba(255, 140, 0, 0.3));
  mix-blend-mode: screen; /* 漂亮的叠加效果 */
  will-change: transform, opacity; /* 性能优化 */
}

/* 🎬 鼠标涟漪动画 */
@keyframes mouse-ripple-flow {
  0% {
    transform: translate(-50%, -50%) scale(0.1) rotate(0deg);
    opacity: 0.9;
    border-radius: 50% 40% 50% 40%;
  }
  30% {
    transform: translate(-50%, -50%) scale(1.2) rotate(90deg);
    opacity: 0.7;
    border-radius: 40% 50% 40% 50%;
  }
  60% {
    transform: translate(-50%, -50%) scale(1.8) rotate(180deg);
    opacity: 0.4;
    border-radius: 50% 50% 40% 60%;
  }
  100% {
    transform: translate(-50%, -50%) scale(2.5) rotate(360deg);
    opacity: 0;
    border-radius: 60% 40% 50% 50%;
  }
}

.mouse-orange-ripple {
  animation: mouse-ripple-flow var(--duration, 2.5s) ease-out forwards;
}

/* ✨ 鼠标悬浮增强效果 */
.orange-starry-sky:hover .orange-ripple {
  filter: blur(2px) 
         drop-shadow(0 0 10px rgba(255, 200, 100, 0.5))
         drop-shadow(0 0 20px rgba(255, 165, 0, 0.3));
  animation-duration: calc(var(--base-duration, 4s) * 0.6);
}

/* 🌈 响应式调整 */
@media (max-width: 768px) {
  .orange-corner {
    width: 150px;
    height: 150px;
  }
  
  .orange-ripple {
    width: 70px;
    height: 70px;
  }
  
  /* 移动端减少涟漪数量 */
  .orange-corner .ripple-3 {
    display: none;
  }
}

/* 📱 触摸设备优化 */
@media (hover: none) {
  .orange-starry-sky {
    cursor: default;
  }
}
</style>