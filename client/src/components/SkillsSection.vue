<script setup lang="ts">
const topSkills = [
  { name: 'openai-whisper', desc: 'AI 语音转文字，语音识别', url: 'https://clawhub.ai/openai-whisper', downloads: 3793 },
  { name: 'whatsapp-business', desc: 'WhatsApp 商业账号集成', url: 'https://clawhub.ai/whatsapp-business', downloads: 3655 },
  { name: 'telegram', desc: 'Telegram 即时通讯集成', url: 'https://clawhub.ai/telegram', downloads: 3622 },
  { name: 'openai-tts', desc: 'AI 文字转语音，语音合成', url: 'https://clawhub.ai/openai-tts', downloads: 3531 },
  { name: 'telegram-bot', desc: 'Telegram 机器人开发框架', url: 'https://clawhub.ai/telegram-bot', downloads: 3528 },
  { name: 'discord-voice', desc: 'Discord 语音频道集成', url: 'https://clawhub.ai/discord-voice', downloads: 3511 },
  { name: 'discord-chat', desc: 'Discord 聊天消息集成', url: 'https://clawhub.ai/discord-chat', downloads: 3469 },
  { name: 'whatsapp-styler', desc: 'WhatsApp 消息样式美化', url: 'https://clawhub.ai/whatsapp-styler', downloads: 3556 },
]
</script>

<template>
  <section class="skills-section" id="skills">
    <h2 class="section-title">
      <span class="gradient-text">🔥 热门 Skills TOP 8</span>
    </h2>
    <p class="section-desc">
      基于社区下载量排行，这些 Skills 正在被广泛使用
    </p>
    
    <div class="skills-grid">
      <a 
        v-for="skill in topSkills" 
        :key="skill.name"
        :href="skill.url"
        target="_blank"
        class="skill-card"
      >
        <div class="skill-rank">#{{ topSkills.indexOf(skill) + 1 }}</div>
        <div class="skill-content">
          <h3 class="skill-name">{{ skill.name }}</h3>
          <p class="skill-desc">{{ skill.desc }}</p>
          <div class="skill-meta">
            <span class="downloads">⬇ {{ skill.downloads }}</span>
            <span class="arrow">→</span>
          </div>
        </div>
      </a>
    </div>
  </section>
</template>

<style scoped>
.skills-section {
  padding: 6rem 2rem;
  background: var(--bg);
  position: relative;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.section-desc {
  text-align: center;
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto 3rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.skill-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  text-decoration: none;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.skill-card:hover {
  border-color: var(--primary);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px -8px rgba(99, 102, 241, 0.3);
}

.skill-rank {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
  opacity: 0.8;
}

.skill-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  margin: 0;
  word-break: break-all;
}

.skill-desc {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin: 0;
  line-height: 1.4;
  flex: 1;
}

.skill-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.downloads {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.arrow {
  color: var(--primary);
  opacity: 0;
  transform: translateX(-5px);
  transition: all 0.3s ease;
}

.skill-card:hover .arrow {
  opacity: 1;
  transform: translateX(0);
}

@media (max-width: 900px) {
  .skills-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .skills-grid {
    grid-template-columns: 1fr;
  }
}
</style>
