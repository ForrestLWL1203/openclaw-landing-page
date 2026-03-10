<script setup lang="ts">
import { onMounted, ref } from 'vue'

const activeStep = ref(1)

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
        }
      })
    },
    { threshold: 0.2 }
  )
  
  document.querySelectorAll('.install-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

const steps = [
  {
    number: 1,
    title: '环境准备',
    desc: '安装 Node.js 环境',
    details: [
      '下载并安装 Node.js（推荐 18.x 或更高版本）',
      'Windows 用户：访问 nodejs.org 下载安装包',
      'Mac 用户：推荐使用 Homebrew 安装：brew install node',
      'Linux 用户：使用包管理器安装，如 Ubuntu: sudo apt install nodejs npm'
    ]
  },
  {
    number: 2,
    title: '安装 OpenClaw',
    desc: '全局安装 CLI 工具',
    details: [
      '打开终端（Windows 用户使用 PowerShell 或 CMD）',
      '运行安装命令：npm install -g openclaw',
      '等待安装完成（约 1-2 分钟）',
      '验证安装：运行 openclaw --version'
    ]
  },
  {
    number: 3,
    title: '初始化 Gateway',
    desc: '启动本地服务',
    details: [
      '初始化配置：openclaw gateway init',
      '启动 Gateway 服务：openclaw gateway服务启动 start',
      '成功后，浏览器访问 http://localhost:8080',
      '按 Ctrl+C 可停止服务'
    ]
  },
  {
    number: 4,
    title: '连接平台',
    desc: '绑定你的通讯渠道',
    details: [
      '在 Gateway 界面选择要连接的平台（Telegram/Discord/微信等）',
      '按照指引获取 API 密钥',
      '完成绑定即可开始使用',
      '支持多平台同时在线'
    ]
  }
]

const copyCommand = (cmd: string) => {
  navigator.clipboard.writeText(cmd)
}

const commands = [
  { comment: '# 1. 安装 OpenClaw CLI', command: 'npm install -g openclaw' },
  { comment: '# 2. 初始化 Gateway', command: 'openclaw gateway init' },
  { comment: '# 3. 启动服务', command: 'openclaw gateway start' },
]
</script>

<template>
  <section class="install-section" id="install">
    <h2 class="section-title reveal">
      <span class="gradient-text">快速开始</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      零基础也能轻松上手，最快 5 分钟完成安装配置
    </p>

    <!-- Quick commands for advanced users -->
    <div class="quick-start terminal glass reveal reveal-delay-2">
      <div class="terminal-header">
        <div class="terminal-dot red"></div>
        <div class="terminal-dot yellow"></div>
        <div class="terminal-dot green"></div>
        <span class="terminal-title">Terminal</span>
      </div>
      <div class="terminal-body">
        <template v-for="item in commands" :key="item.command">
          <div class="cmd-line">
            <span class="cmd-comment">{{ item.comment }}</span>
            <div class="cmd-command" @click="copyCommand(item.command)">
              <span class="cmd-text">{{ item.command }}</span>
              <span class="copy-hint">📋 点击复制</span>
            </div>
          </div>
        </template>
      </div>
    </div>

    <!-- Step by step guide -->
    <div class="steps-container">
      <div 
        v-for="(step, index) in steps" 
        :key="step.number"
        class="step-card reveal"
        :class="[`reveal-delay-${index + 1}`, { active: activeStep === step.number }]"
        @click="activeStep = step.number"
      >
        <div class="step-number">{{ step.number }}</div>
        <div class="step-content">
          <h3 class="step-title">{{ step.title }}</h3>
          <p class="step-desc">{{ step.desc }}</p>
          <div class="step-details" v-show="activeStep === step.number">
            <ul>
              <li v-for="detail in step.details" :key="detail">
                {{ detail }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Prerequisites -->
    <div class="prerequisites glass reveal reveal-delay-5">
      <h3 class="prereq-title">📦 准备工作</h3>
      <div class="prereq-grid">
        <div class="prereq-item">
          <span class="prereq-icon">🟢</span>
          <div>
            <strong>Node.js</strong>
            <p>版本 18.x 或更高</p>
          </div>
        </div>
        <div class="prereq-item">
          <span class="prereq-icon">📦</span>
          <div>
            <strong>npm</strong>
            <p>随 Node.js 一起安装</p>
          </div>
        </div>
        <div class="prereq-item">
          <span class="prereq-icon">🌐</span>
          <div>
            <strong>网络</strong>
            <p>需要访问 npm 仓库</p>
          </div>
        </div>
        <div class="prereq-item">
          <span class="prereq-icon">💻</span>
          <div>
            <strong>终端</strong>
            <p>PowerShell / CMD / Terminal</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Help section -->
    <div class="help-section reveal reveal-delay-5">
      <p>遇到问题？查看 <a href="https://github.com" target="_blank">官方文档</a> 或加入社区寻求帮助</p>
    </div>
  </section>
</template>

<style scoped>
.install-section {
  padding: 6rem 2rem;
  background: var(--bg-subtle);
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
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

/* Quick start terminal */
.quick-start {
  max-width: 700px;
  margin: 0 auto 3rem;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.terminal-header {
  padding: 0.75rem 1rem;
  background: var(--bg-elevated);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-bottom: 1px solid var(--border);
}

.terminal-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.terminal-dot.red { background: #ff5f56; }
.terminal-dot.yellow { background: #ffbd2e; }
.terminal-dot.green { background: #27c93f; }

.terminal-title {
  margin-left: auto;
  margin-right: auto;
  font-size: 0.8rem;
  color: var(--text-muted);
}

.terminal-body {
  padding: 1.5rem;
  font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: 0.95rem;
  line-height: 1.8;
  background: var(--bg);
}

.cmd-line {
  margin-bottom: 1rem;
}

.cmd-comment {
  display: block;
  color: var(--accent);
  margin-bottom: 0.25rem;
}

.cmd-command {
  color: var(--text);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  background: var(--bg-subtle);
}

.cmd-command:hover {
  background: var(--bg-elevated);
}

.cmd-command:hover .cmd-text {
  color: var(--primary);
}

.copy-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  opacity: 0;
  transition: opacity 0.2s;
}

.cmd-command:hover .copy-hint {
  opacity: 1;
}

/* Steps */
.steps-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto 3rem;
}

.step-card {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  cursor: pointer;
  transition: all 0.3s ease;
}

.step-card:hover,
.step-card.active {
  border-color: var(--primary);
  transform: translateY(-4px);
}

.step-card.active {
  box-shadow: 0 10px 40px -10px rgba(99, 102, 241, 0.3);
}

.step-number {
  width: 40px;
  height: 40px;
  background: var(--gradient-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: white;
  flex-shrink: 0;
}

.step-content {
  flex: 1;
}

.step-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.step-desc {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.step-details {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
}

.step-details ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.step-details li {
  font-size: 0.85rem;
  color: var(--text-muted);
  padding: 0.4rem 0;
  padding-left: 1rem;
  position: relative;
}

.step-details li::before {
  content: '›';
  position: absolute;
  left: 0;
  color: var(--primary);
  font-weight: bold;
}

/* Prerequisites */
.prerequisites {
  max-width: 900px;
  margin: 0 auto 2rem;
  padding: 2rem;
  border-radius: var(--radius);
}

.prereq-title {
  text-align: center;
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
}

.prereq-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
}

.prereq-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--bg-subtle);
  border-radius: 0.75rem;
}

.prereq-icon {
  font-size: 1.5rem;
}

.prereq-item strong {
  display: block;
  font-size: 0.95rem;
}

.prereq-item p {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin: 0;
}

/* Help section */
.help-section {
  text-align: center;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.help-section a {
  color: var(--primary);
  text-decoration: none;
}

.help-section a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .steps-container {
    grid-template-columns: 1fr;
  }
}
</style>
