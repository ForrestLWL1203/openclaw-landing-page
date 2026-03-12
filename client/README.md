# OpenClaw Client

OpenClaw 落地页前端项目，基于 Vue 3 + TypeScript + Vite 构建的营销展示网站。

## 项目介绍

OpenClaw 是一个开源的 AI Agent 平台，旨在帮助用户快速搭建属于自己的智能 AI 助手。通过 OpenClaw，你可以：

- 连接 Claude、GPT 等主流大语言模型
- 通过 WhatsApp、Telegram、Discord、微信等渠道与 AI 交互
- 使用丰富的插件（Skill）扩展 AI 能力
- 本地部署，确保数据隐私安全

## 技术栈

- **Vue 3** - 渐进式前端框架
- **TypeScript** - 类型安全的 JavaScript 超集
- **Vite** - 下一代前端构建工具
- **Vue Router** - 官方路由管理器
- **@vueuse/motion** - 动画库

## 功能特性

### 页面模块

| 模块 | 描述 |
|------|------|
| HeroSection | 首屏展示，实时显示 Agent 在线状态 |
| InstallSection | 安装指南，5 步快速上手 |
| FeaturesSection | 核心功能展示 |
| DetailsSection | 详细特性介绍 |

### 交互功能

- 实时 Agent 状态轮询（每 3 秒）
- 滚动揭示动画
- 卡片展开/收起交互
- 命令行一键复制
- 响应式布局设计

## 快速开始

### 环境要求

- Node.js >= 18（推荐 Node.js 22）
- npm >= 9 或 yarn >= 1

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

启动后访问 http://localhost:5173

### 构建生产版本

```bash
npm run build
```

### 预览生产版本

```bash
npm run preview
```

## 项目结构

```
client/
├── src/
│   ├── assets/
│   │   └── main.css          # 全局样式
│   ├── components/
│   │   ├── NavBar.vue        # 导航栏
│   │   ├── HeroSection.vue   # 首屏区域
│   │   ├── InstallSection.vue # 安装指南
│   │   ├── FeaturesSection.vue # 核心功能
│   │   ├── DetailsSection.vue  # 详细特性
│   │   └── FooterSection.vue   # 页脚
│   ├── composables/
│   │   └── useScrollReveal.ts # 滚动揭示 Hook
│   ├── App.vue               # 根组件
│   └── main.ts               # 入口文件
├── index.html                # HTML 模板
├── vite.config.ts            # Vite 配置
├── tsconfig.json             # TypeScript 配置
└── package.json              # 项目依赖
```

## 配置说明

### Agent 状态轮询

在 `HeroSection.vue` 中，Agent 状态通过 HTTP 请求获取：

```typescript
const fetchAgents = async () => {
  const res = await fetch('http://localhost:19000/agents')
  const data = await res.json()
  agents.value = data.filter((a: Agent) => a.name === '贾维斯' || a.name === '马斯克')
}
```

如需修改 API 端点或过滤条件，请编辑此文件。

### 主题样式

全局 CSS 变量定义在 `src/assets/main.css` 中：

```css
:root {
  --primary: #2563EB;
  --accent: #F97316;
  --bg: #f8fafc;
  --text: #1e293b;
}
```

## 许可证

MIT License
