<script setup lang="ts">
interface Feature {
  icon: string
  title: string
  desc: string
}

const features: Feature[] = [
  {
    icon: '🤖',
    title: 'AI Agent',
    desc: '多Agent协作<br>智能任务处理'
  },
  {
    icon: '🔌',
    title: 'Skill 扩展',
    desc: '丰富插件系统<br>按需灵活调用'
  },
  {
    icon: '💬',
    title: '多渠道',
    desc: 'Telegram<br>Discord/微信/Signal'
  },
  {
    icon: '🌐',
    title: 'Web API',
    desc: '随时随地<br>远程控制'
  },
  {
    icon: '🔒',
    title: '本地部署',
    desc: '数据隐私<br>安全可控'
  }
]
</script>

<template>
  <section class="features-section" id="features">
    <h2 class="section-title">✨ 核心功能</h2>
    <div class="features-grid">
      <div 
        v-for="feature in features" 
        :key="feature.title"
        class="feature-card"
      >
        <div class="feature-icon">{{ feature.icon }}</div>
        <div class="feature-title">{{ feature.title }}</div>
        <div class="feature-desc" v-html="feature.desc"></div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.features-section {
  padding: 5rem 2rem;
}

.section-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 3rem;
  color: var(--text);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
}

.feature-card {
  padding: 1.75rem;
  border-radius: var(--radius);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-4px);
  border-color: var(--primary);
  box-shadow: 0 12px 40px -8px rgba(37, 99, 235, 0.15);
}

.feature-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.feature-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.feature-desc {
  font-size: 0.9rem;
  color: var(--text-muted);
  line-height: 1.5;
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
