<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

interface Agent {
  name: string
  state: string
  detail: string
  avatar: string
}

const agents = ref<Agent[]>([])
let pollInterval: number | null = null

const fetchAgents = async () => {
  try {
    const res = await fetch('http://localhost:19000/agents')
    const data = await res.json()
    // 过滤出贾维斯和马斯克
    agents.value = (data as Agent[])
      .filter((a: Agent) => a.name === '贾维斯' || a.name === '马斯克')
      .slice(0, 2)
  } catch (e) {
    // 静默失败
  }
}

onMounted(() => {
  // 立即获取
  fetchAgents()
  // 每 3 秒轮询
  pollInterval = window.setInterval(fetchAgents, 3000)
  
  // Trigger animation on mount
  setTimeout(() => {
    const heroContent = document.querySelector('.hero-content > *')
    heroContent?.classList.add('visible')
  }, 100)
})

onUnmounted(() => {
  if (pollInterval) clearInterval(pollInterval)
})

const getStateText = (state: string) => {
  const map: Record<string, string> = {
    'idle': '待命',
    'working': '工作中',
    'sync': '同步中',
    'alert': '报警',
  }
  return map[state] || state
}

const getStateClass = (state: string) => {
  if (state === 'working') return 'state-working'
  if (state === 'idle') return 'state-idle'
  return ''
}

const openOffice = () => {
  window.open('http://localhost:19000', '_blank')
}
</script>

<template>
  <section class="hero" id="intro">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <!-- Agent 状态展示 -->
      <div class="agents-status" v-if="agents.length > 0">
        <div 
          v-for="agent in agents" 
          :key="agent.name"
          class="agent-card"
          :class="getStateClass(agent.state)"
          @click="openOffice"
          style="cursor: pointer;"
        >
          <div class="agent-avatar">
            <svg viewBox="0 0 40 40" fill="none">
              <circle cx="20" cy="20" r="18" fill="#2563EB"/>
              <ellipse cx="20" cy="23" rx="10" ry="7" fill="#F97316"/>
              <circle cx="16" cy="19" r="2" fill="#1E293B"/>
              <circle cx="24" cy="19" r="2" fill="#1E293B"/>
              <path d="M17 25 Q20 27 23 25" stroke="#1E293B" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
          </div>
          <div class="agent-info">
            <span class="agent-name">{{ agent.name }}</span>
            <span class="agent-state">{{ getStateText(agent.state) }}</span>
          </div>
        </div>
      </div>
      
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

/* Agent 状态卡片 */
.agents-status {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.agent-card {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1.25rem;
  background: var(--bg-elevated);
  border-radius: 12px;
  border: 2px solid var(--border);
  transition: all 0.3s ease;
}

.agent-card.state-working {
  border-color: #22c55e;
  background: rgba(34, 197, 94, 0.1);
}

.agent-card.state-idle {
  border-color: var(--border);
}

.agent-avatar {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}

.agent-avatar svg {
  width: 100%;
  height: 100%;
}

.agent-info {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.agent-name {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text);
}

.agent-state {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.state-working .agent-state {
  color: #22c55e;
}

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
