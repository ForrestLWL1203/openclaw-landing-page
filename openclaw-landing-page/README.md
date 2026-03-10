# OpenClaw Landing Page

现代化的 Vue 3 Landing Page

## 技术栈

- **前端**: Vue 3 + Vite + TypeScript
- **样式**: CSS Variables + Scoped CSS

## 项目结构

```
openclaw-landing-page/
├── client/                 # Vue 3 前端
│   ├── src/
│   │   ├── components/     # Vue 组件
│   │   ├── assets/         # 静态资源
│   ├── index.html
│   ├── vite.config.ts
│   └── package.json
└── README.md
```

## 开发

```bash
# 安装依赖
cd client && npm install

# 启动开发服务器
cd client && npm run dev
```

## 构建部署

```bash
# 构建前端
cd client && npm run build
```

部署到 GitHub Pages：push 到 main 分支自动触发 GitHub Actions 部署。
