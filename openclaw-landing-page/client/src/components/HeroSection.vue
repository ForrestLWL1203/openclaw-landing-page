<script setup lang="ts">
import { ref } from 'vue'

const isExpanded = ref(false)

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}

const features = [
  { icon: '💬', title: '多渠道支持', desc: 'WhatsApp、Telegram、Discord 等主流平台' },
  { icon: '🤖', title: 'AI 智能助手', desc: '连接 Claude、GPT 等大语言模型' },
  { icon: '🔌', title: '插件系统', desc: '灵活扩展，支持自定义集成' },
  { icon: '🌐', title: '跨平台运行', desc: 'Windows、macOS、Linux 全面支持' },
  { icon: '🔒', title: '安全可靠', desc: '本地部署，数据隐私有保障' },
  { icon: '⚡', title: '实时响应', desc: 'WebSocket 低延迟通信' },
]
</script>

<template>
  <section class="hero" id="intro">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="crawfish-container" @click="toggleExpand">
        🦞
      </div>
      <h1>小龙虾闪亮登场！</h1>
      <p>你的智能 AI 助手 · 多平台支持 · 无限可能</p>
      
      <!-- 展开详情区域 -->
      <Transition name="expand">
        <div v-if="isExpanded" class="hero-details">
          <div class="details-grid">
            <div v-for="feature in features" :key="feature.title" class="feature-card">
              <span class="feature-icon">{{ feature.icon }}</span>
              <h3>{{ feature.title }}</h3>
              <p>{{ feature.desc }}</p>
            </div>
          </div>
          <button class="collapse-btn" @click="toggleExpand">
            收起详情 △
          </button>
        </div>
      </Transition>
      
      <button v-if="!isExpanded" class="expand-hint" @click="toggleExpand">
        了解更多 ↓
      </button>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: auto;
  padding: 80px 2rem 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
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
  max-width: 800px;
  width: 100%;
}

.crawfish-container {
  font-size: 100px;
  line-height: 1;
  margin-bottom: 0.5rem;
  animation: float 3s ease-in-out infinite;
  filter: drop-shadow(0 10px 20px rgba(37, 99, 235, 0.2));
  cursor: pointer;
  transition: transform 0.3s ease;
}

.crawfish-container:hover {
  transform: scale(1.1);
}

.hero h1 {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--primary) 0%, #ff8fa3 50%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: fadeInUp 0.8s ease-out;
}

.hero > .hero-content > p {
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 400px;
  margin: 0 auto 1.5rem;
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.expand-hint {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 0.75rem 2rem;
  border-radius: 2rem;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  animation: fadeInUp 0.8s ease-out 0.4s both;
}

.expand-hint:hover {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

/* 展开详情区域 */
.hero-details {
  margin-top: 2rem;
  padding: 2rem 0;
  animation: fadeInUp 0.5s ease-out;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.feature-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  text-align: left;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: var(--primary);
  box-shadow: var(--shadow);
}

.feature-icon {
  font-size: 2rem;
  display: block;
  margin-bottom: 0.75rem;
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

.collapse-btn {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 0.75rem 2rem;
  border-radius: 2rem;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.collapse-btn:hover {
  background: var(--bg-elevated);
  color: var(--text);
}

/* 展开动画 */
.expand-enter-active,
.expand-leave-active {
  transition: all 0.4s ease;
  overflow: hidden;
}

.expand-enter-from,
.expand-leave-to {
  opacity: 0;
  max-height: 0;
  transform: translateY(-20px);
}

.expand-enter-to,
.expand-leave-from {
  opacity: 1;
  max-height: 800px;
  transform: translateY(0);
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.25rem;
  }
  
  .crawfish-container {
    font-size: 80px;
  }
  
  .details-grid {
    grid-template-columns: 1fr;
  }
}
</style>
