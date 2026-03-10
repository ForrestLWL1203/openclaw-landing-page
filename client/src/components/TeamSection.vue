<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
        }
      })
    },
    { threshold: 0.1 }
  )
  
  document.querySelectorAll('.team-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

interface TeamMember {
  name: string
  role: string
  avatar: string
  desc: string
}

const team: TeamMember[] = [
  {
    name: '马斯克',
    role: '创始人 & CEO',
    avatar: '🦞',
    desc: 'AI 爱好者，热爱开源'
  },
  {
    name: '贾维斯',
    role: '首席工程师',
    avatar: '🤖',
    desc: '全栈开发专家'
  },
  {
    name: '星期五',
    role: '产品经理',
    avatar: '💡',
    desc: '专注用户体验'
  }
]
</script>

<template>
  <section class="team-section" id="team">
    <h2 class="section-title reveal">
      <span class="gradient-text">团队成员</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      热爱技术，专注创造
    </p>
    <div class="team-grid">
      <div 
        v-for="(member, index) in team" 
        :key="member.name"
        class="team-card reveal"
        :class="`reveal-delay-${(index % 3) + 1}`"
      >
        <div class="team-avatar">{{ member.avatar }}</div>
        <h3 class="team-name">{{ member.name }}</h3>
        <p class="team-role">{{ member.role }}</p>
        <p class="team-desc">{{ member.desc }}</p>
      </div>
    </div>
    <div class="join-us reveal">
      <p>加入我们一起创造未来？</p>
      <a href="https://github.com" target="_blank" class="github-link">
        <span>GitHub</span>
        <span class="arrow">→</span>
      </a>
    </div>
  </section>
</template>

<style scoped>
.team-section {
  padding: 6rem 2rem;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.section-desc {
  text-align: center;
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 4rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 900px;
  margin: 0 auto 4rem;
}

.team-card {
  text-align: center;
  padding: 2rem;
  border-radius: var(--radius);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  transition: all 0.4s ease;
}

.team-card:hover {
  transform: translateY(-8px);
  border-color: var(--primary);
  box-shadow: 0 20px 60px -15px rgba(99, 102, 241, 0.2);
}

.team-avatar {
  font-size: 4rem;
  margin-bottom: 1rem;
  transition: transform 0.3s ease;
}

.team-card:hover .team-avatar {
  transform: scale(1.1);
}

.team-name {
  font-size: 1.35rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.team-role {
  font-size: 0.9rem;
  color: var(--primary);
  margin-bottom: 0.75rem;
}

.team-desc {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.join-us {
  text-align: center;
  padding: 3rem;
  background: var(--bg-elevated);
  border-radius: var(--radius);
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid var(--border);
}

.join-us p {
  font-size: 1.25rem;
  color: var(--text);
  margin-bottom: 1.5rem;
}

.github-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  color: var(--text);
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.github-link:hover {
  background: var(--bg);
  border-color: var(--primary);
  gap: 1rem;
}

.github-link .arrow {
  transition: transform 0.3s ease;
}

.github-link:hover .arrow {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: 1fr;
  }
}
</style>
