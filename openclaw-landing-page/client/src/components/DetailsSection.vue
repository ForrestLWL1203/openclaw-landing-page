<script setup lang="ts">
import { ref } from 'vue'
import { useScrollReveal } from '../composables/useScrollReveal'

const sectionRef = ref<HTMLElement | null>(null)

const icons = {
  chat: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>`,
  robot: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><circle cx="12" cy="16" r="1" fill="currentColor"/><path d="M8 11h8"/></svg>`,
  plugin: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`,
  globe: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`,
  shield: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
  lightning: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>`,
}

const features = [
  { icon: icons.chat, title: '多渠道支持', desc: 'WhatsApp、Telegram、Discord 等主流平台' },
  { icon: icons.robot, title: 'AI 智能助手', desc: '连接 Claude、GPT 等大语言模型' },
  { icon: icons.plugin, title: '插件系统', desc: '灵活扩展，支持自定义集成' },
  { icon: icons.globe, title: '跨平台运行', desc: 'Windows、macOS、Linux 全面支持' },
  { icon: icons.shield, title: '安全可靠', desc: '本地部署，数据隐私有保障' },
  { icon: icons.lightning, title: '实时响应', desc: 'WebSocket 低延迟通信' },
]

// Use composable for scroll reveal
useScrollReveal(sectionRef)
</script>

<template>
  <section class="details-section section" id="details" ref="sectionRef">
    <h2 class="section-title reveal">
      <span class="title-accent"></span>
      了解更多
    </h2>
    <div class="details-grid">
      <div 
        v-for="(feature, index) in features" 
        :key="feature.title"
        class="feature-card block reveal"
        :class="`reveal-delay-${index + 1}`"
      >
        <span class="feature-icon" v-html="feature.icon"></span>
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.desc }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.details-section {
  background: var(--bg);
  position: relative;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  color: var(--text);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.title-accent {
  width: 48px;
  height: 4px;
  background: var(--gradient-primary);
  border-radius: 2px;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.feature-card {
  padding: 1.5rem;
  text-align: left;
}

.feature-icon {
  width: 40px;
  height: 40px;
  display: block;
  margin-bottom: 0.75rem;
  color: var(--primary);
}

.feature-icon :deep(svg) {
  width: 100%;
  height: 100%;
}

.feature-card h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 0.5rem;
}

.feature-card p {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.5;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .details-grid {
    grid-template-columns: 1fr;
  }
}
</style>
