<script setup lang="ts">
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <svg class="footer-logo" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="16" cy="16" r="14" fill="#2563EB"/>
        <path d="M10 12C10 12 14 8 16 8C18 8 22 12 22 12" stroke="white" stroke-width="2" stroke-linecap="round"/>
        <circle cx="12" cy="14" r="2" fill="white"/>
        <circle cx="20" cy="14" r="2" fill="white"/>
        <path d="M13 20C13 20 14 22 16 22C18 22 19 20 19 20" stroke="white" stroke-width="2" stroke-linecap="round"/>
      </svg>
      <p>OpenClaw - 你的AI助手</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 3rem 2rem;
  text-align: center;
  background: var(--bg-subtle);
  border-top: 1px solid var(--border);
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.footer-logo {
  width: 28px;
  height: 28px;
}

.footer p {
  color: var(--text-muted);
  font-size: 1rem;
  font-weight: 500;
}
</style>
