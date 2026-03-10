<script setup lang="ts">
import NavBar from './components/NavBar.vue'
import InstallSection from './components/InstallSection.vue'
import HeroSection from './components/HeroSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div class="app">
    <NavBar />
    <main>
      <InstallSection />
      <HeroSection />
      <FeaturesSection />
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
