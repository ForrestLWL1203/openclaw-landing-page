<script setup lang="ts">
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
    <h2 class="section-title">📥 快速安装</h2>
    <div class="terminal glass">
      <div class="terminal-header">
        <div class="terminal-dot red"></div>
        <div class="terminal-dot yellow"></div>
        <div class="terminal-dot green"></div>
      </div>
      <div class="terminal-body">
        <template v-for="(item, index) in commands" :key="index">
          <div class="cmd-comment">{{ item.comment }}</div>
          <div class="cmd-command" @click="copyCommand(item.command)">
            {{ item.command }}
            <span class="copy-hint">📋 点击复制</span>
          </div>
        </template>
      </div>
    </div>
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

.terminal {
  max-width: 700px;
  margin: 0 auto;
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
}

.terminal-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.terminal-dot.red { background: #ff5f56; }
.terminal-dot.yellow { background: #ffbd2e; }
.terminal-dot.green { background: #27c93f; }

.terminal-body {
  padding: 1.5rem;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.9rem;
  line-height: 1.8;
  background: var(--bg);
}

.cmd-comment {
  color: var(--accent);
}

.cmd-command {
  color: var(--text);
  cursor: pointer;
  transition: opacity 0.2s;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cmd-command:hover {
  opacity: 0.8;
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
</style>
