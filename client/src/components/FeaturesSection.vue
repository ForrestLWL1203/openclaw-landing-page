<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
        }
      })
    },
    { threshold: 0.1 }
  )
  
  document.querySelectorAll('.features-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

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
  },
  {
    icon: '⚡',
    title: '高性能',
    desc: '异步处理<br>响应迅速'
  }
]
</script>

<template>
  <section class="features-section" id="features">
    <h2 class="section-title reveal">
      <span class="gradient-text">核心功能</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      强大而灵活的 AI 助手框架，满足各种使用场景
    </p>
    <div class="features-grid">
      <div 
        v-for="(feature, index) in features" 
        :key="feature.title"
        class="feature-card reveal"
        :class="`reveal-delay-${(index % 4) + 1}`"
      >
        <div class="feature-glow"></div>
        <div class="feature-icon">{{ feature.icon }}</div>
        <div class="feature-title">{{ feature.title }}</div>
        <div class="feature-desc" v-html="feature.desc"></div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.features-section {
  padding: 6rem 2rem;
  position: relative;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.section-desc {
  text-align: center;
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 500px;
  margin: 0 auto 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1100px;
  margin: 0 auto;
}

.feature-card {
  padding: 2rem;
  border-radius: var(--radius);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.feature-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gradient-primary);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  border-color: transparent;
  box-shadow: 0 20px 60px -15px rgba(99, 102, 241, 0.3);
}

.feature-card:hover .feature-glow {
  opacity: 1;
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  position: relative;
  z-index: 1;
}

.feature-desc {
  font-size: 0.95rem;
  color: var(--text-muted);
  line-height: 1.6;
  position: relative;
  z-index: 1;
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 2rem;
  }
}
</style>
