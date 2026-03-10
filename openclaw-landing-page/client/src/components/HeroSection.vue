<script setup lang="ts">
</script>

<template>
  <section class="hero" id="intro">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="crawfish-container">
        🦞
      </div>
      <h1>小龙虾闪亮登场！</h1>
      <p>你的智能 AI 助手 · 多平台支持 · 无限可能</p>
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
  background: var(--bg-subtle);
}

.hero-bg {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: 
    radial-gradient(circle at 30% 20%, rgba(37, 99, 235, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 70% 80%, rgba(8, 145, 178, 0.06) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(99, 102, 241, 0.05) 0%, transparent 40%);
  animation: bgFloat 20s ease-in-out infinite;
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 600px;
}

.crawfish-container {
  font-size: 100px;
  line-height: 1;
  margin-bottom: 0.5rem;
  animation: float 3s ease-in-out infinite;
  filter: drop-shadow(0 10px 20px rgba(37, 99, 235, 0.2));
}

.hero h1 {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--primary) 0%, #ff8fa3 50%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: fadeInUp 0.8s ease-out;
}

.hero p {
  font-size: 1rem;
  color: var(--text-muted);
  max-width: 400px;
  margin: 0 auto;
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.25rem;
  }
  
  .crawfish-container {
    font-size: 80px;
  }
}
</style>
