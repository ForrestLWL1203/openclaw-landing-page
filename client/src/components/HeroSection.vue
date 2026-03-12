<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  // Trigger animation on mount
  setTimeout(() => {
    const heroContent = document.querySelector('.hero-content > *')
    heroContent?.classList.add('visible')
  }, 100)
})
</script>

<template>
  <section class="hero" id="intro">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="crawfish-container">
        <svg class="crawfish-icon" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="40" cy="40" r="36" fill="#2563EB" fill-opacity="0.1"/>
          <ellipse cx="40" cy="45" rx="20" ry="15" fill="#F97316"/>
          <ellipse cx="40" cy="42" rx="18" ry="12" fill="#FB923C"/>
          <circle cx="32" cy="38" r="4" fill="#1E293B"/>
          <circle cx="48" cy="38" r="4" fill="#1E293B"/>
          <circle cx="33" cy="37" r="1.5" fill="white"/>
          <circle cx="49" cy="37" r="1.5" fill="white"/>
          <path d="M35 48 Q40 52 45 48" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/>
          <path d="M20 40 L30 43" stroke="#F97316" stroke-width="3" stroke-linecap="round"/>
          <path d="M20 45 L28 46" stroke="#F97316" stroke-width="3" stroke-linecap="round"/>
          <path d="M60 40 L50 43" stroke="#F97316" stroke-width="3" stroke-linecap="round"/>
          <path d="M60 45 L52 46" stroke="#F97316" stroke-width="3" stroke-linecap="round"/>
          <path d="M25 55 L30 65 L35 58" stroke="#F97316" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M55 55 L50 65 L45 58" stroke="#F97316" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h1>小龙虾闪亮登场！</h1>
      <p>你的智能 AI 助手 · 多平台支持 · 无限可能</p>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: auto;
  padding: 100px 2rem 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
  background: var(--bg);
}

.hero-bg {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: 
    radial-gradient(circle at 20% 30%, rgba(37, 99, 235, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(249, 115, 22, 0.06) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.04) 0%, transparent 40%);
  animation: bgFloat 20s ease-in-out infinite;
  pointer-events: none;
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
  width: 100%;
}

.hero-content > * {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.8s ease-out forwards;
}

.hero-content > *:nth-child(1) { animation-delay: 0s; }
.hero-content > *:nth-child(2) { animation-delay: 0.15s; }
.hero-content > *:nth-child(3) { animation-delay: 0.3s; }
.hero-content > *:nth-child(4) { animation-delay: 0.45s; }

.crawfish-container {
  width: 120px;
  height: 120px;
  margin: 0 auto 1rem;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.crawfish-container:hover {
  transform: scale(1.1) rotate(-5deg);
}

.crawfish-icon {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 10px 20px rgba(37, 99, 235, 0.25));
  animation: float 3s ease-in-out infinite;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1rem;
  color: var(--text);
}

.hero > .hero-content > p {
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 400px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.25rem;
  }
  
  .crawfish-container {
    width: 100px;
    height: 100px;
  }
}
</style>
