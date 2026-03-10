<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  // Add particle effect
  const hero = document.querySelector('.hero')
  if (hero) {
    for (let i = 0; i < 30; i++) {
      const particle = document.createElement('div')
      particle.className = 'particle'
      particle.style.left = Math.random() * 100 + '%'
      particle.style.top = Math.random() * 100 + '%'
      particle.style.animationDelay = Math.random() * 5 + 's'
      particle.style.animationDuration = (3 + Math.random() * 4) + 's'
      hero.appendChild(particle)
    }
  }
})
</script>

<template>
  <section class="hero" id="intro">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="crawfish-container">
        🦞
      </div>
      <h1>
        <span class="gradient-text">OpenClaw</span>
      </h1>
      <p class="hero-subtitle">你的智能 AI 助手 · 多平台支持 · 无限可能</p>
      <div class="hero-cta">
        <a href="#install" class="btn btn-primary">快速开始</a>
        <a href="#features" class="btn btn-secondary">了解更多</a>
      </div>
      <div class="hero-stats">
        <div class="stat">
          <span class="stat-value gradient-text">10+</span>
          <span class="stat-label">平台支持</span>
        </div>
        <div class="stat">
          <span class="stat-value gradient-text">∞</span>
          <span class="stat-label">可能无限</span>
        </div>
        <div class="stat">
          <span class="stat-value gradient-text">100%</span>
          <span class="stat-label">本地部署</span>
        </div>
      </div>
    </div>
    <div class="scroll-indicator">
      <span>向下滚动</span>
      <div class="scroll-arrow">↓</div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 2rem 2rem;
  position: relative;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: 
    radial-gradient(circle at 30% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 70% 80%, rgba(34, 211, 238, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(244, 114, 182, 0.08) 0%, transparent 40%);
  animation: bgFloat 20s ease-in-out infinite;
}

/* Particles */
:deep(.particle) {
  position: absolute;
  width: 4px;
  height: 4px;
  background: var(--primary);
  border-radius: 50%;
  opacity: 0.3;
  animation: particleFloat 5s ease-in-out infinite;
}

@keyframes particleFloat {
  0%, 100% { transform: translateY(0) scale(1); opacity: 0.3; }
  50% { transform: translateY(-30px) scale(1.5); opacity: 0.6; }
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 700px;
}

.crawfish-container {
  font-size: 120px;
  line-height: 1;
  margin-bottom: 1rem;
  animation: float 3s ease-in-out infinite;
  filter: drop-shadow(0 20px 40px rgba(99, 102, 241, 0.4));
  transition: transform 0.3s ease;
}

.crawfish-container:hover {
  transform: scale(1.1) rotate(5deg);
}

.hero h1 {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1rem;
  animation: fadeInUp 0.8s ease-out;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  max-width: 500px;
  margin: 0 auto 2.5rem;
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 3rem;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.btn {
  padding: 0.875rem 2rem;
  border-radius: var(--radius);
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary {
  background: var(--gradient-primary);
  color: white;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.5);
}

.btn-secondary {
  background: var(--bg-elevated);
  color: var(--text);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  background: var(--bg-subtle);
  border-color: var(--primary);
}

.hero-stats {
  display: flex;
  gap: 3rem;
  justify-content: center;
  animation: fadeInUp 0.8s ease-out 0.6s both;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-muted);
  font-size: 0.75rem;
  animation: fadeIn 1s ease-out 1s both;
}

.scroll-arrow {
  animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(8px); }
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.5rem;
  }
  
  .crawfish-container {
    font-size: 80px;
  }
  
  .hero-cta {
    flex-direction: column;
    align-items: center;
  }
  
  .hero-stats {
    gap: 1.5rem;
  }
  
  .stat-value {
    font-size: 1.5rem;
  }
}
</style>
