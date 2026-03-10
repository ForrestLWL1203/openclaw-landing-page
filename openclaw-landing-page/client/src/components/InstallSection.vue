<script setup lang="ts">
import { ref } from 'vue'

interface Step {
  id: number
  title: string
  desc: string
  command: string
  details: string[]
  link?: string
}

const steps: Step[] = [
  {
    id: 1,
    title: '安装 CLI',
    desc: '全局安装 OpenClaw 命令行工具',
    command: 'npm install -g openclaw@latest',
    details: [
      '前置要求：Node.js >= 18，推荐使用 Node.js 22+',
      'Windows 用户推荐使用 WSL2（Ubuntu）运行',
      'macOS/Linux 用户可直接安装',
      '安装完成后验证：openclaw --version',
    ],
    link: 'https://docs.openclaw.ai/zh-CN/start/quickstart'
  },
  {
    id: 2,
    title: '安装 Node.js',
    desc: '安装 Node.js 环境（如果没有）',
    command: 'node -v',
    details: [
      '推荐使用 nvm 管理 Node.js 版本',
      '运行 nvm install 22 安装 Node.js 22',
      '运行 nvm use 22 切换版本',
      '或从官网 https://nodejs.org 下载安装',
    ],
    link: 'https://nodejs.org/'
  },
  {
    id: 3,
    title: '初始化 Gateway',
    desc: '配置本地 Gateway 服务',
    command: 'openclaw onboard --install-daemon',
    details: [
      '按提示选择认证方式（OAuth 或 API 密钥）',
      '选择所需的渠道（WhatsApp/Telegram/Discord）',
      '配置 Gateway 网关端口（默认 18789）',
      '配置文件保存在 ~/.openclaw/',
    ],
    link: 'https://docs.openclaw.ai/zh-CN/start/wizard'
  },
  {
    id: 4,
    title: '配置 Agent',
    desc: '配置 AI 助手连接',
    command: 'openclaw gateway start',
    details: [
      '启动 Gateway 网关服务',
      '访问 http://127.0.0.1:18789/ 打开控制界面',
      '在控制界面配置 AI 模型和 API 密钥',
      '详细配置请参考官方文档',
    ],
    link: 'https://docs.openclaw.ai/zh-CN'
  }
]

const expandedStep = ref<number | null>(null)

const toggleStep = (id: number) => {
  expandedStep.value = expandedStep.value === id ? null : id
}

// 计算每个步骤的偏移量
const getStepOffset = (stepId: number) => {
  if (expandedStep.value === null) return 0
  if (expandedStep.value >= stepId) return 0
  
  // 展开的步骤会让后面的步骤右移
  const expandedIndex = steps.findIndex(s => s.id === expandedStep.value)
  const currentIndex = steps.findIndex(s => s.id === stepId)
  
  if (currentIndex > expandedIndex) {
    // 返回详情区域的宽度 + gap
    return 380 
  }
  return 0
}

const copyCommand = (cmd: string) => {
  navigator.clipboard.writeText(cmd)
}
</script>

<template>
  <section class="install-section" id="install">
    <h2 class="section-title">🚀 快速开始</h2>
    <p class="section-subtitle">4 步轻松搭建你的 AI 助手</p>
    
    <div class="steps-container">
      <div 
        v-for="step in steps" 
        :key="step.id"
        class="step-wrapper"
        :class="{ 'is-expanded': expandedStep === step.id }"
        :style="{ 
          transform: `translateX(${getStepOffset(step.id)}px)`,
          transition: 'transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)'
        }"
      >
        <div 
          class="step-card"
          :class="{ expanded: expandedStep === step.id }"
          @click="toggleStep(step.id)"
        >
          <div class="step-number">{{ step.id }}</div>
          <div class="step-header-content">
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-desc">{{ step.desc }}</p>
          </div>
          <div class="step-indicator">
            <span v-if="expandedStep === step.id" class="indicator-icon">−</span>
            <span v-else class="indicator-icon">+</span>
          </div>
        </div>
        
        <!-- 展开详情 - 浮动在右侧 -->
        <Transition name="slide">
          <div v-if="expandedStep === step.id" class="step-details">
            <div class="details-arrow"></div>
            <div class="details-content">
              <div class="command-block" @click="copyCommand(step.command)">
                <code>{{ step.command }}</code>
                <span class="copy-hint">点击复制</span>
              </div>
              
              <ul class="details-list">
                <li v-for="(detail, idx) in step.details" :key="idx">
                  {{ detail }}
                </li>
              </ul>
              
              <a 
                v-if="step.link" 
                :href="step.link" 
                target="_blank"
                class="learn-more-link"
              >
                查看官方文档 →
              </a>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </section>
</template>

<style scoped>
.install-section {
  padding: 6rem 2rem;
  background: var(--bg-subtle);
  position: relative;
  overflow: hidden;
}

.install-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--border), transparent);
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-subtitle {
  text-align: center;
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 4rem;
}

.steps-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding-left: 2rem;
}

.step-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 0;
  flex-shrink: 0;
}

.step-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  min-width: 200px;
  display: flex;
  flex-direction: column;
}

.step-card:hover {
  border-color: var(--primary);
  transform: translateY(-3px);
  box-shadow: var(--shadow);
}

.step-card.expanded {
  border-color: var(--primary);
  box-shadow: 0 12px 40px -12px rgba(99, 102, 241, 0.4);
}

.step-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.step-header-content {
  flex: 1;
}

.step-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 0.5rem;
}

.step-desc {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.4;
}

.step-indicator {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 1.2rem;
  transition: all 0.3s ease;
}

.step-card:hover .step-indicator {
  color: var(--primary);
}

/* 展开详情 - 浮动在卡片右侧 */
.step-details {
  position: absolute;
  left: 100%;
  top: 0;
  margin-left: 1rem;
  width: 360px;
  background: var(--bg-elevated);
  border: 1px solid var(--primary);
  border-radius: var(--radius);
  padding: 1.5rem;
  box-shadow: 0 20px 60px -20px rgba(99, 102, 241, 0.5);
  z-index: 10;
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

.details-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.command-block {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.command-block:hover {
  border-color: var(--primary);
  background: rgba(99, 102, 241, 0.1);
}

.command-block code {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  color: var(--accent);
  font-size: 0.9rem;
}

.copy-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  opacity: 0;
  transition: opacity 0.2s;
}

.command-block:hover .copy-hint {
  opacity: 1;
}

.details-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.details-list li {
  color: var(--text-muted);
  padding: 0.5rem 0;
  padding-left: 1.25rem;
  position: relative;
  font-size: 0.85rem;
  line-height: 1.5;
}

.details-list li::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: var(--primary);
  font-size: 0.8rem;
}

.learn-more-link {
  display: inline-block;
  color: var(--accent);
  font-size: 0.85rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.learn-more-link:hover {
  color: var(--primary);
  transform: translateX(3px);
}

/* 展开动画 */
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

@media (max-width: 1200px) {
  .steps-container {
    flex-direction: column;
    align-items: stretch;
    padding-left: 0;
  }
  
  .step-wrapper {
    width: 100%;
  }
  
  .step-card {
    min-width: auto;
    width: 100%;
  }
  
  .step-details {
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
