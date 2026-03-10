<script setup lang="ts">
const currentYear = new Date().getFullYear()

const footerLinks = [
  { label: 'GitHub', href: 'https://github.com', icon: '🐙' },
  { label: '文档', href: '#', icon: '📖' },
  { label: 'Discord', href: '#', icon: '💬' },
  { label: 'Twitter', href: '#', icon: '🐦' },
]
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-brand">
        <span class="footer-logo">🦞 OpenClaw</span>
        <p class="footer-desc">你的智能 AI 助手</p>
      </div>
      <div class="footer-links">
        <a 
          v-for="link in footerLinks" 
          :key="link.label"
          :href="link.href"
          target="_blank"
          class="footer-link"
        >
          <span>{{ link.icon }}</span>
          <span>{{ link.label }}</span>
        </a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© {{ currentYear }} OpenClaw. All rights reserved.</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 4rem 2rem 2rem;
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid var(--border);
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-logo {
  font-size: 1.5rem;
  font-weight: 700;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-desc {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.footer-links {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.footer-link {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: var(--primary);
}

.footer-bottom {
  max-width: 1200px;
  margin: 0 auto;
  padding-top: 2rem;
  text-align: center;
}

.footer-bottom p {
  color: var(--text-muted);
  font-size: 0.8rem;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
  }
  
  .footer-links {
    justify-content: center;
  }
}
</style>
