# OpenClaw Landing Page

现代化的 Vue 3 + Node.js Landing Page

## 技术栈

- **前端**: Vue 3 + Vite + TypeScript
- **后端**: Node.js + Express
- **样式**: CSS Variables + Scoped CSS

## 项目结构

```
openclaw-landing-page/
├── client/                 # Vue 3 前端
│   ├── src/
│   │   ├── components/     # Vue 组件
│   │   ├── views/         # 页面视图
│   │   ├── composables/   # Vue Composables
│   │   ├── assets/        # 静态资源
│   │   └── router/        # 路由配置
│   ├── index.html
│   ├── vite.config.ts
│   └── package.json
├── server/                 # Node.js 后端
│   ├── src/
│   │   ├── routes/        # API 路由
│   │   ├── controllers/  # 控制器
│   │   ├── services/      # 业务逻辑
│   │   └── index.js
│   └── package.json
└── README.md
```

## 开发

```bash
# 安装依赖
cd client && npm install
cd ../server && npm install

# 启动开发服务器
# 终端1: 启动前端
cd client && npm run dev

# 终端2: 启动后端
cd server && npm run dev
```

## 生产构建

```bash
# 构建前端
cd client && npm run build

# 启动生产服务器
cd server && npm start
```
