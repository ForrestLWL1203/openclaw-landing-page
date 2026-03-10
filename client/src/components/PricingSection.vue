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
  
  document.querySelectorAll('.pricing-section .reveal').forEach((el) => {
    observer.observe(el)
  })
})

interface Plan {
  name: string
  price: string
  period: string
  description: string
  features: string[]
  cta: string
  popular?: boolean
}

const plans: Plan[] = [
  {
    name: '免费版',
    price: '¥0',
    period: '永久免费',
    description: '适合个人开发者体验',
    features: [
      '✅ 基础 AI 功能',
      '✅ 1 个平台连接',
      '✅ 100 条/天 消息',
      '✅ 社区支持',
      '❌ 无高级插件'
    ],
    cta: '免费开始'
  },
  {
    name: '专业版',
    price: '¥49',
    period: '/月',
    description: '适合个人用户和小型团队',
    features: [
      '✅ 全部 AI 功能',
      '✅ 无限平台连接',
      '✅ 无限消息',
      '✅ 高级插件',
      '✅ 优先支持',
      '✅ 本地部署'
    ],
    cta: '立即升级',
    popular: true
  },
  {
    name: '企业版',
    price: '定制',
    period: '',
    description: '适合大型组织',
    features: [
      '✅ 专业版全部功能',
      '✅ 专属客服',
      '✅ 定制开发',
      '✅ SLA 保障',
      '✅ 私有化部署',
      '✅ 培训服务'
    ],
    cta: '联系销售'
  }
]
</script>

<template>
  <section class="pricing-section" id="pricing">
    <h2 class="section-title reveal">
      <span class="gradient-text">定价方案</span>
    </h2>
    <p class="section-desc reveal reveal-delay-1">
      选择最适合你的方案
    </p>
    <div class="pricing-grid">
      <div 
        v-for="(plan, index) in plans" 
        :key="plan.name"
        class="pricing-card reveal"
        :class="{ popular: plan.popular, 'reveal-delay-1': index === 0, 'reveal-delay-2': index === 1, 'reveal-delay-3': index === 2 }"
      >
        <div v-if="plan.popular" class="popular-badge">最受欢迎</div>
        <h3 class="plan-name">{{ plan.name }}</h3>
        <div class="plan-price">
          <span class="price gradient-text">{{ plan.price }}</span>
          <span class="period">{{ plan.period }}</span>
        </div>
        <p class="plan-desc">{{ plan.description }}</p>
        <ul class="plan-features">
          <li v-for="feature in plan.features" :key="feature">
            {{ feature }}
          </li>
        </ul>
        <a href="#install" class="plan-cta" :class="{ primary: plan.popular }">
          {{ plan.cta }}
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.pricing-section {
  padding: 6rem 2rem;
  background: var(--bg-subtle);
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

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1100px;
  margin: 0 auto;
  align-items: center;
}

.pricing-card {
  padding: 2.5rem 2rem;
  border-radius: var(--radius);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.pricing-card.popular {
  border-color: var(--primary);
  transform: scale(1.05);
  box-shadow: 0 20px 60px -15px rgba(99, 102, 241, 0.3);
}

.pricing-card:hover {
  transform: translateY(-8px);
}

.pricing-card.popular:hover {
  transform: scale(1.05) translateY(-8px);
}

.popular-badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--gradient-primary);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.35rem 1rem;
  border-radius: 1rem;
  white-space: nowrap;
}

.plan-name {
  font-size: 1.35rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-align: center;
}

.plan-price {
  text-align: center;
  margin-bottom: 1rem;
}

.price {
  font-size: 3rem;
  font-weight: 700;
}

.period {
  font-size: 1rem;
  color: var(--text-muted);
}

.plan-desc {
  text-align: center;
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 2rem;
}

.plan-features {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
}

.plan-features li {
  font-size: 0.9rem;
  padding: 0.6rem 0;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
}

.plan-features li:last-child {
  border-bottom: none;
}

.plan-cta {
  display: block;
  text-align: center;
  padding: 0.875rem 2rem;
  border-radius: var(--radius);
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  background: var(--bg-subtle);
  color: var(--text);
  border: 1px solid var(--border);
}

.plan-cta:hover {
  background: var(--bg-elevated);
  border-color: var(--primary);
}

.plan-cta.primary {
  background: var(--gradient-primary);
  color: white;
  border: none;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
}

.plan-cta.primary:hover {
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.5);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .pricing-card.popular {
    transform: none;
  }
  
  .pricing-card.popular:hover {
    transform: translateY(-8px);
  }
}
</style>
