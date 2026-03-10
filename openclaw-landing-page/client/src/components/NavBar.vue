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
        🦞 OpenClaw
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
  background: rgba(10, 10, 15, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  animation: slideDown 0.5s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-100%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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
  background: rgba(99, 102, 241, 0.1);
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
