<script setup lang="ts">
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import InstallSection from './components/InstallSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import UseCasesSection from './components/UseCasesSection.vue'
</script>

<template>
  <div class="app">
    <NavBar />
    <main>
      <HeroSection />
      <InstallSection />
      <FeaturesSection />
      <UseCasesSection />
    </main>
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
