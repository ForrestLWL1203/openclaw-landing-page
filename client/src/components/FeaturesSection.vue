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
  details: string[]
}

const features: Feature[] = [
  {
    icon: '💬',
    title: '多渠道接入',
    desc: '同时连接多个通讯平台，一个入口掌控全局',
    details: [
      '📱 Telegram - 安全快速的即时通讯',
      '💬 Discord - 社区运营利器',
      '💼 微信/企业微信 - 国内办公首选',
      '📧 邮件 - 智能邮件助手',
      '🌐 Web API - 随时随地远程控制'
    ]
  },
  {
    icon: '🧩',
    title: 'Skill 扩展',
    desc: '模块化技能系统，按需加载想要的功能',
    details: [
      '🔌 插拔式设计 - 随时启用/禁用',
      '📚 丰富生态 - 社区分享大量 Skills',
      '🛠️ 灵活定制 - 开发自己的 Skill',
      '🎯 场景组合 - 多个 Skill 协同工作'
    ]
  },
  {
    icon: '🤖',
    title: '多 Agent 协同',
    desc: '多个 AI Agent 分工合作，解决复杂任务',
    details: [
      '👥 分工协作 - 不同 Agent 处理不同任务',
      '🔄 信息流转 - Agent 之间传递上下文',
      '🧠 智能路由 - 自动选择合适的 Agent',
      '⚡ 效率倍增 - 并行处理复杂流程'
    ]
  },
  {
    icon: '🔒',
    title: '本地部署',
    desc: '数据完全保存在本地，隐私安全有保障',
    details: [
      '🏠 居家可用 - 不依赖外部服务器',
      '🔐 隐私保护 - 数据不外传',
      '🛡️ 安全可控 - 完全由你掌控',
      '⚙️ 灵活配置 - 按需定制安全策略'
    ]
  },
  {
    icon: '⚡',
    title: '高性能架构',
    desc: '异步处理架构，响应迅速稳定',
    details: [
      '🚀 快速响应 - 毫秒级延迟',
      '💪 高并发 - 支持大量同时请求',
      '🔌 长连接 - 实时消息推送',
      '📊 资源友好 - 低内存占用'
    ]
  },
  {
    icon: '🌐',
    title: '开放生态',
    desc: '开源透明，社区活跃，共同成长',
    details: [
      '📖 完全开源 - 代码完全透明',
      '👥 社区活跃 - 众多开发者参与',
      '📦 持续更新 - 每月都有新功能',
      '💬 及时支持 - 遇到问题有人帮'
    ]
  }
]
</script>

<template>
  <section class="features-section" id="features">
    <h2 class="section-title reveal">
      <span class="gradient-text">特色功能</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      强大而灵活的技术架构，让 AI 助手真正成为你的得力工具
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
        <div class="feature-desc">{{ feature.desc }}</div>
        <div class="feature-details">
          <ul>
            <li v-for="detail in feature.details" :key="detail">
              {{ detail }}
            </li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="feature-cta reveal">
      <a href="#install" class="btn btn-primary">开始使用 →</a>
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
  max-width: 600px;
  margin: 0 auto 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
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

.feature-card:hover .feature-details {
  max-height: 200px;
  opacity: 1;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
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

.feature-details {
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: all 0.4s ease;
}

.feature-details ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-details li {
  font-size: 0.85rem;
  color: var(--text-muted);
  padding: 0.4rem 0;
  transition: all 0.2s ease;
}

.feature-card:hover .feature-details li {
  padding-left: 0.5rem;
}

.feature-cta {
  text-align: center;
  margin-top: 3rem;
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

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .feature-card:hover .feature-details {
    max-height: none;
  }
  
  .feature-details {
    max-height: none;
    opacity: 1;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
  }
}
</style>
