<script setup lang="ts">
import { onMounted, ref, nextTick } from 'vue'
import { useScrollReveal } from '../composables/useScrollReveal'

interface Feature {
  icon: string
  title: string
  desc: string
}

interface Skill {
  name: string
  url: string
}

const icons = {
  robot: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="10" width="16" height="11" rx="2"/><circle cx="12" cy="5" r="2.5"/><path d="M12 7.5v3"/><path d="M9 15h6"/><circle cx="9" cy="16" r="1" fill="currentColor"/><circle cx="15" cy="16" r="1" fill="currentColor"/></svg>`,
  plugin: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v6m0 8v6M4.93 4.93l4.24 4.24m5.66 5.66l4.24 4.24M2 12h6m8 0h6M4.93 19.07l4.24-4.24m5.66-5.66l4.24-4.24"/></svg>`,
  chat: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h2m0 0h2m-2 0v2m0-2h2m-2 0v2"/></svg>`,
  globe: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M5.6 5.6l12.8 12.8M18.4 5.6L5.6 18.4"/></svg>`,
  chevron: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>`,
}

const topSkills: Skill[] = [
  { name: 'Tavily Web Search', url: 'https://clawhub.ai/arun-8687/tavily-search' },
  { name: 'Self-Improving Agent', url: 'https://clawhub.ai/pskoett/self-improving-agent' },
  { name: 'Find Skills', url: 'https://clawhub.ai/JimLiuxinghai/find-skills' },
  { name: 'Summarize', url: 'https://clawhub.ai/steipete/summarize' },
  { name: 'Agent Browser', url: 'https://clawhub.ai/TheSethRose/agent-browser' },
]

const features: Feature[] = [
  { icon: icons.robot, title: 'AI Agent', desc: '多Agent协作<br>智能任务处理' },
  { icon: icons.plugin, title: 'Skill 扩展', desc: '丰富插件系统<br>按需灵活调用' },
  { icon: icons.chat, title: '多渠道', desc: 'Telegram<br>Discord/微信/Signal' },
  { icon: icons.globe, title: 'Web API', desc: '随时随地<br>远程控制' },
]

const expandedCard = ref<string | null>(null)

const toggleExpand = (title: string) => {
  expandedCard.value = expandedCard.value === title ? null : title
}

const openSkillUrl = (url: string) => {
  window.open(url, '_blank')
}

const sectionRef = ref<HTMLElement | null>(null)

// Use composable for scroll reveal
useScrollReveal(sectionRef)

// 确保 visible 类在交互时不被移除
onMounted(() => {
  nextTick(() => {
    const reveals = document.querySelectorAll('.features-section .reveal')
    reveals.forEach(el => el.classList.add('visible'))
  })
})
</script>

<template>
  <section class="features-section section" id="features" ref="sectionRef">
    <h2 class="section-title reveal">
      <span class="title-accent"></span>
      核心功能
    </h2>
    
    <div class="features-container">
      <div 
        v-for="(feature, index) in features" 
        :key="feature.title"
        class="feature-wrapper"
      >
        <div 
          class="feature-card block"
          :class="[
            { 'reveal': true, 'expandable': feature.title === 'Skill 扩展', 'active': expandedCard === feature.title },
            `reveal-delay-${index + 1}`,
            { 'visible': true }
          ]"
          @click="feature.title === 'Skill 扩展' && toggleExpand(feature.title)"
        >
          <div class="card-content">
            <div class="feature-icon" v-html="feature.icon"></div>
            <div class="feature-title">{{ feature.title }}</div>
            <div class="feature-desc" v-html="feature.desc"></div>
            
            <div v-if="feature.title === 'Skill 扩展'" class="expand-indicator" :class="{ rotated: expandedCard === feature.title }">
              <span v-html="icons.chevron"></span>
            </div>
          </div>
        </div>
        
        <!-- Skill Details Panel - 横向展开 -->
        <Transition name="slide">
          <div v-if="expandedCard === feature.title && feature.title === 'Skill 扩展'" class="skill-details">
            <div class="details-arrow"></div>
            <div class="details-content">
              <div class="details-header">
                <span class="details-icon" v-html="icons.plugin"></span>
                <span class="details-title">Skill 扩展</span>
              </div>
              <div class="details-subtitle">精选热门插件推荐</div>
              <div class="skills-list">
                <div 
                  v-for="(skill, skillIndex) in topSkills" 
                  :key="skillIndex"
                  class="skill-item"
                  @click="openSkillUrl(skill.url)"
                >
                  <span class="skill-rank">{{ skillIndex + 1 }}</span>
                  <span class="skill-name">{{ skill.name }}</span>
                  <span class="skill-arrow">→</span>
                </div>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </section>
</template>

<style scoped>
.features-section {
  background: var(--bg-subtle);
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

.features-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.feature-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 0;
  flex-shrink: 0;
  position: relative;
}

.feature-card {
  background: var(--bg-elevated);
  padding: 1.5rem;
  cursor: pointer;
  position: relative;
  min-width: 240px;
  min-height: 140px;
  height: 100%;
  display: flex;
  flex-direction: column;
  z-index: 55;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card.expandable:hover {
  border-color: var(--primary);
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.feature-card.active {
  border-color: var(--primary);
  box-shadow: 0 0 0 2px var(--primary);
}

.card-content {
  padding: 0.5rem;
  cursor: pointer;
}

.feature-icon {
  width: 44px;
  height: 44px;
  margin-bottom: 1rem;
  color: var(--primary);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-icon :deep(svg) {
  width: 100%;
  height: 100%;
}

.feature-card:hover .feature-icon {
  color: var(--accent);
  transform: scale(1.1);
}

.feature-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--text);
}

.feature-desc {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.5;
}

.expand-indicator {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 24px;
  height: 24px;
  color: var(--text-muted);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.expand-indicator.rotated {
  transform: rotate(180deg);
  color: var(--primary);
}

.expand-indicator :deep(svg) {
  width: 100%;
  height: 100%;
}

/* Skill Details Panel */
.skill-details {
  position: absolute;
  left: 100%;
  top: 0;
  margin-left: 1rem;
  width: 340px;
  background: var(--bg-elevated);
  border: 1px solid var(--primary);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: 0 20px 60px -20px rgba(37, 99, 235, 0.3);
  z-index: 60;
}

.details-arrow {
  position: absolute;
  left: -8px;
  top: 24px;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-right: 8px solid var(--primary);
}

.details-arrow::before {
  content: '';
  position: absolute;
  left: 2px;
  top: -8px;
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-right: 8px solid var(--bg-elevated);
}

.details-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.25rem;
}

.details-icon {
  width: 24px;
  height: 24px;
  color: var(--primary);
}

.details-icon :deep(svg) {
  width: 100%;
  height: 100%;
}

.details-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
}

.details-subtitle {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 1rem;
}

.skills-list {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.skill-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 0.875rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  background: var(--bg-subtle);
}

.skill-item:hover {
  background: var(--primary);
  transform: translateX(4px);
}

.skill-item:hover .skill-rank {
  background: white;
  color: var(--primary);
}

.skill-item:hover .skill-name {
  color: white;
}

.skill-item:hover .skill-arrow {
  color: white;
}

.skill-rank {
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--primary);
  color: white;
  font-size: 0.7rem;
  font-weight: 600;
  border-radius: 50%;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.skill-name {
  flex: 1;
  font-size: 0.85rem;
  color: var(--text);
  font-weight: 500;
  transition: color 0.2s ease;
}

.skill-arrow {
  color: var(--text-muted);
  font-size: 0.85rem;
  transition: color 0.2s ease;
}

/* Slide Transition */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateX(0);
}

@media (max-width: 900px) {
  .features-container {
    flex-direction: column;
    align-items: stretch;
  }
  
  .feature-wrapper {
    width: 100%;
  }
  
  .feature-card {
    min-width: auto;
    width: 100%;
  }
  
  .skill-details {
    position: relative;
    left: auto;
    top: auto;
    margin-left: 0;
    margin-top: 1rem;
    width: 100%;
  }
  
  .details-arrow {
    display: none;
  }
}

@media (max-width: 600px) {
  .section-title {
    font-size: 2rem;
  }
}
</style>
