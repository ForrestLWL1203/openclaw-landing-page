<script setup lang="ts">
import { onMounted } from 'vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import InstallSection from './components/InstallSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import DetailsSection from './components/DetailsSection.vue'
import FooterSection from './components/FooterSection.vue'

onMounted(() => {
  // Initialize scroll reveal observer
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
        }
      })
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    }
  )

  // Observe all reveal elements
  document.querySelectorAll('.reveal').forEach((el) => {
    observer.observe(el)
  })
})
</script>

<template>
  <div class="app">
    <NavBar />
    <main>
      <HeroSection />
      <InstallSection />
      <FeaturesSection />
      <DetailsSection />
    </main>
    <FooterSection />
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>
