<script setup lang="ts">
const navItems = [
  { label: '快速开始', href: '#install' },
  { label: '功能', href: '#features' },
]
</script>

<template>
  <nav class="navbar">
    <div class="nav-container">
      <a href="#" class="logo">
        <svg class="logo-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="16" cy="16" r="14" fill="#2563EB"/>
          <path d="M10 12C10 12 14 8 16 8C18 8 22 12 22 12" stroke="white" stroke-width="2" stroke-linecap="round"/>
          <circle cx="12" cy="14" r="2" fill="white"/>
          <circle cx="20" cy="14" r="2" fill="white"/>
          <path d="M13 20C13 20 14 22 16 22C18 22 19 20 19 20" stroke="white" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <span>OpenClaw</span>
      </a>
      
      <div class="nav-links">
        <a 
          v-for="item in navItems" 
          :key="item.label"
          :href="item.href" 
          class="nav-link"
        >
          {{ item.label }}
        </a>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1rem 2rem;
  background: rgba(248, 250, 252, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  animation: slideDown 0.5s ease-out;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.logo:hover {
  color: var(--primary);
  transform: scale(1.05);
}

.logo-icon {
  width: 32px;
  height: 32px;
  transition: transform 0.3s ease;
}

.logo:hover .logo-icon {
  transform: rotate(-10deg) scale(1.1);
}

.nav-links {
  display: flex;
  gap: 0.5rem;
}

.nav-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 1.25rem;
  border-radius: 2rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-link::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-link:hover {
  color: var(--text);
  background: rgba(37, 99, 235, 0.08);
}

.nav-link:hover::before {
  width: 60%;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
}
</style>
