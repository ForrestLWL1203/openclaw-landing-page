import { onMounted, onUnmounted, Ref } from 'vue'

/**
 * Composable for scroll reveal animations using IntersectionObserver
 */
export function useScrollReveal(sectionRef: Ref<HTMLElement | null>) {
  let observer: IntersectionObserver | null = null

  onMounted(() => {
    // Add visible class immediately for better UX
    if (sectionRef.value) {
      const elements = sectionRef.value.querySelectorAll('.reveal')
      elements.forEach((el) => el.classList.add('visible'))

      // Also observe for scroll-based reveals
      observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible')
            }
          })
        },
        { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
      )

      elements.forEach((el) => observer?.observe(el))
    }
  })

  onUnmounted(() => {
    observer?.disconnect()
  })
}
