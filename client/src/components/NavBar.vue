<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isDropdownOpen = ref(false)
const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const navItems = [
  { label: '首页', href: '#intro' },
  { label: '功能', href: '#features' },
  { label: '使用场景', href: '#usecases' },
  { label: '定价', href: '#pricing' },
  { label: '安装', href: '#install' },
]

const dropdownItems = [
  { label: '文档', href: '#' },
  { label: 'GitHub', href: 'https://github.com', target: '_blank' },
  { label: '关于团队', href: '#team' },
]
</script>

<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
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
              :target="item.target"
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
  background: rgba(10, 10, 15, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid transparent;
  transition: all 0.3s ease;
}

.navbar.scrolled {
  padding: 0.75rem 2rem;
  background: rgba(10, 10, 15, 0.9);
  border-bottom-color: var(--border);
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
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.nav-links {
  display: flex;
  gap: 0.25rem;
}

.nav-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: var(--radius);
  transition: all 0.2s ease;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0.25rem;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--gradient-primary);
  transition: all 0.3s ease;
  transform: translateX(-50%);
  border-radius: 1px;
}

.nav-link:hover {
  color: var(--text);
}

.nav-link:hover::after {
  width: calc(100% - 2rem);
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
  border-radius: var(--radius);
}

.dropbtn:hover {
  color: var(--text);
  background: var(--bg-subtle);
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
  animation: fadeIn 0.2s ease;
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
  transition: all 0.2s ease;
}

.dropdown-content a:hover {
  background: var(--bg-subtle);
  color: var(--primary);
  padding-left: 1.25rem;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }
}
</style>
