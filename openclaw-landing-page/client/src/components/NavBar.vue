<script setup lang="ts">
import { ref } from 'vue'

const isDropdownOpen = ref(false)

const navItems = [
  { label: '首页', href: '#intro' },
  { label: '安装', href: '#install' },
  { label: '功能', href: '#features' },
]

const dropdownItems = [
  { label: '功能特性', href: '#features' },
  { label: '文档', href: '#' },
  { label: '关于我们', href: '#' },
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
        
        <div 
          class="dropdown"
          @mouseenter="isDropdownOpen = true"
          @mouseleave="isDropdownOpen = false"
        >
          <button class="dropbtn">
            更多 ▾
          </button>
          <div class="dropdown-content" :class="{ open: isDropdownOpen }">
            <a 
              v-for="item in dropdownItems" 
              :key="item.label"
              :href="item.href"
            >
              {{ item.label }}
            </a>
          </div>
        </div>
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
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
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
  color: var(--primary);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
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
  padding: 0.5rem 1rem;
  transition: color 0.2s;
}

.nav-link:hover {
  color: var(--text);
}

.dropdown {
  position: relative;
}

.dropbtn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: color 0.2s;
  font-family: var(--font-sans);
}

.dropbtn:hover {
  color: var(--text);
}

.dropdown-content {
  display: none;
  position: absolute;
  right: 0;
  min-width: 160px;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  z-index: 200;
  overflow: hidden;
}

.dropdown-content.open {
  display: block;
}

.dropdown-content a {
  display: block;
  padding: 0.75rem 1rem;
  color: var(--text);
  text-decoration: none;
  font-size: 0.875rem;
  transition: background 0.2s, color 0.2s;
}

.dropdown-content a:hover {
  background: var(--bg-subtle);
  color: var(--primary);
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
}
</style>
