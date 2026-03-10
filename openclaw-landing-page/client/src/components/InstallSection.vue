<script setup lang="ts">
import { ref } from 'vue'

interface Step {
  id: number
  title: string
  desc: string
  command: string
  details: string[]
}

const steps: Step[] = [
  {
    id: 1,
    title: '安装 CLI',
    desc: '全局安装 OpenClaw 命令行工具',
    command: 'npm install -g openclaw',
    details: [
      '确保已安装 Node.js 18+ 版本',
      '使用 npm 或 yarn 全局安装',
      '安装完成后验证：openclaw --version'
    ]
  },
  {
    id: 2,
    title: '初始化 Gateway',
    desc: '配置本地 Gateway 服务',
    command: 'openclaw gateway init',
    details: [
      '按提示配置 API Key',
      '选择所需的插件和服务',
      '配置文件保存在 ~/.openclaw/'
    ]
  },
  {
    id: 3,
    title: '启动服务',
    desc: '启动本地 Gateway 服务',
    command: 'openclaw gateway start',
    details: [
      '默认端口：7437',
      '支持 HTTP/WebSocket 协议',
      '访问 http://localhost:7437 查看状态'
    ]
  },
  {
    id: 4,
    title: '连接 Assistant',
    desc: '配置 AI 助手连接',
    command: 'openclaw assistant connect',
    details: [
      '支持多种 AI 提供商',
      '配置模型和参数选项',
      '开始使用你的 AI 助手'
    ]
  }
]

const expandedStep = ref<number | null>(null)
const showModal = ref(false)
const modalStep = ref<Step | null>(null)

const toggleStep = (id: number) => {
  expandedStep.value = expandedStep.value === id ? null : id
}

const openModal = (step: Step) => {
  modalStep.value = step
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  modalStep.value = null
}

const copyCommand = (cmd: string) => {
  navigator.clipboard.writeText(cmd)
}
</script>

<template>
  <section class="install-section" id="install">
    <h2 class="section-title">📥 快速开始</h2>
    
    <div class="steps-container">
      <div 
        v-for="step in steps" 
        :key="step.id"
        class="step-item"
        :class="{ expanded: expandedStep === step.id }"
      >
        <div class="step-header" @click="toggleStep(step.id)">
          <div class="step-number">{{ step.id }}</div>
          <div class="step-title">{{ step.title }}</div>
          <div class="step-desc">{{ step.desc }}</div>
          <button class="expand-btn" @click.stop="openModal(step)">
            查看详情
          </button>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <Teleport to="body">
      <div v-if="showModal" class="modal-overlay" @click="closeModal">
        <div class="modal-content" @click.stop>
          <button class="modal-close" @click="closeModal">&times;</button>
          <div class="modal-header">
            <span class="modal-number">{{ modalStep?.id }}</span>
            <h3>{{ modalStep?.title }}</h3>
          </div>
          <p class="modal-desc">{{ modalStep?.desc }}</p>
          
          <div class="modal-command" @click="copyCommand(modalStep?.command || '')">
            <code>{{ modalStep?.command }}</code>
            <span class="copy-hint">📋 点击复制</span>
          </div>
          
          <div class="modal-details">
            <h4>详细说明：</h4>
            <ul>
              <li v-for="(detail, idx) in modalStep?.details" :key="idx">
                {{ detail }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </Teleport>
  </section>
</template>

<style scoped>
.install-section {
  padding: 5rem 2rem;
  background: var(--bg-subtle);
}

.section-title {
  text-align: center;
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 3rem;
  color: var(--text);
}

.steps-container {
  max-width: 700px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.step-item {
  border-radius: var(--radius);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  overflow: hidden;
  transition: all 0.3s ease;
}

.step-item:hover {
  border-color: var(--primary);
}

.step-item.expanded {
  border-color: var(--primary);
}

.step-header {
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
}

.step-number {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}

.step-title {
  font-weight: 600;
  font-size: 1.1rem;
  color: var(--text);
}

.step-desc {
  flex: 1;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.expand-btn {
  padding: 0.5rem 1rem;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text-muted);
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}

.expand-btn:hover {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-content {
  background: var(--bg-elevated);
  border-radius: var(--radius);
  padding: 2rem;
  max-width: 500px;
  width: 100%;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--text-muted);
  cursor: pointer;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s;
}

.modal-close:hover {
  background: var(--bg-subtle);
  color: var(--text);
}

.modal-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.modal-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.2rem;
}

.modal-header h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text);
  margin: 0;
}

.modal-desc {
  color: var(--text-muted);
  margin-bottom: 1.5rem;
}

.modal-command {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 1.5rem;
}

.modal-command:hover {
  border-color: var(--primary);
}

.modal-command code {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  color: var(--text);
}

.copy-hint {
  font-size: 0.8rem;
  color: var(--text-muted);
  opacity: 0;
  transition: opacity 0.2s;
}

.modal-command:hover .copy-hint {
  opacity: 1;
}

.modal-details h4 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 0.75rem;
}

.modal-details ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.modal-details li {
  color: var(--text-muted);
  padding: 0.5rem 0;
  padding-left: 1.5rem;
  position: relative;
  font-size: 0.9rem;
}

.modal-details li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary);
}

@media (max-width: 768px) {
  .step-header {
    flex-wrap: wrap;
  }
  
  .step-desc {
    width: 100%;
    order: 3;
    margin-top: 0.5rem;
  }
  
  .expand-btn {
    margin-left: auto;
  }
}
</style>
