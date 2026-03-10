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
  
  document.querySelectorAll('.usecases-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

interface UseCase {
  icon: string
  title: string
  desc: string
  examples: string[]
}

const useCases: UseCase[] = [
  {
    icon: '🏠',
    title: '智能家居控制',
    desc: '通过语音或消息控制家中设备',
    examples: ['📱 手机远程开灯', '🎙️ 语音控制空调', '🚪 智能门锁管理']
  },
  {
    icon: '💼',
    title: '办公自动化',
    desc: '自动化日常办公任务，提升效率',
    examples: ['📧 邮件自动回复', '📅 日程智能提醒', '📊 数据报告生成']
  },
  {
    icon: '🛒',
    title: '电商助手',
    desc: '智能处理订单和客户咨询',
    examples: ['🤖 24/7 客服机器人', '📦 物流状态查询', '💰 价格监控提醒']
  },
  {
    icon: '🎮',
    title: '个人娱乐',
    desc: '你的私人娱乐顾问',
    examples: ['🎬 电影/音乐推荐', '🎯 游戏攻略查询', '📰 新闻摘要推送']
  }
]
</script>

<template>
  <section class="usecases-section" id="usecases">
    <h2 class="section-title reveal">
      <span class="gradient-text">使用场景</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      无限可能，随心所欲
    </p>
    <div class="usecases-grid">
      <div 
        v-for="(useCase, index) in useCases" 
        :key="useCase.title"
        class="usecase-card reveal"
        :class="`reveal-delay-${(index % 3) + 1}`"
      >
        <div class="usecase-icon">{{ useCase.icon }}</div>
        <h3 class="usecase-title">{{ useCase.title }}</h3>
        <p class="usecase-desc">{{ useCase.desc }}</p>
        <ul class="usecase-examples">
          <li v-for="example in useCase.examples" :key="example">
            {{ example }}
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
.usecases-section {
  padding: 6rem 2rem;
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
  margin-bottom: 4rem;
}

.usecases-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.usecase-card {
  padding: 2rem;
  border-radius: var(--radius);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.usecase-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--gradient-primary);
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 0;
}

.usecase-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: transparent;
}

.usecase-card:hover::before {
  opacity: 0.05;
}

.usecase-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

.usecase-title {
  font-size: 1.35rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  position: relative;
  z-index: 1;
}

.usecase-desc {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 1;
}

.usecase-examples {
  list-style: none;
  padding: 0;
  position: relative;
  z-index: 1;
}

.usecase-examples li {
  font-size: 0.875rem;
  color: var(--text-muted);
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--border);
  transition: all 0.2s ease;
}

.usecase-examples li:last-child {
  border-bottom: none;
}

.usecase-card:hover .usecase-examples li {
  color: var(--text);
  padding-left: 0.5rem;
}

@media (max-width: 768px) {
  .usecases-grid {
    grid-template-columns: 1fr;
  }
}
</style>
