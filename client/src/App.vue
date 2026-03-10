<script setup lang="ts">
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import UseCasesSection from './components/UseCasesSection.vue'
import PricingSection from './components/PricingSection.vue'
import TeamSection from './components/TeamSection.vue'
import InstallSection from './components/InstallSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div class="app">
    <NavBar />
    <main>
      <HeroSection />
      <FeaturesSection />
      <UseCasesSection />
      <PricingSection />
      <TeamSection />
      <InstallSection />
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
