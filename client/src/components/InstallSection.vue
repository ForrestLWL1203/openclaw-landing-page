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
    { threshold: 0.2 }
  )
  
  document.querySelectorAll('.install-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

const commands = [
  { comment: '# 安装 CLI', command: 'npm install -g openclaw' },
  { comment: '# 初始化 Gateway', command: 'openclaw gateway init' },
  { comment: '# 启动服务', command: 'openclaw gateway start' },
]

const copyCommand = (cmd: string) => {
  navigator.clipboard.writeText(cmd)
}
</script>

<template>
  <section class="install-section" id="install">
    <h2 class="section-title reveal">
      <span class="gradient-text">快速安装</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      仅需三步，即可开启你的 AI 助手之旅
    </p>
    <div class="terminal glass reveal reveal-delay-2">
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
    <div class="install-features reveal reveal-delay-3">
      <div class="install-feature">
        <span class="install-icon">🚀</span>
        <span>开箱即用</span>
      </div>
      <div class="install-feature">
        <span class="install-icon">🔄</span>
        <span>自动更新</span>
      </div>
      <div class="install-feature">
        <span class="install-icon">🛡️</span>
        <span>安全可靠</span>
      </div>
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
}

.terminal {
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

.install-features {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.install-feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-muted);
  font-size: 0.95rem;
}

.install-icon {
  font-size: 1.25rem;
}

@media (max-width: 768px) {
  .install-features {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }
}
</style>
