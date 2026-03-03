# OpenClaw 学习笔记

---

## index

---
read_when:
  - 向新用户介绍 OpenClaw
summary: OpenClaw 是一个多渠道 AI 智能体 Gateway 网关，可在任何操作系统上运行。
title: OpenClaw
x-i18n:
  generated_at: "2026-02-04T17:53:40Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: fc8babf7885ef91d526795051376d928599c4cf8aff75400138a0d7d9fa3b75f
  source_path: index.md
  workflow: 15
---

# OpenClaw 🦞

<p align="center">
    <img
        src="/assets/openclaw-logo-text-dark.png"
        alt="OpenClaw"
        width="500"
        class="dark:hidden"
    />
    <img
        src="/assets/openclaw-logo-text.png"
        alt="OpenClaw"
        width="500"
        class="hidden dark:block"
    />
</p>

> _"去壳！去壳！"_ — 大概是一只太空龙虾说的

<p align="center">
  <strong>适用于任何操作系统的 AI 智能体 Gateway 网关，支持 WhatsApp、Telegram、Discord、iMessage 等。</strong><br />
  发送消息，随时随地获取智能体响应。通过插件可添加 Mattermost 等更多渠道。
</p>

<Columns>
  <Card title="入门指南" href="/start/getting-started" icon="rocket">
    安装 OpenClaw 并在几分钟内启动 Gateway 网关。
  </Card>
  <Card title="运行向导" href="/start/wizard" icon="sparkles">
    通过 `openclaw onboard` 和配对流程进行引导式设置。
  </Card>
  <Card title="打开控制界面" href="/web/control-ui" icon="layout-dashboard">
    启动浏览器仪表板，管理聊天、配置和会话。
  </Card>
</Columns>

OpenClaw 通过单个 Gateway 网关进程将聊天应用连接到 Pi 等编程智能体。它为 OpenClaw 助手提供支持，并支持本地或远程部署。

## 工作原理

```mermaid
flowchart LR
  A["Chat apps + plugins"] --> B["Gateway"]
  B --> C["Pi agent"]
  B --> D["CLI"]
  B --> E["Web Control UI"]
  B --> F["macOS app"]
  B --> G["iOS and Android nodes"]
```

Gateway 网关是会话、路由和渠道连接的唯一事实来源。

## 核心功能

<Columns>
  <Card title="多渠道 Gateway 网关" icon="network">
    通过单个 Gateway 网关进程连接 WhatsApp、Telegram、Discord 和 iMessage。
  </Card>
  <Card title="插件渠道" icon="plug">
    通过扩展包添加 Mattermost 等更多渠道。
  </Card>
  <Card title="多智能体路由" icon="route">
    按智能体、工作区或发送者隔离会话。
  </Card>
  <Card title="媒体支持" icon="image">
    发送和接收图片、音频和文档。
  </Card>
  <Card title="Web 控制界面" icon="monitor">
    浏览器仪表板，用于聊天、配置、会话和节点管理。
  </Card>
  <Card title="移动节点" icon="smartphone">
    配对 iOS 和 Android 节点，支持 Canvas。
  </Card>
</Columns>

## 快速开始

<Steps>
  <Step title="安装 OpenClaw">
    ```bash
    npm install -g openclaw@latest
    ```
  </Step>
  <Step title="新手引导并安装服务">
    ```bash
    openclaw onboard --install-daemon
    ```
  </Step>
  <Step title="配对 WhatsApp 并启动 Gateway 网关">
    ```bash
    openclaw channels login
    openclaw gateway --port 18789
    ```
  </Step>
</Steps>

需要完整的安装和开发环境设置？请参阅[快速开始](/start/quickstart)。

## 仪表板

Gateway 网关启动后，打开浏览器控制界面。

- 本地默认地址：http://127.0.0.1:18789/
- 远程访问：[Web 界面](/web)和 [Tailscale](/gateway/tailscale)

<p align="center">
  <img src="whatsapp-openclaw.jpg" alt="OpenClaw" width="420" />
</p>

## 配置（可选）

配置文件位于 `~/.openclaw/openclaw.json`。

- 如果你**不做任何修改**，OpenClaw 将使用内置的 Pi 二进制文件以 RPC 模式运行，并按发送者创建独立会话。
- 如果你想要限制访问，可以从 `channels.whatsapp.allowFrom` 和（针对群组的）提及规则开始配置。

示例：

```json5
{
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } },
    },
  },
  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },
}
```

## 从这里开始

<Columns>
  <Card title="文档中心" href="/start/hubs" icon="book-open">
    所有文档和指南，按用例分类。
  </Card>
  <Card title="配置" href="/gateway/configuration" icon="settings">
    核心 Gateway 网关设置、令牌和提供商配置。
  </Card>
  <Card title="远程访问" href="/gateway/remote" icon="globe">
    SSH 和 tailnet 访问模式。
  </Card>
  <Card title="渠道" href="/channels/telegram" icon="message-square">
    WhatsApp、Telegram、Discord 等渠道的具体设置。
  </Card>
  <Card title="节点" href="/nodes" icon="smartphone">
    iOS 和 Android 节点的配对与 Canvas 功能。
  </Card>
  <Card title="帮助" href="/help" icon="life-buoy">
    常见修复方法和故障排除入口。
  </Card>
</Columns>

## 了解更多

<Columns>
  <Card title="完整功能列表" href="/concepts/features" icon="list">
    全部渠道、路由和媒体功能。
  </Card>
  <Card title="多智能体路由" href="/concepts/multi-agent" icon="route">
    工作区隔离和按智能体的会话管理。
  </Card>
  <Card title="安全" href="/gateway/security" icon="shield">
    令牌、白名单和安全控制。
  </Card>
  <Card title="故障排除" href="/gateway/troubleshooting" icon="wrench">
    Gateway 网关诊断和常见错误。
  </Card>
  <Card title="关于与致谢" href="/reference/credits" icon="info">
    项目起源、贡献者和许可证。
  </Card>
</Columns>


---

## getting-started

---
read_when:
  - 从零开始首次设置
  - 你想要从安装 → 新手引导 → 第一条消息的最快路径
summary: 新手指南：从零到第一条消息（向导、认证、渠道、配对）
title: 入门指南
x-i18n:
  generated_at: "2026-02-03T07:54:14Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 78cfa02eb2e4ea1a83e18edd99d142dbae707ec063e8d74c9a54f94581aa067f
  source_path: start/getting-started.md
  workflow: 15
---

# 入门指南

目标：尽快从**零**到**第一个可用聊天**（使用合理的默认值）。

最快聊天：打开 Control UI（无需渠道设置）。运行 `openclaw dashboard` 并在浏览器中聊天，或在 Gateway 网关主机上打开 `http://127.0.0.1:18789/`。文档：[Dashboard](/web/dashboard) 和 [Control UI](/web/control-ui)。

推荐路径：使用 **CLI 新手引导向导**（`openclaw onboard`）。它设置：

- 模型/认证（推荐 OAuth）
- Gateway 网关设置
- 渠道（WhatsApp/Telegram/Discord/Mattermost（插件）/...）
- 配对默认值（安全私信）
- 工作区引导 + Skills
- 可选的后台服务

如果你想要更深入的参考页面，跳转到：[向导](/start/wizard)、[设置](/start/setup)、[配对](/channels/pairing)、[安全](/gateway/security)。

沙箱注意事项：`agents.defaults.sandbox.mode: "non-main"` 使用 `session.mainKey`（默认 `"main"`），因此群组/渠道会话会被沙箱隔离。如果你想要主智能体始终在主机上运行，设置显式的每智能体覆盖：

```json
{
  "routing": {
    "agents": {
      "main": {
        "workspace": "~/.openclaw/workspace",
        "sandbox": { "mode": "off" }
      }
    }
  }
}
```

## 0) 前置条件

- Node `>=22`
- `pnpm`（可选；如果从源代码构建则推荐）
- **推荐：**Brave Search API 密钥用于网页搜索。最简单的方式：`openclaw configure --section web`（存储 `tools.web.search.apiKey`）。参见 [Web 工具](/tools/web)。

macOS：如果你计划构建应用，安装 Xcode / CLT。仅用于 CLI + Gateway 网关的话，Node 就足够了。
Windows：使用 **WSL2**（推荐 Ubuntu）。强烈推荐 WSL2；原生 Windows 未经测试，问题更多，工具兼容性更差。先安装 WSL2，然后在 WSL 内运行 Linux 步骤。参见 [Windows (WSL2)](/platforms/windows)。

## 1) 安装 CLI（推荐）

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

安装程序选项（安装方法、非交互式、从 GitHub）：[安装](/install)。

Windows (PowerShell)：

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

替代方案（全局安装）：

```bash
npm install -g openclaw@latest
```

```bash
pnpm add -g openclaw@latest
```

## 2) 运行新手引导向导（并安装服务）

```bash
openclaw onboard --install-daemon
```

你将选择：

- **本地 vs 远程** Gateway 网关
- **认证**：OpenAI Code (Codex) 订阅（OAuth）或 API 密钥。对于 Anthropic 我们推荐 API 密钥；也支持 `claude setup-token`。
- **提供商**：WhatsApp QR 登录、Telegram/Discord 机器人令牌、Mattermost 插件令牌等。
- **守护进程**：后台安装（launchd/systemd；WSL2 使用 systemd）
  - **运行时**：Node（推荐；WhatsApp/Telegram 必需）。**不推荐** Bun。
- **Gateway 网关令牌**：向导默认生成一个（即使在 loopback 上）并存储在 `gateway.auth.token`。

向导文档：[向导](/start/wizard)

### 凭证：存储位置（重要）

- **推荐的 Anthropic 路径：**设置 API 密钥（向导可以为服务使用存储它）。如果你想复用 Claude Code 凭证，也支持 `claude setup-token`。

- OAuth 凭证（旧版导入）：`~/.openclaw/credentials/oauth.json`
- 认证配置文件（OAuth + API 密钥）：`~/.openclaw/agents/<agentId>/agent/auth-profiles.json`

无头/服务器提示：先在普通机器上完成 OAuth，然后将 `oauth.json` 复制到 Gateway 网关主机。

## 3) 启动 Gateway 网关

如果你在新手引导期间安装了服务，Gateway 网关应该已经在运行：

```bash
openclaw gateway status
```

手动运行（前台）：

```bash
openclaw gateway --port 18789 --verbose
```

Dashboard（local loopback）：`http://127.0.0.1:18789/`
如果配置了令牌，将其粘贴到 Control UI 设置中（存储为 `connect.params.auth.token`）。

⚠️ **Bun 警告（WhatsApp + Telegram）：**Bun 与这些渠道存在已知问题。如果你使用 WhatsApp 或 Telegram，请使用 **Node** 运行 Gateway 网关。

## 3.5) 快速验证（2 分钟）

```bash
openclaw status
openclaw health
openclaw security audit --deep
```

## 4) 配对 + 连接你的第一个聊天界面

### WhatsApp（QR 登录）

```bash
openclaw channels login
```

通过 WhatsApp → 设置 → 链接设备扫描。

WhatsApp 文档：[WhatsApp](/channels/whatsapp)

### Telegram / Discord / 其他

向导可以为你写入令牌/配置。如果你更喜欢手动配置，从这里开始：

- Telegram：[Telegram](/channels/telegram)
- Discord：[Discord](/channels/discord)
- Mattermost（插件）：[Mattermost](/channels/mattermost)

**Telegram 私信提示：**你的第一条私信会返回配对码。批准它（见下一步），否则机器人不会响应。

## 5) 私信安全（配对审批）

默认姿态：未知私信会获得一个短代码，消息在批准之前不会被处理。如果你的第一条私信没有收到回复，批准配对：

```bash
openclaw pairing list whatsapp
openclaw pairing approve whatsapp <code>
```

配对文档：[配对](/channels/pairing)

## 从源代码（开发）

如果你正在开发 OpenClaw 本身，从源代码运行：

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build # 首次运行时自动安装 UI 依赖
pnpm build
openclaw onboard --install-daemon
```

如果你还没有全局安装，从仓库通过 `pnpm openclaw ...` 运行新手引导步骤。`pnpm build` 也会打包 A2UI 资源；如果你只需要运行那个步骤，使用 `pnpm canvas:a2ui:bundle`。

Gateway 网关（从此仓库）：

```bash
node openclaw.mjs gateway --port 18789 --verbose
```

## 7) 验证端到端

在新终端中，发送测试消息：

```bash
openclaw message send --target +15555550123 --message "Hello from OpenClaw"
```

如果 `openclaw health` 显示"未配置认证"，回到向导设置 OAuth/密钥认证——没有它智能体将无法响应。

提示：`openclaw status --all` 是最佳的可粘贴、只读调试报告。
健康探测：`openclaw health`（或 `openclaw status --deep`）向运行中的 Gateway 网关请求健康快照。

## 下一步（可选，但很棒）

- macOS 菜单栏应用 + 语音唤醒：[macOS 应用](/platforms/macos)
- iOS/Android 节点（Canvas/相机/语音）：[节点](/nodes)
- 远程访问（SSH 隧道 / Tailscale Serve）：[远程访问](/gateway/remote) 和 [Tailscale](/gateway/tailscale)
- 常开 / VPN 设置：[远程访问](/gateway/remote)、[exe.dev](/install/exe-dev)、[Hetzner](/install/hetzner)、[macOS 远程](/platforms/mac/remote)


---

## quickstart

---
read_when:
  - 你希望以最快的方式从安装到运行一个可用的 Gateway 网关
summary: 安装 OpenClaw，完成 Gateway 网关新手引导，并配对你的第一个渠道。
title: 快速开始
x-i18n:
  generated_at: "2026-02-04T17:53:21Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 3c5da65996f89913cd115279ae21dcab794eadd14595951b676d8f7864fbbe2d
  source_path: start/quickstart.md
  workflow: 15
---

<Note>
OpenClaw 需要 Node 22 或更新版本。
</Note>

## 安装

<Tabs>
  <Tab title="npm">
    ```bash
    npm install -g openclaw@latest
    ```
  </Tab>
  <Tab title="pnpm">
    ```bash
    pnpm add -g openclaw@latest
    ```
  </Tab>
</Tabs>

## 新手引导并运行 Gateway 网关

<Steps>
  <Step title="新手引导并安装服务">
    ```bash
    openclaw onboard --install-daemon
    ```
  </Step>
  <Step title="配对 WhatsApp">
    ```bash
    openclaw channels login
    ```
  </Step>
  <Step title="启动 Gateway 网关">
    ```bash
    openclaw gateway --port 18789
    ```
  </Step>
</Steps>

完成新手引导后，Gateway 网关将通过用户服务运行。你也可以使用 `openclaw gateway` 手动启动。

<Info>
之后在 npm 安装和 git 安装之间切换非常简单。安装另一种方式后，运行
`openclaw doctor` 即可更新 Gateway 网关服务入口点。
</Info>

## 从源码安装（开发）

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build # 首次运行时会自动安装 UI 依赖
pnpm build
openclaw onboard --install-daemon
```

如果你还没有全局安装，可以在仓库目录中通过 `pnpm openclaw ...` 运行新手引导。

## 多实例快速开始（可选）

```bash
OPENCLAW_CONFIG_PATH=~/.openclaw/a.json \
OPENCLAW_STATE_DIR=~/.openclaw-a \
openclaw gateway --port 19001
```

## 发送测试消息

需要一个正在运行的 Gateway 网关。

```bash
openclaw message send --target +15555550123 --message "Hello from OpenClaw"
```


---

## features

---
read_when:
  - 你想了解 OpenClaw 支持的完整功能列表
summary: OpenClaw 在渠道、路由、媒体和用户体验方面的功能。
title: 功能
x-i18n:
  generated_at: "2026-02-04T17:53:22Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 1b6aee0bfda751824cb6b3a99080b4c80c00ffb355a96f9cff1b596d55d15ed4
  source_path: concepts/features.md
  workflow: 15
---

## 亮点

<Columns>
  <Card title="渠道" icon="message-square">
    通过单个 Gateway 网关支持 WhatsApp、Telegram、Discord 和 iMessage。
  </Card>
  <Card title="插件" icon="plug">
    通过扩展添加 Mattermost 等更多平台。
  </Card>
  <Card title="路由" icon="route">
    多智能体路由，支持隔离会话。
  </Card>
  <Card title="媒体" icon="image">
    支持图片、音频和文档的收发。
  </Card>
  <Card title="应用与界面" icon="monitor">
    Web 控制界面和 macOS 配套应用。
  </Card>
  <Card title="移动节点" icon="smartphone">
    iOS 和 Android 节点，支持 Canvas。
  </Card>
</Columns>

## 完整列表

- 通过 WhatsApp Web（Baileys）集成 WhatsApp
- Telegram 机器人支持（grammY）
- Discord 机器人支持（channels.discord.js）
- Mattermost 机器人支持（插件）
- 通过本地 imsg CLI 集成 iMessage（macOS）
- Pi 的智能体桥接，支持 RPC 模式和工具流式传输
- 长响应的流式传输和分块处理
- 多智能体路由，按工作区或发送者隔离会话
- 通过 OAuth 进行 Anthropic 和 OpenAI 的订阅认证
- 会话：私信合并为共享的 `main`；群组相互隔离
- 群聊支持，通过提及激活
- 图片、音频和文档的媒体支持
- 可选的语音消息转录钩子
- WebChat 和 macOS 菜单栏应用
- iOS 节点，支持配对和 Canvas 界面
- Android 节点，支持配对、Canvas、聊天和相机

<Note>
旧版 Claude、Codex、Gemini 和 Opencode 路径已被移除。Pi 是唯一的编程智能体路径。
</Note>


---

## architecture

---
read_when:
  - 正在开发 Gateway 网关协议、客户端或传输层
summary: WebSocket Gateway 网关架构、组件和客户端流程
title: Gateway 网关架构
x-i18n:
  generated_at: "2026-02-03T07:45:55Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: c636d5d8a5e628067432b30671466309e3d630b106d413f1708765bf2a9399a1
  source_path: concepts/architecture.md
  workflow: 15
---

# Gateway 网关架构

最后更新：2026-01-22

## 概述

- 单个长期运行的 **Gateway 网关**拥有所有消息平台（通过 Baileys 的 WhatsApp、通过 grammY 的 Telegram、Slack、Discord、Signal、iMessage、WebChat）。
- 控制平面客户端（macOS 应用、CLI、Web 界面、自动化）通过配置的绑定主机（默认 `127.0.0.1:18789`）上的 **WebSocket** 连接到 Gateway 网关。
- **节点**（macOS/iOS/Android/无头设备）也通过 **WebSocket** 连接，但声明 `role: node` 并带有明确的能力/命令。
- 每台主机一个 Gateway 网关；它是唯一打开 WhatsApp 会话的位置。
- **canvas 主机**（默认 `18793`）提供智能体可编辑的 HTML 和 A2UI。

## 组件和流程

### Gateway 网关（守护进程）

- 维护提供商连接。
- 暴露类型化的 WS API（请求、响应、服务器推送事件）。
- 根据 JSON Schema 验证入站帧。
- 发出事件如 `agent`、`chat`、`presence`、`health`、`heartbeat`、`cron`。

### 客户端（mac 应用 / CLI / web 管理）

- 每个客户端一个 WS 连接。
- 发送请求（`health`、`status`、`send`、`agent`、`system-presence`）。
- 订阅事件（`tick`、`agent`、`presence`、`shutdown`）。

### 节点（macOS / iOS / Android / 无头设备）

- 以 `role: node` 连接到**同一个 WS 服务器**。
- 在 `connect` 中提供设备身份；配对是**基于设备**的（角色为 `node`），批准存储在设备配对存储中。
- 暴露命令如 `canvas.*`、`camera.*`、`screen.record`、`location.get`。

协议详情：

- [Gateway 网关协议](/gateway/protocol)

### WebChat

- 静态界面，使用 Gateway 网关 WS API 获取聊天历史和发送消息。
- 在远程设置中，通过与其他客户端相同的 SSH/Tailscale 隧道连接。

## 连接生命周期（单个客户端）

```
Client                    Gateway
  |                          |
  |---- req:connect -------->|
  |<------ res (ok) ---------|   (or res error + close)
  |   (payload=hello-ok carries snapshot: presence + health)
  |                          |
  |<------ event:presence ---|
  |<------ event:tick -------|
  |                          |
  |------- req:agent ------->|
  |<------ res:agent --------|   (ack: {runId,status:"accepted"})
  |<------ event:agent ------|   (streaming)
  |<------ res:agent --------|   (final: {runId,status,summary})
  |                          |
```

## 线路协议（摘要）

- 传输：WebSocket，带 JSON 载荷的文本帧。
- 第一帧**必须**是 `connect`。
- 握手后：
  - 请求：`{type:"req", id, method, params}` → `{type:"res", id, ok, payload|error}`
  - 事件：`{type:"event", event, payload, seq?, stateVersion?}`
- 如果设置了 `OPENCLAW_GATEWAY_TOKEN`（或 `--token`），`connect.params.auth.token` 必须匹配，否则套接字关闭。
- 有副作用的方法（`send`、`agent`）需要幂等键以安全重试；服务器保持短期去重缓存。
- 节点必须在 `connect` 中包含 `role: "node"` 以及能力/命令/权限。

## 配对 + 本地信任

- 所有 WS 客户端（操作员 + 节点）在 `connect` 时包含**设备身份**。
- 新设备 ID 需要配对批准；Gateway 网关为后续连接颁发**设备令牌**。
- **本地**连接（loopback 或 Gateway 网关主机自身的 tailnet 地址）可以自动批准以保持同主机用户体验流畅。
- **非本地**连接必须签名 `connect.challenge` nonce 并需要明确批准。
- Gateway 网关认证（`gateway.auth.*`）仍适用于**所有**连接，无论本地还是远程。

详情：[Gateway 网关协议](/gateway/protocol)、[配对](/channels/pairing)、[安全](/gateway/security)。

## 协议类型和代码生成

- TypeBox 模式定义协议。
- 从这些模式生成 JSON Schema。
- 从 JSON Schema 生成 Swift 模型。

## 远程访问

- 推荐：Tailscale 或 VPN。
- 替代方案：SSH 隧道
  ```bash
  ssh -N -L 18789:127.0.0.1:18789 user@host
  ```
- 相同的握手 + 认证令牌适用于隧道连接。
- 远程设置中可以为 WS 启用 TLS + 可选的证书固定。

## 操作快照

- 启动：`openclaw gateway`（前台，日志输出到 stdout）。
- 健康检查：通过 WS 的 `health`（也包含在 `hello-ok` 中）。
- 监控：使用 launchd/systemd 自动重启。

## 不变量

- 每台主机恰好一个 Gateway 网关控制单个 Baileys 会话。
- 握手是强制的；任何非 JSON 或非 connect 的第一帧都会导致硬关闭。
- 事件不会重放；客户端必须在出现间隙时刷新。


---

## multi-agent

---
read_when: You want multiple isolated agents (workspaces + auth) in one gateway process.
status: active
summary: 多智能体路由：隔离的智能体、渠道账户和绑定
title: 多智能体路由
x-i18n:
  generated_at: "2026-02-03T07:47:38Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 1848266c632cd6c96ff99ea9eb9c17bbfe6d35fa1f90450853083e7c548d5324
  source_path: concepts/multi-agent.md
  workflow: 15
---

# 多智能体路由

目标：多个*隔离的*智能体（独立的工作区 + `agentDir` + 会话），加上多个渠道账户（例如两个 WhatsApp）在一个运行的 Gateway 网关中。入站消息通过绑定路由到智能体。

## 什么是"一个智能体"？

一个**智能体**是一个完全独立作用域的大脑，拥有自己的：

- **工作区**（文件、AGENTS.md/SOUL.md/USER.md、本地笔记、人设规则）。
- **状态目录**（`agentDir`）用于认证配置文件、模型注册表和每智能体配置。
- **会话存储**（聊天历史 + 路由状态）位于 `~/.openclaw/agents/<agentId>/sessions` 下。

认证配置文件是**每智能体独立的**。每个智能体从自己的位置读取：

```
~/.openclaw/agents/<agentId>/agent/auth-profiles.json
```

主智能体凭证**不会**自动共享。切勿在智能体之间重用 `agentDir`（这会导致认证/会话冲突）。如果你想共享凭证，请将 `auth-profiles.json` 复制到另一个智能体的 `agentDir`。

Skills 通过每个工作区的 `skills/` 文件夹实现每智能体独立，共享的 Skills 可从 `~/.openclaw/skills` 获取。参见 [Skills：每智能体 vs 共享](/tools/skills#per-agent-vs-shared-skills)。

Gateway 网关可以托管**一个智能体**（默认）或**多个智能体**并行。

**工作区注意事项：** 每个智能体的工作区是**默认 cwd**，而不是硬性沙箱。相对路径在工作区内解析，但绝对路径可以访问主机的其他位置，除非启用了沙箱隔离。参见 [沙箱隔离](/gateway/sandboxing)。

## 路径（快速映射）

- 配置：`~/.openclaw/openclaw.json`（或 `OPENCLAW_CONFIG_PATH`）
- 状态目录：`~/.openclaw`（或 `OPENCLAW_STATE_DIR`）
- 工作区：`~/.openclaw/workspace`（或 `~/.openclaw/workspace-<agentId>`）
- 智能体目录：`~/.openclaw/agents/<agentId>/agent`（或 `agents.list[].agentDir`）
- 会话：`~/.openclaw/agents/<agentId>/sessions`

### 单智能体模式（默认）

如果你什么都不做，OpenClaw 运行单个智能体：

- `agentId` 默认为 **`main`**。
- 会话键为 `agent:main:<mainKey>`。
- 工作区默认为 `~/.openclaw/workspace`（或当设置了 `OPENCLAW_PROFILE` 时为 `~/.openclaw/workspace-<profile>`）。
- 状态默认为 `~/.openclaw/agents/main/agent`。

## 智能体助手

使用智能体向导添加新的隔离智能体：

```bash
openclaw agents add work
```

然后添加 `bindings`（或让向导完成）来路由入站消息。

验证：

```bash
openclaw agents list --bindings
```

## 多个智能体 = 多个人、多种人格

使用**多个智能体**，每个 `agentId` 成为一个**完全隔离的人格**：

- **不同的电话号码/账户**（每渠道 `accountId`）。
- **不同的人格**（每智能体工作区文件如 `AGENTS.md` 和 `SOUL.md`）。
- **独立的认证 + 会话**（除非明确启用，否则无交叉通信）。

这让**多个人**共享一个 Gateway 网关服务器，同时保持他们的 AI"大脑"和数据隔离。

## 一个 WhatsApp 号码，多个人（私信分割）

你可以将**不同的 WhatsApp 私信**路由到不同的智能体，同时保持**一个 WhatsApp 账户**。使用 `peer.kind: "dm"` 匹配发送者 E.164（如 `+15551234567`）。回复仍然来自同一个 WhatsApp 号码（无每智能体发送者身份）。

重要细节：直接聊天折叠到智能体的**主会话键**，因此真正的隔离需要**每人一个智能体**。

示例：

```json5
{
  agents: {
    list: [
      { id: "alex", workspace: "~/.openclaw/workspace-alex" },
      { id: "mia", workspace: "~/.openclaw/workspace-mia" },
    ],
  },
  bindings: [
    { agentId: "alex", match: { channel: "whatsapp", peer: { kind: "dm", id: "+15551230001" } } },
    { agentId: "mia", match: { channel: "whatsapp", peer: { kind: "dm", id: "+15551230002" } } },
  ],
  channels: {
    whatsapp: {
      dmPolicy: "allowlist",
      allowFrom: ["+15551230001", "+15551230002"],
    },
  },
}
```

注意事项：

- 私信访问控制是**每 WhatsApp 账户全局的**（配对/允许列表），而不是每智能体。
- 对于共享群组，将群组绑定到一个智能体或使用 [广播群组](/channels/broadcast-groups)。

## 路由规则（消息如何选择智能体）

绑定是**确定性的**，**最具体的优先**：

1. `peer` 匹配（精确私信/群组/频道 id）
2. `guildId`（Discord）
3. `teamId`（Slack）
4. 渠道的 `accountId` 匹配
5. 渠道级匹配（`accountId: "*"`）
6. 回退到默认智能体（`agents.list[].default`，否则列表中的第一个条目，默认：`main`）

## 多账户/电话号码

支持**多账户**的渠道（如 WhatsApp）使用 `accountId` 来识别每个登录。每个 `accountId` 可以路由到不同的智能体，因此一个服务器可以托管多个电话号码而不混合会话。

## 概念

- `agentId`：一个"大脑"（工作区、每智能体认证、每智能体会话存储）。
- `accountId`：一个渠道账户实例（例如 WhatsApp 账户 `"personal"` vs `"biz"`）。
- `binding`：通过 `(channel, accountId, peer)` 以及可选的 guild/team id 将入站消息路由到 `agentId`。
- 直接聊天折叠到 `agent:<agentId>:<mainKey>`（每智能体"主"；`session.mainKey`）。

## 示例：两个 WhatsApp → 两个智能体

`~/.openclaw/openclaw.json`（JSON5）：

```js
{
  agents: {
    list: [
      {
        id: "home",
        default: true,
        name: "Home",
        workspace: "~/.openclaw/workspace-home",
        agentDir: "~/.openclaw/agents/home/agent",
      },
      {
        id: "work",
        name: "Work",
        workspace: "~/.openclaw/workspace-work",
        agentDir: "~/.openclaw/agents/work/agent",
      },
    ],
  },

  // 确定性路由：第一个匹配获胜（最具体的优先）。
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },

    // 可选的每对等方覆盖（示例：将特定群组发送到 work 智能体）。
    {
      agentId: "work",
      match: {
        channel: "whatsapp",
        accountId: "personal",
        peer: { kind: "group", id: "1203630...@g.us" },
      },
    },
  ],

  // 默认关闭：智能体到智能体的消息必须明确启用 + 加入允许列表。
  tools: {
    agentToAgent: {
      enabled: false,
      allow: ["home", "work"],
    },
  },

  channels: {
    whatsapp: {
      accounts: {
        personal: {
          // 可选覆盖。默认：~/.openclaw/credentials/whatsapp/personal
          // authDir: "~/.openclaw/credentials/whatsapp/personal",
        },
        biz: {
          // 可选覆盖。默认：~/.openclaw/credentials/whatsapp/biz
          // authDir: "~/.openclaw/credentials/whatsapp/biz",
        },
      },
    },
  },
}
```

## 示例：WhatsApp 日常聊天 + Telegram 深度工作

按渠道分割：将 WhatsApp 路由到快速日常智能体，Telegram 路由到 Opus 智能体。

```json5
{
  agents: {
    list: [
      {
        id: "chat",
        name: "Everyday",
        workspace: "~/.openclaw/workspace-chat",
        model: "anthropic/claude-sonnet-4-5",
      },
      {
        id: "opus",
        name: "Deep Work",
        workspace: "~/.openclaw/workspace-opus",
        model: "anthropic/claude-opus-4-5",
      },
    ],
  },
  bindings: [
    { agentId: "chat", match: { channel: "whatsapp" } },
    { agentId: "opus", match: { channel: "telegram" } },
  ],
}
```

注意事项：

- 如果你有一个渠道的多个账户，请在绑定中添加 `accountId`（例如 `{ channel: "whatsapp", accountId: "personal" }`）。
- 要将单个私信/群组路由到 Opus 而保持其余在 chat 上，请为该对等方添加 `match.peer` 绑定；对等方匹配始终优先于渠道级规则。

## 示例：同一渠道，一个对等方到 Opus

保持 WhatsApp 在快速智能体上，但将一个私信路由到 Opus：

```json5
{
  agents: {
    list: [
      {
        id: "chat",
        name: "Everyday",
        workspace: "~/.openclaw/workspace-chat",
        model: "anthropic/claude-sonnet-4-5",
      },
      {
        id: "opus",
        name: "Deep Work",
        workspace: "~/.openclaw/workspace-opus",
        model: "anthropic/claude-opus-4-5",
      },
    ],
  },
  bindings: [
    { agentId: "opus", match: { channel: "whatsapp", peer: { kind: "dm", id: "+15551234567" } } },
    { agentId: "chat", match: { channel: "whatsapp" } },
  ],
}
```

对等方绑定始终获胜，因此将它们放在渠道级规则之上。

## 绑定到 WhatsApp 群组的家庭智能体

将专用家庭智能体绑定到单个 WhatsApp 群组，使用提及限制和更严格的工具策略：

```json5
{
  agents: {
    list: [
      {
        id: "family",
        name: "Family",
        workspace: "~/.openclaw/workspace-family",
        identity: { name: "Family Bot" },
        groupChat: {
          mentionPatterns: ["@family", "@familybot", "@Family Bot"],
        },
        sandbox: {
          mode: "all",
          scope: "agent",
        },
        tools: {
          allow: [
            "exec",
            "read",
            "sessions_list",
            "sessions_history",
            "sessions_send",
            "sessions_spawn",
            "session_status",
          ],
          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],
        },
      },
    ],
  },
  bindings: [
    {
      agentId: "family",
      match: {
        channel: "whatsapp",
        peer: { kind: "group", id: "120363999999999999@g.us" },
      },
    },
  ],
}
```

注意事项：

- 工具允许/拒绝列表是**工具**，不是 Skills。如果 skill 需要运行二进制文件，请确保 `exec` 被允许且二进制文件存在于沙箱中。
- 对于更严格的限制，设置 `agents.list[].groupChat.mentionPatterns` 并为渠道保持群组允许列表启用。

## 每智能体沙箱和工具配置

从 v2026.1.6 开始，每个智能体可以有自己的沙箱和工具限制：

```js
{
  agents: {
    list: [
      {
        id: "personal",
        workspace: "~/.openclaw/workspace-personal",
        sandbox: {
          mode: "off",  // 个人智能体无沙箱
        },
        // 无工具限制 - 所有工具可用
      },
      {
        id: "family",
        workspace: "~/.openclaw/workspace-family",
        sandbox: {
          mode: "all",     // 始终沙箱隔离
          scope: "agent",  // 每智能体一个容器
          docker: {
            // 容器创建后的可选一次性设置
            setupCommand: "apt-get update && apt-get install -y git curl",
          },
        },
        tools: {
          allow: ["read"],                    // 仅 read 工具
          deny: ["exec", "write", "edit", "apply_patch"],    // 拒绝其他
        },
      },
    ],
  },
}
```

注意：`setupCommand` 位于 `sandbox.docker` 下，在容器创建时运行一次。
当解析的 scope 为 `"shared"` 时，每智能体 `sandbox.docker.*` 覆盖会被忽略。

**好处：**

- **安全隔离**：限制不受信任智能体的工具
- **资源控制**：沙箱隔离特定智能体同时保持其他智能体在主机上
- **灵活策略**：每智能体不同的权限

注意：`tools.elevated` 是**全局的**且基于发送者；不能按智能体配置。
如果你需要每智能体边界，使用 `agents.list[].tools` 拒绝 `exec`。
对于群组定向，使用 `agents.list[].groupChat.mentionPatterns` 使 @提及清晰地映射到目标智能体。

参见 [多智能体沙箱和工具](/tools/multi-agent-sandbox-tools) 了解详细示例。


---

## memory

---
read_when:
  - 你想了解记忆文件布局和工作流程
  - 你想调整自动压缩前的记忆刷新
summary: OpenClaw 记忆的工作原理（工作空间文件 + 自动记忆刷新）
title: 记忆
x-i18n:
  generated_at: "2026-02-03T07:47:38Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: f3a7f5d9f61f9742eb3a8adbc3ccaddeadb7e48ceccdfb595327d6d1f55cd00e
  source_path: concepts/memory.md
  workflow: 15
---

# 记忆

OpenClaw 记忆是**智能体工作空间中的纯 Markdown 文件**。这些文件是唯一的事实来源；模型只"记住"写入磁盘的内容。

记忆搜索工具由活动的记忆插件提供（默认：`memory-core`）。使用 `plugins.slots.memory = "none"` 禁用记忆插件。

## 记忆文件（Markdown）

默认工作空间布局使用两个记忆层：

- `memory/YYYY-MM-DD.md`
  - 每日日志（仅追加）。
  - 在会话开始时读取今天和昨天的内容。
- `MEMORY.md`（可选）
  - 精心整理的长期记忆。
  - **仅在主要的私人会话中加载**（绝不在群组上下文中加载）。

这些文件位于工作空间下（`agents.defaults.workspace`，默认 `~/.openclaw/workspace`）。完整布局参见[智能体工作空间](/concepts/agent-workspace)。

## 何时写入记忆

- 决策、偏好和持久性事实写入 `MEMORY.md`。
- 日常笔记和运行上下文写入 `memory/YYYY-MM-DD.md`。
- 如果有人说"记住这个"，就写下来（不要只保存在内存中）。
- 这个领域仍在发展中。提醒模型存储记忆会有帮助；它会知道该怎么做。
- 如果你想让某些内容持久保存，**请要求机器人将其写入**记忆。

## 自动记忆刷新（压缩前触发）

当会话**接近自动压缩**时，OpenClaw 会触发一个**静默的智能体回合**，提醒模型在上下文被压缩**之前**写入持久记忆。默认提示明确说明模型*可以回复*，但通常 `NO_REPLY` 是正确的响应，因此用户永远不会看到这个回合。

这由 `agents.defaults.compaction.memoryFlush` 控制：

```json5
{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with NO_REPLY if nothing to store.",
        },
      },
    },
  },
}
```

详情：

- **软阈值**：当会话 token 估计超过 `contextWindow - reserveTokensFloor - softThresholdTokens` 时触发刷新。
- 默认**静默**：提示包含 `NO_REPLY`，因此不会发送任何内容。
- **两个提示**：一个用户提示加一个系统提示附加提醒。
- **每个压缩周期刷新一次**（在 `sessions.json` 中跟踪）。
- **工作空间必须可写**：如果会话以 `workspaceAccess: "ro"` 或 `"none"` 在沙箱中运行，则跳过刷新。

完整的压缩生命周期参见[会话管理 + 压缩](/reference/session-management-compaction)。

## 向量记忆搜索

OpenClaw 可以在 `MEMORY.md` 和 `memory/*.md`（以及你选择加入的任何额外目录或文件）上构建小型向量索引，以便语义查询可以找到相关笔记，即使措辞不同。

默认值：

- 默认启用。
- 监视记忆文件的更改（去抖动）。
- 默认使用远程嵌入。如果未设置 `memorySearch.provider`，OpenClaw 自动选择：
  1. 如果配置了 `memorySearch.local.modelPath` 且文件存在，则使用 `local`。
  2. 如果可以解析 OpenAI 密钥，则使用 `openai`。
  3. 如果可以解析 Gemini 密钥，则使用 `gemini`。
  4. 否则记忆搜索保持禁用状态直到配置完成。
- 本地模式使用 node-llama-cpp，可能需要运行 `pnpm approve-builds`。
- 使用 sqlite-vec（如果可用）在 SQLite 中加速向量搜索。

远程嵌入**需要**嵌入提供商的 API 密钥。OpenClaw 从身份验证配置文件、`models.providers.*.apiKey` 或环境变量解析密钥。Codex OAuth 仅涵盖聊天/补全，**不**满足记忆搜索的嵌入需求。对于 Gemini，使用 `GEMINI_API_KEY` 或 `models.providers.google.apiKey`。使用自定义 OpenAI 兼容端点时，设置 `memorySearch.remote.apiKey`（以及可选的 `memorySearch.remote.headers`）。

### 额外记忆路径

如果你想索引默认工作空间布局之外的 Markdown 文件，添加显式路径：

```json5
agents: {
  defaults: {
    memorySearch: {
      extraPaths: ["../team-docs", "/srv/shared-notes/overview.md"]
    }
  }
}
```

说明：

- 路径可以是绝对路径或工作空间相对路径。
- 目录会递归扫描 `.md` 文件。
- 仅索引 Markdown 文件。
- 符号链接被忽略（文件或目录）。

### Gemini 嵌入（原生）

将提供商设置为 `gemini` 以直接使用 Gemini 嵌入 API：

```json5
agents: {
  defaults: {
    memorySearch: {
      provider: "gemini",
      model: "gemini-embedding-001",
      remote: {
        apiKey: "YOUR_GEMINI_API_KEY"
      }
    }
  }
}
```

说明：

- `remote.baseUrl` 是可选的（默认为 Gemini API 基础 URL）。
- `remote.headers` 让你可以在需要时添加额外的标头。
- 默认模型：`gemini-embedding-001`。

如果你想使用**自定义 OpenAI 兼容端点**（OpenRouter、vLLM 或代理），可以使用 `remote` 配置与 OpenAI 提供商：

```json5
agents: {
  defaults: {
    memorySearch: {
      provider: "openai",
      model: "text-embedding-3-small",
      remote: {
        baseUrl: "https://api.example.com/v1/",
        apiKey: "YOUR_OPENAI_COMPAT_API_KEY",
        headers: { "X-Custom-Header": "value" }
      }
    }
  }
}
```

如果你不想设置 API 密钥，使用 `memorySearch.provider = "local"` 或设置 `memorySearch.fallback = "none"`。

回退：

- `memorySearch.fallback` 可以是 `openai`、`gemini`、`local` 或 `none`。
- 回退提供商仅在主嵌入提供商失败时使用。

批量索引（OpenAI + Gemini）：

- OpenAI 和 Gemini 嵌入默认启用。设置 `agents.defaults.memorySearch.remote.batch.enabled = false` 以禁用。
- 默认行为等待批处理完成；如果需要可以调整 `remote.batch.wait`、`remote.batch.pollIntervalMs` 和 `remote.batch.timeoutMinutes`。
- 设置 `remote.batch.concurrency` 以控制我们并行提交多少个批处理作业（默认：2）。
- 批处理模式在 `memorySearch.provider = "openai"` 或 `"gemini"` 时适用，并使用相应的 API 密钥。
- Gemini 批处理作业使用异步嵌入批处理端点，需要 Gemini Batch API 可用。

为什么 OpenAI 批处理快速又便宜：

- 对于大型回填，OpenAI 通常是我们支持的最快选项，因为我们可以在单个批处理作业中提交许多嵌入请求，让 OpenAI 异步处理它们。
- OpenAI 为 Batch API 工作负载提供折扣定价，因此大型索引运行通常比同步发送相同请求更便宜。
- 详情参见 OpenAI Batch API 文档和定价：
  - https://platform.openai.com/docs/api-reference/batch
  - https://platform.openai.com/pricing

配置示例：

```json5
agents: {
  defaults: {
    memorySearch: {
      provider: "openai",
      model: "text-embedding-3-small",
      fallback: "openai",
      remote: {
        batch: { enabled: true, concurrency: 2 }
      },
      sync: { watch: true }
    }
  }
}
```

工具：

- `memory_search` — 返回带有文件 + 行范围的片段。
- `memory_get` — 按路径读取记忆文件内容。

本地模式：

- 设置 `agents.defaults.memorySearch.provider = "local"`。
- 提供 `agents.defaults.memorySearch.local.modelPath`（GGUF 或 `hf:` URI）。
- 可选：设置 `agents.defaults.memorySearch.fallback = "none"` 以避免远程回退。

### 记忆工具的工作原理

- `memory_search` 从 `MEMORY.md` + `memory/**/*.md` 语义搜索 Markdown 块（目标约 400 个 token，80 个 token 重叠）。它返回片段文本（上限约 700 个字符）、文件路径、行范围、分数、提供商/模型，以及我们是否从本地回退到远程嵌入。不返回完整文件内容。
- `memory_get` 读取特定的记忆 Markdown 文件（工作空间相对路径），可选从起始行开始读取 N 行。`MEMORY.md` / `memory/` 之外的路径仅在明确列在 `memorySearch.extraPaths` 中时才允许。
- 两个工具仅在智能体的 `memorySearch.enabled` 解析为 true 时启用。

### 索引内容（及时机）

- 文件类型：仅 Markdown（`MEMORY.md`、`memory/**/*.md`，以及 `memorySearch.extraPaths` 下的任何 `.md` 文件）。
- 索引存储：每个智能体的 SQLite 位于 `~/.openclaw/memory/<agentId>.sqlite`（可通过 `agents.defaults.memorySearch.store.path` 配置，支持 `{agentId}` 令牌）。
- 新鲜度：监视器监视 `MEMORY.md`、`memory/` 和 `memorySearch.extraPaths`，标记索引为脏（去抖动 1.5 秒）。同步在会话开始时、搜索时或按间隔安排，并异步运行。会话记录使用增量阈值触发后台同步。
- 重新索引触发器：索引存储嵌入的**提供商/模型 + 端点指纹 + 分块参数**。如果其中任何一个发生变化，OpenClaw 会自动重置并重新索引整个存储。

### 混合搜索（BM25 + 向量）

启用时，OpenClaw 结合：

- **向量相似度**（语义匹配，措辞可以不同）
- **BM25 关键词相关性**（精确令牌如 ID、环境变量、代码符号）

如果你的平台上全文搜索不可用，OpenClaw 会回退到纯向量搜索。

#### 为什么使用混合搜索？

向量搜索擅长"这意味着同一件事"：

- "Mac Studio gateway host" vs "运行 gateway 的机器"
- "debounce file updates" vs "避免每次写入都索引"

但它在精确的高信号令牌上可能较弱：

- ID（`a828e60`、`b3b9895a…`）
- 代码符号（`memorySearch.query.hybrid`）
- 错误字符串（"sqlite-vec unavailable"）

BM25（全文）正好相反：擅长精确令牌，弱于释义。
混合搜索是务实的中间地带：**同时使用两种检索信号**，这样你可以在"自然语言"查询和"大海捞针"查询上都获得好结果。

#### 我们如何合并结果（当前设计）

实现概述：

1. 从双方检索候选池：

- **向量**：按余弦相似度取前 `maxResults * candidateMultiplier` 个。
- **BM25**：按 FTS5 BM25 排名取前 `maxResults * candidateMultiplier` 个（越低越好）。

2. 将 BM25 排名转换为 0..1 范围的分数：

- `textScore = 1 / (1 + max(0, bm25Rank))`

3. 按块 id 合并候选并计算加权分数：

- `finalScore = vectorWeight * vectorScore + textWeight * textScore`

说明：

- 在配置解析中 `vectorWeight` + `textWeight` 归一化为 1.0，因此权重表现为百分比。
- 如果嵌入不可用（或提供商返回零向量），我们仍然运行 BM25 并返回关键词匹配。
- 如果无法创建 FTS5，我们保持纯向量搜索（不会硬失败）。

这不是"IR 理论完美"的，但它简单、快速，并且往往能提高真实笔记的召回率/精确率。
如果我们以后想要更复杂的方案，常见的下一步是倒数排名融合（RRF）或在混合之前进行分数归一化（最小/最大或 z 分数）。

配置：

```json5
agents: {
  defaults: {
    memorySearch: {
      query: {
        hybrid: {
          enabled: true,
          vectorWeight: 0.7,
          textWeight: 0.3,
          candidateMultiplier: 4
        }
      }
    }
  }
}
```

### 嵌入缓存

OpenClaw 可以在 SQLite 中缓存**块嵌入**，这样重新索引和频繁更新（特别是会话记录）不会重新嵌入未更改的文本。

配置：

```json5
agents: {
  defaults: {
    memorySearch: {
      cache: {
        enabled: true,
        maxEntries: 50000
      }
    }
  }
}
```

### 会话记忆搜索（实验性）

你可以选择性地索引**会话记录**并通过 `memory_search` 呈现它们。
这由实验性标志控制。

```json5
agents: {
  defaults: {
    memorySearch: {
      experimental: { sessionMemory: true },
      sources: ["memory", "sessions"]
    }
  }
}
```

说明：

- 会话索引是**选择加入**的（默认关闭）。
- 会话更新被去抖动并在超过增量阈值后**异步索引**（尽力而为）。
- `memory_search` 永远不会阻塞索引；在后台同步完成之前，结果可能略有延迟。
- 结果仍然只包含片段；`memory_get` 仍然仅限于记忆文件。
- 会话索引按智能体隔离（仅索引该智能体的会话日志）。
- 会话日志存储在磁盘上（`~/.openclaw/agents/<agentId>/sessions/*.jsonl`）。任何具有文件系统访问权限的进程/用户都可以读取它们，因此将磁盘访问视为信任边界。对于更严格的隔离，在单独的操作系统用户或主机下运行智能体。

增量阈值（显示默认值）：

```json5
agents: {
  defaults: {
    memorySearch: {
      sync: {
        sessions: {
          deltaBytes: 100000,   // ~100 KB
          deltaMessages: 50     // JSONL 行数
        }
      }
    }
  }
}
```

### SQLite 向量加速（sqlite-vec）

当 sqlite-vec 扩展可用时，OpenClaw 将嵌入存储在 SQLite 虚拟表（`vec0`）中，并在数据库中执行向量距离查询。这使搜索保持快速，无需将每个嵌入加载到 JS 中。

配置（可选）：

```json5
agents: {
  defaults: {
    memorySearch: {
      store: {
        vector: {
          enabled: true,
          extensionPath: "/path/to/sqlite-vec"
        }
      }
    }
  }
}
```

说明：

- `enabled` 默认为 true；禁用时，搜索回退到对存储嵌入的进程内余弦相似度计算。
- 如果 sqlite-vec 扩展缺失或加载失败，OpenClaw 会记录错误并继续使用 JS 回退（无向量表）。
- `extensionPath` 覆盖捆绑的 sqlite-vec 路径（对于自定义构建或非标准安装位置很有用）。

### 本地嵌入自动下载

- 默认本地嵌入模型：`hf:ggml-org/embeddinggemma-300M-GGUF/embeddinggemma-300M-Q8_0.gguf`（约 0.6 GB）。
- 当 `memorySearch.provider = "local"` 时，`node-llama-cpp` 解析 `modelPath`；如果 GGUF 缺失，它会**自动下载**到缓存（或 `local.modelCacheDir`，如果已设置），然后加载它。下载在重试时会续传。
- 原生构建要求：运行 `pnpm approve-builds`，选择 `node-llama-cpp`，然后运行 `pnpm rebuild node-llama-cpp`。
- 回退：如果本地设置失败且 `memorySearch.fallback = "openai"`，我们自动切换到远程嵌入（`openai/text-embedding-3-small`，除非被覆盖）并记录原因。

### 自定义 OpenAI 兼容端点示例

```json5
agents: {
  defaults: {
    memorySearch: {
      provider: "openai",
      model: "text-embedding-3-small",
      remote: {
        baseUrl: "https://api.example.com/v1/",
        apiKey: "YOUR_REMOTE_API_KEY",
        headers: {
          "X-Organization": "org-id",
          "X-Project": "project-id"
        }
      }
    }
  }
}
```

说明：

- `remote.*` 优先于 `models.providers.openai.*`。
- `remote.headers` 与 OpenAI 标头合并；键冲突时 remote 优先。省略 `remote.headers` 以使用 OpenAI 默认值。


---

## session

---
read_when:
  - 修改会话处理或存储
summary: 聊天的会话管理规则、键和持久化
title: 会话管理
x-i18n:
  generated_at: "2026-02-03T07:47:44Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 147c8d1a4b6b4864cb16ad942feba80181b6b0e29afa765e7958f8c2483746b5
  source_path: concepts/session.md
  workflow: 15
---

# 会话管理

OpenClaw 将**每个智能体的一个直接聊天会话**视为主会话。直接聊天折叠为 `agent:<agentId>:<mainKey>`（默认 `main`），而群组/频道聊天获得各自的键。`session.mainKey` 会被遵循。

使用 `session.dmScope` 控制**私信**如何分组：

- `main`（默认）：所有私信共享主会话以保持连续性。
- `per-peer`：跨渠道按发送者 ID 隔离。
- `per-channel-peer`：按渠道 + 发送者隔离（推荐用于多用户收件箱）。
- `per-account-channel-peer`：按账户 + 渠道 + 发送者隔离（推荐用于多账户收件箱）。
  使用 `session.identityLinks` 将带提供商前缀的对等 ID 映射到规范身份，这样在使用 `per-peer`、`per-channel-peer` 或 `per-account-channel-peer` 时，同一个人可以跨渠道共享私信会话。

## Gateway 网关是唯一数据源

所有会话状态都**由 Gateway 网关拥有**（"主" OpenClaw）。UI 客户端（macOS 应用、WebChat 等）必须向 Gateway 网关查询会话列表和令牌计数，而不是读取本地文件。

- 在**远程模式**下，你关心的会话存储位于远程 Gateway 网关主机上，而不是你的 Mac 上。
- UI 中显示的令牌计数来自 Gateway 网关的存储字段（`inputTokens`、`outputTokens`、`totalTokens`、`contextTokens`）。客户端不会解析 JSONL 对话记录来"修正"总数。

## 状态存储位置

- 在 **Gateway 网关主机**上：
  - 存储文件：`~/.openclaw/agents/<agentId>/sessions/sessions.json`（每个智能体）。
- 对话记录：`~/.openclaw/agents/<agentId>/sessions/<SessionId>.jsonl`（Telegram 话题会话使用 `.../<SessionId>-topic-<threadId>.jsonl`）。
- 存储是一个映射 `sessionKey -> { sessionId, updatedAt, ... }`。删除条目是安全的；它们会按需重新创建。
- 群组条目可能包含 `displayName`、`channel`、`subject`、`room` 和 `space` 以在 UI 中标记会话。
- 会话条目包含 `origin` 元数据（标签 + 路由提示），以便 UI 可以解释会话的来源。
- OpenClaw **不**读取旧版 Pi/Tau 会话文件夹。

## 会话修剪

默认情况下，OpenClaw 在 LLM 调用之前从内存上下文中修剪**旧的工具结果**。
这**不会**重写 JSONL 历史记录。参见 [/concepts/session-pruning](/concepts/session-pruning)。

## 压缩前记忆刷新

当会话接近自动压缩时，OpenClaw 可以运行一个**静默记忆刷新**轮次，提醒模型将持久性笔记写入磁盘。这仅在工作区可写时运行。参见[记忆](/concepts/memory)和[压缩](/concepts/compaction)。

## 传输到会话键的映射

- 直接聊天遵循 `session.dmScope`（默认 `main`）。
  - `main`：`agent:<agentId>:<mainKey>`（跨设备/渠道的连续性）。
    - 多个电话号码和渠道可以映射到同一个智能体主键；它们作为进入同一个对话的传输通道。
  - `per-peer`：`agent:<agentId>:dm:<peerId>`。
  - `per-channel-peer`：`agent:<agentId>:<channel>:dm:<peerId>`。
  - `per-account-channel-peer`：`agent:<agentId>:<channel>:<accountId>:dm:<peerId>`（accountId 默认为 `default`）。
  - 如果 `session.identityLinks` 匹配带提供商前缀的对等 ID（例如 `telegram:123`），则规范键替换 `<peerId>`，这样同一个人可以跨渠道共享会话。
- 群组聊天隔离状态：`agent:<agentId>:<channel>:group:<id>`（房间/频道使用 `agent:<agentId>:<channel>:channel:<id>`）。
  - Telegram 论坛话题在群组 ID 后附加 `:topic:<threadId>` 以进行隔离。
  - 旧版 `group:<id>` 键仍被识别以进行迁移。
- 入站上下文可能仍使用 `group:<id>`；渠道从 `Provider` 推断并规范化为规范的 `agent:<agentId>:<channel>:group:<id>` 形式。
- 其他来源：
  - 定时任务：`cron:<job.id>`
  - Webhooks：`hook:<uuid>`（除非由 hook 显式设置）
  - 节点运行：`node-<nodeId>`

## 生命周期

- 重置策略：会话被重用直到过期，过期在下一条入站消息时评估。
- 每日重置：默认为 **Gateway 网关主机本地时间凌晨 4:00**。当会话的最后更新早于最近的每日重置时间时，会话即为过期。
- 空闲重置（可选）：`idleMinutes` 添加一个滑动空闲窗口。当同时配置每日和空闲重置时，**先过期者**强制新会话。
- 旧版仅空闲模式：如果你设置了 `session.idleMinutes` 而没有任何 `session.reset`/`resetByType` 配置，OpenClaw 会保持仅空闲模式以保持向后兼容。
- 按类型覆盖（可选）：`resetByType` 允许你覆盖 `dm`、`group` 和 `thread` 会话的策略（thread = Slack/Discord 线程、Telegram 话题、连接器提供的 Matrix 线程）。
- 按渠道覆盖（可选）：`resetByChannel` 覆盖渠道的重置策略（适用于该渠道的所有会话类型，优先于 `reset`/`resetByType`）。
- 重置触发器：精确的 `/new` 或 `/reset`（加上 `resetTriggers` 中的任何额外项）启动新的会话 ID 并传递消息的其余部分。`/new <model>` 接受模型别名、`provider/model` 或提供商名称（模糊匹配）来设置新会话模型。如果单独发送 `/new` 或 `/reset`，OpenClaw 会运行一个简短的"问候"轮次来确认重置。
- 手动重置：从存储中删除特定键或删除 JSONL 对话记录；下一条消息会重新创建它们。
- 隔离的定时任务总是每次运行生成新的 `sessionId`（没有空闲重用）。

## 发送策略（可选）

阻止特定会话类型的投递，无需列出单个 ID。

```json5
{
  session: {
    sendPolicy: {
      rules: [
        { action: "deny", match: { channel: "discord", chatType: "group" } },
        { action: "deny", match: { keyPrefix: "cron:" } },
      ],
      default: "allow",
    },
  },
}
```

运行时覆盖（仅所有者）：

- `/send on` → 为此会话允许
- `/send off` → 为此会话拒绝
- `/send inherit` → 清除覆盖并使用配置规则
  将这些作为独立消息发送以使其生效。

## 配置（可选重命名示例）

```json5
// ~/.openclaw/openclaw.json
{
  session: {
    scope: "per-sender", // keep group keys separate
    dmScope: "main", // DM continuity (set per-channel-peer/per-account-channel-peer for shared inboxes)
    identityLinks: {
      alice: ["telegram:123456789", "discord:987654321012345678"],
    },
    reset: {
      // Defaults: mode=daily, atHour=4 (gateway host local time).
      // If you also set idleMinutes, whichever expires first wins.
      mode: "daily",
      atHour: 4,
      idleMinutes: 120,
    },
    resetByType: {
      thread: { mode: "daily", atHour: 4 },
      dm: { mode: "idle", idleMinutes: 240 },
      group: { mode: "idle", idleMinutes: 120 },
    },
    resetByChannel: {
      discord: { mode: "idle", idleMinutes: 10080 },
    },
    resetTriggers: ["/new", "/reset"],
    store: "~/.openclaw/agents/{agentId}/sessions/sessions.json",
    mainKey: "main",
  },
}
```

## 检查

- `openclaw status` — 显示存储路径和最近的会话。
- `openclaw sessions --json` — 导出每个条目（使用 `--active <minutes>` 过滤）。
- `openclaw gateway call sessions.list --params '{}'` — 从运行中的 Gateway 网关获取会话（使用 `--url`/`--token` 进行远程 Gateway 网关访问）。
- 在聊天中单独发送 `/status` 消息可查看智能体是否可达、会话上下文使用了多少、当前的思考/详细模式开关，以及你的 WhatsApp Web 凭证上次刷新时间（有助于发现重新链接需求）。
- 发送 `/context list` 或 `/context detail` 查看系统提示中的内容和注入的工作区文件（以及最大的上下文贡献者）。
- 单独发送 `/stop` 消息可中止当前运行、清除该会话的排队后续操作，并停止从中生成的任何子智能体运行（回复包含已停止的数量）。
- 单独发送 `/compact`（可选指令）消息可总结旧上下文并释放窗口空间。参见 [/concepts/compaction](/concepts/compaction)。
- 可以直接打开 JSONL 对话记录查看完整轮次。

## 提示

- 将主键专用于 1:1 通信；让群组保留各自的键。
- 自动清理时，删除单个键而不是整个存储，以保留其他地方的上下文。

## 会话来源元数据

每个会话条目记录其来源（尽力而为）在 `origin` 中：

- `label`：人类可读标签（从对话标签 + 群组主题/频道解析）
- `provider`：规范化的渠道 ID（包括扩展）
- `from`/`to`：入站信封中的原始路由 ID
- `accountId`：提供商账户 ID（多账户时）
- `threadId`：渠道支持时的线程/话题 ID
  来源字段为私信、频道和群组填充。如果连接器仅更新投递路由（例如，保持私信主会话新鲜），它仍应提供入站上下文，以便会话保留其解释器元数据。扩展可以通过在入站上下文中发送 `ConversationLabel`、`GroupSubject`、`GroupChannel`、`GroupSpace` 和 `SenderName` 并调用 `recordSessionMetaFromInbound`（或将相同上下文传递给 `updateLastRoute`）来实现。


---

## configuration

---
read_when:
  - 添加或修改配置字段时
summary: ~/.openclaw/openclaw.json 的所有配置选项及示例
title: 配置
x-i18n:
  generated_at: "2026-02-01T21:29:41Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: b5e51290bbc755acb259ad455878625aa894c115e5c0ac6a1a3397e10fff8b4b
  source_path: gateway/configuration.md
  workflow: 15
---

# 配置 🔧

OpenClaw 从 `~/.openclaw/openclaw.json` 读取可选的 **JSON5** 配置（支持注释和尾逗号）。

如果文件不存在，OpenClaw 使用安全的默认值（内置 Pi 智能体 + 按发送者分会话 + 工作区 `~/.openclaw/workspace`）。通常只在以下情况需要配置：

- 限制谁可以触发机器人（`channels.whatsapp.allowFrom`、`channels.telegram.allowFrom` 等）
- 控制群组白名单 + 提及行为（`channels.whatsapp.groups`、`channels.telegram.groups`、`channels.discord.guilds`、`agents.list[].groupChat`）
- 自定义消息前缀（`messages`）
- 设置智能体工作区（`agents.defaults.workspace` 或 `agents.list[].workspace`）
- 调整内置智能体默认值（`agents.defaults`）和会话行为（`session`）
- 设置每个智能体的身份标识（`agents.list[].identity`）

> **初次接触配置？** 请查阅[配置示例](/gateway/configuration-examples)指南，获取带有详细说明的完整示例！

## 严格配置验证

OpenClaw 只接受完全匹配 schema 的配置。
未知键、类型错误或无效值会导致 Gateway 网关 **拒绝启动**以确保安全。

验证失败时：

- Gateway 网关不会启动。
- 只允许诊断命令（例如：`openclaw doctor`、`openclaw logs`、`openclaw health`、`openclaw status`、`openclaw service`、`openclaw help`）。
- 运行 `openclaw doctor` 查看具体问题。
- 运行 `openclaw doctor --fix`（或 `--yes`）应用迁移/修复。

Doctor 不会写入任何更改，除非你明确选择了 `--fix`/`--yes`。

## Schema + UI 提示

Gateway 网关通过 `config.schema` 暴露配置的 JSON Schema 表示，供 UI 编辑器使用。
控制台 UI 根据此 schema 渲染表单，并提供 **Raw JSON** 编辑器作为应急手段。

渠道插件和扩展可以为其配置注册 schema + UI 提示，因此渠道设置
在各应用间保持 schema 驱动，无需硬编码表单。

提示信息（标签、分组、敏感字段）随 schema 一起提供，客户端无需硬编码配置知识即可渲染更好的表单。

## 应用 + 重启（RPC）

使用 `config.apply` 在一步中验证 + 写入完整配置并重启 Gateway 网关。
它会写入重启哨兵文件，并在 Gateway 网关恢复后 ping 最后活跃的会话。

警告：`config.apply` 会替换**整个配置**。如果你只想更改部分键，
请使用 `config.patch` 或 `openclaw config set`。请备份 `~/.openclaw/openclaw.json`。

参数：

- `raw`（字符串）— 整个配置的 JSON5 负载
- `baseHash`（可选）— 来自 `config.get` 的配置哈希（当配置已存在时为必需）
- `sessionKey`（可选）— 最后活跃会话的键，用于唤醒 ping
- `note`（可选）— 包含在重启哨兵中的备注
- `restartDelayMs`（可选）— 重启前的延迟（默认 2000）

示例（通过 `gateway call`）：

```bash
openclaw gateway call config.get --params '{}' # capture payload.hash
openclaw gateway call config.apply --params '{
  "raw": "{\\n  agents: { defaults: { workspace: \\"~/.openclaw/workspace\\" } }\\n}\\n",
  "baseHash": "<hash-from-config.get>",
  "sessionKey": "agent:main:whatsapp:dm:+15555550123",
  "restartDelayMs": 1000
}'
```

## 部分更新（RPC）

使用 `config.patch` 将部分更新合并到现有配置中，而不会覆盖
无关的键。它采用 JSON merge patch 语义：

- 对象递归合并
- `null` 删除键
- 数组替换
  与 `config.apply` 类似，它会验证、写入配置、存储重启哨兵，并调度
  Gateway 网关重启（当提供 `sessionKey` 时可选择唤醒）。

参数：

- `raw`（字符串）— 仅包含要更改的键的 JSON5 负载
- `baseHash`（必需）— 来自 `config.get` 的配置哈希
- `sessionKey`（可选）— 最后活跃会话的键，用于唤醒 ping
- `note`（可选）— 包含在重启哨兵中的备注
- `restartDelayMs`（可选）— 重启前的延迟（默认 2000）

示例：

```bash
openclaw gateway call config.get --params '{}' # capture payload.hash
openclaw gateway call config.patch --params '{
  "raw": "{\\n  channels: { telegram: { groups: { \\"*\\": { requireMention: false } } } }\\n}\\n",
  "baseHash": "<hash-from-config.get>",
  "sessionKey": "agent:main:whatsapp:dm:+15555550123",
  "restartDelayMs": 1000
}'
```

## 最小配置（推荐起点）

```json5
{
  agents: { defaults: { workspace: "~/.openclaw/workspace" } },
  channels: { whatsapp: { allowFrom: ["+15555550123"] } },
}
```

首次构建默认镜像：

```bash
scripts/sandbox-setup.sh
```

## 自聊天模式（推荐用于群组控制）

防止机器人在群组中响应 WhatsApp @提及（仅响应特定文本触发器）：

```json5
{
  agents: {
    defaults: { workspace: "~/.openclaw/workspace" },
    list: [
      {
        id: "main",
        groupChat: { mentionPatterns: ["@openclaw", "reisponde"] },
      },
    ],
  },
  channels: {
    whatsapp: {
      // 白名单仅适用于私聊；包含你自己的号码可启用自聊天模式。
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } },
    },
  },
}
```

## 配置包含（`$include`）

使用 `$include` 指令将配置拆分为多个文件。适用于：

- 组织大型配置（例如按客户定义智能体）
- 跨环境共享通用设置
- 将敏感配置单独存放

### 基本用法

```json5
// ~/.openclaw/openclaw.json
{
  gateway: { port: 18789 },

  // 包含单个文件（替换该键的值）
  agents: { $include: "./agents.json5" },

  // 包含多个文件（按顺序深度合并）
  broadcast: {
    $include: ["./clients/mueller.json5", "./clients/schmidt.json5"],
  },
}
```

```json5
// ~/.openclaw/agents.json5
{
  defaults: { sandbox: { mode: "all", scope: "session" } },
  list: [{ id: "main", workspace: "~/.openclaw/workspace" }],
}
```

### 合并行为

- **单个文件**：替换包含 `$include` 的对象
- **文件数组**：按顺序深度合并（后面的文件覆盖前面的）
- **带兄弟键**：兄弟键在包含之后合并（覆盖被包含的值）
- **兄弟键 + 数组/原始值**：不支持（被包含的内容必须是对象）

```json5
// 兄弟键覆盖被包含的值
{
  $include: "./base.json5", // { a: 1, b: 2 }
  b: 99, // 结果：{ a: 1, b: 99 }
}
```

### 嵌套包含

被包含的文件本身可以包含 `$include` 指令（最多 10 层深度）：

```json5
// clients/mueller.json5
{
  agents: { $include: "./mueller/agents.json5" },
  broadcast: { $include: "./mueller/broadcast.json5" },
}
```

### 路径解析

- **相对路径**：相对于包含文件解析
- **绝对路径**：直接使用
- **父目录**：`../` 引用按预期工作

```json5
{ "$include": "./sub/config.json5" }      // 相对路径
{ "$include": "/etc/openclaw/base.json5" } // 绝对路径
{ "$include": "../shared/common.json5" }   // 父目录
```

### 错误处理

- **文件缺失**：显示清晰的错误及解析后的路径
- **解析错误**：显示哪个被包含的文件出错
- **循环包含**：检测并报告包含链

### 示例：多客户法律事务设置

```json5
// ~/.openclaw/openclaw.json
{
  gateway: { port: 18789, auth: { token: "secret" } },

  // 通用智能体默认值
  agents: {
    defaults: {
      sandbox: { mode: "all", scope: "session" },
    },
    // 合并所有客户的智能体列表
    list: { $include: ["./clients/mueller/agents.json5", "./clients/schmidt/agents.json5"] },
  },

  // 合并广播配置
  broadcast: {
    $include: ["./clients/mueller/broadcast.json5", "./clients/schmidt/broadcast.json5"],
  },

  channels: { whatsapp: { groupPolicy: "allowlist" } },
}
```

```json5
// ~/.openclaw/clients/mueller/agents.json5
[
  { id: "mueller-transcribe", workspace: "~/clients/mueller/transcribe" },
  { id: "mueller-docs", workspace: "~/clients/mueller/docs" },
]
```

```json5
// ~/.openclaw/clients/mueller/broadcast.json5
{
  "120363403215116621@g.us": ["mueller-transcribe", "mueller-docs"],
}
```

## 常用选项

### 环境变量 + `.env`

OpenClaw 从父进程（shell、launchd/systemd、CI 等）读取环境变量。

此外，它还会加载：

- 当前工作目录中的 `.env`（如果存在）
- `~/.openclaw/.env`（即 `$OPENCLAW_STATE_DIR/.env`）作为全局回退 `.env`

两个 `.env` 文件都不会覆盖已有的环境变量。

你也可以在配置中提供内联环境变量。这些仅在进程环境中缺少该键时应用（相同的不覆盖规则）：

```json5
{
  env: {
    OPENROUTER_API_KEY: "sk-or-...",
    vars: {
      GROQ_API_KEY: "gsk-...",
    },
  },
}
```

参见 [/environment](/help/environment) 了解优先级和来源详情。

### `env.shellEnv`（可选）

可选便利功能：如果启用且预期键均未设置，OpenClaw 会运行你的登录 shell 并仅导入缺失的预期键（不会覆盖）。
这实际上会 source 你的 shell 配置文件。

```json5
{
  env: {
    shellEnv: {
      enabled: true,
      timeoutMs: 15000,
    },
  },
}
```

等效环境变量：

- `OPENCLAW_LOAD_SHELL_ENV=1`
- `OPENCLAW_SHELL_ENV_TIMEOUT_MS=15000`

### 配置中的环境变量替换

你可以在任何配置字符串值中使用 `${VAR_NAME}` 语法直接引用环境变量。变量在配置加载时、验证之前进行替换。

```json5
{
  models: {
    providers: {
      "vercel-gateway": {
        apiKey: "${VERCEL_GATEWAY_API_KEY}",
      },
    },
  },
  gateway: {
    auth: {
      token: "${OPENCLAW_GATEWAY_TOKEN}",
    },
  },
}
```

**规则：**

- 仅匹配大写环境变量名：`[A-Z_][A-Z0-9_]*`
- 缺失或为空的环境变量在配置加载时会抛出错误
- 使用 `$${VAR}` 转义以输出字面量 `${VAR}`
- 与 `$include` 配合使用（被包含的文件也会进行替换）

**内联替换：**

```json5
{
  models: {
    providers: {
      custom: {
        baseUrl: "${CUSTOM_API_BASE}/v1", // → "https://api.example.com/v1"
      },
    },
  },
}
```

### 认证存储（OAuth + API 密钥）

OpenClaw 在以下位置存储**每个智能体的**认证配置文件（OAuth + API 密钥）：

- `<agentDir>/auth-profiles.json`（默认：`~/.openclaw/agents/<agentId>/agent/auth-profiles.json`）

另请参阅：[/concepts/oauth](/concepts/oauth)

旧版 OAuth 导入：

- `~/.openclaw/credentials/oauth.json`（或 `$OPENCLAW_STATE_DIR/credentials/oauth.json`）

内置 Pi 智能体在以下位置维护运行时缓存：

- `<agentDir>/auth.json`（自动管理；请勿手动编辑）

旧版智能体目录（多智能体之前）：

- `~/.openclaw/agent/*`（由 `openclaw doctor` 迁移到 `~/.openclaw/agents/<defaultAgentId>/agent/*`）

覆盖：

- OAuth 目录（仅旧版导入）：`OPENCLAW_OAUTH_DIR`
- 智能体目录（默认智能体根目录覆盖）：`OPENCLAW_AGENT_DIR`（推荐）、`PI_CODING_AGENT_DIR`（旧版）

首次使用时，OpenClaw 会将 `oauth.json` 条目导入到 `auth-profiles.json` 中。

### `auth`

认证配置文件的可选元数据。这**不**存储密钥；它将配置文件 ID 映射到提供商 + 模式（以及可选的邮箱），并定义用于故障转移的提供商轮换顺序。

```json5
{
  auth: {
    profiles: {
      "anthropic:me@example.com": { provider: "anthropic", mode: "oauth", email: "me@example.com" },
      "anthropic:work": { provider: "anthropic", mode: "api_key" },
    },
    order: {
      anthropic: ["anthropic:me@example.com", "anthropic:work"],
    },
  },
}
```

### `agents.list[].identity`

用于默认值和用户体验的可选每智能体身份标识。由 macOS 新手引导助手写入。

如果设置了，OpenClaw 会推导默认值（仅在你未明确设置时）：

- `messages.ackReaction` 来自**活跃智能体**的 `identity.emoji`（回退到 👀）
- `agents.list[].groupChat.mentionPatterns` 来自智能体的 `identity.name`/`identity.emoji`（因此 "@Samantha" 在 Telegram/Slack/Discord/Google Chat/iMessage/WhatsApp 的群组中均可使用）
- `identity.avatar` 接受工作区相对图片路径或远程 URL/data URL。本地文件必须位于智能体工作区内。

`identity.avatar` 接受：

- 工作区相对路径（必须在智能体工作区内）
- `http(s)` URL
- `data:` URI

```json5
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "Samantha",
          theme: "helpful sloth",
          emoji: "🦥",
          avatar: "avatars/samantha.png",
        },
      },
    ],
  },
}
```

### `wizard`

由 CLI 向导（`onboard`、`configure`、`doctor`）写入的元数据。

```json5
{
  wizard: {
    lastRunAt: "2026-01-01T00:00:00.000Z",
    lastRunVersion: "2026.1.4",
    lastRunCommit: "abc1234",
    lastRunCommand: "configure",
    lastRunMode: "local",
  },
}
```

### `logging`

- 默认日志文件：`/tmp/openclaw/openclaw-YYYY-MM-DD.log`
- 如需稳定路径，将 `logging.file` 设为 `/tmp/openclaw/openclaw.log`。
- 控制台输出可通过以下方式单独调整：
  - `logging.consoleLevel`（默认 `info`，使用 `--verbose` 时提升为 `debug`）
  - `logging.consoleStyle`（`pretty` | `compact` | `json`）
- 工具摘要可以脱敏以避免泄露密钥：
  - `logging.redactSensitive`（`off` | `tools`，默认：`tools`）
  - `logging.redactPatterns`（正则表达式字符串数组；覆盖默认值）

```json5
{
  logging: {
    level: "info",
    file: "/tmp/openclaw/openclaw.log",
    consoleLevel: "info",
    consoleStyle: "pretty",
    redactSensitive: "tools",
    redactPatterns: [
      // 示例：用自定义规则覆盖默认值。
      "\\bTOKEN\\b\\s*[=:]\\s*([\"']?)([^\\s\"']+)\\1",
      "/\\bsk-[A-Za-z0-9_-]{8,}\\b/gi",
    ],
  },
}
```

### `channels.whatsapp.dmPolicy`

控制 WhatsApp 私聊（私信）的处理方式：

- `"pairing"`（默认）：未知发送者会收到配对码；所有者必须批准
- `"allowlist"`：仅允许 `channels.whatsapp.allowFrom`（或已配对的允许存储）中的发送者
- `"open"`：允许所有入站私聊（**需要** `channels.whatsapp.allowFrom` 包含 `"*"`）
- `"disabled"`：忽略所有入站私聊

配对码在 1 小时后过期；机器人仅在创建新请求时发送配对码。待处理的私聊配对请求默认每个渠道上限为 **3 个**。

配对批准：

- `openclaw pairing list whatsapp`
- `openclaw pairing approve whatsapp <code>`

### `channels.whatsapp.allowFrom`

允许触发 WhatsApp 自动回复的 E.164 电话号码白名单（**仅限私聊**）。
如果为空且 `channels.whatsapp.dmPolicy="pairing"`，未知发送者将收到配对码。
对于群组，使用 `channels.whatsapp.groupPolicy` + `channels.whatsapp.groupAllowFrom`。

```json5
{
  channels: {
    whatsapp: {
      dmPolicy: "pairing", // pairing | allowlist | open | disabled
      allowFrom: ["+15555550123", "+447700900123"],
      textChunkLimit: 4000, // 可选的出站分块大小（字符数）
      chunkMode: "length", // 可选的分块模式（length | newline）
      mediaMaxMb: 50, // 可选的入站媒体上限（MB）
    },
  },
}
```

### `channels.whatsapp.sendReadReceipts`

控制入站 WhatsApp 消息是否标记为已读（蓝色双勾）。默认：`true`。

自聊天模式始终跳过已读回执，即使已启用。

每账号覆盖：`channels.whatsapp.accounts.<id>.sendReadReceipts`。

```json5
{
  channels: {
    whatsapp: { sendReadReceipts: false },
  },
}
```

### `channels.whatsapp.accounts`（多账号）

在一个 Gateway 网关中运行多个 WhatsApp 账号：

```json5
{
  channels: {
    whatsapp: {
      accounts: {
        default: {}, // 可选；保持默认 id 稳定
        personal: {},
        biz: {
          // 可选覆盖。默认：~/.openclaw/credentials/whatsapp/biz
          // authDir: "~/.openclaw/credentials/whatsapp/biz",
        },
      },
    },
  },
}
```

说明：

- 出站命令默认使用 `default` 账号（如果存在）；否则使用第一个配置的账号 id（排序后）。
- 旧版单账号 Baileys 认证目录由 `openclaw doctor` 迁移到 `whatsapp/default`。

### `channels.telegram.accounts` / `channels.discord.accounts` / `channels.googlechat.accounts` / `channels.slack.accounts` / `channels.mattermost.accounts` / `channels.signal.accounts` / `channels.imessage.accounts`

每个渠道运行多个账号（每个账号有自己的 `accountId` 和可选的 `name`）：

```json5
{
  channels: {
    telegram: {
      accounts: {
        default: {
          name: "Primary bot",
          botToken: "123456:ABC...",
        },
        alerts: {
          name: "Alerts bot",
          botToken: "987654:XYZ...",
        },
      },
    },
  },
}
```

说明：

- 省略 `accountId` 时使用 `default`（CLI + 路由）。
- 环境变量 token 仅适用于**默认**账号。
- 基础渠道设置（群组策略、提及门控等）适用于所有账号，除非在每个账号中单独覆盖。
- 使用 `bindings[].match.accountId` 将每个账号路由到不同的 agents.defaults。

### 群聊提及门控（`agents.list[].groupChat` + `messages.groupChat`）

群消息默认**需要提及**（元数据提及或正则模式）。适用于 WhatsApp、Telegram、Discord、Google Chat 和 iMessage 群聊。

**提及类型：**

- **元数据提及**：原生平台 @提及（例如 WhatsApp 点按提及）。在 WhatsApp 自聊天模式中被忽略（参见 `channels.whatsapp.allowFrom`）。
- **文本模式**：在 `agents.list[].groupChat.mentionPatterns` 中定义的正则模式。无论自聊天模式如何始终检查。
- 提及门控仅在可以检测提及时执行（原生提及或至少一个 `mentionPattern`）。

```json5
{
  messages: {
    groupChat: { historyLimit: 50 },
  },
  agents: {
    list: [{ id: "main", groupChat: { mentionPatterns: ["@openclaw", "openclaw"] } }],
  },
}
```

`messages.groupChat.historyLimit` 设置群组历史上下文的全局默认值。渠道可以通过 `channels.<channel>.historyLimit`（或多账号的 `channels.<channel>.accounts.*.historyLimit`）覆盖。设为 `0` 禁用历史包装。

#### 私聊历史限制

私聊对话使用由智能体管理的基于会话的历史。你可以限制每个私聊会话保留的用户轮次数：

```json5
{
  channels: {
    telegram: {
      dmHistoryLimit: 30, // 将私聊会话限制为 30 个用户轮次
      dms: {
        "123456789": { historyLimit: 50 }, // 每用户覆盖（用户 ID）
      },
    },
  },
}
```

解析顺序：

1. 每私聊覆盖：`channels.<provider>.dms[userId].historyLimit`
2. 提供商默认值：`channels.<provider>.dmHistoryLimit`
3. 无限制（保留所有历史）

支持的提供商：`telegram`、`whatsapp`、`discord`、`slack`、`signal`、`imessage`、`msteams`。

每智能体覆盖（设置后优先，即使为 `[]`）：

```json5
{
  agents: {
    list: [
      { id: "work", groupChat: { mentionPatterns: ["@workbot", "\\+15555550123"] } },
      { id: "personal", groupChat: { mentionPatterns: ["@homebot", "\\+15555550999"] } },
    ],
  },
}
```

提及门控默认值按渠道设置（`channels.whatsapp.groups`、`channels.telegram.groups`、`channels.imessage.groups`、`channels.discord.guilds`）。当设置了 `*.groups` 时，它也充当群组白名单；包含 `"*"` 以允许所有群组。

仅响应特定文本触发器（忽略原生 @提及）：

```json5
{
  channels: {
    whatsapp: {
      // 包含你自己的号码以启用自聊天模式（忽略原生 @提及）。
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } },
    },
  },
  agents: {
    list: [
      {
        id: "main",
        groupChat: {
          // 仅这些文本模式会触发响应
          mentionPatterns: ["reisponde", "@openclaw"],
        },
      },
    ],
  },
}
```

### 群组策略（按渠道）

使用 `channels.*.groupPolicy` 控制是否接受群组/房间消息：

```json5
{
  channels: {
    whatsapp: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["+15551234567"],
    },
    telegram: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["tg:123456789", "@alice"],
    },
    signal: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["+15551234567"],
    },
    imessage: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["chat_id:123"],
    },
    msteams: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["user@org.com"],
    },
    discord: {
      groupPolicy: "allowlist",
      guilds: {
        GUILD_ID: {
          channels: { help: { allow: true } },
        },
      },
    },
    slack: {
      groupPolicy: "allowlist",
      channels: { "#general": { allow: true } },
    },
  },
}
```

说明：

- `"open"`：群组绕过白名单；提及门控仍然适用。
- `"disabled"`：阻止所有群组/房间消息。
- `"allowlist"`：仅允许匹配配置白名单的群组/房间。
- `channels.defaults.groupPolicy` 设置提供商的 `groupPolicy` 未设置时的默认值。
- WhatsApp/Telegram/Signal/iMessage/Microsoft Teams 使用 `groupAllowFrom`（回退：显式 `allowFrom`）。
- Discord/Slack 使用渠道白名单（`channels.discord.guilds.*.channels`、`channels.slack.channels`）。
- 群组私聊（Discord/Slack）仍由 `dm.groupEnabled` + `dm.groupChannels` 控制。
- 默认为 `groupPolicy: "allowlist"`（除非被 `channels.defaults.groupPolicy` 覆盖）；如果未配置白名单，群组消息将被阻止。

### 多智能体路由（`agents.list` + `bindings`）

在一个 Gateway 网关中运行多个隔离的智能体（独立的工作区、`agentDir`、会话）。
入站消息通过绑定路由到智能体。

- `agents.list[]`：每智能体覆盖。
  - `id`：稳定的智能体 id（必需）。
  - `default`：可选；当设置多个时，第一个获胜并记录警告。
    如果未设置，列表中的**第一个条目**为默认智能体。
  - `name`：智能体的显示名称。
  - `workspace`：默认 `~/.openclaw/workspace-<agentId>`（对于 `main`，回退到 `agents.defaults.workspace`）。
  - `agentDir`：默认 `~/.openclaw/agents/<agentId>/agent`。
  - `model`：每智能体默认模型，覆盖该智能体的 `agents.defaults.model`。
    - 字符串形式：`"provider/model"`，仅覆盖 `agents.defaults.model.primary`
    - 对象形式：`{ primary, fallbacks }`（fallbacks 覆盖 `agents.defaults.model.fallbacks`；`[]` 为该智能体禁用全局回退）
  - `identity`：每智能体的名称/主题/表情（用于提及模式 + 确认反应）。
  - `groupChat`：每智能体的提及门控（`mentionPatterns`）。
  - `sandbox`：每智能体的沙箱配置（覆盖 `agents.defaults.sandbox`）。
    - `mode`：`"off"` | `"non-main"` | `"all"`
    - `workspaceAccess`：`"none"` | `"ro"` | `"rw"`
    - `scope`：`"session"` | `"agent"` | `"shared"`
    - `workspaceRoot`：自定义沙箱工作区根目录
    - `docker`：每智能体 docker 覆盖（例如 `image`、`network`、`env`、`setupCommand`、限制；`scope: "shared"` 时忽略）
    - `browser`：每智能体沙箱浏览器覆盖（`scope: "shared"` 时忽略）
    - `prune`：每智能体沙箱清理覆盖（`scope: "shared"` 时忽略）
  - `subagents`：每智能体子智能体默认值。
    - `allowAgents`：允许从此智能体执行 `sessions_spawn` 的智能体 id 白名单（`["*"]` = 允许任何；默认：仅同一智能体）
  - `tools`：每智能体工具限制（在沙箱工具策略之前应用）。
    - `profile`：基础工具配置文件（在 allow/deny 之前应用）
    - `allow`：允许的工具名称数组
    - `deny`：拒绝的工具名称数组（deny 优先）
- `agents.defaults`：共享的智能体默认值（模型、工作区、沙箱等）。
- `bindings[]`：将入站消息路由到 `agentId`。
  - `match.channel`（必需）
  - `match.accountId`（可选；`*` = 任何账号；省略 = 默认账号）
  - `match.peer`（可选；`{ kind: dm|group|channel, id }`）
  - `match.guildId` / `match.teamId`（可选；渠道特定）

确定性匹配顺序：

1. `match.peer`
2. `match.guildId`
3. `match.teamId`
4. `match.accountId`（精确匹配，无 peer/guild/team）
5. `match.accountId: "*"`（渠道范围，无 peer/guild/team）
6. 默认智能体（`agents.list[].default`，否则第一个列表条目，否则 `"main"`）

在每个匹配层级内，`bindings` 中的第一个匹配条目获胜。

#### 每智能体访问配置（多智能体）

每个智能体可以携带自己的沙箱 + 工具策略。用于在一个 Gateway 网关中混合访问级别：

- **完全访问**（个人智能体）
- **只读**工具 + 工作区
- **无文件系统访问**（仅消息/会话工具）

参见[多智能体沙箱与工具](/tools/multi-agent-sandbox-tools)了解优先级和更多示例。

完全访问（无沙箱）：

```json5
{
  agents: {
    list: [
      {
        id: "personal",
        workspace: "~/.openclaw/workspace-personal",
        sandbox: { mode: "off" },
      },
    ],
  },
}
```

只读工具 + 只读工作区：

```json5
{
  agents: {
    list: [
      {
        id: "family",
        workspace: "~/.openclaw/workspace-family",
        sandbox: {
          mode: "all",
          scope: "agent",
          workspaceAccess: "ro",
        },
        tools: {
          allow: [
            "read",
            "sessions_list",
            "sessions_history",
            "sessions_send",
            "sessions_spawn",
            "session_status",
          ],
          deny: ["write", "edit", "apply_patch", "exec", "process", "browser"],
        },
      },
    ],
  },
}
```

无文件系统访问（启用消息/会话工具）：

```json5
{
  agents: {
    list: [
      {
        id: "public",
        workspace: "~/.openclaw/workspace-public",
        sandbox: {
          mode: "all",
          scope: "agent",
          workspaceAccess: "none",
        },
        tools: {
          allow: [
            "sessions_list",
            "sessions_history",
            "sessions_send",
            "sessions_spawn",
            "session_status",
            "whatsapp",
            "telegram",
            "slack",
            "discord",
            "gateway",
          ],
          deny: [
            "read",
            "write",
            "edit",
            "apply_patch",
            "exec",
            "process",
            "browser",
            "canvas",
            "nodes",
            "cron",
            "gateway",
            "image",
          ],
        },
      },
    ],
  },
}
```

示例：两个 WhatsApp 账号 → 两个智能体：

```json5
{
  agents: {
    list: [
      { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },
      { id: "work", workspace: "~/.openclaw/workspace-work" },
    ],
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
  ],
  channels: {
    whatsapp: {
      accounts: {
        personal: {},
        biz: {},
      },
    },
  },
}
```

### `tools.agentToAgent`（可选）

智能体间消息传递为可选功能：

```json5
{
  tools: {
    agentToAgent: {
      enabled: false,
      allow: ["home", "work"],
    },
  },
}
```

### `messages.queue`

控制智能体运行已在执行时入站消息的行为。

```json5
{
  messages: {
    queue: {
      mode: "collect", // steer | followup | collect | steer-backlog (steer+backlog ok) | interrupt (queue=steer legacy)
      debounceMs: 1000,
      cap: 20,
      drop: "summarize", // old | new | summarize
      byChannel: {
        whatsapp: "collect",
        telegram: "collect",
        discord: "collect",
        imessage: "collect",
        webchat: "collect",
      },
    },
  },
}
```

### `messages.inbound`

防抖**同一发送者**的快速入站消息，使多条连续消息合并为一个智能体轮次。防抖按渠道 + 对话进行范围限定，并使用最新消息进行回复线程/ID。

```json5
{
  messages: {
    inbound: {
      debounceMs: 2000, // 0 禁用
      byChannel: {
        whatsapp: 5000,
        slack: 1500,
        discord: 1500,
      },
    },
  },
}
```

说明：

- 防抖仅批量处理**纯文本**消息；媒体/附件立即刷新。
- 控制命令（例如 `/queue`、`/new`）绕过防抖，保持独立。

### `commands`（聊天命令处理）

控制跨连接器的聊天命令启用方式。

```json5
{
  commands: {
    native: "auto", // 在支持的平台上注册原生命令（auto）
    text: true, // 解析聊天消息中的斜杠命令
    bash: false, // 允许 !（别名：/bash）（仅限主机；需要 tools.elevated 白名单）
    bashForegroundMs: 2000, // bash 前台窗口（0 立即后台运行）
    config: false, // 允许 /config（写入磁盘）
    debug: false, // 允许 /debug（仅运行时覆盖）
    restart: false, // 允许 /restart + gateway 重启工具
    useAccessGroups: true, // 对命令执行访问组白名单/策略
  },
}
```

说明：

- 文本命令必须作为**独立**消息发送，并使用前导 `/`（无纯文本别名）。
- `commands.text: false` 禁用解析聊天消息中的命令。
- `commands.native: "auto"`（默认）为 Discord/Telegram 启用原生命令，Slack 保持关闭；不支持的渠道保持纯文本。
- 设为 `commands.native: true|false` 强制全部开启或关闭，或按渠道覆盖 `channels.discord.commands.native`、`channels.telegram.commands.native`、`channels.slack.commands.native`（bool 或 `"auto"`）。`false` 在启动时清除 Discord/Telegram 上先前注册的命令；Slack 命令在 Slack 应用中管理。
- `channels.telegram.customCommands` 添加额外的 Telegram 机器人菜单项。名称会被规范化；与原生命令冲突的会被忽略。
- `commands.bash: true` 启用 `! <cmd>` 运行主机 shell 命令（`/bash <cmd>` 也可作为别名）。需要 `tools.elevated.enabled` 并在 `tools.elevated.allowFrom.<channel>` 中添加发送者白名单。
- `commands.bashForegroundMs` 控制 bash 在后台运行前等待的时间。当 bash 任务正在运行时，新的 `! <cmd>` 请求会被拒绝（一次一个）。
- `commands.config: true` 启用 `/config`（读写 `openclaw.json`）。
- `channels.<provider>.configWrites` 控制由该渠道发起的配置变更（默认：true）。适用于 `/config set|unset` 以及提供商特定的自动迁移（Telegram 超级群组 ID 变更、Slack 频道 ID 变更）。
- `commands.debug: true` 启用 `/debug`（仅运行时覆盖）。
- `commands.restart: true` 启用 `/restart` 和 gateway 工具重启动作。
- `commands.useAccessGroups: false` 允许命令绕过访问组白名单/策略。
- 斜杠命令和指令仅对**已授权发送者**有效。授权来自渠道白名单/配对以及 `commands.useAccessGroups`。

### `web`（WhatsApp Web 渠道运行时）

WhatsApp 通过 Gateway 网关的 Web 渠道（Baileys Web）运行。当存在已链接的会话时自动启动。
设置 `web.enabled: false` 使其默认关闭。

```json5
{
  web: {
    enabled: true,
    heartbeatSeconds: 60,
    reconnect: {
      initialMs: 2000,
      maxMs: 120000,
      factor: 1.4,
      jitter: 0.2,
      maxAttempts: 0,
    },
  },
}
```

### `channels.telegram`（机器人传输）

OpenClaw 仅在存在 `channels.telegram` 配置段时启动 Telegram。机器人 token 从 `channels.telegram.botToken`（或 `channels.telegram.tokenFile`）解析，`TELEGRAM_BOT_TOKEN` 作为默认账号的回退。
设置 `channels.telegram.enabled: false` 禁用自动启动。
多账号支持在 `channels.telegram.accounts` 下（参见上方多账号部分）。环境变量 token 仅适用于默认账号。
设置 `channels.telegram.configWrites: false` 阻止 Telegram 发起的配置写入（包括超级群组 ID 迁移和 `/config set|unset`）。

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "your-bot-token",
      dmPolicy: "pairing", // pairing | allowlist | open | disabled
      allowFrom: ["tg:123456789"], // 可选；"open" 需要 ["*"]
      groups: {
        "*": { requireMention: true },
        "-1001234567890": {
          allowFrom: ["@admin"],
          systemPrompt: "Keep answers brief.",
          topics: {
            "99": {
              requireMention: false,
              skills: ["search"],
              systemPrompt: "Stay on topic.",
            },
          },
        },
      },
      customCommands: [
        { command: "backup", description: "Git backup" },
        { command: "generate", description: "Create an image" },
      ],
      historyLimit: 50, // 包含最近 N 条群消息作为上下文（0 禁用）
      replyToMode: "first", // off | first | all
      linkPreview: true, // 切换出站链接预览
      streamMode: "partial", // off | partial | block（草稿流式传输；与分块流式传输分开）
      draftChunk: {
        // 可选；仅用于 streamMode=block
        minChars: 200,
        maxChars: 800,
        breakPreference: "paragraph", // paragraph | newline | sentence
      },
      actions: { reactions: true, sendMessage: true }, // 工具动作开关（false 禁用）
      reactionNotifications: "own", // off | own | all
      mediaMaxMb: 5,
      retry: {
        // 出站重试策略
        attempts: 3,
        minDelayMs: 400,
        maxDelayMs: 30000,
        jitter: 0.1,
      },
      network: {
        // 传输覆盖
        autoSelectFamily: false,
      },
      proxy: "socks5://localhost:9050",
      webhookUrl: "https://example.com/telegram-webhook", // 需要 webhookSecret
      webhookSecret: "secret",
      webhookPath: "/telegram-webhook",
    },
  },
}
```

草稿流式传输说明：

- 使用 Telegram `sendMessageDraft`（草稿气泡，不是真正的消息）。
- 需要**私聊话题**（私信 中的 message_thread_id；机器人已启用话题）。
- `/reasoning stream` 将推理过程流式传输到草稿中，然后发送最终答案。
  重试策略默认值和行为记录在[重试策略](/concepts/retry)中。

### `channels.discord`（机器人传输）

通过设置机器人 token 和可选的门控配置 Discord 机器人：
多账号支持在 `channels.discord.accounts` 下（参见上方多账号部分）。环境变量 token 仅适用于默认账号。

```json5
{
  channels: {
    discord: {
      enabled: true,
      token: "your-bot-token",
      mediaMaxMb: 8, // 限制入站媒体大小
      allowBots: false, // 允许机器人发送的消息
      actions: {
        // 工具动作开关（false 禁用）
        reactions: true,
        stickers: true,
        polls: true,
        permissions: true,
        messages: true,
        threads: true,
        pins: true,
        search: true,
        memberInfo: true,
        roleInfo: true,
        roles: false,
        channelInfo: true,
        voiceStatus: true,
        events: true,
        moderation: false,
      },
      replyToMode: "off", // off | first | all
      dm: {
        enabled: true, // 设为 false 时禁用所有私聊
        policy: "pairing", // pairing | allowlist | open | disabled
        allowFrom: ["1234567890", "steipete"], // 可选私聊白名单（"open" 需要 ["*"]）
        groupEnabled: false, // 启用群组私聊
        groupChannels: ["openclaw-dm"], // 可选群组私聊白名单
      },
      guilds: {
        "123456789012345678": {
          // 服务器 id（推荐）或 slug
          slug: "friends-of-openclaw",
          requireMention: false, // 每服务器默认值
          reactionNotifications: "own", // off | own | all | allowlist
          users: ["987654321098765432"], // 可选的每服务器用户白名单
          channels: {
            general: { allow: true },
            help: {
              allow: true,
              requireMention: true,
              users: ["987654321098765432"],
              skills: ["docs"],
              systemPrompt: "Short answers only.",
            },
          },
        },
      },
      historyLimit: 20, // 包含最近 N 条服务器消息作为上下文
      textChunkLimit: 2000, // 可选出站文本分块大小（字符数）
      chunkMode: "length", // 可选分块模式（length | newline）
      maxLinesPerMessage: 17, // 每条消息的软最大行数（Discord UI 裁剪）
      retry: {
        // 出站重试策略
        attempts: 3,
        minDelayMs: 500,
        maxDelayMs: 30000,
        jitter: 0.1,
      },
    },
  },
}
```

OpenClaw 仅在存在 `channels.discord` 配置段时启动 Discord。token 从 `channels.discord.token` 解析，`DISCORD_BOT_TOKEN` 作为默认账号的回退（除非 `channels.discord.enabled` 为 `false`）。在为 cron/CLI 命令指定投递目标时，使用 `user:<id>`（私聊）或 `channel:<id>`（服务器频道）；裸数字 ID 有歧义会被拒绝。
服务器 slug 为小写，空格替换为 `-`；频道键使用 slug 化的频道名称（无前导 `#`）。建议使用服务器 id 作为键以避免重命名歧义。
机器人发送的消息默认被忽略。通过 `channels.discord.allowBots` 启用（自身消息仍会被过滤以防止自回复循环）。
反应通知模式：

- `off`：无反应事件。
- `own`：机器人自身消息上的反应（默认）。
- `all`：所有消息上的所有反应。
- `allowlist`：`guilds.<id>.users` 中的用户在所有消息上的反应（空列表禁用）。
  出站文本按 `channels.discord.textChunkLimit`（默认 2000）分块。设置 `channels.discord.chunkMode="newline"` 在长度分块前按空行（段落边界）分割。Discord 客户端可能裁剪过高的消息，因此 `channels.discord.maxLinesPerMessage`（默认 17）即使在 2000 字符以内也会分割长多行回复。
  重试策略默认值和行为记录在[重试策略](/concepts/retry)中。

### `channels.googlechat`（Chat API webhook）

Google Chat 通过 HTTP webhook 运行，使用应用级认证（服务账号）。
多账号支持在 `channels.googlechat.accounts` 下（参见上方多账号部分）。环境变量仅适用于默认账号。

```json5
{
  channels: {
    googlechat: {
      enabled: true,
      serviceAccountFile: "/path/to/service-account.json",
      audienceType: "app-url", // app-url | project-number
      audience: "https://gateway.example.com/googlechat",
      webhookPath: "/googlechat",
      botUser: "users/1234567890", // 可选；改善提及检测
      dm: {
        enabled: true,
        policy: "pairing", // pairing | allowlist | open | disabled
        allowFrom: ["users/1234567890"], // 可选；"open" 需要 ["*"]
      },
      groupPolicy: "allowlist",
      groups: {
        "spaces/AAAA": { allow: true, requireMention: true },
      },
      actions: { reactions: true },
      typingIndicator: "message",
      mediaMaxMb: 20,
    },
  },
}
```

说明：

- 服务账号 JSON 可以内联（`serviceAccount`）或基于文件（`serviceAccountFile`）。
- 默认账号的环境变量回退：`GOOGLE_CHAT_SERVICE_ACCOUNT` 或 `GOOGLE_CHAT_SERVICE_ACCOUNT_FILE`。
- `audienceType` + `audience` 必须与 Chat 应用的 webhook 认证配置匹配。
- 设置投递目标时使用 `spaces/<spaceId>` 或 `users/<userId|email>`。

### `channels.slack`（socket 模式）

Slack 以 Socket Mode 运行，需要机器人 token 和应用 token：

```json5
{
  channels: {
    slack: {
      enabled: true,
      botToken: "xoxb-...",
      appToken: "xapp-...",
      dm: {
        enabled: true,
        policy: "pairing", // pairing | allowlist | open | disabled
        allowFrom: ["U123", "U456", "*"], // 可选；"open" 需要 ["*"]
        groupEnabled: false,
        groupChannels: ["G123"],
      },
      channels: {
        C123: { allow: true, requireMention: true, allowBots: false },
        "#general": {
          allow: true,
          requireMention: true,
          allowBots: false,
          users: ["U123"],
          skills: ["docs"],
          systemPrompt: "Short answers only.",
        },
      },
      historyLimit: 50, // 包含最近 N 条频道/群组消息作为上下文（0 禁用）
      allowBots: false,
      reactionNotifications: "own", // off | own | all | allowlist
      reactionAllowlist: ["U123"],
      replyToMode: "off", // off | first | all
      thread: {
        historyScope: "thread", // thread | channel
        inheritParent: false,
      },
      actions: {
        reactions: true,
        messages: true,
        pins: true,
        memberInfo: true,
        emojiList: true,
      },
      slashCommand: {
        enabled: true,
        name: "openclaw",
        sessionPrefix: "slack:slash",
        ephemeral: true,
      },
      textChunkLimit: 4000,
      chunkMode: "length",
      mediaMaxMb: 20,
    },
  },
}
```

多账号支持在 `channels.slack.accounts` 下（参见上方多账号部分）。环境变量 token 仅适用于默认账号。

OpenClaw 在提供商启用且两个 token 都已设置时启动 Slack（通过配置或 `SLACK_BOT_TOKEN` + `SLACK_APP_TOKEN`）。在为 cron/CLI 命令指定投递目标时使用 `user:<id>`（私聊）或 `channel:<id>`。
设置 `channels.slack.configWrites: false` 阻止 Slack 发起的配置写入（包括频道 ID 迁移和 `/config set|unset`）。

机器人发送的消息默认被忽略。通过 `channels.slack.allowBots` 或 `channels.slack.channels.<id>.allowBots` 启用。

反应通知模式：

- `off`：无反应事件。
- `own`：机器人自身消息上的反应（默认）。
- `all`：所有消息上的所有反应。
- `allowlist`：`channels.slack.reactionAllowlist` 中的用户在所有消息上的反应（空列表禁用）。

线程会话隔离：

- `channels.slack.thread.historyScope` 控制线程历史是按线程（`thread`，默认）还是跨频道共享（`channel`）。
- `channels.slack.thread.inheritParent` 控制新线程会话是否继承父频道的记录（默认：false）。

Slack 动作组（控制 `slack` 工具动作）：
| 动作组 | 默认 | 说明 |
| --- | --- | --- |
| reactions | 已启用 | 反应 + 列出反应 |
| messages | 已启用 | 读取/发送/编辑/删除 |
| pins | 已启用 | 固定/取消固定/列出 |
| memberInfo | 已启用 | 成员信息 |
| emojiList | 已启用 | 自定义表情列表 |

### `channels.mattermost`（机器人 token）

Mattermost 作为插件提供，不包含在核心安装中。
请先安装：`openclaw plugins install @openclaw/mattermost`（或从 git checkout 使用 `./extensions/mattermost`）。

Mattermost 需要机器人 token 加上服务器的基础 URL：

```json5
{
  channels: {
    mattermost: {
      enabled: true,
      botToken: "mm-token",
      baseUrl: "https://chat.example.com",
      dmPolicy: "pairing",
      chatmode: "oncall", // oncall | onmessage | onchar
      oncharPrefixes: [">", "!"],
      textChunkLimit: 4000,
      chunkMode: "length",
    },
  },
}
```

OpenClaw 在账号已配置（机器人 token + 基础 URL）且已启用时启动 Mattermost。token + 基础 URL 从 `channels.mattermost.botToken` + `channels.mattermost.baseUrl` 或默认账号的 `MATTERMOST_BOT_TOKEN` + `MATTERMOST_URL` 解析（除非 `channels.mattermost.enabled` 为 `false`）。

聊天模式：

- `oncall`（默认）：仅在被 @提及时响应频道消息。
- `onmessage`：响应每条频道消息。
- `onchar`：当消息以触发前缀开头时响应（`channels.mattermost.oncharPrefixes`，默认 `[">", "!"]`）。

访问控制：

- 默认私聊：`channels.mattermost.dmPolicy="pairing"`（未知发送者收到配对码）。
- 公开私聊：`channels.mattermost.dmPolicy="open"` 加上 `channels.mattermost.allowFrom=["*"]`。
- 群组：`channels.mattermost.groupPolicy="allowlist"` 为默认值（提及门控）。使用 `channels.mattermost.groupAllowFrom` 限制发送者。

多账号支持在 `channels.mattermost.accounts` 下（参见上方多账号部分）。环境变量仅适用于默认账号。
指定投递目标时使用 `channel:<id>` 或 `user:<id>`（或 `@username`）；裸 id 被视为频道 id。

### `channels.signal`（signal-cli）

Signal 反应可以发出系统事件（共享反应工具）：

```json5
{
  channels: {
    signal: {
      reactionNotifications: "own", // off | own | all | allowlist
      reactionAllowlist: ["+15551234567", "uuid:123e4567-e89b-12d3-a456-426614174000"],
      historyLimit: 50, // 包含最近 N 条群消息作为上下文（0 禁用）
    },
  },
}
```

反应通知模式：

- `off`：无反应事件。
- `own`：机器人自身消息上的反应（默认）。
- `all`：所有消息上的所有反应。
- `allowlist`：`channels.signal.reactionAllowlist` 中的用户在所有消息上的反应（空列表禁用）。

### `channels.imessage`（imsg CLI）

OpenClaw 会生成 `imsg rpc`（通过 stdio 的 JSON-RPC）。无需守护进程或端口。

```json5
{
  channels: {
    imessage: {
      enabled: true,
      cliPath: "imsg",
      dbPath: "~/Library/Messages/chat.db",
      remoteHost: "user@gateway-host", // 使用 SSH 包装器时通过 SCP 获取远程附件
      dmPolicy: "pairing", // pairing | allowlist | open | disabled
      allowFrom: ["+15555550123", "user@example.com", "chat_id:123"],
      historyLimit: 50, // 包含最近 N 条群消息作为上下文（0 禁用）
      includeAttachments: false,
      mediaMaxMb: 16,
      service: "auto",
      region: "US",
    },
  },
}
```

多账号支持在 `channels.imessage.accounts` 下（参见上方多账号部分）。

说明：

- 需要对消息数据库的完全磁盘访问权限。
- 首次发送时会提示请求消息自动化权限。
- 建议使用 `chat_id:<id>` 目标。使用 `imsg chats --limit 20` 列出聊天。
- `channels.imessage.cliPath` 可以指向包装脚本（例如 `ssh` 到另一台运行 `imsg rpc` 的 Mac）；使用 SSH 密钥避免密码提示。
- 对于远程 SSH 包装器，设置 `channels.imessage.remoteHost` 以便在启用 `includeAttachments` 时通过 SCP 获取附件。

示例包装器：

```bash
#!/usr/bin/env bash
exec ssh -T gateway-host imsg "$@"
```

### `agents.defaults.workspace`

设置智能体用于文件操作的**单一全局工作区目录**。

默认：`~/.openclaw/workspace`。

```json5
{
  agents: { defaults: { workspace: "~/.openclaw/workspace" } },
}
```

如果启用了 `agents.defaults.sandbox`，非主会话可以在 `agents.defaults.sandbox.workspaceRoot` 下使用各自的每范围工作区来覆盖此设置。

### `agents.defaults.repoRoot`

在系统提示的 Runtime 行中显示的可选仓库根目录。如果未设置，OpenClaw 会从工作区（和当前工作目录）向上查找 `.git` 目录进行检测。路径必须存在才能使用。

```json5
{
  agents: { defaults: { repoRoot: "~/Projects/openclaw" } },
}
```

### `agents.defaults.skipBootstrap`

禁用自动创建工作区引导文件（`AGENTS.md`、`SOUL.md`、`TOOLS.md`、`IDENTITY.md`、`USER.md` 和 `BOOTSTRAP.md`）。

适用于工作区文件来自仓库的预置部署。

```json5
{
  agents: { defaults: { skipBootstrap: true } },
}
```

### `agents.defaults.bootstrapMaxChars`

注入系统提示前每个工作区引导文件截断前的最大字符数。默认：`20000`。

当文件超过此限制时，OpenClaw 会记录警告并注入带标记的头尾截断内容。

```json5
{
  agents: { defaults: { bootstrapMaxChars: 20000 } },
}
```

### `agents.defaults.userTimezone`

设置用户时区用于**系统提示上下文**（不用于消息信封中的时间戳）。如果未设置，OpenClaw 在运行时使用主机时区。

```json5
{
  agents: { defaults: { userTimezone: "America/Chicago" } },
}
```

### `agents.defaults.timeFormat`

控制系统提示中"当前日期和时间"部分显示的**时间格式**。
默认：`auto`（操作系统偏好）。

```json5
{
  agents: { defaults: { timeFormat: "auto" } }, // auto | 12 | 24
}
```

### `messages`

控制入站/出站前缀和可选的确认反应。
参见[消息](/concepts/messages)了解排队、会话和流式上下文。

```json5
{
  messages: {
    responsePrefix: "🦞", // 或 "auto"
    ackReaction: "👀",
    ackReactionScope: "group-mentions",
    removeAckAfterReply: false,
  },
}
```

`responsePrefix` 应用于跨渠道的**所有出站回复**（工具摘要、分块流式传输、最终回复），除非已存在。

如果未设置 `messages.responsePrefix`，默认不应用前缀。WhatsApp 自聊天回复是例外：它们在设置时默认为 `[{identity.name}]`，否则为 `[openclaw]`，以保持同一手机上的对话可读性。
设为 `"auto"` 可为路由的智能体推导 `[{identity.name}]`（当设置时）。

#### 模板变量

`responsePrefix` 字符串可以包含动态解析的模板变量：

| 变量              | 描述           | 示例                        |
| ----------------- | -------------- | --------------------------- |
| `{model}`         | 短模型名称     | `claude-opus-4-5`、`gpt-4o` |
| `{modelFull}`     | 完整模型标识符 | `anthropic/claude-opus-4-5` |
| `{provider}`      | 提供商名称     | `anthropic`、`openai`       |
| `{thinkingLevel}` | 当前思考级别   | `high`、`low`、`off`        |
| `{identity.name}` | 智能体身份名称 | （与 `"auto"` 模式相同）    |

变量不区分大小写（`{MODEL}` = `{model}`）。`{think}` 是 `{thinkingLevel}` 的别名。
未解析的变量保持为字面文本。

```json5
{
  messages: {
    responsePrefix: "[{model} | think:{thinkingLevel}]",
  },
}
```

输出示例：`[claude-opus-4-5 | think:high] Here's my response...`

WhatsApp 入站前缀通过 `channels.whatsapp.messagePrefix` 配置（已弃用：`messages.messagePrefix`）。默认保持**不变**：当 `channels.whatsapp.allowFrom` 为空时为 `"[openclaw]"`，否则为 `""`（无前缀）。使用 `"[openclaw]"` 时，如果路由的智能体设置了 `identity.name`，OpenClaw 会改用 `[{identity.name}]`。

`ackReaction` 在支持反应的渠道（Slack/Discord/Telegram/Google Chat）上发送尽力而为的表情反应来确认入站消息。设置时默认为活跃智能体的 `identity.emoji`，否则为 `"👀"`。设为 `""` 禁用。

`ackReactionScope` 控制反应触发时机：

- `group-mentions`（默认）：仅在群组/房间要求提及**且**机器人被提及时
- `group-all`：所有群组/房间消息
- `direct`：仅私聊消息
- `all`：所有消息

`removeAckAfterReply` 在发送回复后移除机器人的确认反应（仅 Slack/Discord/Telegram/Google Chat）。默认：`false`。

#### `messages.tts`

为出站回复启用文字转语音。开启后，OpenClaw 使用 ElevenLabs 或 OpenAI 生成音频并附加到回复中。Telegram 使用 Opus 语音消息；其他渠道发送 MP3 音频。

```json5
{
  messages: {
    tts: {
      auto: "always", // off | always | inbound | tagged
      mode: "final", // final | all（包含工具/块回复）
      provider: "elevenlabs",
      summaryModel: "openai/gpt-4.1-mini",
      modelOverrides: {
        enabled: true,
      },
      maxTextLength: 4000,
      timeoutMs: 30000,
      prefsPath: "~/.openclaw/settings/tts.json",
      elevenlabs: {
        apiKey: "elevenlabs_api_key",
        baseUrl: "https://api.elevenlabs.io",
        voiceId: "voice_id",
        modelId: "eleven_multilingual_v2",
        seed: 42,
        applyTextNormalization: "auto",
        languageCode: "en",
        voiceSettings: {
          stability: 0.5,
          similarityBoost: 0.75,
          style: 0.0,
          useSpeakerBoost: true,
          speed: 1.0,
        },
      },
      openai: {
        apiKey: "openai_api_key",
        model: "gpt-4o-mini-tts",
        voice: "alloy",
      },
    },
  },
}
```

说明：

- `messages.tts.auto` 控制自动 TTS（`off`、`always`、`inbound`、`tagged`）。
- `/tts off|always|inbound|tagged` 设置每会话的自动模式（覆盖配置）。
- `messages.tts.enabled` 为旧版；doctor 会将其迁移为 `messages.tts.auto`。
- `prefsPath` 存储本地覆盖（提供商/限制/摘要）。
- `maxTextLength` 是 TTS 输入的硬上限；摘要会被截断以适应。
- `summaryModel` 覆盖自动摘要的 `agents.defaults.model.primary`。
  - 接受 `provider/model` 或来自 `agents.defaults.models` 的别名。
- `modelOverrides` 启用模型驱动的覆盖如 `[[tts:...]]` 标签（默认开启）。
- `/tts limit` 和 `/tts summary` 控制每用户的摘要设置。
- `apiKey` 值回退到 `ELEVENLABS_API_KEY`/`XI_API_KEY` 和 `OPENAI_API_KEY`。
- `elevenlabs.baseUrl` 覆盖 ElevenLabs API 基础 URL。
- `elevenlabs.voiceSettings` 支持 `stability`/`similarityBoost`/`style`（0..1）、
  `useSpeakerBoost` 和 `speed`（0.5..2.0）。

### `talk`

Talk 模式（macOS/iOS/Android）的默认值。语音 ID 在未设置时回退到 `ELEVENLABS_VOICE_ID` 或 `SAG_VOICE_ID`。
`apiKey` 在未设置时回退到 `ELEVENLABS_API_KEY`（或 Gateway 网关的 shell 配置文件）。
`voiceAliases` 允许 Talk 指令使用友好名称（例如 `"voice":"Clawd"`）。

```json5
{
  talk: {
    voiceId: "elevenlabs_voice_id",
    voiceAliases: {
      Clawd: "EXAVITQu4vr4xnSDxMaL",
      Roger: "CwhRBWXzGAHq8TQ4Fs17",
    },
    modelId: "eleven_v3",
    outputFormat: "mp3_44100_128",
    apiKey: "elevenlabs_api_key",
    interruptOnSpeech: true,
  },
}
```

### `agents.defaults`

控制内置智能体运行时（模型/思考/详细/超时）。
`agents.defaults.models` 定义已配置的模型目录（也充当 `/model` 的白名单）。
`agents.defaults.model.primary` 设置默认模型；`agents.defaults.model.fallbacks` 是全局故障转移。
`agents.defaults.imageModel` 是可选的，**仅在主模型缺少图像输入时使用**。
每个 `agents.defaults.models` 条目可以包含：

- `alias`（可选的模型快捷方式，例如 `/opus`）。
- `params`（可选的提供商特定 API 参数，传递给模型请求）。

`params` 也应用于流式运行（内置智能体 + 压缩）。目前支持的键：`temperature`、`maxTokens`。这些与调用时选项合并；调用方提供的值优先。`temperature` 是高级旋钮——除非你了解模型的默认值且需要更改，否则不要设置。

示例：

```json5
{
  agents: {
    defaults: {
      models: {
        "anthropic/claude-sonnet-4-5-20250929": {
          params: { temperature: 0.6 },
        },
        "openai/gpt-5.2": {
          params: { maxTokens: 8192 },
        },
      },
    },
  },
}
```

Z.AI GLM-4.x 模型会自动启用思考模式，除非你：

- 设置 `--thinking off`，或
- 自行定义 `agents.defaults.models["zai/<model>"].params.thinking`。

OpenClaw 还内置了一些别名快捷方式。默认值仅在模型已存在于 `agents.defaults.models` 中时才应用：

- `opus` -> `anthropic/claude-opus-4-5`
- `sonnet` -> `anthropic/claude-sonnet-4-5`
- `gpt` -> `openai/gpt-5.2`
- `gpt-mini` -> `openai/gpt-5-mini`
- `gemini` -> `google/gemini-3-pro-preview`
- `gemini-flash` -> `google/gemini-3-flash-preview`

如果你配置了相同的别名（不区分大小写），你的值优先（默认值不会覆盖）。

示例：Opus 4.5 主模型，MiniMax M2.1 回退（托管 MiniMax）：

```json5
{
  agents: {
    defaults: {
      models: {
        "anthropic/claude-opus-4-5": { alias: "opus" },
        "minimax/MiniMax-M2.1": { alias: "minimax" },
      },
      model: {
        primary: "anthropic/claude-opus-4-5",
        fallbacks: ["minimax/MiniMax-M2.1"],
      },
    },
  },
}
```

MiniMax 认证：设置 `MINIMAX_API_KEY`（环境变量）或配置 `models.providers.minimax`。

#### `agents.defaults.cliBackends`（CLI 回退）

可选的 CLI 后端用于纯文本回退运行（无工具调用）。当 API 提供商失败时可作为备用路径。当你配置了接受文件路径的 `imageArg` 时支持图像透传。

说明：

- CLI 后端**以文本为主**；工具始终禁用。
- 设置 `sessionArg` 时支持会话；会话 id 按后端持久化。
- 对于 `claude-cli`，默认值已内置。如果 PATH 不完整（launchd/systemd），请覆盖命令路径。

示例：

```json5
{
  agents: {
    defaults: {
      cliBackends: {
        "claude-cli": {
          command: "/opt/homebrew/bin/claude",
        },
        "my-cli": {
          command: "my-cli",
          args: ["--json"],
          output: "json",
          modelArg: "--model",
          sessionArg: "--session",
          sessionMode: "existing",
          systemPromptArg: "--system",
          systemPromptWhen: "first",
          imageArg: "--image",
          imageMode: "repeat",
        },
      },
    },
  },
}
```

```json5
{
  agents: {
    defaults: {
      models: {
        "anthropic/claude-opus-4-5": { alias: "Opus" },
        "anthropic/claude-sonnet-4-1": { alias: "Sonnet" },
        "openrouter/deepseek/deepseek-r1:free": {},
        "zai/glm-4.7": {
          alias: "GLM",
          params: {
            thinking: {
              type: "enabled",
              clear_thinking: false,
            },
          },
        },
      },
      model: {
        primary: "anthropic/claude-opus-4-5",
        fallbacks: [
          "openrouter/deepseek/deepseek-r1:free",
          "openrouter/meta-llama/llama-3.3-70b-instruct:free",
        ],
      },
      imageModel: {
        primary: "openrouter/qwen/qwen-2.5-vl-72b-instruct:free",
        fallbacks: ["openrouter/google/gemini-2.0-flash-vision:free"],
      },
      thinkingDefault: "low",
      verboseDefault: "off",
      elevatedDefault: "on",
      timeoutSeconds: 600,
      mediaMaxMb: 5,
      heartbeat: {
        every: "30m",
        target: "last",
      },
      maxConcurrent: 3,
      subagents: {
        model: "minimax/MiniMax-M2.1",
        maxConcurrent: 1,
        archiveAfterMinutes: 60,
      },
      exec: {
        backgroundMs: 10000,
        timeoutSec: 1800,
        cleanupMs: 1800000,
      },
      contextTokens: 200000,
    },
  },
}
```

#### `agents.defaults.contextPruning`（工具结果裁剪）

`agents.defaults.contextPruning` 在请求发送到 LLM 之前裁剪内存上下文中的**旧工具结果**。
它**不会**修改磁盘上的会话历史（`*.jsonl` 保持完整）。

这旨在减少随时间积累大量工具输出的智能体的 token 消耗。

概述：

- 不触及用户/助手消息。
- 保护最后 `keepLastAssistants` 条助手消息（该点之后的工具结果不会被裁剪）。
- 保护引导前缀（第一条用户消息之前的内容不会被裁剪）。
- 模式：
  - `adaptive`：当估计的上下文比率超过 `softTrimRatio` 时，软裁剪过大的工具结果（保留头尾）。
    然后当估计的上下文比率超过 `hardClearRatio` **且**有足够的可裁剪工具结果量（`minPrunableToolChars`）时，硬清除最旧的符合条件的工具结果。
  - `aggressive`：始终用 `hardClear.placeholder` 替换截止点之前符合条件的工具结果（不做比率检查）。

软裁剪 vs 硬裁剪（发送给 LLM 的上下文中的变化）：

- **软裁剪**：仅针对*过大*的工具结果。保留开头 + 结尾，在中间插入 `...`。
  - 之前：`toolResult("…很长的输出…")`
  - 之后：`toolResult("HEAD…\n...\n…TAIL\n\n[Tool result trimmed: …]")`
- **硬清除**：用占位符替换整个工具结果。
  - 之前：`toolResult("…很长的输出…")`
  - 之后：`toolResult("[Old tool result content cleared]")`

说明 / 当前限制：

- 目前包含**图像块的工具结果会被跳过**（不会被裁剪/清除）。
- 估计的"上下文比率"基于**字符**（近似值），不是精确的 token 数。
- 如果会话尚未包含至少 `keepLastAssistants` 条助手消息，则跳过裁剪。
- 在 `aggressive` 模式下，`hardClear.enabled` 被忽略（符合条件的工具结果始终被替换为 `hardClear.placeholder`）。

默认值（adaptive）：

```json5
{
  agents: { defaults: { contextPruning: { mode: "adaptive" } } },
}
```

禁用：

```json5
{
  agents: { defaults: { contextPruning: { mode: "off" } } },
}
```

默认值（当 `mode` 为 `"adaptive"` 或 `"aggressive"` 时）：

- `keepLastAssistants`：`3`
- `softTrimRatio`：`0.3`（仅 adaptive）
- `hardClearRatio`：`0.5`（仅 adaptive）
- `minPrunableToolChars`：`50000`（仅 adaptive）
- `softTrim`：`{ maxChars: 4000, headChars: 1500, tailChars: 1500 }`（仅 adaptive）
- `hardClear`：`{ enabled: true, placeholder: "[Old tool result content cleared]" }`

示例（aggressive，最小化）：

```json5
{
  agents: { defaults: { contextPruning: { mode: "aggressive" } } },
}
```

示例（调优的 adaptive）：

```json5
{
  agents: {
    defaults: {
      contextPruning: {
        mode: "adaptive",
        keepLastAssistants: 3,
        softTrimRatio: 0.3,
        hardClearRatio: 0.5,
        minPrunableToolChars: 50000,
        softTrim: { maxChars: 4000, headChars: 1500, tailChars: 1500 },
        hardClear: { enabled: true, placeholder: "[Old tool result content cleared]" },
        // 可选：限制裁剪仅针对特定工具（deny 优先；支持 "*" 通配符）
        tools: { deny: ["browser", "canvas"] },
      },
    },
  },
}
```

参见 [/concepts/session-pruning](/concepts/session-pruning) 了解行为细节。

#### `agents.defaults.compaction`（预留空间 + 记忆刷新）

`agents.defaults.compaction.mode` 选择压缩摘要策略。默认为 `default`；设为 `safeguard` 可为超长历史启用分块摘要。参见 [/concepts/compaction](/concepts/compaction)。

`agents.defaults.compaction.reserveTokensFloor` 为 Pi 压缩强制一个最小 `reserveTokens` 值（默认：`20000`）。设为 `0` 禁用此底线。

`agents.defaults.compaction.memoryFlush` 在自动压缩前运行一个**静默**智能体轮次，指示模型将持久记忆存储到磁盘（例如 `memory/YYYY-MM-DD.md`）。当会话 token 估计值超过压缩限制以下的软阈值时触发。

旧版默认值：

- `memoryFlush.enabled`：`true`
- `memoryFlush.softThresholdTokens`：`4000`
- `memoryFlush.prompt` / `memoryFlush.systemPrompt`：带 `NO_REPLY` 的内置默认值
- 注意：当会话工作区为只读时跳过记忆刷新（`agents.defaults.sandbox.workspaceAccess: "ro"` 或 `"none"`）。

示例（调优）：

```json5
{
  agents: {
    defaults: {
      compaction: {
        mode: "safeguard",
        reserveTokensFloor: 24000,
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 6000,
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with NO_REPLY if nothing to store.",
        },
      },
    },
  },
}
```

分块流式传输：

- `agents.defaults.blockStreamingDefault`：`"on"`/`"off"`（默认 off）。
- 渠道覆盖：`*.blockStreaming`（及每账号变体）强制分块流式传输开/关。
  非 Telegram 渠道需要显式设置 `*.blockStreaming: true` 来启用块回复。
- `agents.defaults.blockStreamingBreak`：`"text_end"` 或 `"message_end"`（默认：text_end）。
- `agents.defaults.blockStreamingChunk`：流式块的软分块。默认 800–1200 字符，优先段落分隔（`\n\n`），然后换行，然后句子。
  示例：
  ```json5
  {
    agents: { defaults: { blockStreamingChunk: { minChars: 800, maxChars: 1200 } } },
  }
  ```
- `agents.defaults.blockStreamingCoalesce`：发送前合并流式块。
  默认为 `{ idleMs: 1000 }`，从 `blockStreamingChunk` 继承 `minChars`，
  `maxChars` 上限为渠道文本限制。Signal/Slack/Discord/Google Chat 默认
  `minChars: 1500`，除非被覆盖。
  渠道覆盖：`channels.whatsapp.blockStreamingCoalesce`、`channels.telegram.blockStreamingCoalesce`、
  `channels.discord.blockStreamingCoalesce`、`channels.slack.blockStreamingCoalesce`、`channels.mattermost.blockStreamingCoalesce`、
  `channels.signal.blockStreamingCoalesce`、`channels.imessage.blockStreamingCoalesce`、`channels.msteams.blockStreamingCoalesce`、
  `channels.googlechat.blockStreamingCoalesce`
  （及每账号变体）。
- `agents.defaults.humanDelay`：第一条之后**块回复**之间的随机延迟。
  模式：`off`（默认）、`natural`（800–2500ms）、`custom`（使用 `minMs`/`maxMs`）。
  每智能体覆盖：`agents.list[].humanDelay`。
  示例：
  ```json5
  {
    agents: { defaults: { humanDelay: { mode: "natural" } } },
  }
  ```
  参见 [/concepts/streaming](/concepts/streaming) 了解行为 + 分块细节。

输入指示器：

- `agents.defaults.typingMode`：`"never" | "instant" | "thinking" | "message"`。私聊/提及默认为
  `instant`，未被提及的群聊默认为 `message`。
- `session.typingMode`：每会话的模式覆盖。
- `agents.defaults.typingIntervalSeconds`：输入信号刷新频率（默认：6s）。
- `session.typingIntervalSeconds`：每会话的刷新间隔覆盖。
  参见 [/concepts/typing-indicators](/concepts/typing-indicators) 了解行为细节。

`agents.defaults.model.primary` 应设为 `provider/model`（例如 `anthropic/claude-opus-4-5`）。
别名来自 `agents.defaults.models.*.alias`（例如 `Opus`）。
如果省略提供商，OpenClaw 目前假定 `anthropic` 作为临时弃用回退。
Z.AI 模型可通过 `zai/<model>` 使用（例如 `zai/glm-4.7`），需要环境中设置
`ZAI_API_KEY`（或旧版 `Z_AI_API_KEY`）。

`agents.defaults.heartbeat` 配置定期心跳运行：

- `every`：持续时间字符串（`ms`、`s`、`m`、`h`）；默认单位分钟。默认：
  `30m`。设为 `0m` 禁用。
- `model`：可选的心跳运行覆盖模型（`provider/model`）。
- `includeReasoning`：为 `true` 时，心跳也会传递单独的 `Reasoning:` 消息（与 `/reasoning on` 相同形式）。默认：`false`。
- `session`：可选的会话键，控制心跳在哪个会话中运行。默认：`main`。
- `to`：可选的收件人覆盖（渠道特定 id，例如 WhatsApp 的 E.164，Telegram 的聊天 id）。
- `target`：可选的投递渠道（`last`、`whatsapp`、`telegram`、`discord`、`slack`、`msteams`、`signal`、`imessage`、`none`）。默认：`last`。
- `prompt`：可选的心跳内容覆盖（默认：`Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.`）。覆盖值按原样发送；如果仍需读取文件，请包含 `Read HEARTBEAT.md` 行。
- `ackMaxChars`：`HEARTBEAT_OK` 之后投递前允许的最大字符数（默认：300）。

每智能体心跳：

- 设置 `agents.list[].heartbeat` 为特定智能体启用或覆盖心跳设置。
- 如果任何智能体条目定义了 `heartbeat`，**仅那些智能体**运行心跳；默认值
  成为那些智能体的共享基线。

心跳运行完整的智能体轮次。较短的间隔消耗更多 token；请注意
`every`，保持 `HEARTBEAT.md` 精简，和/或选择更便宜的 `model`。

`tools.exec` 配置后台执行默认值：

- `backgroundMs`：自动后台化前的时间（ms，默认 10000）
- `timeoutSec`：超过此运行时间后自动终止（秒，默认 1800）
- `cleanupMs`：完成的会话在内存中保留多久（ms，默认 1800000）
- `notifyOnExit`：后台执行退出时加入系统事件 + 请求心跳（默认 true）
- `applyPatch.enabled`：启用实验性 `apply_patch`（仅 OpenAI/OpenAI Codex；默认 false）
- `applyPatch.allowModels`：可选的模型 id 白名单（例如 `gpt-5.2` 或 `openai/gpt-5.2`）
  注意：`applyPatch` 仅在 `tools.exec` 下。

`tools.web` 配置 Web 搜索 + 获取工具：

- `tools.web.search.enabled`（默认：有密钥时为 true）
- `tools.web.search.apiKey`（推荐：通过 `openclaw configure --section web` 设置，或使用 `BRAVE_API_KEY` 环境变量）
- `tools.web.search.maxResults`（1–10，默认 5）
- `tools.web.search.timeoutSeconds`（默认 30）
- `tools.web.search.cacheTtlMinutes`（默认 15）
- `tools.web.fetch.enabled`（默认 true）
- `tools.web.fetch.maxChars`（默认 50000）
- `tools.web.fetch.timeoutSeconds`（默认 30）
- `tools.web.fetch.cacheTtlMinutes`（默认 15）
- `tools.web.fetch.userAgent`（可选覆盖）
- `tools.web.fetch.readability`（默认 true；禁用后仅使用基本 HTML 清理）
- `tools.web.fetch.firecrawl.enabled`（默认：设置了 API 密钥时为 true）
- `tools.web.fetch.firecrawl.apiKey`（可选；默认为 `FIRECRAWL_API_KEY`）
- `tools.web.fetch.firecrawl.baseUrl`（默认 https://api.firecrawl.dev）
- `tools.web.fetch.firecrawl.onlyMainContent`（默认 true）
- `tools.web.fetch.firecrawl.maxAgeMs`（可选）
- `tools.web.fetch.firecrawl.timeoutSeconds`（可选）

`tools.media` 配置入站媒体理解（图片/音频/视频）：

- `tools.media.models`：共享模型列表（按能力标记；在每能力列表之后使用）。
- `tools.media.concurrency`：最大并发能力运行数（默认 2）。
- `tools.media.image` / `tools.media.audio` / `tools.media.video`：
  - `enabled`：选择退出开关（配置了模型时默认为 true）。
  - `prompt`：可选的提示覆盖（图片/视频自动附加 `maxChars` 提示）。
  - `maxChars`：最大输出字符数（图片/视频默认 500；音频未设置）。
  - `maxBytes`：发送的最大媒体大小（默认：图片 10MB，音频 20MB，视频 50MB）。
  - `timeoutSeconds`：请求超时（默认：图片 60s，音频 60s，视频 120s）。
  - `language`：可选的音频提示。
  - `attachments`：附件策略（`mode`、`maxAttachments`、`prefer`）。
  - `scope`：可选的门控（第一个匹配获胜），带 `match.channel`、`match.chatType` 或 `match.keyPrefix`。
  - `models`：有序的模型条目列表；失败或超大媒体回退到下一个条目。
- 每个 `models[]` 条目：
  - 提供商条目（`type: "provider"` 或省略）：
    - `provider`：API 提供商 id（`openai`、`anthropic`、`google`/`gemini`、`groq` 等）。
    - `model`：模型 id 覆盖（图片必需；音频提供商默认为 `gpt-4o-mini-transcribe`/`whisper-large-v3-turbo`，视频默认为 `gemini-3-flash-preview`）。
    - `profile` / `preferredProfile`：认证配置文件选择。
  - CLI 条目（`type: "cli"`）：
    - `command`：要运行的可执行文件。
    - `args`：模板化参数（支持 `{{MediaPath}}`、`{{Prompt}}`、`{{MaxChars}}` 等）。
  - `capabilities`：可选的能力列表（`image`、`audio`、`video`）用于门控共享条目。省略时的默认值：`openai`/`anthropic`/`minimax` → image，`google` → image+audio+video，`groq` → audio。
  - `prompt`、`maxChars`、`maxBytes`、`timeoutSeconds`、`language` 可在每个条目中覆盖。

如果未配置模型（或 `enabled: false`），理解将被跳过；模型仍会接收原始附件。

提供商认证遵循标准模型认证顺序（认证配置文件、环境变量如 `OPENAI_API_KEY`/`GROQ_API_KEY`/`GEMINI_API_KEY`，或 `models.providers.*.apiKey`）。

示例：

```json5
{
  tools: {
    media: {
      audio: {
        enabled: true,
        maxBytes: 20971520,
        scope: {
          default: "deny",
          rules: [{ action: "allow", match: { chatType: "direct" } }],
        },
        models: [
          { provider: "openai", model: "gpt-4o-mini-transcribe" },
          { type: "cli", command: "whisper", args: ["--model", "base", "{{MediaPath}}"] },
        ],
      },
      video: {
        enabled: true,
        maxBytes: 52428800,
        models: [{ provider: "google", model: "gemini-3-flash-preview" }],
      },
    },
  },
}
```

`agents.defaults.subagents` 配置子智能体默认值：

- `model`：生成的子智能体的默认模型（字符串或 `{ primary, fallbacks }`）。如果省略，子智能体继承调用者的模型，除非按智能体或按调用覆盖。
- `maxConcurrent`：最大并发子智能体运行数（默认 1）
- `archiveAfterMinutes`：N 分钟后自动归档子智能体会话（默认 60；设为 `0` 禁用）
- 每子智能体工具策略：`tools.subagents.tools.allow` / `tools.subagents.tools.deny`（deny 优先）

`tools.profile` 设置 `tools.allow`/`tools.deny` 之前的**基础工具白名单**：

- `minimal`：仅 `session_status`
- `coding`：`group:fs`、`group:runtime`、`group:sessions`、`group:memory`、`image`
- `messaging`：`group:messaging`、`sessions_list`、`sessions_history`、`sessions_send`、`session_status`
- `full`：无限制（与未设置相同）

每智能体覆盖：`agents.list[].tools.profile`。

示例（默认仅消息传递，另外允许 Slack + Discord 工具）：

```json5
{
  tools: {
    profile: "messaging",
    allow: ["slack", "discord"],
  },
}
```

示例（编码配置文件，但全局拒绝 exec/process）：

```json5
{
  tools: {
    profile: "coding",
    deny: ["group:runtime"],
  },
}
```

`tools.byProvider` 允许你为特定提供商（或单个 `provider/model`）**进一步限制**工具。
每智能体覆盖：`agents.list[].tools.byProvider`。

顺序：基础配置文件 → 提供商配置文件 → allow/deny 策略。
提供商键接受 `provider`（例如 `google-antigravity`）或 `provider/model`
（例如 `openai/gpt-5.2`）。

示例（保持全局编码配置文件，但为 Google Antigravity 使用最小工具）：

```json5
{
  tools: {
    profile: "coding",
    byProvider: {
      "google-antigravity": { profile: "minimal" },
    },
  },
}
```

示例（提供商/模型特定白名单）：

```json5
{
  tools: {
    allow: ["group:fs", "group:runtime", "sessions_list"],
    byProvider: {
      "openai/gpt-5.2": { allow: ["group:fs", "sessions_list"] },
    },
  },
}
```

`tools.allow` / `tools.deny` 配置全局工具允许/拒绝策略（deny 优先）。
匹配不区分大小写并支持 `*` 通配符（`"*"` 表示所有工具）。
即使 Docker 沙箱**关闭**，此策略也会应用。

示例（全局禁用 browser/canvas）：

```json5
{
  tools: { deny: ["browser", "canvas"] },
}
```

工具组（简写）在**全局**和**每智能体**工具策略中可用：

- `group:runtime`：`exec`、`bash`、`process`
- `group:fs`：`read`、`write`、`edit`、`apply_patch`
- `group:sessions`：`sessions_list`、`sessions_history`、`sessions_send`、`sessions_spawn`、`session_status`
- `group:memory`：`memory_search`、`memory_get`
- `group:web`：`web_search`、`web_fetch`
- `group:ui`：`browser`、`canvas`
- `group:automation`：`cron`、`gateway`
- `group:messaging`：`message`
- `group:nodes`：`nodes`
- `group:openclaw`：所有内置 OpenClaw 工具（不包含提供商插件）

`tools.elevated` 控制提升（主机）执行访问：

- `enabled`：允许提升模式（默认 true）
- `allowFrom`：每渠道白名单（空 = 禁用）
  - `whatsapp`：E.164 号码
  - `telegram`：聊天 id 或用户名
  - `discord`：用户 id 或用户名（省略时回退到 `channels.discord.dm.allowFrom`）
  - `signal`：E.164 号码
  - `imessage`：句柄/聊天 id
  - `webchat`：会话 id 或用户名

示例：

```json5
{
  tools: {
    elevated: {
      enabled: true,
      allowFrom: {
        whatsapp: ["+15555550123"],
        discord: ["steipete", "1234567890123"],
      },
    },
  },
}
```

每智能体覆盖（进一步限制）：

```json5
{
  agents: {
    list: [
      {
        id: "family",
        tools: {
          elevated: { enabled: false },
        },
      },
    ],
  },
}
```

说明：

- `tools.elevated` 是全局基线。`agents.list[].tools.elevated` 只能进一步限制（两者都必须允许）。
- `/elevated on|off|ask|full` 按会话键存储状态；内联指令仅应用于单条消息。
- 提升的 `exec` 在主机上运行并绕过沙箱。
- 工具策略仍然适用；如果 `exec` 被拒绝，则无法使用提升。

`agents.defaults.maxConcurrent` 设置跨会话可并行执行的内置智能体运行的最大数量。每个会话仍然是串行的（每个会话键同时只有一个运行）。默认：1。

### `agents.defaults.sandbox`

为内置智能体提供可选的 **Docker 沙箱**。适用于非主会话，使其无法访问你的主机系统。

详情：[沙箱](/gateway/sandboxing)

默认值（如果启用）：

- scope：`"agent"`（每个智能体一个容器 + 工作区）
- 基于 Debian bookworm-slim 的镜像
- 智能体工作区访问：`workspaceAccess: "none"`（默认）
  - `"none"`：在 `~/.openclaw/sandboxes` 下使用每范围的沙箱工作区
- `"ro"`：将沙箱工作区保持在 `/workspace`，智能体工作区以只读方式挂载到 `/agent`（禁用 `write`/`edit`/`apply_patch`）
  - `"rw"`：将智能体工作区以读写方式挂载到 `/workspace`
- 自动清理：空闲超过 24h 或存在超过 7d
- 工具策略：仅允许 `exec`、`process`、`read`、`write`、`edit`、`apply_patch`、`sessions_list`、`sessions_history`、`sessions_send`、`sessions_spawn`、`session_status`（deny 优先）
  - 通过 `tools.sandbox.tools` 配置，通过 `agents.list[].tools.sandbox.tools` 进行每智能体覆盖
  - 沙箱策略中支持工具组简写：`group:runtime`、`group:fs`、`group:sessions`、`group:memory`（参见[沙箱 vs 工具策略 vs 提升](/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands)）
- 可选的沙箱浏览器（Chromium + CDP，noVNC 观察器）
- 加固旋钮：`network`、`user`、`pidsLimit`、`memory`、`cpus`、`ulimits`、`seccompProfile`、`apparmorProfile`

警告：`scope: "shared"` 意味着共享容器和共享工作区。无跨会话隔离。使用 `scope: "session"` 获得每会话隔离。

旧版：`perSession` 仍然支持（`true` → `scope: "session"`，`false` → `scope: "shared"`）。

`setupCommand` 在容器创建后**运行一次**（在容器内通过 `sh -lc` 执行）。
对于包安装，确保网络出口、可写根文件系统和 root 用户。

```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main", // off | non-main | all
        scope: "agent", // session | agent | shared（agent 为默认）
        workspaceAccess: "none", // none | ro | rw
        workspaceRoot: "~/.openclaw/sandboxes",
        docker: {
          image: "openclaw-sandbox:bookworm-slim",
          containerPrefix: "openclaw-sbx-",
          workdir: "/workspace",
          readOnlyRoot: true,
          tmpfs: ["/tmp", "/var/tmp", "/run"],
          network: "none",
          user: "1000:1000",
          capDrop: ["ALL"],
          env: { LANG: "C.UTF-8" },
          setupCommand: "apt-get update && apt-get install -y git curl jq",
          // 每智能体覆盖（多智能体）：agents.list[].sandbox.docker.*
          pidsLimit: 256,
          memory: "1g",
          memorySwap: "2g",
          cpus: 1,
          ulimits: {
            nofile: { soft: 1024, hard: 2048 },
            nproc: 256,
          },
          seccompProfile: "/path/to/seccomp.json",
          apparmorProfile: "openclaw-sandbox",
          dns: ["1.1.1.1", "8.8.8.8"],
          extraHosts: ["internal.service:10.0.0.5"],
          binds: ["/var/run/docker.sock:/var/run/docker.sock", "/home/user/source:/source:rw"],
        },
        browser: {
          enabled: false,
          image: "openclaw-sandbox-browser:bookworm-slim",
          containerPrefix: "openclaw-sbx-browser-",
          cdpPort: 9222,
          vncPort: 5900,
          noVncPort: 6080,
          headless: false,
          enableNoVnc: true,
          allowHostControl: false,
          allowedControlUrls: ["http://10.0.0.42:18791"],
          allowedControlHosts: ["browser.lab.local", "10.0.0.42"],
          allowedControlPorts: [18791],
          autoStart: true,
          autoStartTimeoutMs: 12000,
        },
        prune: {
          idleHours: 24, // 0 禁用空闲清理
          maxAgeDays: 7, // 0 禁用最大存活时间清理
        },
      },
    },
  },
  tools: {
    sandbox: {
      tools: {
        allow: [
          "exec",
          "process",
          "read",
          "write",
          "edit",
          "apply_patch",
          "sessions_list",
          "sessions_history",
          "sessions_send",
          "sessions_spawn",
          "session_status",
        ],
        deny: ["browser", "canvas", "nodes", "cron", "discord", "gateway"],
      },
    },
  },
}
```

首次构建默认沙箱镜像：

```bash
scripts/sandbox-setup.sh
```

注意：沙箱容器默认为 `network: "none"`；如果智能体需要出站访问，请将 `agents.defaults.sandbox.docker.network` 设为 `"bridge"`（或你的自定义网络）。

注意：入站附件会暂存到活跃工作区的 `media/inbound/*` 中。使用 `workspaceAccess: "rw"` 时，文件会写入智能体工作区。

注意：`docker.binds` 挂载额外的主机目录；全局和每智能体的 binds 会合并。

构建可选的浏览器镜像：

```bash
scripts/sandbox-browser-setup.sh
```

当 `agents.defaults.sandbox.browser.enabled=true` 时，浏览器工具使用沙箱化的
Chromium 实例（CDP）。如果启用了 noVNC（headless=false 时默认启用），
noVNC URL 会注入系统提示中，以便智能体可以引用它。
这不需要主配置中的 `browser.enabled`；沙箱控制 URL 按会话注入。

`agents.defaults.sandbox.browser.allowHostControl`（默认：false）允许
沙箱会话通过浏览器工具显式访问**主机**浏览器控制服务器
（`target: "host"`）。如果你需要严格的沙箱隔离，请保持关闭。

远程控制白名单：

- `allowedControlUrls`：`target: "custom"` 允许的精确控制 URL。
- `allowedControlHosts`：允许的主机名（仅主机名，无端口）。
- `allowedControlPorts`：允许的端口（默认：http=80，https=443）。
  默认：所有白名单未设置（无限制）。`allowHostControl` 默认为 false。

### `models`（自定义提供商 + 基础 URL）

OpenClaw 使用 **pi-coding-agent** 模型目录。你可以通过编写
`~/.openclaw/agents/<agentId>/agent/models.json` 或在 OpenClaw 配置中的 `models.providers` 下定义相同的 schema 来添加自定义提供商（LiteLLM、本地 OpenAI 兼容服务器、Anthropic 代理等）。
按提供商的概述 + 示例：[/concepts/model-providers](/concepts/model-providers)。

当存在 `models.providers` 时，OpenClaw 在启动时将 `models.json` 写入/合并到
`~/.openclaw/agents/<agentId>/agent/`：

- 默认行为：**合并**（保留现有提供商，按名称覆盖）
- 设为 `models.mode: "replace"` 覆盖文件内容

通过 `agents.defaults.model.primary`（provider/model）选择模型。

```json5
{
  agents: {
    defaults: {
      model: { primary: "custom-proxy/llama-3.1-8b" },
      models: {
        "custom-proxy/llama-3.1-8b": {},
      },
    },
  },
  models: {
    mode: "merge",
    providers: {
      "custom-proxy": {
        baseUrl: "http://localhost:4000/v1",
        apiKey: "LITELLM_KEY",
        api: "openai-completions",
        models: [
          {
            id: "llama-3.1-8b",
            name: "Llama 3.1 8B",
            reasoning: false,
            input: ["text"],
            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
            contextWindow: 128000,
            maxTokens: 32000,
          },
        ],
      },
    },
  },
}
```

### OpenCode Zen（多模型代理）

OpenCode Zen 是一个具有每模型端点的多模型网关。OpenClaw 使用
pi-ai 内置的 `opencode` 提供商；从 https://opencode.ai/auth 设置 `OPENCODE_API_KEY`（或
`OPENCODE_ZEN_API_KEY`）。

说明：

- 模型引用使用 `opencode/<modelId>`（示例：`opencode/claude-opus-4-5`）。
- 如果你通过 `agents.defaults.models` 启用白名单，请添加你计划使用的每个模型。
- 快捷方式：`openclaw onboard --auth-choice opencode-zen`。

```json5
{
  agents: {
    defaults: {
      model: { primary: "opencode/claude-opus-4-5" },
      models: { "opencode/claude-opus-4-5": { alias: "Opus" } },
    },
  },
}
```

### Z.AI（GLM-4.7）— 提供商别名支持

Z.AI 模型通过内置的 `zai` 提供商提供。在环境中设置 `ZAI_API_KEY`
并通过 provider/model 引用模型。

快捷方式：`openclaw onboard --auth-choice zai-api-key`。

```json5
{
  agents: {
    defaults: {
      model: { primary: "zai/glm-4.7" },
      models: { "zai/glm-4.7": {} },
    },
  },
}
```

说明：

- `z.ai/*` 和 `z-ai/*` 是接受的别名，规范化为 `zai/*`。
- 如果缺少 `ZAI_API_KEY`，对 `zai/*` 的请求将在运行时因认证错误失败。
- 示例错误：`No API key found for provider "zai".`
- Z.AI 的通用 API 端点是 `https://api.z.ai/api/paas/v4`。GLM 编码
  请求使用专用编码端点 `https://api.z.ai/api/coding/paas/v4`。
  内置的 `zai` 提供商使用编码端点。如果你需要通用
  端点，请在 `models.providers` 中定义自定义提供商并覆盖基础 URL
  （参见上方自定义提供商部分）。
- 在文档/配置中使用假占位符；切勿提交真实 API 密钥。

### Moonshot AI（Kimi）

使用 Moonshot 的 OpenAI 兼容端点：

```json5
{
  env: { MOONSHOT_API_KEY: "sk-..." },
  agents: {
    defaults: {
      model: { primary: "moonshot/kimi-k2.5" },
      models: { "moonshot/kimi-k2.5": { alias: "Kimi K2.5" } },
    },
  },
  models: {
    mode: "merge",
    providers: {
      moonshot: {
        baseUrl: "https://api.moonshot.ai/v1",
        apiKey: "${MOONSHOT_API_KEY}",
        api: "openai-completions",
        models: [
          {
            id: "kimi-k2.5",
            name: "Kimi K2.5",
            reasoning: false,
            input: ["text"],
            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
            contextWindow: 256000,
            maxTokens: 8192,
          },
        ],
      },
    },
  },
}
```

说明：

- 在环境中设置 `MOONSHOT_API_KEY` 或使用 `openclaw onboard --auth-choice moonshot-api-key`。
- 模型引用：`moonshot/kimi-k2.5`。
- 如需中国端点，使用 `https://api.moonshot.cn/v1`。

### Kimi Coding

使用 Moonshot AI 的 Kimi Coding 端点（Anthropic 兼容，内置提供商）：

```json5
{
  env: { KIMI_API_KEY: "sk-..." },
  agents: {
    defaults: {
      model: { primary: "kimi-coding/k2p5" },
      models: { "kimi-coding/k2p5": { alias: "Kimi K2.5" } },
    },
  },
}
```

说明：

- 在环境中设置 `KIMI_API_KEY` 或使用 `openclaw onboard --auth-choice kimi-code-api-key`。
- 模型引用：`kimi-coding/k2p5`。

### Synthetic（Anthropic 兼容）

使用 Synthetic 的 Anthropic 兼容端点：

```json5
{
  env: { SYNTHETIC_API_KEY: "sk-..." },
  agents: {
    defaults: {
      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.1" },
      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.1": { alias: "MiniMax M2.1" } },
    },
  },
  models: {
    mode: "merge",
    providers: {
      synthetic: {
        baseUrl: "https://api.synthetic.new/anthropic",
        apiKey: "${SYNTHETIC_API_KEY}",
        api: "anthropic-messages",
        models: [
          {
            id: "hf:MiniMaxAI/MiniMax-M2.1",
            name: "MiniMax M2.1",
            reasoning: false,
            input: ["text"],
            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
            contextWindow: 192000,
            maxTokens: 65536,
          },
        ],
      },
    },
  },
}
```

说明：

- 设置 `SYNTHETIC_API_KEY` 或使用 `openclaw onboard --auth-choice synthetic-api-key`。
- 模型引用：`synthetic/hf:MiniMaxAI/MiniMax-M2.1`。
- 基础 URL 应省略 `/v1`，因为 Anthropic 客户端会自动附加。

### 本地模型（LM Studio）— 推荐设置

参见 [/gateway/local-models](/gateway/local-models) 了解当前本地指南。简而言之：在高性能硬件上通过 LM Studio Responses API 运行 MiniMax M2.1；保留托管模型合并作为回退。

### MiniMax M2.1

不通过 LM Studio 直接使用 MiniMax M2.1：

```json5
{
  agent: {
    model: { primary: "minimax/MiniMax-M2.1" },
    models: {
      "anthropic/claude-opus-4-5": { alias: "Opus" },
      "minimax/MiniMax-M2.1": { alias: "Minimax" },
    },
  },
  models: {
    mode: "merge",
    providers: {
      minimax: {
        baseUrl: "https://api.minimax.io/anthropic",
        apiKey: "${MINIMAX_API_KEY}",
        api: "anthropic-messages",
        models: [
          {
            id: "MiniMax-M2.1",
            name: "MiniMax M2.1",
            reasoning: false,
            input: ["text"],
            // 定价：如需精确费用跟踪，请在 models.json 中更新。
            cost: { input: 15, output: 60, cacheRead: 2, cacheWrite: 10 },
            contextWindow: 200000,
            maxTokens: 8192,
          },
        ],
      },
    },
  },
}
```

说明：

- 设置 `MINIMAX_API_KEY` 环境变量或使用 `openclaw onboard --auth-choice minimax-api`。
- 可用模型：`MiniMax-M2.1`（默认）。
- 如需精确费用跟踪，请在 `models.json` 中更新定价。

### Cerebras（GLM 4.6 / 4.7）

通过 Cerebras 的 OpenAI 兼容端点使用：

```json5
{
  env: { CEREBRAS_API_KEY: "sk-..." },
  agents: {
    defaults: {
      model: {
        primary: "cerebras/zai-glm-4.7",
        fallbacks: ["cerebras/zai-glm-4.6"],
      },
      models: {
        "cerebras/zai-glm-4.7": { alias: "GLM 4.7 (Cerebras)" },
        "cerebras/zai-glm-4.6": { alias: "GLM 4.6 (Cerebras)" },
      },
    },
  },
  models: {
    mode: "merge",
    providers: {
      cerebras: {
        baseUrl: "https://api.cerebras.ai/v1",
        apiKey: "${CEREBRAS_API_KEY}",
        api: "openai-completions",
        models: [
          { id: "zai-glm-4.7", name: "GLM 4.7 (Cerebras)" },
          { id: "zai-glm-4.6", name: "GLM 4.6 (Cerebras)" },
        ],
      },
    },
  },
}
```

说明：

- Cerebras 使用 `cerebras/zai-glm-4.7`；Z.AI 直连使用 `zai/glm-4.7`。
- 在环境或配置中设置 `CEREBRAS_API_KEY`。

说明：

- 支持的 API：`openai-completions`、`openai-responses`、`anthropic-messages`、
  `google-generative-ai`
- 对于自定义认证需求使用 `authHeader: true` + `headers`。
- 如果你希望 `models.json` 存储在其他位置，请使用 `OPENCLAW_AGENT_DIR`（或 `PI_CODING_AGENT_DIR`）覆盖智能体配置根目录（默认：`~/.openclaw/agents/main/agent`）。

### `session`

控制会话作用域、重置策略、重置触发器以及会话存储的写入位置。

```json5
{
  session: {
    scope: "per-sender",
    dmScope: "main",
    identityLinks: {
      alice: ["telegram:123456789", "discord:987654321012345678"],
    },
    reset: {
      mode: "daily",
      atHour: 4,
      idleMinutes: 60,
    },
    resetByType: {
      thread: { mode: "daily", atHour: 4 },
      dm: { mode: "idle", idleMinutes: 240 },
      group: { mode: "idle", idleMinutes: 120 },
    },
    resetTriggers: ["/new", "/reset"],
    // 默认已按智能体存储在 ~/.openclaw/agents/<agentId>/sessions/sessions.json
    // 你可以使用 {agentId} 模板进行覆盖：
    store: "~/.openclaw/agents/{agentId}/sessions/sessions.json",
    // 私聊折叠到 agent:<agentId>:<mainKey>（默认："main"）。
    mainKey: "main",
    agentToAgent: {
      // 请求者/目标之间的最大乒乓回复轮次（0–5）。
      maxPingPongTurns: 5,
    },
    sendPolicy: {
      rules: [{ action: "deny", match: { channel: "discord", chatType: "group" } }],
      default: "allow",
    },
  },
}
```

字段：

- `mainKey`：私聊桶键（默认：`"main"`）。当你想"重命名"主私聊线程而不更改 `agentId` 时有用。
  - 沙箱说明：`agents.defaults.sandbox.mode: "non-main"` 使用此键检测主会话。任何不匹配 `mainKey` 的会话键（群组/频道）都会被沙箱化。
- `dmScope`：私聊会话如何分组（默认：`"main"`）。
  - `main`：所有私聊共享主会话以保持连续性。
  - `per-peer`：按发送者 id 跨渠道隔离私聊。
  - `per-channel-peer`：按渠道 + 发送者隔离私聊（推荐用于多用户收件箱）。
  - `per-account-channel-peer`：按账号 + 渠道 + 发送者隔离私聊（推荐用于多账号收件箱）。
- `identityLinks`：将规范 id 映射到提供商前缀的对等方，以便在使用 `per-peer`、`per-channel-peer` 或 `per-account-channel-peer` 时同一人跨渠道共享私聊会话。
  - 示例：`alice: ["telegram:123456789", "discord:987654321012345678"]`。
- `reset`：主重置策略。默认为 Gateway 网关主机上本地时间凌晨 4:00 每日重置。
  - `mode`：`daily` 或 `idle`（当存在 `reset` 时默认：`daily`）。
  - `atHour`：本地小时（0-23）作为每日重置边界。
  - `idleMinutes`：滑动空闲窗口（分钟）。当 daily + idle 都配置时，先到期的获胜。
- `resetByType`：`dm`、`group` 和 `thread` 的每会话覆盖。
  - 如果你只设置了旧版 `session.idleMinutes` 而没有任何 `reset`/`resetByType`，OpenClaw 保持仅空闲模式以向后兼容。
- `heartbeatIdleMinutes`：可选的心跳检查空闲覆盖（启用时每日重置仍然适用）。
- `agentToAgent.maxPingPongTurns`：请求者/目标之间的最大回复轮次（0–5，默认 5）。
- `sendPolicy.default`：无规则匹配时的 `allow` 或 `deny` 回退。
- `sendPolicy.rules[]`：按 `channel`、`chatType`（`direct|group|room`）或 `keyPrefix`（例如 `cron:`）匹配。第一个 deny 获胜；否则 allow。

### `skills`（Skills 配置）

控制内置白名单、安装偏好、额外 Skills 文件夹和每 Skills 覆盖。适用于**内置**Skills 和 `~/.openclaw/skills`（工作区 Skills 在名称冲突时仍然优先）。

字段：

- `allowBundled`：可选的**仅内置**Skills 白名单。如果设置，仅那些内置 Skills 符合条件（管理/工作区 Skills 不受影响）。
- `load.extraDirs`：额外要扫描的 Skills 目录（最低优先级）。
- `install.preferBrew`：可用时优先使用 brew 安装程序（默认：true）。
- `install.nodeManager`：node 安装偏好（`npm` | `pnpm` | `yarn`，默认：npm）。
- `entries.<skillKey>`：每 Skills 配置覆盖。

每 Skills 字段：

- `enabled`：设为 `false` 禁用 Skills，即使它是内置/已安装的。
- `env`：为智能体运行注入的环境变量（仅在尚未设置时）。
- `apiKey`：对于声明了主环境变量的 Skills 的可选便利字段（例如 `nano-banana-pro` → `GEMINI_API_KEY`）。

示例：

```json5
{
  skills: {
    allowBundled: ["gemini", "peekaboo"],
    load: {
      extraDirs: ["~/Projects/agent-scripts/skills", "~/Projects/oss/some-skill-pack/skills"],
    },
    install: {
      preferBrew: true,
      nodeManager: "npm",
    },
    entries: {
      "nano-banana-pro": {
        apiKey: "GEMINI_KEY_HERE",
        env: {
          GEMINI_API_KEY: "GEMINI_KEY_HERE",
        },
      },
      peekaboo: { enabled: true },
      sag: { enabled: false },
    },
  },
}
```

### `plugins`（扩展）

控制插件发现、允许/拒绝和每插件配置。插件从 `~/.openclaw/extensions`、`<workspace>/.openclaw/extensions` 以及任何 `plugins.load.paths` 条目加载。**配置更改需要重启 Gateway 网关。**
参见 [/plugin](/tools/plugin) 了解详情。

字段：

- `enabled`：插件加载的主开关（默认：true）。
- `allow`：可选的插件 id 白名单；设置后仅加载列出的插件。
- `deny`：可选的插件 id 拒绝列表（deny 优先）。
- `load.paths`：要加载的额外插件文件或目录（绝对路径或 `~`）。
- `entries.<pluginId>`：每插件覆盖。
  - `enabled`：设为 `false` 禁用。
  - `config`：插件特定的配置对象（如果提供，由插件验证）。

示例：

```json5
{
  plugins: {
    enabled: true,
    allow: ["voice-call"],
    load: {
      paths: ["~/Projects/oss/voice-call-extension"],
    },
    entries: {
      "voice-call": {
        enabled: true,
        config: {
          provider: "twilio",
        },
      },
    },
  },
}
```

### `browser`（OpenClaw 管理的浏览器）

OpenClaw 可以为 OpenClaw 启动一个**专用、隔离的** Chrome/Brave/Edge/Chromium 实例并暴露一个小型 local loopback 控制服务。
配置文件可以通过 `profiles.<name>.cdpUrl` 指向**远程** Chromium 浏览器。远程配置文件为仅附加模式（start/stop/reset 被禁用）。

`browser.cdpUrl` 保留用于旧版单配置文件配置，以及作为仅设置 `cdpPort` 的配置文件的基础 scheme/host。

默认值：

- enabled：`true`
- evaluateEnabled：`true`（设为 `false` 禁用 `act:evaluate` 和 `wait --fn`）
- 控制服务：仅 local loopback（端口从 `gateway.port` 派生，默认 `18791`）
- CDP URL：`http://127.0.0.1:18792`（控制服务 + 1，旧版单配置文件）
- 配置文件颜色：`#FF4500`（龙虾橙）
- 注意：控制服务器由运行中的 Gateway 网关（OpenClaw.app 菜单栏或 `openclaw gateway`）启动。
- 自动检测顺序：如果为 Chromium 内核则使用默认浏览器；否则 Chrome → Brave → Edge → Chromium → Chrome Canary。

```json5
{
  browser: {
    enabled: true,
    evaluateEnabled: true,
    // cdpUrl: "http://127.0.0.1:18792", // 旧版单配置文件覆盖
    defaultProfile: "chrome",
    profiles: {
      openclaw: { cdpPort: 18800, color: "#FF4500" },
      work: { cdpPort: 18801, color: "#0066CC" },
      remote: { cdpUrl: "http://10.0.0.42:9222", color: "#00AA00" },
    },
    color: "#FF4500",
    // 高级：
    // headless: false,
    // noSandbox: false,
    // executablePath: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    // attachOnly: false, // 将远程 CDP 隧道到 localhost 时设为 true
  },
}
```

### `ui`（外观）

原生应用用于 UI 外观的可选强调色（例如 Talk 模式气泡着色）。

如果未设置，客户端回退到柔和的浅蓝色。

```json5
{
  ui: {
    seamColor: "#FF4500", // 十六进制（RRGGBB 或 #RRGGBB）
    // 可选：控制台 UI 助手身份覆盖。
    // 如果未设置，控制台 UI 使用活跃智能体的身份（配置或 IDENTITY.md）。
    assistant: {
      name: "OpenClaw",
      avatar: "CB", // 表情、短文本，或图片 URL/data URI
    },
  },
}
```

### `gateway`（Gateway 网关服务器模式 + 绑定）

使用 `gateway.mode` 明确声明此机器是否应运行 Gateway 网关。

默认值：

- mode：**未设置**（视为"不自动启动"）
- bind：`loopback`
- port：`18789`（WS + HTTP 单端口）

```json5
{
  gateway: {
    mode: "local", // 或 "remote"
    port: 18789, // WS + HTTP 多路复用
    bind: "loopback",
    // controlUi: { enabled: true, basePath: "/openclaw" }
    // auth: { mode: "token", token: "your-token" } // token 控制 WS + 控制台 UI 访问
    // tailscale: { mode: "off" | "serve" | "funnel" }
  },
}
```

控制台 UI 基础路径：

- `gateway.controlUi.basePath` 设置控制台 UI 提供服务的 URL 前缀。
- 示例：`"/ui"`、`"/openclaw"`、`"/apps/openclaw"`。
- 默认：根路径（`/`）（不变）。
- `gateway.controlUi.root` 设置控制台 UI 资产的文件系统根目录（默认：`dist/control-ui`）。
- `gateway.controlUi.allowInsecureAuth` 允许在省略设备身份时对控制台 UI 进行仅 token 认证（通常通过 HTTP）。默认：`false`。建议使用 HTTPS（Tailscale Serve）或 `127.0.0.1`。
- `gateway.controlUi.dangerouslyDisableDeviceAuth` 禁用控制台 UI 的设备身份检查（仅 token/密码）。默认：`false`。仅用于紧急情况。

相关文档：

- [控制台 UI](/web/control-ui)
- [Web 概述](/web)
- [Tailscale](/gateway/tailscale)
- [远程访问](/gateway/remote)

信任的代理：

- `gateway.trustedProxies`：在 Gateway 网关前面终止 TLS 的反向代理 IP 列表。
- 当连接来自这些 IP 之一时，OpenClaw 使用 `x-forwarded-for`（或 `x-real-ip`）来确定客户端 IP，用于本地配对检查和 HTTP 认证/本地检查。
- 仅列出你完全控制的代理，并确保它们**覆盖**传入的 `x-forwarded-for`。

说明：

- `openclaw gateway` 拒绝启动，除非 `gateway.mode` 设为 `local`（或你传递了覆盖标志）。
- `gateway.port` 控制用于 WebSocket + HTTP（控制台 UI、hooks、A2UI）的单一多路复用端口。
- OpenAI Chat Completions 端点：**默认禁用**；通过 `gateway.http.endpoints.chatCompletions.enabled: true` 启用。
- 优先级：`--port` > `OPENCLAW_GATEWAY_PORT` > `gateway.port` > 默认 `18789`。
- 默认需要 Gateway 网关认证（token/密码或 Tailscale Serve 身份）。非 local loopback 绑定需要共享 token/密码。
- 新手引导向导默认生成 gateway token（即使在 local loopback 上）。
- `gateway.remote.token` **仅**用于远程 CLI 调用；它不启用本地 gateway 认证。`gateway.token` 被忽略。

认证和 Tailscale：

- `gateway.auth.mode` 设置握手要求（`token` 或 `password`）。未设置时，假定 token 认证。
- `gateway.auth.token` 存储 token 认证的共享 token（同一机器上的 CLI 使用）。
- 当设置了 `gateway.auth.mode` 时，仅接受该方法（加上可选的 Tailscale 头部）。
- `gateway.auth.password` 可在此设置，或通过 `OPENCLAW_GATEWAY_PASSWORD`（推荐）。
- `gateway.auth.allowTailscale` 允许 Tailscale Serve 身份头部
  （`tailscale-user-login`）在请求通过 local loopback 到达且带有 `x-forwarded-for`、
  `x-forwarded-proto` 和 `x-forwarded-host` 时满足认证。OpenClaw 在接受之前
  通过 `tailscale whois` 解析 `x-forwarded-for` 地址来验证身份。为 `true` 时，
  Serve 请求不需要 token/密码；设为 `false` 要求显式凭据。当
  `tailscale.mode = "serve"` 且认证模式不是 `password` 时默认为 `true`。
- `gateway.tailscale.mode: "serve"` 使用 Tailscale Serve（仅 tailnet，local loopback 绑定）。
- `gateway.tailscale.mode: "funnel"` 公开暴露仪表板；需要认证。
- `gateway.tailscale.resetOnExit` 在关闭时重置 Serve/Funnel 配置。

远程客户端默认值（CLI）：

- `gateway.remote.url` 设置 `gateway.mode = "remote"` 时 CLI 调用的默认 Gateway 网关 WebSocket URL。
- `gateway.remote.transport` 选择 macOS 远程传输（`ssh` 默认，`direct` 用于 ws/wss）。使用 `direct` 时，`gateway.remote.url` 必须为 `ws://` 或 `wss://`。`ws://host` 默认端口 `18789`。
- `gateway.remote.token` 提供远程调用的 token（不需要认证时留空）。
- `gateway.remote.password` 提供远程调用的密码（不需要认证时留空）。

macOS 应用行为：

- OpenClaw.app 监视 `~/.openclaw/openclaw.json`，当 `gateway.mode` 或 `gateway.remote.url` 变更时实时切换模式。
- 如果 `gateway.mode` 未设置但 `gateway.remote.url` 已设置，macOS 应用将其视为远程模式。
- 当你在 macOS 应用中更改连接模式时，它会将 `gateway.mode`（以及远程模式下的 `gateway.remote.url` + `gateway.remote.transport`）写回配置文件。

```json5
{
  gateway: {
    mode: "remote",
    remote: {
      url: "ws://gateway.tailnet:18789",
      token: "your-token",
      password: "your-password",
    },
  },
}
```

直连传输示例（macOS 应用）：

```json5
{
  gateway: {
    mode: "remote",
    remote: {
      transport: "direct",
      url: "wss://gateway.example.ts.net",
      token: "your-token",
    },
  },
}
```

### `gateway.reload`（配置热重载）

Gateway 网关监视 `~/.openclaw/openclaw.json`（或 `OPENCLAW_CONFIG_PATH`）并自动应用更改。

模式：

- `hybrid`（默认）：安全更改热应用；关键更改重启 Gateway 网关。
- `hot`：仅应用热安全更改；需要重启时记录日志。
- `restart`：任何配置更改都重启 Gateway 网关。
- `off`：禁用热重载。

```json5
{
  gateway: {
    reload: {
      mode: "hybrid",
      debounceMs: 300,
    },
  },
}
```

#### 热重载矩阵（文件 + 影响）

监视的文件：

- `~/.openclaw/openclaw.json`（或 `OPENCLAW_CONFIG_PATH`）

热应用（无需完全重启 Gateway 网关）：

- `hooks`（webhook 认证/路径/映射）+ `hooks.gmail`（Gmail 监视器重启）
- `browser`（浏览器控制服务器重启）
- `cron`（cron 服务重启 + 并发更新）
- `agents.defaults.heartbeat`（心跳运行器重启）
- `web`（WhatsApp Web 渠道重启）
- `telegram`、`discord`、`signal`、`imessage`（渠道重启）
- `agent`、`models`、`routing`、`messages`、`session`、`whatsapp`、`logging`、`skills`、`ui`、`talk`、`identity`、`wizard`（动态读取）

需要完全重启 Gateway 网关：

- `gateway`（端口/绑定/认证/控制台 UI/tailscale）
- `bridge`（旧版）
- `discovery`
- `canvasHost`
- `plugins`
- 任何未知/不支持的配置路径（为安全默认重启）

### 多实例隔离

要在一台主机上运行多个 Gateway 网关（用于冗余或救援机器人），请隔离每个实例的状态 + 配置并使用唯一端口：

- `OPENCLAW_CONFIG_PATH`（每实例配置）
- `OPENCLAW_STATE_DIR`（会话/凭据）
- `agents.defaults.workspace`（记忆）
- `gateway.port`（每实例唯一）

便利标志（CLI）：

- `openclaw --dev …` → 使用 `~/.openclaw-dev` + 端口从基础 `19001` 偏移
- `openclaw --profile <name> …` → 使用 `~/.openclaw-<name>`（端口通过配置/环境变量/标志）

参见 [Gateway 网关运维手册](/gateway) 了解派生的端口映射（gateway/browser/canvas）。
参见[多 Gateway 网关](/gateway/multiple-gateways) 了解浏览器/CDP 端口隔离细节。

示例：

```bash
OPENCLAW_CONFIG_PATH=~/.openclaw/a.json \
OPENCLAW_STATE_DIR=~/.openclaw-a \
openclaw gateway --port 19001
```

### `hooks`（Gateway 网关 webhook）

在 Gateway 网关 HTTP 服务器上启用简单的 HTTP webhook 端点。

默认值：

- enabled：`false`
- path：`/hooks`
- maxBodyBytes：`262144`（256 KB）

```json5
{
  hooks: {
    enabled: true,
    token: "shared-secret",
    path: "/hooks",
    presets: ["gmail"],
    transformsDir: "~/.openclaw/hooks",
    mappings: [
      {
        match: { path: "gmail" },
        action: "agent",
        wakeMode: "now",
        name: "Gmail",
        sessionKey: "hook:gmail:{{messages[0].id}}",
        messageTemplate: "From: {{messages[0].from}}\nSubject: {{messages[0].subject}}\n{{messages[0].snippet}}",
        deliver: true,
        channel: "last",
        model: "openai/gpt-5.2-mini",
      },
    ],
  },
}
```

请求必须包含 hook token：

- `Authorization: Bearer <token>` **或**
- `x-openclaw-token: <token>` **或**
- `?token=<token>`

端点：

- `POST /hooks/wake` → `{ text, mode?: "now"|"next-heartbeat" }`
- `POST /hooks/agent` → `{ message, name?, sessionKey?, wakeMode?, deliver?, channel?, to?, model?, thinking?, timeoutSeconds? }`
- `POST /hooks/<name>` → 通过 `hooks.mappings` 解析

`/hooks/agent` 始终将摘要发布到主会话（并可通过 `wakeMode: "now"` 可选地触发即时心跳）。

映射说明：

- `match.path` 匹配 `/hooks` 之后的子路径（例如 `/hooks/gmail` → `gmail`）。
- `match.source` 匹配负载字段（例如 `{ source: "gmail" }`），以便使用通用的 `/hooks/ingest` 路径。
- `{{messages[0].subject}}` 等模板从负载中读取。
- `transform` 可以指向返回 hook 动作的 JS/TS 模块。
- `deliver: true` 将最终回复发送到渠道；`channel` 默认为 `last`（回退到 WhatsApp）。
- 如果没有先前的投递路由，请显式设置 `channel` + `to`（Telegram/Discord/Google Chat/Slack/Signal/iMessage/MS Teams 必需）。
- `model` 覆盖此 hook 运行的 LLM（`provider/model` 或别名；如果设置了 `agents.defaults.models` 则必须被允许）。

Gmail 辅助配置（由 `openclaw webhooks gmail setup` / `run` 使用）：

```json5
{
  hooks: {
    gmail: {
      account: "openclaw@gmail.com",
      topic: "projects/<project-id>/topics/gog-gmail-watch",
      subscription: "gog-gmail-watch-push",
      pushToken: "shared-push-token",
      hookUrl: "http://127.0.0.1:18789/hooks/gmail",
      includeBody: true,
      maxBytes: 20000,
      renewEveryMinutes: 720,
      serve: { bind: "127.0.0.1", port: 8788, path: "/" },
      tailscale: { mode: "funnel", path: "/gmail-pubsub" },

      // 可选：为 Gmail hook 处理使用更便宜的模型
      // 在认证/速率限制/超时时回退到 agents.defaults.model.fallbacks，然后 primary
      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",
      // 可选：Gmail hook 的默认思考级别
      thinking: "off",
    },
  },
}
```

Gmail hook 的模型覆盖：

- `hooks.gmail.model` 指定用于 Gmail hook 处理的模型（默认为会话主模型）。
- 接受 `provider/model` 引用或来自 `agents.defaults.models` 的别名。
- 在认证/速率限制/超时时回退到 `agents.defaults.model.fallbacks`，然后 `agents.defaults.model.primary`。
- 如果设置了 `agents.defaults.models`，请将 hooks 模型包含在白名单中。
- 启动时，如果配置的模型不在模型目录或白名单中，会发出警告。
- `hooks.gmail.thinking` 设置 Gmail hook 的默认思考级别，被每 hook 的 `thinking` 覆盖。

Gateway 网关自动启动：

- 如果 `hooks.enabled=true` 且 `hooks.gmail.account` 已设置，Gateway 网关在启动时
  启动 `gog gmail watch serve` 并自动续期监视。
- 设置 `OPENCLAW_SKIP_GMAIL_WATCHER=1` 禁用自动启动（用于手动运行）。
- 避免在 Gateway 网关旁边单独运行 `gog gmail watch serve`；它会
  因 `listen tcp 127.0.0.1:8788: bind: address already in use` 而失败。

注意：当 `tailscale.mode` 开启时，OpenClaw 将 `serve.path` 默认为 `/`，以便
Tailscale 可以正确代理 `/gmail-pubsub`（它会去除设置的路径前缀）。
如果你需要后端接收带前缀的路径，请将
`hooks.gmail.tailscale.target` 设为完整 URL（并对齐 `serve.path`）。

### `canvasHost`（LAN/tailnet Canvas 文件服务器 + 实时重载）

Gateway 网关通过 HTTP 提供 HTML/CSS/JS 目录服务，以便 iOS/Android 节点可以简单地 `canvas.navigate` 到它。

默认根目录：`~/.openclaw/workspace/canvas`
默认端口：`18793`（选择此端口以避免 OpenClaw 浏览器 CDP 端口 `18792`）
服务器监听 **Gateway 网关绑定主机**（LAN 或 Tailnet），以便节点可以访问。

服务器：

- 提供 `canvasHost.root` 下的文件
- 向提供的 HTML 注入微型实时重载客户端
- 监视目录并通过 `/__openclaw__/ws` 的 WebSocket 端点广播重载
- 目录为空时自动创建起始 `index.html`（以便你立即看到内容）
- 同时在 `/__openclaw__/a2ui/` 提供 A2UI，并作为 `canvasHostUrl` 通告给节点
  （节点始终使用它来访问 Canvas/A2UI）

如果目录很大或遇到 `EMFILE`，请禁用实时重载（和文件监视）：

- 配置：`canvasHost: { liveReload: false }`

```json5
{
  canvasHost: {
    root: "~/.openclaw/workspace/canvas",
    port: 18793,
    liveReload: true,
  },
}
```

`canvasHost.*` 的更改需要重启 Gateway 网关（配置重载会触发重启）。

禁用方式：

- 配置：`canvasHost: { enabled: false }`
- 环境变量：`OPENCLAW_SKIP_CANVAS_HOST=1`

### `bridge`（旧版 TCP 桥接，已移除）

当前版本不再包含 TCP 桥接监听器；`bridge.*` 配置键会被忽略。
节点通过 Gateway 网关 WebSocket 连接。此部分仅保留供历史参考。

旧版行为：

- Gateway 网关可以为节点（iOS/Android）暴露简单的 TCP 桥接，通常在端口 `18790`。

默认值：

- enabled：`true`
- port：`18790`
- bind：`lan`（绑定到 `0.0.0.0`）

绑定模式：

- `lan`：`0.0.0.0`（可通过任何接口访问，包括 LAN/Wi‑Fi 和 Tailscale）
- `tailnet`：仅绑定到机器的 Tailscale IP（推荐用于跨地域访问）
- `loopback`：`127.0.0.1`（仅本地）
- `auto`：如果存在 tailnet IP 则优先使用，否则 `lan`

TLS：

- `bridge.tls.enabled`：为桥接连接启用 TLS（启用时仅 TLS）。
- `bridge.tls.autoGenerate`：当无证书/密钥时生成自签名证书（默认：true）。
- `bridge.tls.certPath` / `bridge.tls.keyPath`：桥接证书 + 私钥的 PEM 路径。
- `bridge.tls.caPath`：可选的 PEM CA 捆绑包（自定义根证书或未来的 mTLS）。

启用 TLS 后，Gateway 网关在发现 TXT 记录中通告 `bridgeTls=1` 和 `bridgeTlsSha256`，以便节点可以固定证书。如果尚未存储指纹，手动连接使用首次信任。
自动生成的证书需要 PATH 中有 `openssl`；如果生成失败，桥接不会启动。

```json5
{
  bridge: {
    enabled: true,
    port: 18790,
    bind: "tailnet",
    tls: {
      enabled: true,
      // 省略时使用 ~/.openclaw/bridge/tls/bridge-{cert,key}.pem。
      // certPath: "~/.openclaw/bridge/tls/bridge-cert.pem",
      // keyPath: "~/.openclaw/bridge/tls/bridge-key.pem"
    },
  },
}
```

### `discovery.mdns`（Bonjour / mDNS 广播模式）

控制 LAN mDNS 发现广播（`_openclaw-gw._tcp`）。

- `minimal`（默认）：从 TXT 记录中省略 `cliPath` + `sshPort`
- `full`：在 TXT 记录中包含 `cliPath` + `sshPort`
- `off`：完全禁用 mDNS 广播
- 主机名：默认为 `openclaw`（通告 `openclaw.local`）。通过 `OPENCLAW_MDNS_HOSTNAME` 覆盖。

```json5
{
  discovery: { mdns: { mode: "minimal" } },
}
```

### `discovery.wideArea`（广域 Bonjour / 单播 DNS‑SD）

启用后，Gateway 网关在 `~/.openclaw/dns/` 下使用配置的发现域（示例：`openclaw.internal.`）为 `_openclaw-gw._tcp` 写入单播 DNS-SD 区域。

要使 iOS/Android 跨网络发现（跨地域访问），请配合以下使用：

- 在 Gateway 网关主机上运行 DNS 服务器，为你选择的域名提供服务（推荐 CoreDNS）
- Tailscale **split DNS**，使客户端通过 Gateway 网关 DNS 服务器解析该域名

一次性设置助手（Gateway 网关主机）：

```bash
openclaw dns setup --apply
```

```json5
{
  discovery: { wideArea: { enabled: true } },
}
```

## 模板变量

模板占位符在 `tools.media.*.models[].args` 和 `tools.media.models[].args`（以及未来任何模板化参数字段）中展开。

| 变量               | 描述                                                  |
| ------------------ | ----------------------------------------------------- | -------- | ------- | ---------- | ----- | ------ | -------- | ------- | ------- | --- |
| `{{Body}}`         | 完整的入站消息正文                                    |
| `{{RawBody}}`      | 原始入站消息正文（无历史/发送者包装；最适合命令解析） |
| `{{BodyStripped}}` | 去除群组提及的正文（最适合智能体的默认值）            |
| `{{From}}`         | 发送者标识符（WhatsApp 为 E.164；按渠道可能不同）     |
| `{{To}}`           | 目标标识符                                            |
| `{{MessageSid}}`   | 渠道消息 id（如果可用）                               |
| `{{SessionId}}`    | 当前会话 UUID                                         |
| `{{IsNewSession}}` | 创建新会话时为 `"true"`                               |
| `{{MediaUrl}}`     | 入站媒体伪 URL（如果存在）                            |
| `{{MediaPath}}`    | 本地媒体路径（如果已下载）                            |
| `{{MediaType}}`    | 媒体类型（image/audio/document/…）                    |
| `{{Transcript}}`   | 音频转录（启用时）                                    |
| `{{Prompt}}`       | CLI 条目的已解析媒体提示                              |
| `{{MaxChars}}`     | CLI 条目的已解析最大输出字符数                        |
| `{{ChatType}}`     | `"direct"` 或 `"group"`                               |
| `{{GroupSubject}}` | 群组主题（尽力而为）                                  |
| `{{GroupMembers}}` | 群组成员预览（尽力而为）                              |
| `{{SenderName}}`   | 发送者显示名称（尽力而为）                            |
| `{{SenderE164}}`   | 发送者电话号码（尽力而为）                            |
| `{{Provider}}`     | 提供商提示（whatsapp                                  | telegram | discord | googlechat | slack | signal | imessage | msteams | webchat | …） |

## Cron（Gateway 网关调度器）

Cron 是 Gateway 网关自有的唤醒和定时任务调度器。参见 [Cron 任务](/automation/cron-jobs) 了解功能概述和 CLI 示例。

```json5
{
  cron: {
    enabled: true,
    maxConcurrentRuns: 2,
  },
}
```

---

_下一步：[智能体运行时](/concepts/agent)_ 🦞


---

## index

---
read_when:
  - 添加或修改 CLI 命令或选项
  - 为新命令界面编写文档
summary: OpenClaw `openclaw` 命令、子命令和选项的 CLI 参考
title: CLI 参考
x-i18n:
  generated_at: "2026-02-03T07:47:54Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: a73923763d7b89d4b183f569d543927ffbfd1f3e02f9e66639913f6daf226850
  source_path: cli/index.md
  workflow: 15
---

# CLI 参考

本页描述当前的 CLI 行为。如果命令发生变化，请更新此文档。

## 命令页面

- [`setup`](/cli/setup)
- [`onboard`](/cli/onboard)
- [`configure`](/cli/configure)
- [`config`](/cli/config)
- [`doctor`](/cli/doctor)
- [`dashboard`](/cli/dashboard)
- [`reset`](/cli/reset)
- [`uninstall`](/cli/uninstall)
- [`update`](/cli/update)
- [`message`](/cli/message)
- [`agent`](/cli/agent)
- [`agents`](/cli/agents)
- [`acp`](/cli/acp)
- [`status`](/cli/status)
- [`health`](/cli/health)
- [`sessions`](/cli/sessions)
- [`gateway`](/cli/gateway)
- [`logs`](/cli/logs)
- [`system`](/cli/system)
- [`models`](/cli/models)
- [`memory`](/cli/memory)
- [`nodes`](/cli/nodes)
- [`devices`](/cli/devices)
- [`node`](/cli/node)
- [`approvals`](/cli/approvals)
- [`sandbox`](/cli/sandbox)
- [`tui`](/cli/tui)
- [`browser`](/cli/browser)
- [`cron`](/cli/cron)
- [`dns`](/cli/dns)
- [`docs`](/cli/docs)
- [`hooks`](/cli/hooks)
- [`webhooks`](/cli/webhooks)
- [`pairing`](/cli/pairing)
- [`plugins`](/cli/plugins)（插件命令）
- [`channels`](/cli/channels)
- [`security`](/cli/security)
- [`skills`](/cli/skills)
- [`voicecall`](/cli/voicecall)（插件；如已安装）

## 全局标志

- `--dev`：将状态隔离到 `~/.openclaw-dev` 下并调整默认端口。
- `--profile <name>`：将状态隔离到 `~/.openclaw-<name>` 下。
- `--no-color`：禁用 ANSI 颜色。
- `--update`：`openclaw update` 的简写（仅限源码安装）。
- `-V`、`--version`、`-v`：打印版本并退出。

## 输出样式

- ANSI 颜色和进度指示器仅在 TTY 会话中渲染。
- OSC-8 超链接在支持的终端中渲染为可点击链接；否则回退到纯 URL。
- `--json`（以及支持的地方使用 `--plain`）禁用样式以获得干净输出。
- `--no-color` 禁用 ANSI 样式；也支持 `NO_COLOR=1`。
- 长时间运行的命令显示进度指示器（支持时使用 OSC 9;4）。

## 颜色调色板

OpenClaw 在 CLI 输出中使用龙虾调色板。

- `accent`（#FF5A2D）：标题、标签、主要高亮。
- `accentBright`（#FF7A3D）：命令名称、强调。
- `accentDim`（#D14A22）：次要高亮文本。
- `info`（#FF8A5B）：信息性值。
- `success`（#2FBF71）：成功状态。
- `warn`（#FFB020）：警告、回退、注意。
- `error`（#E23D2D）：错误、失败。
- `muted`（#8B7F77）：弱化、元数据。

调色板权威来源：`src/terminal/palette.ts`（又名"lobster seam"）。

## 命令树

```
openclaw [--dev] [--profile <name>] <command>
  setup
  onboard
  configure
  config
    get
    set
    unset
  doctor
  security
    audit
  reset
  uninstall
  update
  channels
    list
    status
    logs
    add
    remove
    login
    logout
  skills
    list
    info
    check
  plugins
    list
    info
    install
    enable
    disable
    doctor
  memory
    status
    index
    search
  message
  agent
  agents
    list
    add
    delete
  acp
  status
  health
  sessions
  gateway
    call
    health
    status
    probe
    discover
    install
    uninstall
    start
    stop
    restart
    run
  logs
  system
    event
    heartbeat last|enable|disable
    presence
  models
    list
    status
    set
    set-image
    aliases list|add|remove
    fallbacks list|add|remove|clear
    image-fallbacks list|add|remove|clear
    scan
    auth add|setup-token|paste-token
    auth order get|set|clear
  sandbox
    list
    recreate
    explain
  cron
    status
    list
    add
    edit
    rm
    enable
    disable
    runs
    run
  nodes
  devices
  node
    run
    status
    install
    uninstall
    start
    stop
    restart
  approvals
    get
    set
    allowlist add|remove
  browser
    status
    start
    stop
    reset-profile
    tabs
    open
    focus
    close
    profiles
    create-profile
    delete-profile
    screenshot
    snapshot
    navigate
    resize
    click
    type
    press
    hover
    drag
    select
    upload
    fill
    dialog
    wait
    evaluate
    console
    pdf
  hooks
    list
    info
    check
    enable
    disable
    install
    update
  webhooks
    gmail setup|run
  pairing
    list
    approve
  docs
  dns
    setup
  tui
```

注意：插件可以添加额外的顶级命令（例如 `openclaw voicecall`）。

## 安全

- `openclaw security audit` — 审计配置 + 本地状态中常见的安全隐患。
- `openclaw security audit --deep` — 尽力进行实时 Gateway 网关探测。
- `openclaw security audit --fix` — 收紧安全默认值并 chmod 状态/配置。

## 插件

管理扩展及其配置：

- `openclaw plugins list` — 发现插件（使用 `--json` 获取机器可读输出）。
- `openclaw plugins info <id>` — 显示插件详情。
- `openclaw plugins install <path|.tgz|npm-spec>` — 安装插件（或将插件路径添加到 `plugins.load.paths`）。
- `openclaw plugins enable <id>` / `disable <id>` — 切换 `plugins.entries.<id>.enabled`。
- `openclaw plugins doctor` — 报告插件加载错误。

大多数插件更改需要重启 Gateway 网关。参见 [/plugin](/tools/plugin)。

## 记忆

对 `MEMORY.md` + `memory/*.md` 进行向量搜索：

- `openclaw memory status` — 显示索引统计。
- `openclaw memory index` — 重新索引记忆文件。
- `openclaw memory search "<query>"` — 对记忆进行语义搜索。

## 聊天斜杠命令

聊天消息支持 `/...` 命令（文本和原生）。参见 [/tools/slash-commands](/tools/slash-commands)。

亮点：

- `/status` 用于快速诊断。
- `/config` 用于持久化配置更改。
- `/debug` 用于仅运行时的配置覆盖（内存中，不写入磁盘；需要 `commands.debug: true`）。

## 设置 + 新手引导

### `setup`

初始化配置 + 工作区。

选项：

- `--workspace <dir>`：智能体工作区路径（默认 `~/.openclaw/workspace`）。
- `--wizard`：运行新手引导向导。
- `--non-interactive`：无提示运行向导。
- `--mode <local|remote>`：向导模式。
- `--remote-url <url>`：远程 Gateway 网关 URL。
- `--remote-token <token>`：远程 Gateway 网关令牌。

当存在任何向导标志（`--non-interactive`、`--mode`、`--remote-url`、`--remote-token`）时，向导自动运行。

### `onboard`

交互式向导，用于设置 Gateway 网关、工作区和 Skills。

选项：

- `--workspace <dir>`
- `--reset`（在向导之前重置配置 + 凭证 + 会话 + 工作区）
- `--non-interactive`
- `--mode <local|remote>`
- `--flow <quickstart|advanced|manual>`（manual 是 advanced 的别名）
- `--auth-choice <setup-token|token|chutes|openai-codex|openai-api-key|openrouter-api-key|ai-gateway-api-key|moonshot-api-key|kimi-code-api-key|synthetic-api-key|venice-api-key|gemini-api-key|zai-api-key|apiKey|minimax-api|minimax-api-lightning|opencode-zen|skip>`
- `--token-provider <id>`（非交互式；与 `--auth-choice token` 配合使用）
- `--token <token>`（非交互式；与 `--auth-choice token` 配合使用）
- `--token-profile-id <id>`（非交互式；默认：`<provider>:manual`）
- `--token-expires-in <duration>`（非交互式；例如 `365d`、`12h`）
- `--anthropic-api-key <key>`
- `--openai-api-key <key>`
- `--openrouter-api-key <key>`
- `--ai-gateway-api-key <key>`
- `--moonshot-api-key <key>`
- `--kimi-code-api-key <key>`
- `--gemini-api-key <key>`
- `--zai-api-key <key>`
- `--minimax-api-key <key>`
- `--opencode-zen-api-key <key>`
- `--gateway-port <port>`
- `--gateway-bind <loopback|lan|tailnet|auto|custom>`
- `--gateway-auth <token|password>`
- `--gateway-token <token>`
- `--gateway-password <password>`
- `--remote-url <url>`
- `--remote-token <token>`
- `--tailscale <off|serve|funnel>`
- `--tailscale-reset-on-exit`
- `--install-daemon`
- `--no-install-daemon`（别名：`--skip-daemon`）
- `--daemon-runtime <node|bun>`
- `--skip-channels`
- `--skip-skills`
- `--skip-health`
- `--skip-ui`
- `--node-manager <npm|pnpm|bun>`（推荐 pnpm；不建议将 bun 用于 Gateway 网关运行时）
- `--json`

### `configure`

交互式配置向导（模型、渠道、Skills、Gateway 网关）。

### `config`

非交互式配置辅助工具（get/set/unset）。不带子命令运行 `openclaw config` 会启动向导。

子命令：

- `config get <path>`：打印配置值（点/括号路径）。
- `config set <path> <value>`：设置值（JSON5 或原始字符串）。
- `config unset <path>`：删除值。

### `doctor`

健康检查 + 快速修复（配置 + Gateway 网关 + 旧版服务）。

选项：

- `--no-workspace-suggestions`：禁用工作区记忆提示。
- `--yes`：无提示接受默认值（无头模式）。
- `--non-interactive`：跳过提示；仅应用安全迁移。
- `--deep`：扫描系统服务以查找额外的 Gateway 网关安装。

## 渠道辅助工具

### `channels`

管理聊天渠道账户（WhatsApp/Telegram/Discord/Google Chat/Slack/Mattermost（插件）/Signal/iMessage/MS Teams）。

子命令：

- `channels list`：显示已配置的渠道和认证配置文件。
- `channels status`：检查 Gateway 网关可达性和渠道健康状况（`--probe` 运行额外检查；使用 `openclaw health` 或 `openclaw status --deep` 进行 Gateway 网关健康探测）。
- 提示：`channels status` 在检测到常见配置错误时会打印带有建议修复的警告（然后指向 `openclaw doctor`）。
- `channels logs`：显示 Gateway 网关日志文件中最近的渠道日志。
- `channels add`：不传标志时使用向导式设置；标志切换到非交互模式。
- `channels remove`：默认禁用；传 `--delete` 可无提示删除配置条目。
- `channels login`：交互式渠道登录（仅限 WhatsApp Web）。
- `channels logout`：登出渠道会话（如支持）。

通用选项：

- `--channel <name>`：`whatsapp|telegram|discord|googlechat|slack|mattermost|signal|imessage|msteams`
- `--account <id>`：渠道账户 id（默认 `default`）
- `--name <label>`：账户的显示名称

`channels login` 选项：

- `--channel <channel>`（默认 `whatsapp`；支持 `whatsapp`/`web`）
- `--account <id>`
- `--verbose`

`channels logout` 选项：

- `--channel <channel>`（默认 `whatsapp`）
- `--account <id>`

`channels list` 选项：

- `--no-usage`：跳过模型提供商用量/配额快照（仅限 OAuth/API 支持的）。
- `--json`：输出 JSON（除非设置 `--no-usage`，否则包含用量）。

`channels logs` 选项：

- `--channel <name|all>`（默认 `all`）
- `--lines <n>`（默认 `200`）
- `--json`

更多详情：[/concepts/oauth](/concepts/oauth)

示例：

```bash
openclaw channels add --channel telegram --account alerts --name "Alerts Bot" --token $TELEGRAM_BOT_TOKEN
openclaw channels add --channel discord --account work --name "Work Bot" --token $DISCORD_BOT_TOKEN
openclaw channels remove --channel discord --account work --delete
openclaw channels status --probe
openclaw status --deep
```

### `skills`

列出和检查可用的 Skills 及就绪信息。

子命令：

- `skills list`：列出 Skills（无子命令时的默认行为）。
- `skills info <name>`：显示单个 Skill 的详情。
- `skills check`：就绪与缺失需求的摘要。

选项：

- `--eligible`：仅显示就绪的 Skills。
- `--json`：输出 JSON（无样式）。
- `-v`、`--verbose`：包含缺失需求详情。

提示：使用 `npx clawhub` 搜索、安装和同步 Skills。

### `pairing`

批准跨渠道的私信配对请求。

子命令：

- `pairing list <channel> [--json]`
- `pairing approve <channel> <code> [--notify]`

### `webhooks gmail`

Gmail Pub/Sub 钩子设置 + 运行器。参见 [/automation/gmail-pubsub](/automation/gmail-pubsub)。

子命令：

- `webhooks gmail setup`（需要 `--account <email>`；支持 `--project`、`--topic`、`--subscription`、`--label`、`--hook-url`、`--hook-token`、`--push-token`、`--bind`、`--port`、`--path`、`--include-body`、`--max-bytes`、`--renew-minutes`、`--tailscale`、`--tailscale-path`、`--tailscale-target`、`--push-endpoint`、`--json`）
- `webhooks gmail run`（相同标志的运行时覆盖）

### `dns setup`

广域发现 DNS 辅助工具（CoreDNS + Tailscale）。参见 [/gateway/discovery](/gateway/discovery)。

选项：

- `--apply`：安装/更新 CoreDNS 配置（需要 sudo；仅限 macOS）。

## 消息 + 智能体

### `message`

统一的出站消息 + 渠道操作。

参见：[/cli/message](/cli/message)

子命令：

- `message send|poll|react|reactions|read|edit|delete|pin|unpin|pins|permissions|search|timeout|kick|ban`
- `message thread <create|list|reply>`
- `message emoji <list|upload>`
- `message sticker <send|upload>`
- `message role <info|add|remove>`
- `message channel <info|list>`
- `message member info`
- `message voice status`
- `message event <list|create>`

示例：

- `openclaw message send --target +15555550123 --message "Hi"`
- `openclaw message poll --channel discord --target channel:123 --poll-question "Snack?" --poll-option Pizza --poll-option Sushi`

### `agent`

通过 Gateway 网关运行一个智能体回合（或使用 `--local` 嵌入式运行）。

必需：

- `--message <text>`

选项：

- `--to <dest>`（用于会话键和可选发送）
- `--session-id <id>`
- `--thinking <off|minimal|low|medium|high|xhigh>`（仅限 GPT-5.2 + Codex 模型）
- `--verbose <on|full|off>`
- `--channel <whatsapp|telegram|discord|slack|mattermost|signal|imessage|msteams>`
- `--local`
- `--deliver`
- `--json`
- `--timeout <seconds>`

### `agents`

管理隔离的智能体（工作区 + 认证 + 路由）。

#### `agents list`

列出已配置的智能体。

选项：

- `--json`
- `--bindings`

#### `agents add [name]`

添加新的隔离智能体。除非传入标志（或 `--non-interactive`），否则运行引导向导；非交互模式下 `--workspace` 是必需的。

选项：

- `--workspace <dir>`
- `--model <id>`
- `--agent-dir <dir>`
- `--bind <channel[:accountId]>`（可重复）
- `--non-interactive`
- `--json`

绑定规范使用 `channel[:accountId]`。对于 WhatsApp，省略 `accountId` 时使用默认账户 id。

#### `agents delete <id>`

删除智能体并清理其工作区 + 状态。

选项：

- `--force`
- `--json`

### `acp`

运行连接 IDE 到 Gateway 网关的 ACP 桥接。

完整选项和示例参见 [`acp`](/cli/acp)。

### `status`

显示关联会话健康状况和最近的收件人。

选项：

- `--json`
- `--all`（完整诊断；只读，可粘贴）
- `--deep`（探测渠道）
- `--usage`（显示模型提供商用量/配额）
- `--timeout <ms>`
- `--verbose`
- `--debug`（`--verbose` 的别名）

说明：

- 概览包含 Gateway 网关 + 节点主机服务状态（如可用）。

### 用量跟踪

当 OAuth/API 凭证可用时，OpenClaw 可以显示提供商用量/配额。

显示位置：

- `/status`（可用时添加简短的提供商用量行）
- `openclaw status --usage`（打印完整的提供商明细）
- macOS 菜单栏（上下文下的用量部分）

说明：

- 数据直接来自提供商用量端点（非估算）。
- 提供商：Anthropic、GitHub Copilot、OpenAI Codex OAuth，以及启用这些提供商插件时的 Gemini CLI/Antigravity。
- 如果没有匹配的凭证，用量会被隐藏。
- 详情：参见[用量跟踪](/concepts/usage-tracking)。

### `health`

从运行中的 Gateway 网关获取健康状态。

选项：

- `--json`
- `--timeout <ms>`
- `--verbose`

### `sessions`

列出存储的对话会话。

选项：

- `--json`
- `--verbose`
- `--store <path>`
- `--active <minutes>`

## 重置/卸载

### `reset`

重置本地配置/状态（保留 CLI 安装）。

选项：

- `--scope <config|config+creds+sessions|full>`
- `--yes`
- `--non-interactive`
- `--dry-run`

说明：

- `--non-interactive` 需要 `--scope` 和 `--yes`。

### `uninstall`

卸载 Gateway 网关服务 + 本地数据（CLI 保留）。

选项：

- `--service`
- `--state`
- `--workspace`
- `--app`
- `--all`
- `--yes`
- `--non-interactive`
- `--dry-run`

说明：

- `--non-interactive` 需要 `--yes` 和明确的范围（或 `--all`）。

## Gateway 网关

### `gateway`

运行 WebSocket Gateway 网关。

选项：

- `--port <port>`
- `--bind <loopback|tailnet|lan|auto|custom>`
- `--token <token>`
- `--auth <token|password>`
- `--password <password>`
- `--tailscale <off|serve|funnel>`
- `--tailscale-reset-on-exit`
- `--allow-unconfigured`
- `--dev`
- `--reset`（重置 dev 配置 + 凭证 + 会话 + 工作区）
- `--force`（终止端口上的现有监听器）
- `--verbose`
- `--claude-cli-logs`
- `--ws-log <auto|full|compact>`
- `--compact`（`--ws-log compact` 的别名）
- `--raw-stream`
- `--raw-stream-path <path>`

### `gateway service`

管理 Gateway 网关服务（launchd/systemd/schtasks）。

子命令：

- `gateway status`（默认探测 Gateway 网关 RPC）
- `gateway install`（服务安装）
- `gateway uninstall`
- `gateway start`
- `gateway stop`
- `gateway restart`

说明：

- `gateway status` 默认使用服务解析的端口/配置探测 Gateway 网关 RPC（使用 `--url/--token/--password` 覆盖）。
- `gateway status` 支持 `--no-probe`、`--deep` 和 `--json` 用于脚本化。
- `gateway status` 在检测到旧版或额外的 Gateway 网关服务时也会显示（`--deep` 添加系统级扫描）。配置文件命名的 OpenClaw 服务被视为一等公民，不会被标记为"额外"。
- `gateway status` 打印 CLI 使用的配置路径与服务可能使用的配置（服务环境），以及解析的探测目标 URL。
- `gateway install|uninstall|start|stop|restart` 支持 `--json` 用于脚本化（默认输出保持人类友好）。
- `gateway install` 默认使用 Node 运行时；**不建议**使用 bun（WhatsApp/Telegram bug）。
- `gateway install` 选项：`--port`、`--runtime`、`--token`、`--force`、`--json`。

### `logs`

通过 RPC 跟踪 Gateway 网关文件日志。

说明：

- TTY 会话渲染彩色、结构化视图；非 TTY 回退到纯文本。
- `--json` 输出行分隔的 JSON（每行一个日志事件）。

示例：

```bash
openclaw logs --follow
openclaw logs --limit 200
openclaw logs --plain
openclaw logs --json
openclaw logs --no-color
```

### `gateway <subcommand>`

Gateway 网关 CLI 辅助工具（RPC 子命令使用 `--url`、`--token`、`--password`、`--timeout`、`--expect-final`）。

子命令：

- `gateway call <method> [--params <json>]`
- `gateway health`
- `gateway status`
- `gateway probe`
- `gateway discover`
- `gateway install|uninstall|start|stop|restart`
- `gateway run`

常见 RPC：

- `config.apply`（验证 + 写入配置 + 重启 + 唤醒）
- `config.patch`（合并部分更新 + 重启 + 唤醒）
- `update.run`（运行更新 + 重启 + 唤醒）

提示：直接调用 `config.set`/`config.apply`/`config.patch` 时，如果配置已存在，请传入来自 `config.get` 的 `baseHash`。

## 模型

回退行为和扫描策略参见 [/concepts/models](/concepts/models)。

首选 Anthropic 认证（setup-token）：

```bash
claude setup-token
openclaw models auth setup-token --provider anthropic
openclaw models status
```

### `models`（根命令）

`openclaw models` 是 `models status` 的别名。

根选项：

- `--status-json`（`models status --json` 的别名）
- `--status-plain`（`models status --plain` 的别名）

### `models list`

选项：

- `--all`
- `--local`
- `--provider <name>`
- `--json`
- `--plain`

### `models status`

选项：

- `--json`
- `--plain`
- `--check`（退出码 1=过期/缺失，2=即将过期）
- `--probe`（对已配置认证配置文件进行实时探测）
- `--probe-provider <name>`
- `--probe-profile <id>`（重复或逗号分隔）
- `--probe-timeout <ms>`
- `--probe-concurrency <n>`
- `--probe-max-tokens <n>`

始终包含认证概览和认证存储中配置文件的 OAuth 过期状态。`--probe` 运行实时请求（可能消耗令牌并触发速率限制）。

### `models set <model>`

设置 `agents.defaults.model.primary`。

### `models set-image <model>`

设置 `agents.defaults.imageModel.primary`。

### `models aliases list|add|remove`

选项：

- `list`：`--json`、`--plain`
- `add <alias> <model>`
- `remove <alias>`

### `models fallbacks list|add|remove|clear`

选项：

- `list`：`--json`、`--plain`
- `add <model>`
- `remove <model>`
- `clear`

### `models image-fallbacks list|add|remove|clear`

选项：

- `list`：`--json`、`--plain`
- `add <model>`
- `remove <model>`
- `clear`

### `models scan`

选项：

- `--min-params <b>`
- `--max-age-days <days>`
- `--provider <name>`
- `--max-candidates <n>`
- `--timeout <ms>`
- `--concurrency <n>`
- `--no-probe`
- `--yes`
- `--no-input`
- `--set-default`
- `--set-image`
- `--json`

### `models auth add|setup-token|paste-token`

选项：

- `add`：交互式认证辅助工具
- `setup-token`：`--provider <name>`（默认 `anthropic`）、`--yes`
- `paste-token`：`--provider <name>`、`--profile-id <id>`、`--expires-in <duration>`

### `models auth order get|set|clear`

选项：

- `get`：`--provider <name>`、`--agent <id>`、`--json`
- `set`：`--provider <name>`、`--agent <id>`、`<profileIds...>`
- `clear`：`--provider <name>`、`--agent <id>`

## 系统

### `system event`

将系统事件加入队列并可选触发心跳（Gateway 网关 RPC）。

必需：

- `--text <text>`

选项：

- `--mode <now|next-heartbeat>`
- `--json`
- `--url`、`--token`、`--timeout`、`--expect-final`

### `system heartbeat last|enable|disable`

心跳控制（Gateway 网关 RPC）。

选项：

- `--json`
- `--url`、`--token`、`--timeout`、`--expect-final`

### `system presence`

列出系统存在条目（Gateway 网关 RPC）。

选项：

- `--json`
- `--url`、`--token`、`--timeout`、`--expect-final`

## 定时任务

管理计划任务（Gateway 网关 RPC）。参见 [/automation/cron-jobs](/automation/cron-jobs)。

子命令：

- `cron status [--json]`
- `cron list [--all] [--json]`（默认表格输出；使用 `--json` 获取原始数据）
- `cron add`（别名：`create`；需要 `--name` 和 `--at` | `--every` | `--cron` 三选一，以及 `--system-event` | `--message` 负载二选一）
- `cron edit <id>`（补丁字段）
- `cron rm <id>`（别名：`remove`、`delete`）
- `cron enable <id>`
- `cron disable <id>`
- `cron runs --id <id> [--limit <n>]`
- `cron run <id> [--force]`

所有 `cron` 命令接受 `--url`、`--token`、`--timeout`、`--expect-final`。

## 节点主机

`node` 运行**无头节点主机**或将其作为后台服务管理。参见 [`openclaw node`](/cli/node)。

子命令：

- `node run --host <gateway-host> --port 18789`
- `node status`
- `node install [--host <gateway-host>] [--port <port>] [--tls] [--tls-fingerprint <sha256>] [--node-id <id>] [--display-name <name>] [--runtime <node|bun>] [--force]`
- `node uninstall`
- `node stop`
- `node restart`

## 节点

`nodes` 与 Gateway 网关通信并针对已配对的节点。参见 [/nodes](/nodes)。

通用选项：

- `--url`、`--token`、`--timeout`、`--json`

子命令：

- `nodes status [--connected] [--last-connected <duration>]`
- `nodes describe --node <id|name|ip>`
- `nodes list [--connected] [--last-connected <duration>]`
- `nodes pending`
- `nodes approve <requestId>`
- `nodes reject <requestId>`
- `nodes rename --node <id|name|ip> --name <displayName>`
- `nodes invoke --node <id|name|ip> --command <command> [--params <json>] [--invoke-timeout <ms>] [--idempotency-key <key>]`
- `nodes run --node <id|name|ip> [--cwd <path>] [--env KEY=VAL] [--command-timeout <ms>] [--needs-screen-recording] [--invoke-timeout <ms>] <command...>`（mac 节点或无头节点主机）
- `nodes notify --node <id|name|ip> [--title <text>] [--body <text>] [--sound <name>] [--priority <passive|active|timeSensitive>] [--delivery <system|overlay|auto>] [--invoke-timeout <ms>]`（仅限 mac）

相机：

- `nodes camera list --node <id|name|ip>`
- `nodes camera snap --node <id|name|ip> [--facing front|back|both] [--device-id <id>] [--max-width <px>] [--quality <0-1>] [--delay-ms <ms>] [--invoke-timeout <ms>]`
- `nodes camera clip --node <id|name|ip> [--facing front|back] [--device-id <id>] [--duration <ms|10s|1m>] [--no-audio] [--invoke-timeout <ms>]`

画布 + 屏幕：

- `nodes canvas snapshot --node <id|name|ip> [--format png|jpg|jpeg] [--max-width <px>] [--quality <0-1>] [--invoke-timeout <ms>]`
- `nodes canvas present --node <id|name|ip> [--target <urlOrPath>] [--x <px>] [--y <px>] [--width <px>] [--height <px>] [--invoke-timeout <ms>]`
- `nodes canvas hide --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes canvas navigate <url> --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes canvas eval [<js>] --node <id|name|ip> [--js <code>] [--invoke-timeout <ms>]`
- `nodes canvas a2ui push --node <id|name|ip> (--jsonl <path> | --text <text>) [--invoke-timeout <ms>]`
- `nodes canvas a2ui reset --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes screen record --node <id|name|ip> [--screen <index>] [--duration <ms|10s>] [--fps <n>] [--no-audio] [--out <path>] [--invoke-timeout <ms>]`

位置：

- `nodes location get --node <id|name|ip> [--max-age <ms>] [--accuracy <coarse|balanced|precise>] [--location-timeout <ms>] [--invoke-timeout <ms>]`

## 浏览器

浏览器控制 CLI（专用 Chrome/Brave/Edge/Chromium）。参见 [`openclaw browser`](/cli/browser) 和[浏览器工具](/tools/browser)。

通用选项：

- `--url`、`--token`、`--timeout`、`--json`
- `--browser-profile <name>`

管理：

- `browser status`
- `browser start`
- `browser stop`
- `browser reset-profile`
- `browser tabs`
- `browser open <url>`
- `browser focus <targetId>`
- `browser close [targetId]`
- `browser profiles`
- `browser create-profile --name <name> [--color <hex>] [--cdp-url <url>]`
- `browser delete-profile --name <name>`

检查：

- `browser screenshot [targetId] [--full-page] [--ref <ref>] [--element <selector>] [--type png|jpeg]`
- `browser snapshot [--format aria|ai] [--target-id <id>] [--limit <n>] [--interactive] [--compact] [--depth <n>] [--selector <sel>] [--out <path>]`

操作：

- `browser navigate <url> [--target-id <id>]`
- `browser resize <width> <height> [--target-id <id>]`
- `browser click <ref> [--double] [--button <left|right|middle>] [--modifiers <csv>] [--target-id <id>]`
- `browser type <ref> <text> [--submit] [--slowly] [--target-id <id>]`
- `browser press <key> [--target-id <id>]`
- `browser hover <ref> [--target-id <id>]`
- `browser drag <startRef> <endRef> [--target-id <id>]`
- `browser select <ref> <values...> [--target-id <id>]`
- `browser upload <paths...> [--ref <ref>] [--input-ref <ref>] [--element <selector>] [--target-id <id>] [--timeout-ms <ms>]`
- `browser fill [--fields <json>] [--fields-file <path>] [--target-id <id>]`
- `browser dialog --accept|--dismiss [--prompt <text>] [--target-id <id>] [--timeout-ms <ms>]`
- `browser wait [--time <ms>] [--text <value>] [--text-gone <value>] [--target-id <id>]`
- `browser evaluate --fn <code> [--ref <ref>] [--target-id <id>]`
- `browser console [--level <error|warn|info>] [--target-id <id>]`
- `browser pdf [--target-id <id>]`

## 文档搜索

### `docs [query...]`

搜索在线文档索引。

## TUI

### `tui`

打开连接到 Gateway 网关的终端 UI。

选项：

- `--url <url>`
- `--token <token>`
- `--password <password>`
- `--session <key>`
- `--deliver`
- `--thinking <level>`
- `--message <text>`
- `--timeout-ms <ms>`（默认为 `agents.defaults.timeoutSeconds`）
- `--history-limit <n>`


---


## index

---
read_when:
  - 你想为 OpenClaw 选择一个聊天渠道
  - 你需要快速了解支持的消息平台
summary: OpenClaw 可连接的消息平台
title: 聊天渠道
x-i18n:
  generated_at: "2026-02-03T07:43:27Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 2632863def6dee97e0fa8b931762f0969174fd4fb22303a00dcd46527fe4a141
  source_path: channels/index.md
  workflow: 15
---

# 聊天渠道

OpenClaw 可以在你已经使用的任何聊天应用上与你交流。每个渠道通过 Gateway 网关连接。
所有渠道都支持文本；媒体和表情回应的支持因渠道而异。

## 支持的渠道

- [WhatsApp](/channels/whatsapp) — 最受欢迎；使用 Baileys，需要二维码配对。
- [Telegram](/channels/telegram) — 通过 grammY 使用 Bot API；支持群组。
- [Discord](/channels/discord) — Discord Bot API + Gateway；支持服务器、频道和私信。
- [Slack](/channels/slack) — Bolt SDK；工作区应用。
- [飞书](/channels/feishu) — 飞书（Lark）机器人（插件，需单独安装）。
- [Google Chat](/channels/googlechat) — 通过 HTTP webhook 的 Google Chat API 应用。
- [Mattermost](/channels/mattermost) — Bot API + WebSocket；频道、群组、私信（插件，需单独安装）。
- [Signal](/channels/signal) — signal-cli；注重隐私。
- [BlueBubbles](/channels/bluebubbles) — **推荐用于 iMessage**；使用 BlueBubbles macOS 服务器 REST API，功能完整（编辑、撤回、特效、回应、群组管理——编辑功能在 macOS 26 Tahoe 上目前不可用）。
- [iMessage（旧版）](/channels/imessage) — 通过 imsg CLI 的旧版 macOS 集成（已弃用，新设置请使用 BlueBubbles）。
- [Microsoft Teams](/channels/msteams) — Bot Framework；企业支持（插件，需单独安装）。
- [LINE](/channels/line) — LINE Messaging API 机器人（插件，需单独安装）。
- [Nextcloud Talk](/channels/nextcloud-talk) — 通过 Nextcloud Talk 的自托管聊天（插件，需单独安装）。
- [Matrix](/channels/matrix) — Matrix 协议（插件，需单独安装）。
- [Nostr](/channels/nostr) — 通过 NIP-04 的去中心化私信（插件，需单独安装）。
- [Tlon](/channels/tlon) — 基于 Urbit 的消息应用（插件，需单独安装）。
- [Twitch](/channels/twitch) — 通过 IRC 连接的 Twitch 聊天（插件，需单独安装）。
- [Zalo](/channels/zalo) — Zalo Bot API；越南流行的消息应用（插件，需单独安装）。
- [Zalo Personal](/channels/zalouser) — 通过二维码登录的 Zalo 个人账号（插件，需单独安装）。
- [WebChat](/web/webchat) — 基于 WebSocket 的 Gateway 网关 WebChat 界面。

## 注意事项

- 渠道可以同时运行；配置多个渠道后，OpenClaw 会按聊天进行路由。
- 最快的设置方式通常是 **Telegram**（简单的机器人令牌）。WhatsApp 需要二维码配对，
  并在磁盘上存储更多状态。
- 群组行为因渠道而异；参见[群组](/channels/groups)。
- 为安全起见，私信配对和允许列表会被强制执行；参见[安全](/gateway/security)。
- Telegram 内部机制：[grammY 说明](/channels/grammy)。
- 故障排除：[渠道故障排除](/channels/troubleshooting)。
- 模型提供商单独记录；参见[模型提供商](/providers/models)。


---

## whatsapp

---
read_when:
  - 处理 WhatsApp/网页渠道行为或收件箱路由时
summary: WhatsApp（网页渠道）集成：登录、收件箱、回复、媒体和运维
title: WhatsApp
x-i18n:
  generated_at: "2026-02-03T07:46:24Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 44fd88f8e269284999e5a5a52b230edae6e6f978528dd298d6a5603d03c0c38d
  source_path: channels/whatsapp.md
  workflow: 15
---

# WhatsApp（网页渠道）

状态：仅支持通过 Baileys 的 WhatsApp Web。Gateway 网关拥有会话。

## 快速设置（新手）

1. 如果可能，使用**单独的手机号码**（推荐）。
2. 在 `~/.openclaw/openclaw.json` 中配置 WhatsApp。
3. 运行 `openclaw channels login` 扫描二维码（关联设备）。
4. 启动 Gateway 网关。

最小配置：

```json5
{
  channels: {
    whatsapp: {
      dmPolicy: "allowlist",
      allowFrom: ["+15551234567"],
    },
  },
}
```

## 目标

- 在一个 Gateway 网关进程中支持多个 WhatsApp 账户（多账户）。
- 确定性路由：回复返回到 WhatsApp，无模型路由。
- 模型能看到足够的上下文来理解引用回复。

## 配置写入

默认情况下，WhatsApp 允许写入由 `/config set|unset` 触发的配置更新（需要 `commands.config: true`）。

禁用方式：

```json5
{
  channels: { whatsapp: { configWrites: false } },
}
```

## 架构（谁拥有什么）

- **Gateway 网关**拥有 Baileys socket 和收件箱循环。
- **CLI / macOS 应用**与 Gateway 网关通信；不直接使用 Baileys。
- 发送出站消息需要**活跃的监听器**；否则发送会快速失败。

## 获取手机号码（两种模式）

WhatsApp 需要真实手机号码进行验证。VoIP 和虚拟号码通常会被封锁。在 WhatsApp 上运行 OpenClaw 有两种支持的方式：

### 专用号码（推荐）

为 OpenClaw 使用**单独的手机号码**。最佳用户体验，清晰的路由，无自聊天怪异问题。理想设置：**备用/旧 Android 手机 + eSIM**。保持 Wi-Fi 和电源连接，通过二维码关联。

**WhatsApp Business：** 你可以在同一设备上使用不同号码的 WhatsApp Business。非常适合将个人 WhatsApp 分开——安装 WhatsApp Business 并在那里注册 OpenClaw 号码。

**示例配置（专用号码，单用户允许列表）：**

```json5
{
  channels: {
    whatsapp: {
      dmPolicy: "allowlist",
      allowFrom: ["+15551234567"],
    },
  },
}
```

**配对模式（可选）：**
如果你想使用配对而不是允许列表，请将 `channels.whatsapp.dmPolicy` 设置为 `pairing`。未知发送者会收到配对码；使用以下命令批准：
`openclaw pairing approve whatsapp <code>`

### 个人号码（备选方案）

快速备选方案：在**你自己的号码**上运行 OpenClaw。给自己发消息（WhatsApp"给自己发消息"）进行测试，这样就不会打扰联系人。在设置和实验期间需要在主手机上阅读验证码。**必须启用自聊天模式。**
当向导询问你的个人 WhatsApp 号码时，输入你将用于发送消息的手机（所有者/发送者），而不是助手号码。

**示例配置（个人号码，自聊天）：**

```json
{
  "whatsapp": {
    "selfChatMode": true,
    "dmPolicy": "allowlist",
    "allowFrom": ["+15551234567"]
  }
}
```

当设置了 `identity.name` 时，自聊天回复默认为 `[{identity.name}]`（否则为 `[openclaw]`），
前提是 `messages.responsePrefix` 未设置。明确设置它可以自定义或禁用
前缀（使用 `""` 来移除）。

### 号码获取提示

- **本地 eSIM** 来自你所在国家的移动运营商（最可靠）
  - 奥地利：[hot.at](https://www.hot.at)
  - 英国：[giffgaff](https://www.giffgaff.com) — 免费 SIM 卡，无合约
- **预付费 SIM 卡** — 便宜，只需接收一条验证短信

**避免：** TextNow、Google Voice、大多数"免费短信"服务——WhatsApp 会积极封锁这些。

**提示：** 该号码只需要接收一条验证短信。之后，WhatsApp Web 会话通过 `creds.json` 持久化。

## 为什么不用 Twilio？

- 早期 OpenClaw 版本支持 Twilio 的 WhatsApp Business 集成。
- WhatsApp Business 号码不适合个人助手。
- Meta 强制执行 24 小时回复窗口；如果你在过去 24 小时内没有回复，商业号码无法发起新消息。
- 高频或"频繁"使用会触发激进的封锁，因为商业账户不适合发送大量个人助手消息。
- 结果：投递不可靠且频繁被封锁，因此该支持已被移除。

## 登录 + 凭证

- 登录命令：`openclaw channels login`（通过关联设备扫描二维码）。
- 多账户登录：`openclaw channels login --account <id>`（`<id>` = `accountId`）。
- 默认账户（省略 `--account` 时）：如果存在则为 `default`，否则为第一个配置的账户 id（排序后）。
- 凭证存储在 `~/.openclaw/credentials/whatsapp/<accountId>/creds.json`。
- 备份副本在 `creds.json.bak`（损坏时恢复）。
- 旧版兼容性：较旧的安装将 Baileys 文件直接存储在 `~/.openclaw/credentials/` 中。
- 登出：`openclaw channels logout`（或 `--account <id>`）删除 WhatsApp 认证状态（但保留共享的 `oauth.json`）。
- 已登出的 socket => 错误提示重新关联。

## 入站流程（私信 + 群组）

- WhatsApp 事件来自 `messages.upsert`（Baileys）。
- 收件箱监听器在关闭时分离，以避免在测试/重启时累积事件处理器。
- 状态/广播聊天被忽略。
- 直接聊天使用 E.164；群组使用群组 JID。
- **私信策略**：`channels.whatsapp.dmPolicy` 控制直接聊天访问（默认：`pairing`）。
  - 配对：未知发送者会收到配对码（通过 `openclaw pairing approve whatsapp <code>` 批准；码在 1 小时后过期）。
  - 开放：需要 `channels.whatsapp.allowFrom` 包含 `"*"`。
  - 你关联的 WhatsApp 号码是隐式信任的，因此自身消息会跳过 `channels.whatsapp.dmPolicy` 和 `channels.whatsapp.allowFrom` 检查。

### 个人号码模式（备选方案）

如果你在**个人 WhatsApp 号码**上运行 OpenClaw，请启用 `channels.whatsapp.selfChatMode`（见上面的示例）。

行为：

- 出站私信永远不会触发配对回复（防止打扰联系人）。
- 入站未知发送者仍遵循 `channels.whatsapp.dmPolicy`。
- 自聊天模式（allowFrom 包含你的号码）避免自动已读回执并忽略提及 JID。
- 非自聊天私信会发送已读回执。

## 已读回执

默认情况下，Gateway 网关在接受入站 WhatsApp 消息后将其标记为已读（蓝色勾号）。

全局禁用：

```json5
{
  channels: { whatsapp: { sendReadReceipts: false } },
}
```

按账户禁用：

```json5
{
  channels: {
    whatsapp: {
      accounts: {
        personal: { sendReadReceipts: false },
      },
    },
  },
}
```

注意事项：

- 自聊天模式始终跳过已读回执。

## WhatsApp 常见问题：发送消息 + 配对

**当我关联 WhatsApp 时，OpenClaw 会给随机联系人发消息吗？**
不会。默认私信策略是**配对**，因此未知发送者只会收到配对码，他们的消息**不会被处理**。OpenClaw 只会回复它收到的聊天，或你明确触发的发送（智能体/CLI）。

**WhatsApp 上的配对是如何工作的？**
配对是未知发送者的私信门控：

- 来自新发送者的第一条私信返回一个短码（消息不会被处理）。
- 使用以下命令批准：`openclaw pairing approve whatsapp <code>`（使用 `openclaw pairing list whatsapp` 列出）。
- 码在 1 小时后过期；每个渠道的待处理请求上限为 3 个。

**多个人可以在一个 WhatsApp 号码上使用不同的 OpenClaw 实例吗？**
可以，通过 `bindings` 将每个发送者路由到不同的智能体（peer `kind: "dm"`，发送者 E.164 如 `+15551234567`）。回复仍然来自**同一个 WhatsApp 账户**，直接聊天会折叠到每个智能体的主会话，因此**每人使用一个智能体**。私信访问控制（`dmPolicy`/`allowFrom`）是每个 WhatsApp 账户全局的。参见[多智能体路由](/concepts/multi-agent)。

**为什么向导会询问我的手机号码？**
向导使用它来设置你的**允许列表/所有者**，以便允许你自己的私信。它不会用于自动发送。如果你在个人 WhatsApp 号码上运行，请使用相同的号码并启用 `channels.whatsapp.selfChatMode`。

## 消息规范化（模型看到的内容）

- `Body` 是带有信封的当前消息正文。
- 引用回复上下文**始终附加**：
  ```
  [Replying to +1555 id:ABC123]
  <quoted text or <media:...>>
  [/Replying]
  ```
- 回复元数据也会设置：
  - `ReplyToId` = stanzaId
  - `ReplyToBody` = 引用正文或媒体占位符
  - `ReplyToSender` = 已知时为 E.164
- 纯媒体入站消息使用占位符：
  - `<media:image|video|audio|document|sticker>`

## 群组

- 群组映射到 `agent:<agentId>:whatsapp:group:<jid>` 会话。
- 群组策略：`channels.whatsapp.groupPolicy = open|disabled|allowlist`（默认 `allowlist`）。
- 激活模式：
  - `mention`（默认）：需要 @提及或正则匹配。
  - `always`：始终触发。
- `/activation mention|always` 仅限所有者，必须作为独立消息发送。
- 所有者 = `channels.whatsapp.allowFrom`（如果未设置则为自身 E.164）。
- **历史注入**（仅待处理）：
  - 最近*未处理*的消息（默认 50 条）插入在：
    `[Chat messages since your last reply - for context]`（已在会话中的消息不会重新注入）
  - 当前消息在：
    `[Current message - respond to this]`
  - 附加发送者后缀：`[from: Name (+E164)]`
- 群组元数据缓存 5 分钟（主题 + 参与者）。

## 回复投递（线程）

- WhatsApp Web 发送标准消息（当前 Gateway 网关无引用回复线程）。
- 此渠道忽略回复标签。

## 确认表情（收到时自动回应）

WhatsApp 可以在收到传入消息时立即自动发送表情回应，在机器人生成回复之前。这为用户提供即时反馈，表明他们的消息已收到。

**配置：**

```json
{
  "whatsapp": {
    "ackReaction": {
      "emoji": "👀",
      "direct": true,
      "group": "mentions"
    }
  }
}
```

**选项：**

- `emoji`（字符串）：用于确认的表情（例如"👀"、"✅"、"📨"）。为空或省略 = 功能禁用。
- `direct`（布尔值，默认：`true`）：在直接/私信聊天中发送表情回应。
- `group`（字符串，默认：`"mentions"`）：群聊行为：
  - `"always"`：对所有群消息做出回应（即使没有 @提及）
  - `"mentions"`：仅在机器人被 @提及时做出回应
  - `"never"`：从不在群组中做出回应

**按账户覆盖：**

```json
{
  "whatsapp": {
    "accounts": {
      "work": {
        "ackReaction": {
          "emoji": "✅",
          "direct": false,
          "group": "always"
        }
      }
    }
  }
}
```

**行为说明：**

- 表情回应在消息收到时**立即**发送，在输入指示器或机器人回复之前。
- 在 `requireMention: false`（激活：always）的群组中，`group: "mentions"` 会对所有消息做出回应（不仅仅是 @提及）。
- 即发即忘：表情回应失败会被记录但不会阻止机器人回复。
- 群组表情回应会自动包含参与者 JID。
- WhatsApp 忽略 `messages.ackReaction`；请改用 `channels.whatsapp.ackReaction`。

## 智能体工具（表情回应）

- 工具：`whatsapp`，带有 `react` 动作（`chatJid`、`messageId`、`emoji`，可选 `remove`）。
- 可选：`participant`（群组发送者）、`fromMe`（对自己的消息做出回应）、`accountId`（多账户）。
- 表情移除语义：参见 [/tools/reactions](/tools/reactions)。
- 工具门控：`channels.whatsapp.actions.reactions`（默认：启用）。

## 限制

- 出站文本按 `channels.whatsapp.textChunkLimit` 分块（默认 4000）。
- 可选换行分块：设置 `channels.whatsapp.chunkMode="newline"` 在长度分块之前按空行（段落边界）分割。
- 入站媒体保存受 `channels.whatsapp.mediaMaxMb` 限制（默认 50 MB）。
- 出站媒体项受 `agents.defaults.mediaMaxMb` 限制（默认 5 MB）。

## 出站发送（文本 + 媒体）

- 使用活跃的网页监听器；如果 Gateway 网关未运行则报错。
- 文本分块：每条消息最大 4k（可通过 `channels.whatsapp.textChunkLimit` 配置，可选 `channels.whatsapp.chunkMode`）。
- 媒体：
  - 支持图片/视频/音频/文档。
  - 音频作为 PTT 发送；`audio/ogg` => `audio/ogg; codecs=opus`。
  - 仅在第一个媒体项上添加标题。
  - 媒体获取支持 HTTP(S) 和本地路径。
  - 动画 GIF：WhatsApp 期望带有 `gifPlayback: true` 的 MP4 以实现内联循环。
    - CLI：`openclaw message send --media <mp4> --gif-playback`
    - Gateway 网关：`send` 参数包含 `gifPlayback: true`

## 语音消息（PTT 音频）

WhatsApp 将音频作为**语音消息**（PTT 气泡）发送。

- 最佳效果：OGG/Opus。OpenClaw 将 `audio/ogg` 重写为 `audio/ogg; codecs=opus`。
- WhatsApp 忽略 `[[audio_as_voice]]`（音频已作为语音消息发送）。

## 媒体限制 + 优化

- 默认出站上限：5 MB（每个媒体项）。
- 覆盖：`agents.defaults.mediaMaxMb`。
- 图片自动优化为上限以下的 JPEG（调整大小 + 质量扫描）。
- 超大媒体 => 错误；媒体回复降级为文本警告。

## 心跳

- **Gateway 网关心跳**记录连接健康状态（`web.heartbeatSeconds`，默认 60 秒）。
- **智能体心跳**可以按智能体配置（`agents.list[].heartbeat`）或通过
  `agents.defaults.heartbeat` 全局配置（当没有设置按智能体条目时的降级）。
  - 使用配置的心跳提示词（默认：`Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.`）+ `HEARTBEAT_OK` 跳过行为。
  - 投递默认为最后使用的渠道（或配置的目标）。

## 重连行为

- 退避策略：`web.reconnect`：
  - `initialMs`、`maxMs`、`factor`、`jitter`、`maxAttempts`。
- 如果达到 maxAttempts，网页监控停止（降级）。
- 已登出 => 停止并要求重新关联。

## 配置快速映射

- `channels.whatsapp.dmPolicy`（私信策略：pairing/allowlist/open/disabled）。
- `channels.whatsapp.selfChatMode`（同手机设置；机器人使用你的个人 WhatsApp 号码）。
- `channels.whatsapp.allowFrom`（私信允许列表）。WhatsApp 使用 E.164 手机号码（无用户名）。
- `channels.whatsapp.mediaMaxMb`（入站媒体保存上限）。
- `channels.whatsapp.ackReaction`（消息收到时的自动回应：`{emoji, direct, group}`）。
- `channels.whatsapp.accounts.<accountId>.*`（按账户设置 + 可选 `authDir`）。
- `channels.whatsapp.accounts.<accountId>.mediaMaxMb`（按账户入站媒体上限）。
- `channels.whatsapp.accounts.<accountId>.ackReaction`（按账户确认回应覆盖）。
- `channels.whatsapp.groupAllowFrom`（群组发送者允许列表）。
- `channels.whatsapp.groupPolicy`（群组策略）。
- `channels.whatsapp.historyLimit` / `channels.whatsapp.accounts.<accountId>.historyLimit`（群组历史上下文；`0` 禁用）。
- `channels.whatsapp.dmHistoryLimit`（私信历史限制，按用户轮次）。按用户覆盖：`channels.whatsapp.dms["<phone>"].historyLimit`。
- `channels.whatsapp.groups`（群组允许列表 + 提及门控默认值；使用 `"*"` 允许全部）
- `channels.whatsapp.actions.reactions`（门控 WhatsApp 工具表情回应）。
- `agents.list[].groupChat.mentionPatterns`（或 `messages.groupChat.mentionPatterns`）
- `messages.groupChat.historyLimit`
- `channels.whatsapp.messagePrefix`（入站前缀；按账户：`channels.whatsapp.accounts.<accountId>.messagePrefix`；已弃用：`messages.messagePrefix`）
- `messages.responsePrefix`（出站前缀）
- `agents.defaults.mediaMaxMb`
- `agents.defaults.heartbeat.every`
- `agents.defaults.heartbeat.model`（可选覆盖）
- `agents.defaults.heartbeat.target`
- `agents.defaults.heartbeat.to`
- `agents.defaults.heartbeat.session`
- `agents.list[].heartbeat.*`（按智能体覆盖）
- `session.*`（scope、idle、store、mainKey）
- `web.enabled`（为 false 时禁用渠道启动）
- `web.heartbeatSeconds`
- `web.reconnect.*`

## 日志 + 故障排除

- 子系统：`whatsapp/inbound`、`whatsapp/outbound`、`web-heartbeat`、`web-reconnect`。
- 日志文件：`/tmp/openclaw/openclaw-YYYY-MM-DD.log`（可配置）。
- 故障排除指南：[Gateway 网关故障排除](/gateway/troubleshooting)。

## 故障排除（快速）

**未关联 / 需要二维码登录**

- 症状：`channels status` 显示 `linked: false` 或警告"Not linked"。
- 修复：在 Gateway 网关主机上运行 `openclaw channels login` 并扫描二维码（WhatsApp → 设置 → 关联设备）。

**已关联但断开连接 / 重连循环**

- 症状：`channels status` 显示 `running, disconnected` 或警告"Linked but disconnected"。
- 修复：`openclaw doctor`（或重启 Gateway 网关）。如果问题持续，通过 `channels login` 重新关联并检查 `openclaw logs --follow`。

**Bun 运行时**

- **不推荐** Bun。WhatsApp（Baileys）和 Telegram 在 Bun 上不可靠。
  请使用 **Node** 运行 Gateway 网关。（参见入门指南运行时说明。）


---

## telegram

---
read_when:
  - 开发 Telegram 功能或 webhook
summary: Telegram 机器人支持状态、功能和配置
title: Telegram
x-i18n:
  generated_at: "2026-02-03T10:07:32Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 65da427e5f2383edb674054f8133a5777b2aae8a7c4bd78defa065124090a19c
  source_path: channels/telegram.md
  workflow: 15
---

# Telegram（Bot API）

状态：通过 grammY 支持机器人私信和群组，已可用于生产环境。默认使用长轮询；webhook 可选。

## 快速设置（入门）

1. 通过 **@BotFather**（[直达链接](https://t.me/BotFather)）创建机器人。确认用户名确实是 `@BotFather`，然后复制 token。
2. 设置 token：
   - 环境变量：`TELEGRAM_BOT_TOKEN=...`
   - 或配置：`channels.telegram.botToken: "..."`。
   - 如果两者都设置了，配置优先（环境变量回退仅适用于默认账户）。
3. 启动 Gateway 网关。
4. 私信访问默认使用配对模式；首次联系时需要批准配对码。

最小配置：

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
    },
  },
}
```

## 这是什么

- 一个由 Gateway 网关拥有的 Telegram Bot API 渠道。
- 确定性路由：回复返回到 Telegram；模型不会选择渠道。
- 私信共享智能体的主会话；群组保持隔离（`agent:<agentId>:telegram:group:<chatId>`）。

## 设置（快速路径）

### 1）创建机器人 token（BotFather）

1. 打开 Telegram 并与 **@BotFather**（[直达链接](https://t.me/BotFather)）对话。确认用户名确实是 `@BotFather`。
2. 运行 `/newbot`，然后按照提示操作（名称 + 以 `bot` 结尾的用户名）。
3. 复制 token 并安全保存。

可选的 BotFather 设置：

- `/setjoingroups` — 允许/拒绝将机器人添加到群组。
- `/setprivacy` — 控制机器人是否可以看到所有群组消息。

### 2）配置 token（环境变量或配置文件）

示例：

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
      groups: { "*": { requireMention: true } },
    },
  },
}
```

环境变量选项：`TELEGRAM_BOT_TOKEN=...`（适用于默认账户）。
如果环境变量和配置都设置了，配置优先。

多账户支持：使用 `channels.telegram.accounts`，每个账户有独立的 token 和可选的 `name`。参见 [`gateway/configuration`](/gateway/configuration#telegramaccounts--discordaccounts--slackaccounts--signalaccounts--imessageaccounts) 了解共享模式。

3. 启动 Gateway 网关。当 token 解析成功时 Telegram 启动（配置优先，环境变量回退）。
4. 私信访问默认为配对模式。机器人首次被联系时批准配对码。
5. 对于群组：添加机器人，决定隐私/管理员行为（见下文），然后设置 `channels.telegram.groups` 来控制提及门控和允许列表。

## Token + 隐私 + 权限（Telegram 端）

### Token 创建（BotFather）

- `/newbot` 创建机器人并返回 token（请保密）。
- 如果 token 泄露，通过 @BotFather 撤销/重新生成，并更新你的配置。

### 群组消息可见性（隐私模式）

Telegram 机器人默认启用**隐私模式**，这会限制它们接收哪些群组消息。
如果你的机器人必须看到*所有*群组消息，有两个选项：

- 使用 `/setprivacy` 禁用隐私模式**或**
- 将机器人添加为群组**管理员**（管理员机器人可以接收所有消息）。

**注意：** 当你切换隐私模式时，Telegram 要求将机器人从每个群组中移除并重新添加，更改才能生效。

### 群组权限（管理员权限）

管理员状态在群组内设置（Telegram UI）。管理员机器人始终接收所有群组消息，因此如果需要完全可见性，请使用管理员身份。

## 工作原理（行为）

- 入站消息被规范化为共享渠道信封，包含回复上下文和媒体占位符。
- 群组回复默认需要提及（原生 @提及或 `agents.list[].groupChat.mentionPatterns` / `messages.groupChat.mentionPatterns`）。
- 多智能体覆盖：在 `agents.list[].groupChat.mentionPatterns` 上设置每个智能体的模式。
- 回复始终路由回同一个 Telegram 聊天。
- 长轮询使用 grammY runner，每个聊天按顺序处理；总体并发受 `agents.defaults.maxConcurrent` 限制。
- Telegram Bot API 不支持已读回执；没有 `sendReadReceipts` 选项。

## 草稿流式传输

OpenClaw 可以在 Telegram 私信中使用 `sendMessageDraft` 流式传输部分回复。

要求：

- 在 @BotFather 中为机器人启用线程模式（论坛话题模式）。
- 仅限私聊线程（Telegram 在入站消息中包含 `message_thread_id`）。
- `channels.telegram.streamMode` 未设置为 `"off"`（默认：`"partial"`，`"block"` 启用分块草稿更新）。

草稿流式传输仅限私信；Telegram 在群组或频道中不支持此功能。

## 格式化（Telegram HTML）

- 出站 Telegram 文本使用 `parse_mode: "HTML"`（Telegram 支持的标签子集）。
- 类 Markdown 输入被渲染为 **Telegram 安全 HTML**（粗体/斜体/删除线/代码/链接）；块级元素被扁平化为带换行/项目符号的文本。
- 来自模型的原始 HTML 会被转义，以避免 Telegram 解析错误。
- 如果 Telegram 拒绝 HTML 负载，OpenClaw 会以纯文本重试相同的消息。

## 命令（原生 + 自定义）

OpenClaw 在启动时向 Telegram 的机器人菜单注册原生命令（如 `/status`、`/reset`、`/model`）。
你可以通过配置向菜单添加自定义命令：

```json5
{
  channels: {
    telegram: {
      customCommands: [
        { command: "backup", description: "Git 备份" },
        { command: "generate", description: "创建图片" },
      ],
    },
  },
}
```

## 故障排除

- 日志中出现 `setMyCommands failed` 通常意味着到 `api.telegram.org` 的出站 HTTPS/DNS 被阻止。
- 如果你看到 `sendMessage` 或 `sendChatAction` 失败，检查 IPv6 路由和 DNS。

更多帮助：[渠道故障排除](/channels/troubleshooting)。

注意：

- 自定义命令**仅是菜单条目**；除非你在其他地方处理它们，否则 OpenClaw 不会实现它们。
- 命令名称会被规范化（去除前导 `/`，转为小写），必须匹配 `a-z`、`0-9`、`_`（1-32 个字符）。
- 自定义命令**不能覆盖原生命令**。冲突会被忽略并记录日志。
- 如果禁用了 `commands.native`，则只注册自定义命令（如果没有则清空）。

## 限制

- 出站文本按 `channels.telegram.textChunkLimit` 分块（默认 4000）。
- 可选的换行分块：设置 `channels.telegram.chunkMode="newline"` 在长度分块之前按空行（段落边界）分割。
- 媒体下载/上传受 `channels.telegram.mediaMaxMb` 限制（默认 5）。
- Telegram Bot API 请求在 `channels.telegram.timeoutSeconds` 后超时（通过 grammY 默认 500）。设置较低的值以避免长时间挂起。
- 群组历史上下文使用 `channels.telegram.historyLimit`（或 `channels.telegram.accounts.*.historyLimit`），回退到 `messages.groupChat.historyLimit`。设置 `0` 禁用（默认 50）。
- 私信历史可以用 `channels.telegram.dmHistoryLimit`（用户轮次）限制。每用户覆盖：`channels.telegram.dms["<user_id>"].historyLimit`。

## 群组激活模式

默认情况下，机器人只响应群组中的提及（`@botname` 或 `agents.list[].groupChat.mentionPatterns` 中的模式）。要更改此行为：

### 通过配置（推荐）

```json5
{
  channels: {
    telegram: {
      groups: {
        "-1001234567890": { requireMention: false }, // 在此群组中始终响应
      },
    },
  },
}
```

**重要：** 设置 `channels.telegram.groups` 会创建一个**允许列表** - 只有列出的群组（或 `"*"`）会被接受。
论坛话题继承其父群组配置（allowFrom、requireMention、skills、prompts），除非你在 `channels.telegram.groups.<groupId>.topics.<topicId>` 下添加每话题覆盖。

要允许所有群组并始终响应：

```json5
{
  channels: {
    telegram: {
      groups: {
        "*": { requireMention: false }, // 所有群组，始终响应
      },
    },
  },
}
```

要保持所有群组仅提及响应（默认行为）：

```json5
{
  channels: {
    telegram: {
      groups: {
        "*": { requireMention: true }, // 或完全省略 groups
      },
    },
  },
}
```

### 通过命令（会话级别）

在群组中发送：

- `/activation always` - 响应所有消息
- `/activation mention` - 需要提及（默认）

**注意：** 命令只更新会话状态。要在重启后保持持久行为，请使用配置。

### 获取群组聊天 ID

将群组中的任何消息转发给 Telegram 上的 `@userinfobot` 或 `@getidsbot` 以查看聊天 ID（负数，如 `-1001234567890`）。

**提示：** 要获取你自己的用户 ID，私信机器人，它会回复你的用户 ID（配对消息），或者在命令启用后使用 `/whoami`。

**隐私注意：** `@userinfobot` 是第三方机器人。如果你更倾向于其他方式，将机器人添加到群组，发送一条消息，然后使用 `openclaw logs --follow` 读取 `chat.id`，或使用 Bot API `getUpdates`。

## 配置写入

默认情况下，Telegram 允许写入由渠道事件或 `/config set|unset` 触发的配置更新。

这发生在以下情况：

- 群组升级为超级群组，Telegram 发出 `migrate_to_chat_id`（聊天 ID 更改）。OpenClaw 可以自动迁移 `channels.telegram.groups`。
- 你在 Telegram 聊天中运行 `/config set` 或 `/config unset`（需要 `commands.config: true`）。

禁用方式：

```json5
{
  channels: { telegram: { configWrites: false } },
}
```

## 话题（论坛超级群组）

Telegram 论坛话题在每条消息中包含 `message_thread_id`。OpenClaw：

- 将 `:topic:<threadId>` 附加到 Telegram 群组会话键，使每个话题隔离。
- 发送输入指示器和回复时带上 `message_thread_id`，使响应保持在话题内。
- 通用话题（线程 id `1`）是特殊的：消息发送省略 `message_thread_id`（Telegram 会拒绝），但输入指示器仍然包含它。
- 在模板上下文中暴露 `MessageThreadId` + `IsForum` 用于路由/模板。
- 话题特定配置可在 `channels.telegram.groups.<chatId>.topics.<threadId>` 下设置（skills、允许列表、自动回复、系统提示、禁用）。
- 话题配置继承群组设置（requireMention、允许列表、skills、提示、enabled），除非每话题覆盖。

私聊在某些边缘情况下可能包含 `message_thread_id`。OpenClaw 保持私信会话键不变，但在存在线程 id 时仍将其用于回复/草稿流式传输。

## 内联按钮

Telegram 支持带回调按钮的内联键盘。

```json5
{
  channels: {
    telegram: {
      capabilities: {
        inlineButtons: "allowlist",
      },
    },
  },
}
```

对于每账户配置：

```json5
{
  channels: {
    telegram: {
      accounts: {
        main: {
          capabilities: {
            inlineButtons: "allowlist",
          },
        },
      },
    },
  },
}
```

作用域：

- `off` — 禁用内联按钮
- `dm` — 仅私信（群组目标被阻止）
- `group` — 仅群组（私信目标被阻止）
- `all` — 私信 + 群组
- `allowlist` — 私信 + 群组，但仅限 `allowFrom`/`groupAllowFrom` 允许的发送者（与控制命令规则相同）

默认：`allowlist`。
旧版：`capabilities: ["inlineButtons"]` = `inlineButtons: "all"`。

### 发送按钮

使用带 `buttons` 参数的消息工具：

```json5
{
  action: "send",
  channel: "telegram",
  to: "123456789",
  message: "选择一个选项：",
  buttons: [
    [
      { text: "是", callback_data: "yes" },
      { text: "否", callback_data: "no" },
    ],
    [{ text: "取消", callback_data: "cancel" }],
  ],
}
```

当用户点击按钮时，回调数据会以以下格式作为消息发送回智能体：
`callback_data: value`

### 配置选项

Telegram 功能可以在两个级别配置（上面显示的对象形式；旧版字符串数组仍然支持）：

- `channels.telegram.capabilities`：应用于所有 Telegram 账户的全局默认功能配置，除非被覆盖。
- `channels.telegram.accounts.<account>.capabilities`：每账户功能，覆盖该特定账户的全局默认值。

当所有 Telegram 机器人/账户应具有相同行为时使用全局设置。当不同机器人需要不同行为时使用每账户配置（例如，一个账户只处理私信，而另一个允许在群组中使用）。

## 访问控制（私信 + 群组）

### 私信访问

- 默认：`channels.telegram.dmPolicy = "pairing"`。未知发送者收到配对码；在批准之前消息被忽略（配对码 1 小时后过期）。
- 批准方式：
  - `openclaw pairing list telegram`
  - `openclaw pairing approve telegram <CODE>`
- 配对是 Telegram 私信使用的默认 token 交换。详情：[配对](/channels/pairing)
- `channels.telegram.allowFrom` 接受数字用户 ID（推荐）或 `@username` 条目。这**不是**机器人用户名；使用人类发送者的 ID。向导接受 `@username` 并在可能时将其解析为数字 ID。

#### 查找你的 Telegram 用户 ID

更安全（无第三方机器人）：

1. 启动 Gateway 网关并私信你的机器人。
2. 运行 `openclaw logs --follow` 并查找 `from.id`。

备选（官方 Bot API）：

1. 私信你的机器人。
2. 使用你的机器人 token 获取更新并读取 `message.from.id`：
   ```bash
   curl "https://api.telegram.org/bot<bot_token>/getUpdates"
   ```

第三方（隐私性较低）：

- 私信 `@userinfobot` 或 `@getidsbot` 并使用返回的用户 id。

### 群组访问

两个独立的控制：

**1. 允许哪些群组**（通过 `channels.telegram.groups` 的群组允许列表）：

- 无 `groups` 配置 = 允许所有群组
- 有 `groups` 配置 = 只允许列出的群组或 `"*"`
- 示例：`"groups": { "-1001234567890": {}, "*": {} }` 允许所有群组

**2. 允许哪些发送者**（通过 `channels.telegram.groupPolicy` 的发送者过滤）：

- `"open"` = 允许群组中的所有发送者发消息
- `"allowlist"` = 只有 `channels.telegram.groupAllowFrom` 中的发送者可以发消息
- `"disabled"` = 不接受任何群组消息
  默认是 `groupPolicy: "allowlist"`（除非添加 `groupAllowFrom` 否则被阻止）。

大多数用户需要：`groupPolicy: "allowlist"` + `groupAllowFrom` + 在 `channels.telegram.groups` 中列出特定群组

## 长轮询 vs webhook

- 默认：长轮询（不需要公共 URL）。
- Webhook 模式：设置 `channels.telegram.webhookUrl` 和 `channels.telegram.webhookSecret`（可选 `channels.telegram.webhookPath`）。
  - 本地监听器绑定到 `0.0.0.0:8787`，默认服务于 `POST /telegram-webhook`。
  - 如果你的公共 URL 不同，使用反向代理并将 `channels.telegram.webhookUrl` 指向公共端点。

## 回复线程

Telegram 通过标签支持可选的线程回复：

- `[[reply_to_current]]` -- 回复触发消息。
- `[[reply_to:<id>]]` -- 回复特定消息 id。

通过 `channels.telegram.replyToMode` 控制：

- `first`（默认）、`all`、`off`。

## 音频消息（语音 vs 文件）

Telegram 区分**语音备忘录**（圆形气泡）和**音频文件**（元数据卡片）。
OpenClaw 默认使用音频文件以保持向后兼容性。

要在智能体回复中强制使用语音备忘录气泡，在回复中的任何位置包含此标签：

- `[[audio_as_voice]]` — 将音频作为语音备忘录而不是文件发送。

该标签会从发送的文本中去除。其他渠道会忽略此标签。

对于消息工具发送，设置 `asVoice: true` 并配合兼容语音的音频 `media` URL（当存在 media 时 `message` 是可选的）：

```json5
{
  action: "send",
  channel: "telegram",
  to: "123456789",
  media: "https://example.com/voice.ogg",
  asVoice: true,
}
```

## 贴纸

OpenClaw 支持接收和发送 Telegram 贴纸，并具有智能缓存功能。

### 接收贴纸

当用户发送贴纸时，OpenClaw 根据贴纸类型处理：

- **静态贴纸（WEBP）：** 下载并通过视觉处理。贴纸在消息内容中显示为 `<media:sticker>` 占位符。
- **动画贴纸（TGS）：** 跳过（Lottie 格式不支持处理）。
- **视频贴纸（WEBM）：** 跳过（视频格式不支持处理）。

接收贴纸时可用的模板上下文字段：

- `Sticker` — 包含以下属性的对象：
  - `emoji` — 与贴纸关联的表情符号
  - `setName` — 贴纸集名称
  - `fileId` — Telegram 文件 ID（用于发送相同贴纸）
  - `fileUniqueId` — 用于缓存查找的稳定 ID
  - `cachedDescription` — 可用时的缓存视觉描述

### 贴纸缓存

贴纸通过 AI 的视觉功能处理以生成描述。由于相同的贴纸经常重复发送，OpenClaw 缓存这些描述以避免冗余的 API 调用。

**工作原理：**

1. **首次遇到：** 贴纸图像被发送给 AI 进行视觉分析。AI 生成描述（例如"一只卡通猫热情地挥手"）。
2. **缓存存储：** 描述与贴纸的文件 ID、表情符号和集合名称一起保存。
3. **后续遇到：** 当再次看到相同贴纸时，直接使用缓存的描述。图像不会发送给 AI。

**缓存位置：** `~/.openclaw/telegram/sticker-cache.json`

**缓存条目格式：**

```json
{
  "fileId": "CAACAgIAAxkBAAI...",
  "fileUniqueId": "AgADBAADb6cxG2Y",
  "emoji": "👋",
  "setName": "CoolCats",
  "description": "一只卡通猫热情地挥手",
  "cachedAt": "2026-01-15T10:30:00.000Z"
}
```

**优点：**

- 通过避免对相同贴纸重复调用视觉 API 来降低 API 成本
- 缓存贴纸响应更快（无视觉处理延迟）
- 基于缓存描述启用贴纸搜索功能

缓存在接收贴纸时自动填充。无需手动缓存管理。

### 发送贴纸

智能体可以使用 `sticker` 和 `sticker-search` 动作发送和搜索贴纸。这些默认禁用，必须在配置中启用：

```json5
{
  channels: {
    telegram: {
      actions: {
        sticker: true,
      },
    },
  },
}
```

**发送贴纸：**

```json5
{
  action: "sticker",
  channel: "telegram",
  to: "123456789",
  fileId: "CAACAgIAAxkBAAI...",
}
```

参数：

- `fileId`（必需）— 贴纸的 Telegram 文件 ID。从接收贴纸时的 `Sticker.fileId` 获取，或从 `sticker-search` 结果获取。
- `replyTo`（可选）— 要回复的消息 ID。
- `threadId`（可选）— 论坛话题的消息线程 ID。

**搜索贴纸：**

智能体可以按描述、表情符号或集合名称搜索缓存的贴纸：

```json5
{
  action: "sticker-search",
  channel: "telegram",
  query: "猫 挥手",
  limit: 5,
}
```

返回缓存中匹配的贴纸：

```json5
{
  ok: true,
  count: 2,
  stickers: [
    {
      fileId: "CAACAgIAAxkBAAI...",
      emoji: "👋",
      description: "一只卡通猫热情地挥手",
      setName: "CoolCats",
    },
  ],
}
```

搜索在描述文本、表情符号字符和集合名称之间使用模糊匹配。

**带线程的示例：**

```json5
{
  action: "sticker",
  channel: "telegram",
  to: "-1001234567890",
  fileId: "CAACAgIAAxkBAAI...",
  replyTo: 42,
  threadId: 123,
}
```

## 流式传输（草稿）

Telegram 可以在智能体生成响应时流式传输**草稿气泡**。
OpenClaw 使用 Bot API `sendMessageDraft`（不是真实消息），然后将最终回复作为普通消息发送。

要求（Telegram Bot API 9.3+）：

- **启用话题的私聊**（机器人的论坛话题模式）。
- 入站消息必须包含 `message_thread_id`（私有话题线程）。
- 群组/超级群组/频道的流式传输被忽略。

配置：

- `channels.telegram.streamMode: "off" | "partial" | "block"`（默认：`partial`）
  - `partial`：用最新的流式文本更新草稿气泡。
  - `block`：以较大块（分块）更新草稿气泡。
  - `off`：禁用草稿流式传输。
- 可选（仅用于 `streamMode: "block"`）：
  - `channels.telegram.draftChunk: { minChars?, maxChars?, breakPreference? }`
    - 默认值：`minChars: 200`、`maxChars: 800`、`breakPreference: "paragraph"`（限制在 `channels.telegram.textChunkLimit` 内）。

注意：草稿流式传输与**分块流式传输**（渠道消息）不同。
分块流式传输默认关闭，如果你想要早期 Telegram 消息而不是草稿更新，需要 `channels.telegram.blockStreaming: true`。

推理流（仅限 Telegram）：

- `/reasoning stream` 在回复生成时将推理流式传输到草稿气泡中，然后发送不带推理的最终答案。
- 如果 `channels.telegram.streamMode` 为 `off`，推理流被禁用。
  更多上下文：[流式传输 + 分块](/concepts/streaming)。

## 重试策略

出站 Telegram API 调用在遇到临时网络/429 错误时会以指数退避和抖动进行重试。通过 `channels.telegram.retry` 配置。参见[重试策略](/concepts/retry)。

## 智能体工具（消息 + 反应）

- 工具：`telegram`，使用 `sendMessage` 动作（`to`、`content`，可选 `mediaUrl`、`replyToMessageId`、`messageThreadId`）。
- 工具：`telegram`，使用 `react` 动作（`chatId`、`messageId`、`emoji`）。
- 工具：`telegram`，使用 `deleteMessage` 动作（`chatId`、`messageId`）。
- 反应移除语义：参见 [/tools/reactions](/tools/reactions)。
- 工具门控：`channels.telegram.actions.reactions`、`channels.telegram.actions.sendMessage`、`channels.telegram.actions.deleteMessage`（默认：启用），以及 `channels.telegram.actions.sticker`（默认：禁用）。

## 反应通知

**反应工作原理：**
Telegram 反应作为**单独的 `message_reaction` 事件**到达，而不是消息负载中的属性。当用户添加反应时，OpenClaw：

1. 从 Telegram API 接收 `message_reaction` 更新
2. 将其转换为**系统事件**，格式为：`"Telegram reaction added: {emoji} by {user} on msg {id}"`
3. 使用与常规消息**相同的会话键**将系统事件加入队列
4. 当该对话中的下一条消息到达时，系统事件被排出并前置到智能体的上下文中

智能体将反应视为对话历史中的**系统通知**，而不是消息元数据。

**配置：**

- `channels.telegram.reactionNotifications`：控制哪些反应触发通知
  - `"off"` — 忽略所有反应
  - `"own"` — 当用户对机器人消息做出反应时通知（尽力而为；内存中）（默认）
  - `"all"` — 通知所有反应

- `channels.telegram.reactionLevel`：控制智能体的反应能力
  - `"off"` — 智能体不能对消息做出反应
  - `"ack"` — 机器人发送确认反应（处理时显示 👀）（默认）
  - `"minimal"` — 智能体可以少量反应（指导：每 5-10 次交换 1 次）
  - `"extensive"` — 智能体可以在适当时自由反应

**论坛群组：** 论坛群组中的反应包含 `message_thread_id`，使用类似 `agent:main:telegram:group:{chatId}:topic:{threadId}` 的会话键。这确保同一话题中的反应和消息保持在一起。

**示例配置：**

```json5
{
  channels: {
    telegram: {
      reactionNotifications: "all", // 查看所有反应
      reactionLevel: "minimal", // 智能体可以少量反应
    },
  },
}
```

**要求：**

- Telegram 机器人必须在 `allowed_updates` 中明确请求 `message_reaction`（由 OpenClaw 自动配置）
- 对于 webhook 模式，反应包含在 webhook `allowed_updates` 中
- 对于轮询模式，反应包含在 `getUpdates` `allowed_updates` 中

## 投递目标（CLI/cron）

- 使用聊天 id（`123456789`）或用户名（`@name`）作为目标。
- 示例：`openclaw message send --channel telegram --target 123456789 --message "hi"`。

## 故障排除

**机器人不响应群组中的非提及消息：**

- 如果你设置了 `channels.telegram.groups.*.requireMention=false`，Telegram 的 Bot API **隐私模式**必须禁用。
  - BotFather：`/setprivacy` → **Disable**（然后从群组中移除并重新添加机器人）
- `openclaw channels status` 在配置期望未提及群组消息时显示警告。
- `openclaw channels status --probe` 可以额外检查显式数字群组 ID 的成员资格（它无法审计通配符 `"*"` 规则）。
- 快速测试：`/activation always`（仅会话级别；使用配置以持久化）

**机器人完全看不到群组消息：**

- 如果设置了 `channels.telegram.groups`，群组必须被列出或使用 `"*"`
- 在 @BotFather 中检查隐私设置 →"Group Privacy"应为 **OFF**
- 验证机器人确实是成员（不仅仅是没有读取权限的管理员）
- 检查 Gateway 网关日志：`openclaw logs --follow`（查找"skipping group message"）

**机器人响应提及但不响应 `/activation always`：**

- `/activation` 命令更新会话状态但不持久化到配置
- 要持久化行为，将群组添加到 `channels.telegram.groups` 并设置 `requireMention: false`

**像 `/status` 这样的命令不起作用：**

- 确保你的 Telegram 用户 ID 已授权（通过配对或 `channels.telegram.allowFrom`）
- 即使在 `groupPolicy: "open"` 的群组中，命令也需要授权

**长轮询在 Node 22+ 上立即中止（通常与代理/自定义 fetch 有关）：**

- Node 22+ 对 `AbortSignal` 实例更严格；外部信号可以立即中止 `fetch` 调用。
- 升级到规范化中止信号的 OpenClaw 构建版本，或在可以升级之前在 Node 20 上运行 Gateway 网关。

**机器人启动后静默停止响应（或日志显示 `HttpError: Network request ... failed`）：**

- 某些主机首先将 `api.telegram.org` 解析为 IPv6。如果你的服务器没有可用的 IPv6 出口，grammY 可能会卡在仅 IPv6 的请求上。
- 通过启用 IPv6 出口**或**强制 `api.telegram.org` 使用 IPv4 解析来修复（例如，使用 IPv4 A 记录添加 `/etc/hosts` 条目，或在你的 OS DNS 堆栈中优先使用 IPv4），然后重启 Gateway 网关。
- 快速检查：`dig +short api.telegram.org A` 和 `dig +short api.telegram.org AAAA` 确认 DNS 返回的内容。

## 配置参考（Telegram）

完整配置：[配置](/gateway/configuration)

提供商选项：

- `channels.telegram.enabled`：启用/禁用渠道启动。
- `channels.telegram.botToken`：机器人 token（BotFather）。
- `channels.telegram.tokenFile`：从文件路径读取 token。
- `channels.telegram.dmPolicy`：`pairing | allowlist | open | disabled`（默认：pairing）。
- `channels.telegram.allowFrom`：私信允许列表（id/用户名）。`open` 需要 `"*"`。
- `channels.telegram.groupPolicy`：`open | allowlist | disabled`（默认：allowlist）。
- `channels.telegram.groupAllowFrom`：群组发送者允许列表（id/用户名）。
- `channels.telegram.groups`：每群组默认值 + 允许列表（使用 `"*"` 作为全局默认值）。
  - `channels.telegram.groups.<id>.requireMention`：提及门控默认值。
  - `channels.telegram.groups.<id>.skills`：skill 过滤器（省略 = 所有 skills，空 = 无）。
  - `channels.telegram.groups.<id>.allowFrom`：每群组发送者允许列表覆盖。
  - `channels.telegram.groups.<id>.systemPrompt`：群组的额外系统提示。
  - `channels.telegram.groups.<id>.enabled`：为 `false` 时禁用群组。
  - `channels.telegram.groups.<id>.topics.<threadId>.*`：每话题覆盖（与群组相同的字段）。
  - `channels.telegram.groups.<id>.topics.<threadId>.requireMention`：每话题提及门控覆盖。
- `channels.telegram.capabilities.inlineButtons`：`off | dm | group | all | allowlist`（默认：allowlist）。
- `channels.telegram.accounts.<account>.capabilities.inlineButtons`：每账户覆盖。
- `channels.telegram.replyToMode`：`off | first | all`（默认：`off`）。
- `channels.telegram.textChunkLimit`：出站分块大小（字符）。
- `channels.telegram.chunkMode`：`length`（默认）或 `newline` 在长度分块之前按空行（段落边界）分割。
- `channels.telegram.linkPreview`：切换出站消息的链接预览（默认：true）。
- `channels.telegram.streamMode`：`off | partial | block`（草稿流式传输）。
- `channels.telegram.mediaMaxMb`：入站/出站媒体上限（MB）。
- `channels.telegram.retry`：出站 Telegram API 调用的重试策略（attempts、minDelayMs、maxDelayMs、jitter）。
- `channels.telegram.network.autoSelectFamily`：覆盖 Node autoSelectFamily（true=启用，false=禁用）。在 Node 22 上默认禁用以避免 Happy Eyeballs 超时。
- `channels.telegram.proxy`：Bot API 调用的代理 URL（SOCKS/HTTP）。
- `channels.telegram.webhookUrl`：启用 webhook 模式（需要 `channels.telegram.webhookSecret`）。
- `channels.telegram.webhookSecret`：webhook 密钥（设置 webhookUrl 时必需）。
- `channels.telegram.webhookPath`：本地 webhook 路径（默认 `/telegram-webhook`）。
- `channels.telegram.actions.reactions`：门控 Telegram 工具反应。
- `channels.telegram.actions.sendMessage`：门控 Telegram 工具消息发送。
- `channels.telegram.actions.deleteMessage`：门控 Telegram 工具消息删除。
- `channels.telegram.actions.sticker`：门控 Telegram 贴纸动作 — 发送和搜索（默认：false）。
- `channels.telegram.reactionNotifications`：`off | own | all` — 控制哪些反应触发系统事件（未设置时默认：`own`）。
- `channels.telegram.reactionLevel`：`off | ack | minimal | extensive` — 控制智能体的反应能力（未设置时默认：`minimal`）。

相关全局选项：

- `agents.list[].groupChat.mentionPatterns`（提及门控模式）。
- `messages.groupChat.mentionPatterns`（全局回退）。
- `commands.native`（默认为 `"auto"` → Telegram/Discord 开启，Slack 关闭）、`commands.text`、`commands.useAccessGroups`（命令行为）。使用 `channels.telegram.commands.native` 覆盖。
- `messages.responsePrefix`、`messages.ackReaction`、`messages.ackReactionScope`、`messages.removeAckAfterReply`。


---

## feishu

---
summary: "飞书机器人支持状态、功能和配置"
read_when:
  - 您想要连接飞书机器人
  - 您正在配置飞书渠道
title: 飞书
---

# 飞书机器人

状态：生产就绪，支持机器人私聊和群组。使用 WebSocket 长连接模式接收消息。

---

## 需要插件

安装 Feishu 插件：

```bash
openclaw plugins install @openclaw/feishu
```

本地 checkout（在 git 仓库内运行）：

```bash
openclaw plugins install ./extensions/feishu
```

---

## 快速开始

添加飞书渠道有两种方式：

### 方式一：通过安装向导添加（推荐）

如果您刚安装完 OpenClaw，可以直接运行向导，根据提示添加飞书：

```bash
openclaw onboard
```

向导会引导您完成：

1. 创建飞书应用并获取凭证
2. 配置应用凭证
3. 启动网关

✅ **完成配置后**，您可以使用以下命令检查网关状态：

- `openclaw gateway status` - 查看网关运行状态
- `openclaw logs --follow` - 查看实时日志

### 方式二：通过命令行添加

如果您已经完成了初始安装，可以用以下命令添加飞书渠道：

```bash
openclaw channels add
```

然后根据交互式提示选择 Feishu，输入 App ID 和 App Secret 即可。

✅ **完成配置后**，您可以使用以下命令管理网关：

- `openclaw gateway status` - 查看网关运行状态
- `openclaw gateway restart` - 重启网关以应用新配置
- `openclaw logs --follow` - 查看实时日志

---

## 第一步：创建飞书应用

### 1. 打开飞书开放平台

访问 [飞书开放平台](https://open.feishu.cn/app)，使用飞书账号登录。

Lark（国际版）请使用 https://open.larksuite.com/app，并在配置中设置 `domain: "lark"`。

### 2. 创建应用

1. 点击 **创建企业自建应用**
2. 填写应用名称和描述
3. 选择应用图标

![创建企业自建应用](/images/feishu-step2-create-app.png)

### 3. 获取应用凭证

在应用的 **凭证与基础信息** 页面，复制：

- **App ID**（格式如 `cli_xxx`）
- **App Secret**

❗ **重要**：请妥善保管 App Secret，不要分享给他人。

![获取应用凭证](/images/feishu-step3-credentials.png)

### 4. 配置应用权限

在 **权限管理** 页面，点击 **批量导入** 按钮，粘贴以下 JSON 配置一键导入所需权限：

```json
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "docs:document.content:read",
      "event:ip_list",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource",
      "sheets:spreadsheet",
      "wiki:wiki:readonly"
    ],
    "user": ["aily:file:read", "aily:file:write", "im:chat.access_event.bot_p2p_chat:read"]
  }
}
```

![配置应用权限](/images/feishu-step4-permissions.png)

### 5. 启用机器人能力

在 **应用能力** > **机器人** 页面：

1. 开启机器人能力
2. 配置机器人名称

![启用机器人能力](/images/feishu-step5-bot-capability.png)

### 6. 配置事件订阅

⚠️ **重要提醒**：在配置事件订阅前，请务必确保已完成以下步骤：

1. 运行 `openclaw channels add` 添加了 Feishu 渠道
2. 网关处于启动状态（可通过 `openclaw gateway status` 检查状态）

在 **事件订阅** 页面：

1. 选择 **使用长连接接收事件**（WebSocket 模式）
2. 添加事件：`im.message.receive_v1`（接收消息）

⚠️ **注意**：如果网关未启动或渠道未添加，长连接设置将保存失败。

![配置事件订阅](/images/feishu-step6-event-subscription.png)

### 7. 发布应用

1. 在 **版本管理与发布** 页面创建版本
2. 提交审核并发布
3. 等待管理员审批（企业自建应用通常自动通过）

---

## 第二步：配置 OpenClaw

### 通过向导配置（推荐）

运行以下命令，根据提示粘贴 App ID 和 App Secret：

```bash
openclaw channels add
```

选择 **Feishu**，然后输入您在第一步获取的凭证即可。

### 通过配置文件配置

编辑 `~/.openclaw/openclaw.json`：

```json5
{
  channels: {
    feishu: {
      enabled: true,
      dmPolicy: "pairing",
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
          botName: "我的AI助手",
        },
      },
    },
  },
}
```

### 通过环境变量配置

```bash
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

### Lark（国际版）域名

如果您的租户在 Lark（国际版），请设置域名为 `lark`（或完整域名），可配置 `channels.feishu.domain` 或 `channels.feishu.accounts.<id>.domain`：

```json5
{
  channels: {
    feishu: {
      domain: "lark",
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
        },
      },
    },
  },
}
```

---

## 第三步：启动并测试

### 1. 启动网关

```bash
openclaw gateway
```

### 2. 发送测试消息

在飞书中找到您创建的机器人，发送一条消息。

### 3. 配对授权

默认情况下，机器人会回复一个 **配对码**。您需要批准此代码：

```bash
openclaw pairing approve feishu <配对码>
```

批准后即可正常对话。

---

## 介绍

- **飞书机器人渠道**：由网关管理的飞书机器人
- **确定性路由**：回复始终返回飞书，模型不会选择渠道
- **会话隔离**：私聊共享主会话；群组独立隔离
- **WebSocket 连接**：使用飞书 SDK 的长连接模式，无需公网 URL

---

## 访问控制

### 私聊访问

- **默认**：`dmPolicy: "pairing"`，陌生用户会收到配对码
- **批准配对**：
  ```bash
  openclaw pairing list feishu      # 查看待审批列表
  openclaw pairing approve feishu <CODE>  # 批准
  ```
- **白名单模式**：通过 `channels.feishu.allowFrom` 配置允许的用户 Open ID

### 群组访问

**1. 群组策略**（`channels.feishu.groupPolicy`）：

- `"open"` = 允许群组中所有人（默认）
- `"allowlist"` = 仅允许 `groupAllowFrom` 中的用户
- `"disabled"` = 禁用群组消息

**2. @提及要求**（`channels.feishu.groups.<chat_id>.requireMention`）：

- `true` = 需要 @机器人才响应（默认）
- `false` = 无需 @也响应

---

## 群组配置示例

### 允许所有群组，需要 @提及（默认行为）

```json5
{
  channels: {
    feishu: {
      groupPolicy: "open",
      // 默认 requireMention: true
    },
  },
}
```

### 允许所有群组，无需 @提及

需要为特定群组配置：

```json5
{
  channels: {
    feishu: {
      groups: {
        oc_xxx: { requireMention: false },
      },
    },
  },
}
```

### 仅允许特定用户在群组中使用

```json5
{
  channels: {
    feishu: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["ou_xxx", "ou_yyy"],
    },
  },
}
```

---

## 获取群组/用户 ID

### 获取群组 ID（chat_id）

群组 ID 格式为 `oc_xxx`，可以通过以下方式获取：

**方法一**（推荐）：

1. 启动网关并在群组中 @机器人发消息
2. 运行 `openclaw logs --follow` 查看日志中的 `chat_id`

**方法二**：
使用飞书 API 调试工具获取机器人所在群组列表。

### 获取用户 ID（open_id）

用户 ID 格式为 `ou_xxx`，可以通过以下方式获取：

**方法一**（推荐）：

1. 启动网关并给机器人发消息
2. 运行 `openclaw logs --follow` 查看日志中的 `open_id`

**方法二**：
查看配对请求列表，其中包含用户的 Open ID：

```bash
openclaw pairing list feishu
```

---

## 常用命令

| 命令      | 说明           |
| --------- | -------------- |
| `/status` | 查看机器人状态 |
| `/reset`  | 重置对话会话   |
| `/model`  | 查看/切换模型  |

> 注意：飞书目前不支持原生命令菜单，命令需要以文本形式发送。

## 网关管理命令

在配置和使用飞书渠道时，您可能需要使用以下网关管理命令：

| 命令                       | 说明              |
| -------------------------- | ----------------- |
| `openclaw gateway status`  | 查看网关运行状态  |
| `openclaw gateway install` | 安装/启动网关服务 |
| `openclaw gateway stop`    | 停止网关服务      |
| `openclaw gateway restart` | 重启网关服务      |
| `openclaw logs --follow`   | 实时查看日志输出  |

---

## 故障排除

### 机器人在群组中不响应

1. 检查机器人是否已添加到群组
2. 检查是否 @了机器人（默认需要 @提及）
3. 检查 `groupPolicy` 是否为 `"disabled"`
4. 查看日志：`openclaw logs --follow`

### 机器人收不到消息

1. 检查应用是否已发布并审批通过
2. 检查事件订阅是否配置正确（`im.message.receive_v1`）
3. 检查是否选择了 **长连接** 模式
4. 检查应用权限是否完整
5. 检查网关是否正在运行：`openclaw gateway status`
6. 查看实时日志：`openclaw logs --follow`

### App Secret 泄露怎么办

1. 在飞书开放平台重置 App Secret
2. 更新配置文件中的 App Secret
3. 重启网关

### 发送消息失败

1. 检查应用是否有 `im:message:send_as_bot` 权限
2. 检查应用是否已发布
3. 查看日志获取详细错误信息

---

## 高级配置

### 多账号配置

如果需要管理多个飞书机器人：

```json5
{
  channels: {
    feishu: {
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
          botName: "主机器人",
        },
        backup: {
          appId: "cli_yyy",
          appSecret: "yyy",
          botName: "备用机器人",
          enabled: false, // 暂时禁用
        },
      },
    },
  },
}
```

### 消息限制

- `textChunkLimit`：出站文本分块大小（默认 2000 字符）
- `mediaMaxMb`：媒体上传/下载限制（默认 30MB）

### 流式输出

飞书支持通过交互式卡片实现流式输出，机器人会实时更新卡片内容显示生成进度。默认配置：

```json5
{
  channels: {
    feishu: {
      streaming: true, // 启用流式卡片输出（默认 true）
      blockStreaming: true, // 启用块级流式（默认 true）
    },
  },
}
```

如需禁用流式输出（等待完整回复后一次性发送），可设置 `streaming: false`。

### 消息引用

在群聊中，机器人的回复可以引用用户发送的原始消息，让对话上下文更加清晰。

配置选项：

```json5
{
  channels: {
    feishu: {
      // 账户级别配置（默认 "all"）
      replyToMode: "all",
      groups: {
        oc_xxx: {
          // 特定群组可以覆盖
          replyToMode: "first",
        },
      },
    },
  },
}
```

`replyToMode` 值说明：

| 值        | 行为                               |
| --------- | ---------------------------------- |
| `"off"`   | 不引用原消息（私聊默认值）         |
| `"first"` | 仅在第一条回复时引用原消息         |
| `"all"`   | 所有回复都引用原消息（群聊默认值） |

> 注意：消息引用功能与流式卡片输出（`streaming: true`）不能同时使用。当启用流式输出时，回复会以卡片形式呈现，不会显示引用。

### 多 Agent 路由

通过 `bindings` 配置，您可以用一个飞书机器人对接多个不同功能或性格的 Agent。系统会根据用户 ID 或群组 ID 自动将对话分发到对应的 Agent。

配置示例：

```json5
{
  agents: {
    list: [
      { id: "main" },
      {
        id: "clawd-fan",
        workspace: "/home/user/clawd-fan",
        agentDir: "/home/user/.openclaw/agents/clawd-fan/agent",
      },
      {
        id: "clawd-xi",
        workspace: "/home/user/clawd-xi",
        agentDir: "/home/user/.openclaw/agents/clawd-xi/agent",
      },
    ],
  },
  bindings: [
    {
      // 用户 A 的私聊 → main agent
      agentId: "main",
      match: {
        channel: "feishu",
        peer: { kind: "dm", id: "ou_28b31a88..." },
      },
    },
    {
      // 用户 B 的私聊 → clawd-fan agent
      agentId: "clawd-fan",
      match: {
        channel: "feishu",
        peer: { kind: "dm", id: "ou_0fe6b1c9..." },
      },
    },
    {
      // 某个群组 → clawd-xi agent
      agentId: "clawd-xi",
      match: {
        channel: "feishu",
        peer: { kind: "group", id: "oc_xxx..." },
      },
    },
  ],
}
```

匹配规则说明：

| 字段              | 说明                                          |
| ----------------- | --------------------------------------------- |
| `agentId`         | 目标 Agent 的 ID，需要在 `agents.list` 中定义 |
| `match.channel`   | 渠道类型，这里固定为 `"feishu"`               |
| `match.peer.kind` | 对话类型：`"dm"`（私聊）或 `"group"`（群组）  |
| `match.peer.id`   | 用户 Open ID（`ou_xxx`）或群组 ID（`oc_xxx`） |

> 获取 ID 的方法：参见上文 [获取群组/用户 ID](#获取群组用户-id) 章节。

---

## 配置参考

完整配置请参考：[网关配置](/gateway/configuration)

主要选项：

| 配置项                                            | 说明                           | 默认值    |
| ------------------------------------------------- | ------------------------------ | --------- |
| `channels.feishu.enabled`                         | 启用/禁用渠道                  | `true`    |
| `channels.feishu.domain`                          | API 域名（`feishu` 或 `lark`） | `feishu`  |
| `channels.feishu.accounts.<id>.appId`             | 应用 App ID                    | -         |
| `channels.feishu.accounts.<id>.appSecret`         | 应用 App Secret                | -         |
| `channels.feishu.accounts.<id>.domain`            | 单账号 API 域名覆盖            | `feishu`  |
| `channels.feishu.dmPolicy`                        | 私聊策略                       | `pairing` |
| `channels.feishu.allowFrom`                       | 私聊白名单（open_id 列表）     | -         |
| `channels.feishu.groupPolicy`                     | 群组策略                       | `open`    |
| `channels.feishu.groupAllowFrom`                  | 群组白名单                     | -         |
| `channels.feishu.groups.<chat_id>.requireMention` | 是否需要 @提及                 | `true`    |
| `channels.feishu.groups.<chat_id>.enabled`        | 是否启用该群组                 | `true`    |
| `channels.feishu.textChunkLimit`                  | 消息分块大小                   | `2000`    |
| `channels.feishu.mediaMaxMb`                      | 媒体大小限制                   | `30`      |
| `channels.feishu.streaming`                       | 启用流式卡片输出               | `true`    |
| `channels.feishu.blockStreaming`                  | 启用块级流式                   | `true`    |

---

## dmPolicy 策略说明

| 值            | 行为                                               |
| ------------- | -------------------------------------------------- |
| `"pairing"`   | **默认**。未知用户收到配对码，管理员批准后才能对话 |
| `"allowlist"` | 仅 `allowFrom` 列表中的用户可对话，其他静默忽略    |
| `"open"`      | 允许所有人对话（需在 allowFrom 中加 `"*"`）        |
| `"disabled"`  | 完全禁止私聊                                       |

---

## 支持的消息类型

### 接收

- ✅ 文本消息
- ✅ 图片
- ✅ 文件
- ✅ 音频
- ✅ 视频
- ✅ 表情包

### 发送

- ✅ 文本消息
- ✅ 图片
- ✅ 文件
- ✅ 音频
- ⚠️ 富文本（部分支持）


---

## index

---
read_when:
  - 添加或修改智能体工具
  - 停用或更改 `openclaw-*` Skills
summary: OpenClaw 的智能体工具接口（browser、canvas、nodes、message、cron），替代旧版 `openclaw-*` Skills
title: 工具
x-i18n:
  generated_at: "2026-02-03T10:12:41Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: a1ec62a9c9bea4c1d2cebfb88509739a3b48b451ab3e378193c620832e2aa07b
  source_path: tools/index.md
  workflow: 15
---

# 工具（OpenClaw）

OpenClaw 为 browser、canvas、nodes 和 cron 暴露**一流的智能体工具**。
这些工具取代了旧的 `openclaw-*` Skills：工具是类型化的，无需调用 shell，
智能体应该直接依赖它们。

## 禁用工具

你可以通过 `openclaw.json` 中的 `tools.allow` / `tools.deny` 全局允许/拒绝工具
（deny 优先）。这会阻止不允许的工具被发送到模型提供商。

```json5
{
  tools: { deny: ["browser"] },
}
```

注意：

- 匹配不区分大小写。
- 支持 `*` 通配符（`"*"` 表示所有工具）。
- 如果 `tools.allow` 仅引用未知或未加载的插件工具名称，OpenClaw 会记录警告并忽略允许列表，以确保核心工具保持可用。

## 工具配置文件（基础允许列表）

`tools.profile` 在 `tools.allow`/`tools.deny` 之前设置**基础工具允许列表**。
按智能体覆盖：`agents.list[].tools.profile`。

配置文件：

- `minimal`：仅 `session_status`
- `coding`：`group:fs`、`group:runtime`、`group:sessions`、`group:memory`、`image`
- `messaging`：`group:messaging`、`sessions_list`、`sessions_history`、`sessions_send`、`session_status`
- `full`：无限制（与未设置相同）

示例（默认仅消息，同时允许 Slack + Discord 工具）：

```json5
{
  tools: {
    profile: "messaging",
    allow: ["slack", "discord"],
  },
}
```

示例（coding 配置文件，但在所有地方拒绝 exec/process）：

```json5
{
  tools: {
    profile: "coding",
    deny: ["group:runtime"],
  },
}
```

示例（全局 coding 配置文件，仅消息的支持智能体）：

```json5
{
  tools: { profile: "coding" },
  agents: {
    list: [
      {
        id: "support",
        tools: { profile: "messaging", allow: ["slack"] },
      },
    ],
  },
}
```

## 特定提供商的工具策略

使用 `tools.byProvider` 为特定提供商（或单个 `provider/model`）**进一步限制**工具，
而不更改你的全局默认值。
按智能体覆盖：`agents.list[].tools.byProvider`。

这在基础工具配置文件**之后**和允许/拒绝列表**之前**应用，
因此它只能缩小工具集。
提供商键接受 `provider`（例如 `google-antigravity`）或
`provider/model`（例如 `openai/gpt-5.2`）。

示例（保持全局 coding 配置文件，但 Google Antigravity 使用最小工具）：

```json5
{
  tools: {
    profile: "coding",
    byProvider: {
      "google-antigravity": { profile: "minimal" },
    },
  },
}
```

示例（针对不稳定端点的 provider/model 特定允许列表）：

```json5
{
  tools: {
    allow: ["group:fs", "group:runtime", "sessions_list"],
    byProvider: {
      "openai/gpt-5.2": { allow: ["group:fs", "sessions_list"] },
    },
  },
}
```

示例（针对单个提供商的智能体特定覆盖）：

```json5
{
  agents: {
    list: [
      {
        id: "support",
        tools: {
          byProvider: {
            "google-antigravity": { allow: ["message", "sessions_list"] },
          },
        },
      },
    ],
  },
}
```

## 工具组（简写）

工具策略（全局、智能体、沙箱）支持 `group:*` 条目，它们会展开为多个工具。
在 `tools.allow` / `tools.deny` 中使用这些。

可用的组：

- `group:runtime`：`exec`、`bash`、`process`
- `group:fs`：`read`、`write`、`edit`、`apply_patch`
- `group:sessions`：`sessions_list`、`sessions_history`、`sessions_send`、`sessions_spawn`、`session_status`
- `group:memory`：`memory_search`、`memory_get`
- `group:web`：`web_search`、`web_fetch`
- `group:ui`：`browser`、`canvas`
- `group:automation`：`cron`、`gateway`
- `group:messaging`：`message`
- `group:nodes`：`nodes`
- `group:openclaw`：所有内置 OpenClaw 工具（不包括提供商插件）

示例（仅允许文件工具 + browser）：

```json5
{
  tools: {
    allow: ["group:fs", "browser"],
  },
}
```

## 插件 + 工具

插件可以在核心集之外注册**额外的工具**（和 CLI 命令）。
参见[插件](/tools/plugin)了解安装 + 配置，以及 [Skills](/tools/skills) 了解
工具使用指导如何被注入到提示中。一些插件随工具一起提供自己的 Skills
（例如，voice-call 插件）。

可选的插件工具：

- [Lobster](/tools/lobster)：带有可恢复审批的类型化工作流运行时（需要 Gateway 网关主机上的 Lobster CLI）。
- [LLM Task](/tools/llm-task)：用于结构化工作流输出的 JSON-only LLM 步骤（可选 schema 验证）。

## 工具清单

### `apply_patch`

跨一个或多个文件应用结构化补丁。用于多块编辑。
实验性：通过 `tools.exec.applyPatch.enabled` 启用（仅 OpenAI 模型）。

### `exec`

在工作区中运行 shell 命令。

核心参数：

- `command`（必需）
- `yieldMs`（超时后自动后台运行，默认 10000）
- `background`（立即后台运行）
- `timeout`（秒；超过则终止进程，默认 1800）
- `elevated`（布尔值；如果启用/允许提升模式，则在主机上运行；仅在智能体被沙箱隔离时改变行为）
- `host`（`sandbox | gateway | node`）
- `security`（`deny | allowlist | full`）
- `ask`（`off | on-miss | always`）
- `node`（`host=node` 时的节点 id/名称）
- 需要真正的 TTY？设置 `pty: true`。

注意：

- 后台运行时返回带有 `sessionId` 的 `status: "running"`。
- 使用 `process` 来轮询/日志/写入/终止/清除后台会话。
- 如果不允许 `process`，`exec` 会同步运行并忽略 `yieldMs`/`background`。
- `elevated` 受 `tools.elevated` 加上任何 `agents.list[].tools.elevated` 覆盖的门控（两者都必须允许），是 `host=gateway` + `security=full` 的别名。
- `elevated` 仅在智能体被沙箱隔离时改变行为（否则是空操作）。
- `host=node` 可以针对 macOS 配套应用或无头节点主机（`openclaw node run`）。
- Gateway 网关/节点审批和允许列表：[执行审批](/tools/exec-approvals)。

### `process`

管理后台 exec 会话。

核心操作：

- `list`、`poll`、`log`、`write`、`kill`、`clear`、`remove`

注意：

- `poll` 返回新输出，完成时返回退出状态。
- `log` 支持基于行的 `offset`/`limit`（省略 `offset` 以获取最后 N 行）。
- `process` 按智能体作用域；来自其他智能体的会话不可见。

### `web_search`

使用 Brave Search API 搜索网络。

核心参数：

- `query`（必需）
- `count`（1-10；默认来自 `tools.web.search.maxResults`）

注意：

- 需要 Brave API 密钥（推荐：`openclaw configure --section web`，或设置 `BRAVE_API_KEY`）。
- 通过 `tools.web.search.enabled` 启用。
- 响应被缓存（默认 15 分钟）。
- 参见 [Web 工具](/tools/web) 了解设置。

### `web_fetch`

从 URL 获取并提取可读内容（HTML → markdown/text）。

核心参数：

- `url`（必需）
- `extractMode`（`markdown` | `text`）
- `maxChars`（截断长页面）

注意：

- 通过 `tools.web.fetch.enabled` 启用。
- 响应被缓存（默认 15 分钟）。
- 对于 JS 密集型网站，优先使用 browser 工具。
- 参见 [Web 工具](/tools/web) 了解设置。
- 参见 [Firecrawl](/tools/firecrawl) 了解可选的反机器人回退。

### `browser`

控制专用的 OpenClaw 管理的浏览器。

核心操作：

- `status`、`start`、`stop`、`tabs`、`open`、`focus`、`close`
- `snapshot`（aria/ai）
- `screenshot`（返回图像块 + `MEDIA:<path>`）
- `act`（UI 操作：click/type/press/hover/drag/select/fill/resize/wait/evaluate）
- `navigate`、`console`、`pdf`、`upload`、`dialog`

配置文件管理：

- `profiles` — 列出所有浏览器配置文件及其状态
- `create-profile` — 使用自动分配的端口（或 `cdpUrl`）创建新配置文件
- `delete-profile` — 停止浏览器，删除用户数据，从配置中移除（仅本地）
- `reset-profile` — 终止配置文件端口上的孤儿进程（仅本地）

常用参数：

- `profile`（可选；默认为 `browser.defaultProfile`）
- `target`（`sandbox` | `host` | `node`）
- `node`（可选；选择特定的节点 id/名称）
  注意：
- 需要 `browser.enabled=true`（默认为 `true`；设置为 `false` 以禁用）。
- 所有操作接受可选的 `profile` 参数以支持多实例。
- 当省略 `profile` 时，使用 `browser.defaultProfile`（默认为"chrome"）。
- 配置文件名称：仅小写字母数字 + 连字符（最多 64 字符）。
- 端口范围：18800-18899（最多约 100 个配置文件）。
- 远程配置文件仅支持附加（无 start/stop/reset）。
- 如果连接了支持浏览器的节点，工具可能会自动路由到它（除非你固定了 `target`）。
- 安装 Playwright 时 `snapshot` 默认为 `ai`；使用 `aria` 获取无障碍树。
- `snapshot` 还支持角色快照选项（`interactive`、`compact`、`depth`、`selector`），返回像 `e12` 这样的引用。
- `act` 需要来自 `snapshot` 的 `ref`（AI 快照中的数字 `12`，或角色快照中的 `e12`）；对于罕见的 CSS 选择器需求使用 `evaluate`。
- 默认避免 `act` → `wait`；仅在特殊情况下使用（没有可靠的 UI 状态可等待）。
- `upload` 可以选择性地传递 `ref` 以在准备后自动点击。
- `upload` 还支持 `inputRef`（aria 引用）或 `element`（CSS 选择器）以直接设置 `<input type="file">`。

### `canvas`

驱动节点 Canvas（present、eval、snapshot、A2UI）。

核心操作：

- `present`、`hide`、`navigate`、`eval`
- `snapshot`（返回图像块 + `MEDIA:<path>`）
- `a2ui_push`、`a2ui_reset`

注意：

- 底层使用 Gateway 网关 `node.invoke`。
- 如果未提供 `node`，工具会选择默认值（单个连接的节点或本地 mac 节点）。
- A2UI 仅限 v0.8（无 `createSurface`）；CLI 会拒绝 v0.9 JSONL 并显示行错误。
- 快速冒烟测试：`openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"`。

### `nodes`

发现和定位配对的节点；发送通知；捕获摄像头/屏幕。

核心操作：

- `status`、`describe`
- `pending`、`approve`、`reject`（配对）
- `notify`（macOS `system.notify`）
- `run`（macOS `system.run`）
- `camera_snap`、`camera_clip`、`screen_record`
- `location_get`

注意：

- 摄像头/屏幕命令需要节点应用在前台。
- 图像返回图像块 + `MEDIA:<path>`。
- 视频返回 `FILE:<path>`（mp4）。
- 位置返回 JSON 负载（lat/lon/accuracy/timestamp）。
- `run` 参数：`command` argv 数组；可选的 `cwd`、`env`（`KEY=VAL`）、`commandTimeoutMs`、`invokeTimeoutMs`、`needsScreenRecording`。

示例（`run`）：

```json
{
  "action": "run",
  "node": "office-mac",
  "command": ["echo", "Hello"],
  "env": ["FOO=bar"],
  "commandTimeoutMs": 12000,
  "invokeTimeoutMs": 45000,
  "needsScreenRecording": false
}
```

### `image`

使用配置的图像模型分析图像。

核心参数：

- `image`（必需的路径或 URL）
- `prompt`（可选；默认为"Describe the image."）
- `model`（可选覆盖）
- `maxBytesMb`（可选大小上限）

注意：

- 仅在配置了 `agents.defaults.imageModel`（主要或回退）时可用，或者当可以从你的默认模型 + 配置的认证推断出隐式图像模型时（尽力配对）。
- 直接使用图像模型（独立于主聊天模型）。

### `message`

跨 Discord/Google Chat/Slack/Telegram/WhatsApp/Signal/iMessage/MS Teams 发送消息和渠道操作。

核心操作：

- `send`（文本 + 可选媒体；MS Teams 还支持用于 Adaptive Cards 的 `card`）
- `poll`（WhatsApp/Discord/MS Teams 投票）
- `react` / `reactions` / `read` / `edit` / `delete`
- `pin` / `unpin` / `list-pins`
- `permissions`
- `thread-create` / `thread-list` / `thread-reply`
- `search`
- `sticker`
- `member-info` / `role-info`
- `emoji-list` / `emoji-upload` / `sticker-upload`
- `role-add` / `role-remove`
- `channel-info` / `channel-list`
- `voice-status`
- `event-list` / `event-create`
- `timeout` / `kick` / `ban`

注意：

- `send` 通过 Gateway 网关路由 WhatsApp；其他渠道直接发送。
- `poll` 对 WhatsApp 和 MS Teams 使用 Gateway 网关；Discord 投票直接发送。
- 当消息工具调用绑定到活动聊天会话时，发送被限制到该会话的目标以避免跨上下文泄露。

### `cron`

管理 Gateway 网关定时任务和唤醒。

核心操作：

- `status`、`list`
- `add`、`update`、`remove`、`run`、`runs`
- `wake`（入队系统事件 + 可选的立即心跳）

注意：

- `add` 期望完整的定时任务对象（与 `cron.add` RPC 相同的 schema）。
- `update` 使用 `{ id, patch }`。

### `gateway`

重启或对运行中的 Gateway 网关进程应用更新（就地）。

核心操作：

- `restart`（授权 + 发送 `SIGUSR1` 进行进程内重启；`openclaw gateway` 就地重启）
- `config.get` / `config.schema`
- `config.apply`（验证 + 写入配置 + 重启 + 唤醒）
- `config.patch`（合并部分更新 + 重启 + 唤醒）
- `update.run`（运行更新 + 重启 + 唤醒）

注意：

- 使用 `delayMs`（默认 2000）以避免中断进行中的回复。
- `restart` 默认禁用；使用 `commands.restart: true` 启用。

### `sessions_list` / `sessions_history` / `sessions_send` / `sessions_spawn` / `session_status`

列出会话，检查转录历史，或发送到另一个会话。

核心参数：

- `sessions_list`：`kinds?`、`limit?`、`activeMinutes?`、`messageLimit?`（0 = 无）
- `sessions_history`：`sessionKey`（或 `sessionId`）、`limit?`、`includeTools?`
- `sessions_send`：`sessionKey`（或 `sessionId`）、`message`、`timeoutSeconds?`（0 = fire-and-forget）
- `sessions_spawn`：`task`、`label?`、`agentId?`、`model?`、`runTimeoutSeconds?`、`cleanup?`
- `session_status`：`sessionKey?`（默认当前；接受 `sessionId`）、`model?`（`default` 清除覆盖）

注意：

- `main` 是规范的私聊键；global/unknown 是隐藏的。
- `messageLimit > 0` 获取每个会话的最后 N 条消息（工具消息被过滤）。
- 当 `timeoutSeconds > 0` 时，`sessions_send` 等待最终完成。
- 递送/宣告发生在完成后，是尽力而为的；`status: "ok"` 确认智能体运行完成，而不是宣告已递送。
- `sessions_spawn` 启动子智能体运行并将宣告回复发送回请求者聊天。
- `sessions_spawn` 是非阻塞的，立即返回 `status: "accepted"`。
- `sessions_send` 运行回复往返乒乓（回复 `REPLY_SKIP` 以停止；最大轮次通过 `session.agentToAgent.maxPingPongTurns`，0-5）。
- 乒乓之后，目标智能体运行一个**宣告步骤**；回复 `ANNOUNCE_SKIP` 以抑制宣告。

### `agents_list`

列出当前会话可以用 `sessions_spawn` 定位的智能体 id。

注意：

- 结果受每智能体允许列表限制（`agents.list[].subagents.allowAgents`）。
- 当配置为 `["*"]` 时，工具包含所有已配置的智能体并标记 `allowAny: true`。

## 参数（通用）

Gateway 网关支持的工具（`canvas`、`nodes`、`cron`）：

- `gatewayUrl`（默认 `ws://127.0.0.1:18789`）
- `gatewayToken`（如果启用了认证）
- `timeoutMs`

Browser 工具：

- `profile`（可选；默认为 `browser.defaultProfile`）
- `target`（`sandbox` | `host` | `node`）
- `node`（可选；固定特定的节点 id/名称）

## 推荐的智能体流程

浏览器自动化：

1. `browser` → `status` / `start`
2. `snapshot`（ai 或 aria）
3. `act`（click/type/press）
4. `screenshot` 如果你需要视觉确认

Canvas 渲染：

1. `canvas` → `present`
2. `a2ui_push`（可选）
3. `snapshot`

节点定位：

1. `nodes` → `status`
2. 在选定的节点上 `describe`
3. `notify` / `run` / `camera_snap` / `screen_record`

## 安全性

- 避免直接 `system.run`；仅在用户明确同意时使用 `nodes` → `run`。
- 尊重用户对摄像头/屏幕捕获的同意。
- 在调用媒体命令前使用 `status/describe` 确保权限。

## 工具如何呈现给智能体

工具通过两个并行渠道暴露：

1. **系统提示文本**：人类可读的列表 + 指导。
2. **工具 schema**：发送到模型 API 的结构化函数定义。

这意味着智能体同时看到"存在哪些工具"和"如何调用它们"。如果工具
没有出现在系统提示或 schema 中，模型就无法调用它。


---

## browser

---
read_when:
  - 添加智能体控制的浏览器自动化
  - 调试 openclaw 干扰你自己 Chrome 的问题
  - 在 macOS 应用中实现浏览器设置和生命周期管理
summary: 集成浏览器控制服务 + 操作命令
title: 浏览器（OpenClaw 托管）
x-i18n:
  generated_at: "2026-02-03T09:26:06Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: a868d040183436a1fb355130995e79782cb817b5ea298beaf1e1d2cb82e21c4c
  source_path: tools/browser.md
  workflow: 15
---

# 浏览器（openclaw 托管）

OpenClaw 可以运行一个由智能体控制的**专用 Chrome/Brave/Edge/Chromium 配置文件**。
它与你的个人浏览器隔离，通过 Gateway 网关内部的小型本地控制服务进行管理（仅限 loopback）。

新手视角：

- 把它想象成一个**独立的、仅供智能体使用的浏览器**。
- `openclaw` 配置文件**不会**触及你的个人浏览器配置文件。
- 智能体可以在安全的通道中**打开标签页、读取页面、点击和输入**。
- 默认的 `chrome` 配置文件通过扩展中继使用**系统默认的 Chromium 浏览器**；切换到 `openclaw` 可使用隔离的托管浏览器。

## 功能概览

- 一个名为 **openclaw** 的独立浏览器配置文件（默认橙色主题）。
- 确定性标签页控制（列出/打开/聚焦/关闭）。
- 智能体操作（点击/输入/拖动/选择）、快照、截图、PDF。
- 可选的多配置文件支持（`openclaw`、`work`、`remote` 等）。

此浏览器**不是**你的日常浏览器。它是一个安全、隔离的界面，用于智能体自动化和验证。

## 快速开始

```bash
openclaw browser --browser-profile openclaw status
openclaw browser --browser-profile openclaw start
openclaw browser --browser-profile openclaw open https://example.com
openclaw browser --browser-profile openclaw snapshot
```

如果出现"Browser disabled"，请在配置中启用它（见下文）并重启 Gateway 网关。

## 配置文件：`openclaw` 与 `chrome`

- `openclaw`：托管的隔离浏览器（无需扩展）。
- `chrome`：到你**系统浏览器**的扩展中继（需要将 OpenClaw 扩展附加到标签页）。

如果你希望默认使用托管模式，请设置 `browser.defaultProfile: "openclaw"`。

## 配置

浏览器设置位于 `~/.openclaw/openclaw.json`。

```json5
{
  browser: {
    enabled: true, // default: true
    // cdpUrl: "http://127.0.0.1:18792", // legacy single-profile override
    remoteCdpTimeoutMs: 1500, // remote CDP HTTP timeout (ms)
    remoteCdpHandshakeTimeoutMs: 3000, // remote CDP WebSocket handshake timeout (ms)
    defaultProfile: "chrome",
    color: "#FF4500",
    headless: false,
    noSandbox: false,
    attachOnly: false,
    executablePath: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    profiles: {
      openclaw: { cdpPort: 18800, color: "#FF4500" },
      work: { cdpPort: 18801, color: "#0066CC" },
      remote: { cdpUrl: "http://10.0.0.42:9222", color: "#00AA00" },
    },
  },
}
```

注意事项：

- 浏览器控制服务绑定到 loopback 上的端口，该端口从 `gateway.port` 派生（默认：`18791`，即 gateway + 2）。中继使用下一个端口（`18792`）。
- 如果你覆盖了 Gateway 网关端口（`gateway.port` 或 `OPENCLAW_GATEWAY_PORT`），派生的浏览器端口会相应调整以保持在同一"系列"中。
- 未设置时，`cdpUrl` 默认为中继端口。
- `remoteCdpTimeoutMs` 适用于远程（非 loopback）CDP 可达性检查。
- `remoteCdpHandshakeTimeoutMs` 适用于远程 CDP WebSocket 可达性检查。
- `attachOnly: true` 表示"永不启动本地浏览器；仅在浏览器已运行时附加"。
- `color` + 每个配置文件的 `color` 为浏览器 UI 着色，以便你能看到哪个配置文件处于活动状态。
- 默认配置文件是 `chrome`（扩展中继）。使用 `defaultProfile: "openclaw"` 来使用托管浏览器。
- 自动检测顺序：如果系统默认浏览器是基于 Chromium 的则使用它；否则 Chrome → Brave → Edge → Chromium → Chrome Canary。
- 本地 `openclaw` 配置文件会自动分配 `cdpPort`/`cdpUrl` — 仅为远程 CDP 设置这些。

## 使用 Brave（或其他基于 Chromium 的浏览器）

如果你的**系统默认**浏览器是基于 Chromium 的（Chrome/Brave/Edge 等），OpenClaw 会自动使用它。设置 `browser.executablePath` 可覆盖自动检测：

CLI 示例：

```bash
openclaw config set browser.executablePath "/usr/bin/google-chrome"
```

```json5
// macOS
{
  browser: {
    executablePath: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
  }
}

// Windows
{
  browser: {
    executablePath: "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
  }
}

// Linux
{
  browser: {
    executablePath: "/usr/bin/brave-browser"
  }
}
```

## 本地控制与远程控制

- **本地控制（默认）：** Gateway 网关启动 loopback 控制服务，可以启动本地浏览器。
- **远程控制（节点主机）：** 在有浏览器的机器上运行节点主机；Gateway 网关将浏览器操作代理到该节点。
- **远程 CDP：** 设置 `browser.profiles.<name>.cdpUrl`（或 `browser.cdpUrl`）以附加到远程的基于 Chromium 的浏览器。在这种情况下，OpenClaw 不会启动本地浏览器。

远程 CDP URL 可以包含认证信息：

- 查询令牌（例如 `https://provider.example?token=<token>`）
- HTTP Basic 认证（例如 `https://user:pass@provider.example`）

OpenClaw 在调用 `/json/*` 端点和连接 CDP WebSocket 时会保留认证信息。建议使用环境变量或密钥管理器存储令牌，而不是将其提交到配置文件中。

## 节点浏览器代理（零配置默认）

如果你在有浏览器的机器上运行**节点主机**，OpenClaw 可以自动将浏览器工具调用路由到该节点，无需任何额外的浏览器配置。这是远程 Gateway 网关的默认路径。

注意事项：

- 节点主机通过**代理命令**暴露其本地浏览器控制服务器。
- 配置文件来自节点自己的 `browser.profiles` 配置（与本地相同）。
- 如果不需要可以禁用：
  - 在节点上：`nodeHost.browserProxy.enabled=false`
  - 在 Gateway 网关上：`gateway.nodes.browser.mode="off"`

## Browserless（托管远程 CDP）

[Browserless](https://browserless.io) 是一个托管的 Chromium 服务，通过 HTTPS 暴露 CDP 端点。你可以将 OpenClaw 浏览器配置文件指向 Browserless 区域端点，并使用你的 API 密钥进行认证。

示例：

```json5
{
  browser: {
    enabled: true,
    defaultProfile: "browserless",
    remoteCdpTimeoutMs: 2000,
    remoteCdpHandshakeTimeoutMs: 4000,
    profiles: {
      browserless: {
        cdpUrl: "https://production-sfo.browserless.io?token=<BROWSERLESS_API_KEY>",
        color: "#00AA00",
      },
    },
  },
}
```

注意事项：

- 将 `<BROWSERLESS_API_KEY>` 替换为你真实的 Browserless 令牌。
- 选择与你的 Browserless 账户匹配的区域端点（请参阅其文档）。

## 安全性

核心理念：

- 浏览器控制仅限 loopback；访问通过 Gateway 网关的认证或节点配对进行。
- 将 Gateway 网关和任何节点主机保持在私有网络上（Tailscale）；避免公开暴露。
- 将远程 CDP URL/令牌视为机密；优先使用环境变量或密钥管理器。

远程 CDP 提示：

- 尽可能使用 HTTPS 端点和短期令牌。
- 避免在配置文件中直接嵌入长期令牌。

## 配置文件（多浏览器）

OpenClaw 支持多个命名配置文件（路由配置）。配置文件可以是：

- **openclaw 托管**：具有独立用户数据目录和 CDP 端口的专用基于 Chromium 的浏览器实例
- **远程**：显式 CDP URL（在其他地方运行的基于 Chromium 的浏览器）
- **扩展中继**：通过本地中继 + Chrome 扩展访问你现有的 Chrome 标签页

默认值：

- 如果缺少 `openclaw` 配置文件，会自动创建。
- `chrome` 配置文件是内置的，用于 Chrome 扩展中继（默认指向 `http://127.0.0.1:18792`）。
- 本地 CDP 端口默认从 **18800–18899** 分配。
- 删除配置文件会将其本地数据目录移至回收站。

所有控制端点接受 `?profile=<name>`；CLI 使用 `--browser-profile`。

## Chrome 扩展中继（使用你现有的 Chrome）

OpenClaw 还可以通过本地 CDP 中继 + Chrome 扩展驱动**你现有的 Chrome 标签页**（无需单独的"openclaw"Chrome 实例）。

完整指南：[Chrome 扩展](/tools/chrome-extension)

流程：

- Gateway 网关在本地运行（同一台机器）或节点主机在浏览器所在机器上运行。
- 本地**中继服务器**在 loopback 的 `cdpUrl` 上监听（默认：`http://127.0.0.1:18792`）。
- 你点击标签页上的 **OpenClaw Browser Relay** 扩展图标来附加（它不会自动附加）。
- 智能体通过选择正确的配置文件，使用普通的 `browser` 工具控制该标签页。

如果 Gateway 网关在其他地方运行，请在浏览器所在机器上运行节点主机，以便 Gateway 网关可以代理浏览器操作。

### 沙箱会话

如果智能体会话是沙箱隔离的，`browser` 工具可能默认为 `target="sandbox"`（沙箱浏览器）。
Chrome 扩展中继接管需要主机浏览器控制，因此要么：

- 在非沙箱模式下运行会话，或者
- 设置 `agents.defaults.sandbox.browser.allowHostControl: true` 并在调用工具时使用 `target="host"`。

### 设置

1. 加载扩展（开发/未打包）：

```bash
openclaw browser extension install
```

- Chrome → `chrome://extensions` → 启用"开发者模式"
- "加载已解压的扩展程序" → 选择 `openclaw browser extension path` 打印的目录
- 固定扩展，然后在你想要控制的标签页上点击它（徽章显示 `ON`）。

2. 使用它：

- CLI：`openclaw browser --browser-profile chrome tabs`
- 智能体工具：`browser` 配合 `profile="chrome"`

可选：如果你想要不同的名称或中继端口，创建你自己的配置文件：

```bash
openclaw browser create-profile \
  --name my-chrome \
  --driver extension \
  --cdp-url http://127.0.0.1:18792 \
  --color "#00AA00"
```

注意事项：

- 此模式依赖 Playwright-on-CDP 进行大多数操作（截图/快照/操作）。
- 再次点击扩展图标可分离。

## 隔离保证

- **专用用户数据目录**：永不触及你的个人浏览器配置文件。
- **专用端口**：避免使用 `9222` 以防止与开发工作流冲突。
- **确定性标签页控制**：通过 `targetId` 定位标签页，而非"最后一个标签页"。

## 浏览器选择

本地启动时，OpenClaw 选择第一个可用的：

1. Chrome
2. Brave
3. Edge
4. Chromium
5. Chrome Canary

你可以使用 `browser.executablePath` 覆盖。

平台：

- macOS：检查 `/Applications` 和 `~/Applications`。
- Linux：查找 `google-chrome`、`brave`、`microsoft-edge`、`chromium` 等。
- Windows：检查常见安装位置。

## 控制 API（可选）

仅用于本地集成，Gateway 网关暴露一个小型的 loopback HTTP API：

- 状态/启动/停止：`GET /`、`POST /start`、`POST /stop`
- 标签页：`GET /tabs`、`POST /tabs/open`、`POST /tabs/focus`、`DELETE /tabs/:targetId`
- 快照/截图：`GET /snapshot`、`POST /screenshot`
- 操作：`POST /navigate`、`POST /act`
- 钩子：`POST /hooks/file-chooser`、`POST /hooks/dialog`
- 下载：`POST /download`、`POST /wait/download`
- 调试：`GET /console`、`POST /pdf`
- 调试：`GET /errors`、`GET /requests`、`POST /trace/start`、`POST /trace/stop`、`POST /highlight`
- 网络：`POST /response/body`
- 状态：`GET /cookies`、`POST /cookies/set`、`POST /cookies/clear`
- 状态：`GET /storage/:kind`、`POST /storage/:kind/set`、`POST /storage/:kind/clear`
- 设置：`POST /set/offline`、`POST /set/headers`、`POST /set/credentials`、`POST /set/geolocation`、`POST /set/media`、`POST /set/timezone`、`POST /set/locale`、`POST /set/device`

所有端点接受 `?profile=<name>`。

### Playwright 要求

某些功能（navigate/act/AI 快照/角色快照、元素截图、PDF）需要 Playwright。如果未安装 Playwright，这些端点会返回明确的 501 错误。ARIA 快照和基本截图对于 openclaw 托管的 Chrome 仍然有效。对于 Chrome 扩展中继驱动程序，ARIA 快照和截图需要 Playwright。

如果你看到 `Playwright is not available in this gateway build`，请安装完整的 Playwright 包（不是 `playwright-core`）并重启 Gateway 网关，或者重新安装带浏览器支持的 OpenClaw。

#### Docker Playwright 安装

如果你的 Gateway 网关在 Docker 中运行，避免使用 `npx playwright`（npm 覆盖冲突）。改用捆绑的 CLI：

```bash
docker compose run --rm openclaw-cli \
  node /app/node_modules/playwright-core/cli.js install chromium
```

要持久化浏览器下载，设置 `PLAYWRIGHT_BROWSERS_PATH`（例如 `/home/node/.cache/ms-playwright`）并确保 `/home/node` 通过 `OPENCLAW_HOME_VOLUME` 或绑定挂载持久化。参见 [Docker](/install/docker)。

## 工作原理（内部）

高层流程：

- 一个小型**控制服务器**接受 HTTP 请求。
- 它通过 **CDP** 连接到基于 Chromium 的浏览器（Chrome/Brave/Edge/Chromium）。
- 对于高级操作（点击/输入/快照/PDF），它在 CDP 之上使用 **Playwright**。
- 当缺少 Playwright 时，仅非 Playwright 操作可用。

这种设计使智能体保持在稳定、确定性的接口上，同时让你可以切换本地/远程浏览器和配置文件。

## CLI 快速参考

所有命令接受 `--browser-profile <name>` 以定位特定配置文件。
所有命令也接受 `--json` 以获得机器可读的输出（稳定的负载）。

基础操作：

- `openclaw browser status`
- `openclaw browser start`
- `openclaw browser stop`
- `openclaw browser tabs`
- `openclaw browser tab`
- `openclaw browser tab new`
- `openclaw browser tab select 2`
- `openclaw browser tab close 2`
- `openclaw browser open https://example.com`
- `openclaw browser focus abcd1234`
- `openclaw browser close abcd1234`

检查：

- `openclaw browser screenshot`
- `openclaw browser screenshot --full-page`
- `openclaw browser screenshot --ref 12`
- `openclaw browser screenshot --ref e12`
- `openclaw browser snapshot`
- `openclaw browser snapshot --format aria --limit 200`
- `openclaw browser snapshot --interactive --compact --depth 6`
- `openclaw browser snapshot --efficient`
- `openclaw browser snapshot --labels`
- `openclaw browser snapshot --selector "#main" --interactive`
- `openclaw browser snapshot --frame "iframe#main" --interactive`
- `openclaw browser console --level error`
- `openclaw browser errors --clear`
- `openclaw browser requests --filter api --clear`
- `openclaw browser pdf`
- `openclaw browser responsebody "**/api" --max-chars 5000`

操作：

- `openclaw browser navigate https://example.com`
- `openclaw browser resize 1280 720`
- `openclaw browser click 12 --double`
- `openclaw browser click e12 --double`
- `openclaw browser type 23 "hello" --submit`
- `openclaw browser press Enter`
- `openclaw browser hover 44`
- `openclaw browser scrollintoview e12`
- `openclaw browser drag 10 11`
- `openclaw browser select 9 OptionA OptionB`
- `openclaw browser download e12 /tmp/report.pdf`
- `openclaw browser waitfordownload /tmp/report.pdf`
- `openclaw browser upload /tmp/file.pdf`
- `openclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'`
- `openclaw browser dialog --accept`
- `openclaw browser wait --text "Done"`
- `openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"`
- `openclaw browser evaluate --fn '(el) => el.textContent' --ref 7`
- `openclaw browser highlight e12`
- `openclaw browser trace start`
- `openclaw browser trace stop`

状态：

- `openclaw browser cookies`
- `openclaw browser cookies set session abc123 --url "https://example.com"`
- `openclaw browser cookies clear`
- `openclaw browser storage local get`
- `openclaw browser storage local set theme dark`
- `openclaw browser storage session clear`
- `openclaw browser set offline on`
- `openclaw browser set headers --json '{"X-Debug":"1"}'`
- `openclaw browser set credentials user pass`
- `openclaw browser set credentials --clear`
- `openclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"`
- `openclaw browser set geo --clear`
- `openclaw browser set media dark`
- `openclaw browser set timezone America/New_York`
- `openclaw browser set locale en-US`
- `openclaw browser set device "iPhone 14"`

注意事项：

- `upload` 和 `dialog` 是**预备**调用；在触发选择器/对话框的点击/按键之前运行它们。
- `upload` 也可以通过 `--input-ref` 或 `--element` 直接设置文件输入。
- `snapshot`：
  - `--format ai`（安装 Playwright 时的默认值）：返回带有数字 ref 的 AI 快照（`aria-ref="<n>"`）。
  - `--format aria`：返回无障碍树（无 ref；仅供检查）。
  - `--efficient`（或 `--mode efficient`）：紧凑角色快照预设（interactive + compact + depth + 较低的 maxChars）。
  - 配置默认值（仅限工具/CLI）：设置 `browser.snapshotDefaults.mode: "efficient"` 以在调用者未传递模式时使用高效快照（参见 [Gateway 网关配置](/gateway/configuration#browser-openclaw-managed-browser)）。
  - 角色快照选项（`--interactive`、`--compact`、`--depth`、`--selector`）强制使用带有 `ref=e12` 等 ref 的基于角色的快照。
  - `--frame "<iframe selector>"` 将角色快照范围限定到 iframe（与 `e12` 等角色 ref 配合使用）。
  - `--interactive` 输出一个扁平的、易于选择的交互元素列表（最适合驱动操作）。
  - `--labels` 添加一个带有叠加 ref 标签的视口截图（打印 `MEDIA:<path>`）。
- `click`/`type` 等需要来自 `snapshot` 的 `ref`（数字 `12` 或角色 ref `e12`）。
  操作故意不支持 CSS 选择器。

## 快照和 ref

OpenClaw 支持两种"快照"风格：

- **AI 快照（数字 ref）**：`openclaw browser snapshot`（默认；`--format ai`）
  - 输出：包含数字 ref 的文本快照。
  - 操作：`openclaw browser click 12`、`openclaw browser type 23 "hello"`。
  - 内部通过 Playwright 的 `aria-ref` 解析 ref。

- **角色快照（角色 ref 如 `e12`）**：`openclaw browser snapshot --interactive`（或 `--compact`、`--depth`、`--selector`、`--frame`）
  - 输出：带有 `[ref=e12]`（和可选的 `[nth=1]`）的基于角色的列表/树。
  - 操作：`openclaw browser click e12`、`openclaw browser highlight e12`。
  - 内部通过 `getByRole(...)`（加上重复项的 `nth()`）解析 ref。
  - 添加 `--labels` 可包含带有叠加 `e12` 标签的视口截图。

ref 行为：

- ref 在**导航之间不稳定**；如果出错，重新运行 `snapshot` 并使用新的 ref。
- 如果角色快照是使用 `--frame` 拍摄的，角色 ref 将限定在该 iframe 内，直到下一次角色快照。

## 等待增强功能

你可以等待的不仅仅是时间/文本：

- 等待 URL（Playwright 支持通配符）：
  - `openclaw browser wait --url "**/dash"`
- 等待加载状态：
  - `openclaw browser wait --load networkidle`
- 等待 JS 断言：
  - `openclaw browser wait --fn "window.ready===true"`
- 等待选择器变得可见：
  - `openclaw browser wait "#main"`

这些可以组合使用：

```bash
openclaw browser wait "#main" \
  --url "**/dash" \
  --load networkidle \
  --fn "window.ready===true" \
  --timeout-ms 15000
```

## 调试工作流

当操作失败时（例如"not visible"、"strict mode violation"、"covered"）：

1. `openclaw browser snapshot --interactive`
2. 使用 `click <ref>` / `type <ref>`（在交互模式下优先使用角色 ref）
3. 如果仍然失败：`openclaw browser highlight <ref>` 查看 Playwright 定位的目标
4. 如果页面行为异常：
   - `openclaw browser errors --clear`
   - `openclaw browser requests --filter api --clear`
5. 深度调试：录制 trace：
   - `openclaw browser trace start`
   - 重现问题
   - `openclaw browser trace stop`（打印 `TRACE:<path>`）

## JSON 输出

`--json` 用于脚本和结构化工具。

示例：

```bash
openclaw browser status --json
openclaw browser snapshot --interactive --json
openclaw browser requests --filter api --json
openclaw browser cookies --json
```

JSON 格式的角色快照包含 `refs` 加上一个小的 `stats` 块（lines/chars/refs/interactive），以便工具可以推断负载大小和密度。

## 状态和环境开关

这些对于"让网站表现得像 X"的工作流很有用：

- Cookies：`cookies`、`cookies set`、`cookies clear`
- 存储：`storage local|session get|set|clear`
- 离线：`set offline on|off`
- 请求头：`set headers --json '{"X-Debug":"1"}'`（或 `--clear`）
- HTTP basic 认证：`set credentials user pass`（或 `--clear`）
- 地理位置：`set geo <lat> <lon> --origin "https://example.com"`（或 `--clear`）
- 媒体：`set media dark|light|no-preference|none`
- 时区/语言环境：`set timezone ...`、`set locale ...`
- 设备/视口：
  - `set device "iPhone 14"`（Playwright 设备预设）
  - `set viewport 1280 720`

## 安全与隐私

- openclaw 浏览器配置文件可能包含已登录的会话；请将其视为敏感信息。
- `browser act kind=evaluate` / `openclaw browser evaluate` 和 `wait --fn` 在页面上下文中执行任意 JavaScript。提示注入可能会操纵它。如果不需要，请使用 `browser.evaluateEnabled=false` 禁用它。
- 有关登录和反机器人注意事项（X/Twitter 等），请参阅 [浏览器登录 + X/Twitter 发帖](/tools/browser-login)。
- 保持 Gateway 网关/节点主机私有（仅限 loopback 或 tailnet）。
- 远程 CDP 端点功能强大；请通过隧道保护它们。

## 故障排除

有关 Linux 特定问题（特别是 snap Chromium），请参阅[浏览器故障排除](/tools/browser-linux-troubleshooting)。

## 智能体工具 + 控制工作原理

智能体获得**一个工具**用于浏览器自动化：

- `browser` — status/start/stop/tabs/open/focus/close/snapshot/screenshot/navigate/act

映射方式：

- `browser snapshot` 返回稳定的 UI 树（AI 或 ARIA）。
- `browser act` 使用快照 `ref` ID 来点击/输入/拖动/选择。
- `browser screenshot` 捕获像素（整页或元素）。
- `browser` 接受：
  - `profile` 来选择命名的浏览器配置文件（openclaw、chrome 或远程 CDP）。
  - `target`（`sandbox` | `host` | `node`）来选择浏览器所在位置。
  - 在沙箱会话中，`target: "host"` 需要 `agents.defaults.sandbox.browser.allowHostControl=true`。
  - 如果省略 `target`：沙箱会话默认为 `sandbox`，非沙箱会话默认为 `host`。
  - 如果连接了具有浏览器能力的节点，工具可能会自动路由到该节点，除非你指定 `target="host"` 或 `target="node"`。

这使智能体保持确定性并避免脆弱的选择器。


---

## exec

---
read_when:
  - 使用或修改 exec 工具
  - 调试 stdin 或 TTY 行为
summary: Exec 工具用法、stdin 模式和 TTY 支持
title: Exec 工具
x-i18n:
  generated_at: "2026-02-03T09:26:51Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 3b32238dd8dce93d4f24100eaa521ce9f8485eff6d8498e2680ce9ed6045d25f
  source_path: tools/exec.md
  workflow: 15
---

# Exec 工具

在工作区中运行 shell 命令。通过 `process` 支持前台和后台执行。
如果 `process` 被禁用，`exec` 将同步运行并忽略 `yieldMs`/`background`。
后台会话按智能体隔离；`process` 只能看到同一智能体的会话。

## 参数

- `command`（必填）
- `workdir`（默认为当前工作目录）
- `env`（键值对覆盖）
- `yieldMs`（默认 10000）：延迟后自动转入后台
- `background`（布尔值）：立即转入后台
- `timeout`（秒，默认 1800）：超时后终止
- `pty`（布尔值）：在可用时使用伪终端运行（仅限 TTY 的 CLI、编程智能体、终端 UI）
- `host`（`sandbox | gateway | node`）：执行位置
- `security`（`deny | allowlist | full`）：`gateway`/`node` 的执行策略
- `ask`（`off | on-miss | always`）：`gateway`/`node` 的审批提示
- `node`（字符串）：`host=node` 时的节点 id/名称
- `elevated`（布尔值）：请求提升模式（gateway 主机）；仅当 elevated 解析为 `full` 时才强制 `security=full`

注意事项：

- `host` 默认为 `sandbox`。
- 当沙箱隔离关闭时，`elevated` 会被忽略（exec 已在主机上运行）。
- `gateway`/`node` 审批由 `~/.openclaw/exec-approvals.json` 控制。
- `node` 需要已配对的节点（配套应用或无头节点主机）。
- 如果有多个可用节点，设置 `exec.node` 或 `tools.exec.node` 来选择一个。
- 在非 Windows 主机上，exec 会使用已设置的 `SHELL`；如果 `SHELL` 是 `fish`，它会优先从 `PATH` 中选择 `bash`（或 `sh`）以避免 fish 不兼容的脚本，如果两者都不存在则回退到 `SHELL`。
- 主机执行（`gateway`/`node`）会拒绝 `env.PATH` 和加载器覆盖（`LD_*`/`DYLD_*`），以防止二进制劫持或代码注入。
- 重要提示：沙箱隔离**默认关闭**。如果沙箱隔离关闭，`host=sandbox` 将直接在 Gateway 网关主机上运行（无容器）且**不需要审批**。如需审批，请使用 `host=gateway` 运行并配置 exec 审批（或启用沙箱隔离）。

## 配置

- `tools.exec.notifyOnExit`（默认：true）：为 true 时，后台 exec 会话在退出时会入队系统事件并请求心跳。
- `tools.exec.approvalRunningNoticeMs`（默认：10000）：当需要审批的 exec 运行时间超过此值时发出单次"运行中"通知（0 表示禁用）。
- `tools.exec.host`（默认：`sandbox`）
- `tools.exec.security`（默认：sandbox 为 `deny`，gateway + node 未设置时为 `allowlist`）
- `tools.exec.ask`（默认：`on-miss`）
- `tools.exec.node`（默认：未设置）
- `tools.exec.pathPrepend`：exec 运行时添加到 `PATH` 前面的目录列表。
- `tools.exec.safeBins`：仅限 stdin 的安全二进制文件，无需显式白名单条目即可运行。

示例：

```json5
{
  tools: {
    exec: {
      pathPrepend: ["~/bin", "/opt/oss/bin"],
    },
  },
}
```

### PATH 处理

- `host=gateway`：将你的登录 shell `PATH` 合并到 exec 环境中。主机执行时会拒绝 `env.PATH` 覆盖。守护进程本身仍使用最小 `PATH` 运行：
  - macOS：`/opt/homebrew/bin`、`/usr/local/bin`、`/usr/bin`、`/bin`
  - Linux：`/usr/local/bin`、`/usr/bin`、`/bin`
- `host=sandbox`：在容器内运行 `sh -lc`（登录 shell），因此 `/etc/profile` 可能会重置 `PATH`。OpenClaw 在 profile 加载后通过内部环境变量将 `env.PATH` 添加到前面（无 shell 插值）；`tools.exec.pathPrepend` 在此也适用。
- `host=node`：只有你传递的未被阻止的 env 覆盖会发送到节点。主机执行时会拒绝 `env.PATH` 覆盖。无头节点主机仅在 `PATH` 添加到节点主机 PATH 前面时才接受（不允许替换）。macOS 节点完全丢弃 `PATH` 覆盖。

按智能体绑定节点（在配置中使用智能体列表索引）：

```bash
openclaw config get agents.list
openclaw config set agents.list[0].tools.exec.node "node-id-or-name"
```

控制 UI：Nodes 标签页包含一个小的"Exec 节点绑定"面板用于相同的设置。

## 会话覆盖（`/exec`）

使用 `/exec` 为 `host`、`security`、`ask` 和 `node` 设置**每会话**默认值。
不带参数发送 `/exec` 可显示当前值。

示例：

```
/exec host=gateway security=allowlist ask=on-miss node=mac-1
```

## 授权模型

`/exec` 仅对**已授权发送者**（渠道白名单/配对加 `commands.useAccessGroups`）生效。
它仅更新**会话状态**，不写入配置。要彻底禁用 exec，请通过工具策略拒绝它（`tools.deny: ["exec"]` 或按智能体配置）。除非你显式设置 `security=full` 和 `ask=off`，否则主机审批仍然适用。

## Exec 审批（配套应用/节点主机）

沙箱隔离的智能体可以要求在 `exec` 于 Gateway 网关或节点主机上运行前进行逐请求审批。
参阅 [Exec 审批](/tools/exec-approvals) 了解策略、白名单和 UI 流程。

当需要审批时，exec 工具会立即返回 `status: "approval-pending"` 和审批 id。一旦被批准（或拒绝/超时），Gateway 网关会发出系统事件（`Exec finished` / `Exec denied`）。如果命令在 `tools.exec.approvalRunningNoticeMs` 之后仍在运行，会发出单次 `Exec running` 通知。

## 白名单 + 安全二进制文件

白名单执行仅匹配**解析后的二进制路径**（不匹配基本名称）。当 `security=allowlist` 时，仅当每个管道段都在白名单中或是安全二进制文件时，shell 命令才会自动允许。在白名单模式下，链式命令（`;`、`&&`、`||`）和重定向会被拒绝。

## 示例

前台：

```json
{ "tool": "exec", "command": "ls -la" }
```

后台 + 轮询：

```json
{"tool":"exec","command":"npm run build","yieldMs":1000}
{"tool":"process","action":"poll","sessionId":"<id>"}
```

发送按键（tmux 风格）：

```json
{"tool":"process","action":"send-keys","sessionId":"<id>","keys":["Enter"]}
{"tool":"process","action":"send-keys","sessionId":"<id>","keys":["C-c"]}
{"tool":"process","action":"send-keys","sessionId":"<id>","keys":["Up","Up","Enter"]}
```

提交（仅发送 CR）：

```json
{ "tool": "process", "action": "submit", "sessionId": "<id>" }
```

粘贴（默认带括号）：

```json
{ "tool": "process", "action": "paste", "sessionId": "<id>", "text": "line1\nline2\n" }
```

## apply_patch（实验性）

`apply_patch` 是 `exec` 的子工具，用于结构化多文件编辑。
需显式启用：

```json5
{
  tools: {
    exec: {
      applyPatch: { enabled: true, allowModels: ["gpt-5.2"] },
    },
  },
}
```

注意事项：

- 仅适用于 OpenAI/OpenAI Codex 模型。
- 工具策略仍然适用；`allow: ["exec"]` 隐式允许 `apply_patch`。
- 配置位于 `tools.exec.applyPatch` 下。


---

## skills

---
read_when:
  - 添加或修改 Skills
  - 更改 Skills 门控或加载规则
summary: Skills：托管与工作区、门控规则以及配置/环境变量连接
title: Skills
x-i18n:
  generated_at: "2026-02-03T10:12:27Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 54685da5885600b367ccdad6342497199fcb168ce33f8cdc00391d993f3bab7e
  source_path: tools/skills.md
  workflow: 15
---

# Skills（OpenClaw）

OpenClaw 使用**兼容 [AgentSkills](https://agentskills.io)** 的 Skills 文件夹来教智能体如何使用工具。每个 Skills 是一个包含带有 YAML frontmatter 和说明的 `SKILL.md` 的目录。OpenClaw 加载**内置 Skills** 以及可选的本地覆盖，并在加载时根据环境、配置和二进制文件存在情况进行过滤。

## 位置和优先级

Skills 从**三个**位置加载：

1. **内置 Skills**：随安装包一起发布（npm 包或 OpenClaw.app）
2. **托管/本地 Skills**：`~/.openclaw/skills`
3. **工作区 Skills**：`<workspace>/skills`

如果 Skills 名称冲突，优先级为：

`<workspace>/skills`（最高）→ `~/.openclaw/skills` → 内置 Skills（最低）

此外，你可以通过 `~/.openclaw/openclaw.json` 中的 `skills.load.extraDirs` 配置额外的 Skills 文件夹（最低优先级）。

## 单智能体 vs 共享 Skills

在**多智能体**设置中，每个智能体有自己的工作区。这意味着：

- **单智能体 Skills** 位于 `<workspace>/skills` 中，仅供该智能体使用。
- **共享 Skills** 位于 `~/.openclaw/skills`（托管/本地），对同一机器上的**所有智能体**可见。
- 如果你想要多个智能体使用一个通用的 Skills 包，也可以通过 `skills.load.extraDirs`（最低优先级）添加**共享文件夹**。

如果同一个 Skills 名称存在于多个位置，将应用通常的优先级规则：工作区优先，然后是托管/本地，最后是内置。

## 插件 + Skills

插件可以通过在 `openclaw.plugin.json` 中列出 `skills` 目录（相对于插件根目录的路径）来发布自己的 Skills。插件 Skills 在插件启用时加载，并参与正常的 Skills 优先级规则。你可以通过插件配置条目上的 `metadata.openclaw.requires.config` 对它们进行门控。参见[插件](/tools/plugin)了解发现/配置，以及[工具](/tools)了解这些 Skills 所教授的工具接口。

## ClawHub（安装 + 同步）

ClawHub 是 OpenClaw 的公共 Skills 注册表。浏览 https://clawhub.com。使用它来发现、安装、更新和备份 Skills。完整指南：[ClawHub](/tools/clawhub)。

常见流程：

- 将 Skills 安装到你的工作区：
  - `clawhub install <skill-slug>`
- 更新所有已安装的 Skills：
  - `clawhub update --all`
- 同步（扫描 + 发布更新）：
  - `clawhub sync --all`

默认情况下，`clawhub` 安装到当前工作目录下的 `./skills`（或回退到配置的 OpenClaw 工作区）。OpenClaw 在下一个会话中将其识别为 `<workspace>/skills`。

## 安全注意事项

- 将第三方 Skills 视为**不受信任的代码**。启用前请阅读它们。
- 对于不受信任的输入和高风险工具，优先使用沙箱隔离运行。参见[沙箱隔离](/gateway/sandboxing)。
- `skills.entries.*.env` 和 `skills.entries.*.apiKey` 为该智能体轮次将秘密注入到**宿主机**进程中（而非沙箱）。将秘密保持在提示词和日志之外。
- 有关更广泛的威胁模型和检查清单，参见[安全性](/gateway/security)。

## 格式（AgentSkills + Pi 兼容）

`SKILL.md` 必须至少包含：

```markdown
---
name: nano-banana-pro
description: Generate or edit images via Gemini 3 Pro Image
---
```

注意事项：

- 我们遵循 AgentSkills 规范的布局/意图。
- 内嵌智能体使用的解析器仅支持**单行** frontmatter 键。
- `metadata` 应该是**单行 JSON 对象**。
- 在说明中使用 `{baseDir}` 来引用 Skills 文件夹路径。
- 可选的 frontmatter 键：
  - `homepage` — 在 macOS Skills UI 中显示为"Website"的 URL（也支持通过 `metadata.openclaw.homepage`）。
  - `user-invocable` — `true|false`（默认：`true`）。当为 `true` 时，Skills 作为用户斜杠命令暴露。
  - `disable-model-invocation` — `true|false`（默认：`false`）。当为 `true` 时，Skills 从模型提示词中排除（仍可通过用户调用使用）。
  - `command-dispatch` — `tool`（可选）。当设置为 `tool` 时，斜杠命令绕过模型直接调度到工具。
  - `command-tool` — 当设置 `command-dispatch: tool` 时要调用的工具名称。
  - `command-arg-mode` — `raw`（默认）。对于工具调度，将原始参数字符串转发到工具（无核心解析）。

    工具使用以下参数调用：
    `{ command: "<raw args>", commandName: "<slash command>", skillName: "<skill name>" }`。

## 门控（加载时过滤）

OpenClaw 使用 `metadata`（单行 JSON）**在加载时过滤 Skills**：

```markdown
---
name: nano-banana-pro
description: Generate or edit images via Gemini 3 Pro Image
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["uv"], "env": ["GEMINI_API_KEY"], "config": ["browser.enabled"] },
        "primaryEnv": "GEMINI_API_KEY",
      },
  }
---
```

`metadata.openclaw` 下的字段：

- `always: true` — 始终包含该 Skills（跳过其他门控）。
- `emoji` — macOS Skills UI 使用的可选表情符号。
- `homepage` — 在 macOS Skills UI 中显示为"Website"的可选 URL。
- `os` — 可选的平台列表（`darwin`、`linux`、`win32`）。如果设置，该 Skills 仅在这些操作系统上有资格。
- `requires.bins` — 列表；每个都必须存在于 `PATH` 中。
- `requires.anyBins` — 列表；至少一个必须存在于 `PATH` 中。
- `requires.env` — 列表；环境变量必须存在**或**在配置中提供。
- `requires.config` — `openclaw.json` 路径列表，必须为真值。
- `primaryEnv` — 与 `skills.entries.<name>.apiKey` 关联的环境变量名称。
- `install` — macOS Skills UI 使用的可选安装器规格数组（brew/node/go/uv/download）。

沙箱隔离注意事项：

- `requires.bins` 在 Skills 加载时在**宿主机**上检查。
- 如果智能体处于沙箱隔离状态，二进制文件也必须存在于**容器内部**。通过 `agents.defaults.sandbox.docker.setupCommand`（或自定义镜像）安装它。`setupCommand` 在容器创建后运行一次。包安装还需要网络出口、可写的根文件系统和沙箱中的 root 用户。示例：`summarize` Skills（`skills/summarize/SKILL.md`）需要 `summarize` CLI 在沙箱容器中才能运行。

安装器示例：

```markdown
---
name: gemini
description: Use Gemini CLI for coding assistance and Google search lookups.
metadata:
  {
    "openclaw":
      {
        "emoji": "♊️",
        "requires": { "bins": ["gemini"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "gemini-cli",
              "bins": ["gemini"],
              "label": "Install Gemini CLI (brew)",
            },
          ],
      },
  }
---
```

注意事项：

- 如果列出了多个安装器，Gateway 网关会选择**单个**首选选项（可用时选择 brew，否则选择 node）。
- 如果所有安装器都是 `download`，OpenClaw 会列出每个条目，以便你查看可用的构件。
- 安装器规格可以包含 `os: ["darwin"|"linux"|"win32"]` 按平台过滤选项。
- Node 安装遵循 `openclaw.json` 中的 `skills.install.nodeManager`（默认：npm；选项：npm/pnpm/yarn/bun）。这仅影响 **Skills 安装**；Gateway 网关运行时应仍为 Node（不推荐 Bun 用于 WhatsApp/Telegram）。
- Go 安装：如果缺少 `go` 且 `brew` 可用，Gateway 网关会首先通过 Homebrew 安装 Go，并在可能时将 `GOBIN` 设置为 Homebrew 的 `bin`。
- Download 安装：`url`（必填）、`archive`（`tar.gz` | `tar.bz2` | `zip`）、`extract`（默认：检测到归档时自动）、`stripComponents`、`targetDir`（默认：`~/.openclaw/tools/<skillKey>`）。

如果没有 `metadata.openclaw`，该 Skills 始终有资格（除非在配置中禁用或被 `skills.allowBundled` 阻止用于内置 Skills）。

## 配置覆盖（`~/.openclaw/openclaw.json`）

内置/托管 Skills 可以被切换并提供环境变量值：

```json5
{
  skills: {
    entries: {
      "nano-banana-pro": {
        enabled: true,
        apiKey: "GEMINI_KEY_HERE",
        env: {
          GEMINI_API_KEY: "GEMINI_KEY_HERE",
        },
        config: {
          endpoint: "https://example.invalid",
          model: "nano-pro",
        },
      },
      peekaboo: { enabled: true },
      sag: { enabled: false },
    },
  },
}
```

注意：如果 Skills 名称包含连字符，请用引号括起键名（JSON5 允许带引号的键名）。

配置键默认匹配 **Skills 名称**。如果 Skills 定义了 `metadata.openclaw.skillKey`，请在 `skills.entries` 下使用该键。

规则：

- `enabled: false` 禁用该 Skills，即使它是内置/已安装的。
- `env`：**仅在**变量在进程中尚未设置时注入。
- `apiKey`：为声明 `metadata.openclaw.primaryEnv` 的 Skills 提供的便捷字段。
- `config`：用于自定义单 Skills 字段的可选容器；自定义键必须放在这里。
- `allowBundled`：可选的仅用于**内置** Skills 的白名单。如果设置，只有列表中的内置 Skills 才有资格（托管/工作区 Skills 不受影响）。

## 环境变量注入（每次智能体运行）

当智能体运行开始时，OpenClaw：

1. 读取 Skills 元数据。
2. 将任何 `skills.entries.<key>.env` 或 `skills.entries.<key>.apiKey` 应用到 `process.env`。
3. 使用**有资格的** Skills 构建系统提示词。
4. 在运行结束后恢复原始环境。

这是**限定于智能体运行范围内的**，不是全局 shell 环境。

## 会话快照（性能）

OpenClaw 在**会话开始时**对有资格的 Skills 进行快照，并在同一会话的后续轮次中重用该列表。对 Skills 或配置的更改在下一个新会话中生效。

当 Skills 监视器启用或出现新的有资格的远程节点时，Skills 也可以在会话中刷新（见下文）。将此视为**热重载**：刷新后的列表会在下一个智能体轮次被获取。

## 远程 macOS 节点（Linux Gateway 网关）

如果 Gateway 网关运行在 Linux 上但连接了一个**允许 `system.run` 的 macOS 节点**（Exec 批准安全设置未设为 `deny`），当所需的二进制文件存在于该节点上时，OpenClaw 可以将仅限 macOS 的 Skills 视为有资格。智能体应通过 `nodes` 工具（通常是 `nodes.run`）执行这些 Skills。

这依赖于节点报告其命令支持以及通过 `system.run` 进行的二进制文件探测。如果 macOS 节点稍后离线，Skills 仍然可见；调用可能会失败，直到节点重新连接。

## Skills 监视器（自动刷新）

默认情况下，OpenClaw 监视 Skills 文件夹，并在 `SKILL.md` 文件更改时更新 Skills 快照。在 `skills.load` 下配置：

```json5
{
  skills: {
    load: {
      watch: true,
      watchDebounceMs: 250,
    },
  },
}
```

## Token 影响（Skills 列表）

当 Skills 有资格时，OpenClaw 将可用 Skills 的紧凑 XML 列表注入到系统提示词中（通过 `pi-coding-agent` 中的 `formatSkillsForPrompt`）。成本是确定性的：

- **基础开销（仅当 ≥1 个 Skills 时）：** 195 字符。
- **每个 Skills：** 97 字符 + XML 转义的 `<name>`、`<description>` 和 `<location>` 值的长度。

公式（字符）：

```
total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

注意事项：

- XML 转义将 `& < > " '` 扩展为实体（`&amp;`、`&lt;` 等），增加长度。
- Token 数量因模型分词器而异。粗略的 OpenAI 风格估计是 ~4 字符/token，所以**每个 Skills 97 字符 ≈ 24 token** 加上你的实际字段长度。

## 托管 Skills 生命周期

OpenClaw 作为安装的一部分（npm 包或 OpenClaw.app）发布一组基线 Skills 作为**内置 Skills**。`~/.openclaw/skills` 用于本地覆盖（例如，在不更改内置副本的情况下固定/修补 Skills）。工作区 Skills 由用户拥有，在名称冲突时覆盖两者。

## 配置参考

参见 [Skills 配置](/tools/skills-config)了解完整的配置 schema。

## 寻找更多 Skills？

浏览 https://clawhub.com。

---


---

## index

---
read_when:
  - 将 iOS/Android 节点配对到 Gateway 网关时
  - 使用节点 canvas/camera 为智能体提供上下文时
  - 添加新的节点命令或 CLI 辅助工具时
summary: 节点：配对、能力、权限以及 canvas/camera/screen/system 的 CLI 辅助工具
title: 节点
x-i18n:
  generated_at: "2026-02-03T07:51:55Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 74e9420f61c653e4ceeb00f5a27e4266bd1c7715c1000edd969c3ee185e74de9
  source_path: nodes/index.md
  workflow: 15
---

# 节点

**节点**是一个配套设备（macOS/iOS/Android/无头），它以 `role: "node"` 连接到 Gateway 网关 **WebSocket**（与操作员相同的端口），并通过 `node.invoke` 暴露命令接口（例如 `canvas.*`、`camera.*`、`system.*`）。协议详情：[Gateway 网关协议](/gateway/protocol)。

旧版传输：[Bridge 协议](/gateway/bridge-protocol)（TCP JSONL；当前节点已弃用/移除）。

macOS 也可以在**节点模式**下运行：菜单栏应用连接到 Gateway 网关的 WS 服务器，并将其本地 canvas/camera 命令作为节点暴露（因此 `openclaw nodes …` 可以针对这台 Mac 工作）。

注意事项：

- 节点是**外围设备**，不是 Gateway 网关。它们不运行 Gateway 网关服务。
- Telegram/WhatsApp 等消息落在 **Gateway 网关**上，而不是节点上。

## 配对 + 状态

**WS 节点使用设备配对。** 节点在 `connect` 期间呈现设备身份；Gateway 网关
为 `role: node` 创建设备配对请求。通过设备 CLI（或 UI）批准。

快速 CLI：

```bash
openclaw devices list
openclaw devices approve <requestId>
openclaw devices reject <requestId>
openclaw nodes status
openclaw nodes describe --node <idOrNameOrIp>
```

注意事项：

- 当节点的设备配对角色包含 `node` 时，`nodes status` 将节点标记为**已配对**。
- `node.pair.*`（CLI：`openclaw nodes pending/approve/reject`）是一个单独的 Gateway 网关拥有的
  节点配对存储；它**不会**限制 WS `connect` 握手。

## 远程节点主机（system.run）

当你的 Gateway 网关在一台机器上运行而你希望命令
在另一台机器上执行时，使用**节点主机**。模型仍然与 **Gateway 网关**通信；当选择 `host=node` 时，Gateway 网关
将 `exec` 调用转发到**节点主机**。

### 什么在哪里运行

- **Gateway 网关主机**：接收消息，运行模型，路由工具调用。
- **节点主机**：在节点机器上执行 `system.run`/`system.which`。
- **批准**：通过 `~/.openclaw/exec-approvals.json` 在节点主机上执行。

### 启动节点主机（前台）

在节点机器上：

```bash
openclaw node run --host <gateway-host> --port 18789 --display-name "Build Node"
```

### 通过 SSH 隧道访问远程 Gateway 网关（loopback 绑定）

如果 Gateway 网关绑定到 loopback（`gateway.bind=loopback`，本地模式下的默认值），
远程节点主机无法直接连接。创建 SSH 隧道并将
节点主机指向隧道的本地端。

示例（节点主机 -> Gateway 网关主机）：

```bash
# 终端 A（保持运行）：转发本地 18790 -> Gateway 网关 127.0.0.1:18789
ssh -N -L 18790:127.0.0.1:18789 user@gateway-host

# 终端 B：导出 Gateway 网关令牌并通过隧道连接
export OPENCLAW_GATEWAY_TOKEN="<gateway-token>"
openclaw node run --host 127.0.0.1 --port 18790 --display-name "Build Node"
```

注意事项：

- 令牌是 Gateway 网关配置中的 `gateway.auth.token`（Gateway 网关主机上的 `~/.openclaw/openclaw.json`）。
- `openclaw node run` 读取 `OPENCLAW_GATEWAY_TOKEN` 进行认证。

### 启动节点主机（服务）

```bash
openclaw node install --host <gateway-host> --port 18789 --display-name "Build Node"
openclaw node restart
```

### 配对 + 命名

在 Gateway 网关主机上：

```bash
openclaw nodes pending
openclaw nodes approve <requestId>
openclaw nodes list
```

命名选项：

- 在 `openclaw node run` / `openclaw node install` 上使用 `--display-name`（持久化在节点上的 `~/.openclaw/node.json` 中）。
- `openclaw nodes rename --node <id|name|ip> --name "Build Node"`（Gateway 网关覆盖）。

### 将命令加入允许列表

Exec 批准是**每个节点主机**的。从 Gateway 网关添加允许列表条目：

```bash
openclaw approvals allowlist add --node <id|name|ip> "/usr/bin/uname"
openclaw approvals allowlist add --node <id|name|ip> "/usr/bin/sw_vers"
```

批准存储在节点主机的 `~/.openclaw/exec-approvals.json` 中。

### 将 exec 指向节点

配置默认值（Gateway 网关配置）：

```bash
openclaw config set tools.exec.host node
openclaw config set tools.exec.security allowlist
openclaw config set tools.exec.node "<id-or-name>"
```

或按会话：

```
/exec host=node security=allowlist node=<id-or-name>
```

设置后，任何带有 `host=node` 的 `exec` 调用都会在节点主机上运行（受
节点允许列表/批准约束）。

相关：

- [节点主机 CLI](/cli/node)
- [Exec 工具](/tools/exec)
- [Exec 批准](/tools/exec-approvals)

## 调用命令

低级（原始 RPC）：

```bash
openclaw nodes invoke --node <idOrNameOrIp> --command canvas.eval --params '{"javaScript":"location.href"}'
```

对于常见的"给智能体一个 MEDIA 附件"工作流，存在更高级的辅助工具。

## 截图（canvas 快照）

如果节点正在显示 Canvas（WebView），`canvas.snapshot` 返回 `{ format, base64 }`。

CLI 辅助工具（写入临时文件并打印 `MEDIA:<path>`）：

```bash
openclaw nodes canvas snapshot --node <idOrNameOrIp> --format png
openclaw nodes canvas snapshot --node <idOrNameOrIp> --format jpg --max-width 1200 --quality 0.9
```

### Canvas 控制

```bash
openclaw nodes canvas present --node <idOrNameOrIp> --target https://example.com
openclaw nodes canvas hide --node <idOrNameOrIp>
openclaw nodes canvas navigate https://example.com --node <idOrNameOrIp>
openclaw nodes canvas eval --node <idOrNameOrIp> --js "document.title"
```

注意事项：

- `canvas present` 接受 URL 或本地文件路径（`--target`），以及可选的 `--x/--y/--width/--height` 用于定位。
- `canvas eval` 接受内联 JS（`--js`）或位置参数。

### A2UI（Canvas）

```bash
openclaw nodes canvas a2ui push --node <idOrNameOrIp> --text "Hello"
openclaw nodes canvas a2ui push --node <idOrNameOrIp> --jsonl ./payload.jsonl
openclaw nodes canvas a2ui reset --node <idOrNameOrIp>
```

注意事项：

- 仅支持 A2UI v0.8 JSONL（v0.9/createSurface 被拒绝）。

## 照片 + 视频（节点相机）

照片（`jpg`）：

```bash
openclaw nodes camera list --node <idOrNameOrIp>
openclaw nodes camera snap --node <idOrNameOrIp>            # 默认：两个朝向（2 个 MEDIA 行）
openclaw nodes camera snap --node <idOrNameOrIp> --facing front
```

视频片段（`mp4`）：

```bash
openclaw nodes camera clip --node <idOrNameOrIp> --duration 10s
openclaw nodes camera clip --node <idOrNameOrIp> --duration 3000 --no-audio
```

注意事项：

- 节点必须处于**前台**才能使用 `canvas.*` 和 `camera.*`（后台调用返回 `NODE_BACKGROUND_UNAVAILABLE`）。
- 片段时长被限制（当前 `<= 60s`）以避免过大的 base64 负载。
- Android 会在可能时提示 `CAMERA`/`RECORD_AUDIO` 权限；权限被拒绝会以 `*_PERMISSION_REQUIRED` 失败。

## 屏幕录制（节点）

节点暴露 `screen.record`（mp4）。示例：

```bash
openclaw nodes screen record --node <idOrNameOrIp> --duration 10s --fps 10
openclaw nodes screen record --node <idOrNameOrIp> --duration 10s --fps 10 --no-audio
```

注意事项：

- `screen.record` 需要节点应用处于前台。
- Android 会在录制前显示系统屏幕捕获提示。
- 屏幕录制被限制为 `<= 60s`。
- `--no-audio` 禁用麦克风捕获（iOS/Android 支持；macOS 使用系统捕获音频）。
- 当有多个屏幕可用时，使用 `--screen <index>` 选择显示器。

## 位置（节点）

当在设置中启用位置时，节点暴露 `location.get`。

CLI 辅助工具：

```bash
openclaw nodes location get --node <idOrNameOrIp>
openclaw nodes location get --node <idOrNameOrIp> --accuracy precise --max-age 15000 --location-timeout 10000
```

注意事项：

- 位置**默认关闭**。
- "始终"需要系统权限；后台获取是尽力而为的。
- 响应包括纬度/经度、精度（米）和时间戳。

## 短信（Android 节点）

当用户授予 **SMS** 权限且设备支持电话功能时，Android 节点可以暴露 `sms.send`。

低级调用：

```bash
openclaw nodes invoke --node <idOrNameOrIp> --command sms.send --params '{"to":"+15555550123","message":"Hello from OpenClaw"}'
```

注意事项：

- 在能力被广播之前，必须在 Android 设备上接受权限提示。
- 没有电话功能的纯 Wi-Fi 设备不会广播 `sms.send`。

## 系统命令（节点主机 / mac 节点）

macOS 节点暴露 `system.run`、`system.notify` 和 `system.execApprovals.get/set`。
无头节点主机暴露 `system.run`、`system.which` 和 `system.execApprovals.get/set`。

示例：

```bash
openclaw nodes run --node <idOrNameOrIp> -- echo "Hello from mac node"
openclaw nodes notify --node <idOrNameOrIp> --title "Ping" --body "Gateway ready"
```

注意事项：

- `system.run` 在负载中返回 stdout/stderr/退出码。
- `system.notify` 遵守 macOS 应用上的通知权限状态。
- `system.run` 支持 `--cwd`、`--env KEY=VAL`、`--command-timeout` 和 `--needs-screen-recording`。
- `system.notify` 支持 `--priority <passive|active|timeSensitive>` 和 `--delivery <system|overlay|auto>`。
- macOS 节点会丢弃 `PATH` 覆盖；无头节点主机仅在 `PATH` 前置到节点主机 PATH 时才接受它。
- 在 macOS 节点模式下，`system.run` 受 macOS 应用中的 exec 批准限制（设置 → Exec 批准）。
  Ask/allowlist/full 的行为与无头节点主机相同；被拒绝的提示返回 `SYSTEM_RUN_DENIED`。
- 在无头节点主机上，`system.run` 受 exec 批准限制（`~/.openclaw/exec-approvals.json`）。

## Exec 节点绑定

当有多个节点可用时，你可以将 exec 绑定到特定节点。
这设置了 `exec host=node` 的默认节点（可以按智能体覆盖）。

全局默认：

```bash
openclaw config set tools.exec.node "node-id-or-name"
```

按智能体覆盖：

```bash
openclaw config get agents.list
openclaw config set agents.list[0].tools.exec.node "node-id-or-name"
```

取消设置以允许任何节点：

```bash
openclaw config unset tools.exec.node
openclaw config unset agents.list[0].tools.exec.node
```

## 权限映射

节点可能在 `node.list` / `node.describe` 中包含 `permissions` 映射，按权限名称（例如 `screenRecording`、`accessibility`）键入，值为布尔值（`true` = 已授予）。

## 无头节点主机（跨平台）

OpenClaw 可以运行**无头节点主机**（无 UI），它连接到 Gateway 网关
WebSocket 并暴露 `system.run` / `system.which`。这在 Linux/Windows
上或在服务器旁运行最小节点时很有用。

启动它：

```bash
openclaw node run --host <gateway-host> --port 18789
```

注意事项：

- 仍然需要配对（Gateway 网关会显示节点批准提示）。
- 节点主机将其节点 id、令牌、显示名称和 Gateway 网关连接信息存储在 `~/.openclaw/node.json` 中。
- Exec 批准通过 `~/.openclaw/exec-approvals.json` 在本地执行
  （参见 [Exec 批准](/tools/exec-approvals)）。
- 在 macOS 上，当配套应用 exec 主机可达时，无头节点主机优先使用它，
  如果应用不可用则回退到本地执行。设置 `OPENCLAW_NODE_EXEC_HOST=app` 要求
  使用应用，或设置 `OPENCLAW_NODE_EXEC_FALLBACK=0` 禁用回退。
- 当 Gateway 网关 WS 使用 TLS 时，添加 `--tls` / `--tls-fingerprint`。

## Mac 节点模式

- macOS 菜单栏应用作为节点连接到 Gateway 网关 WS 服务器（因此 `openclaw nodes …` 可以针对这台 Mac 工作）。
- 在远程模式下，应用为 Gateway 网关端口打开 SSH 隧道并连接到 `localhost`。


---

## index

---
read_when:
  - 你想选择一个模型提供商
  - 你需要快速了解支持的 LLM 后端
summary: OpenClaw 支持的模型提供商（LLM）
title: 模型提供商
x-i18n:
  generated_at: "2026-02-03T07:53:32Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: eb4a97438adcf610499253afcf8b2af6624f4be098df389a6c3746f14c4a901b
  source_path: providers/index.md
  workflow: 15
---

# 模型提供商

OpenClaw 可以使用许多 LLM 提供商。选择一个提供商，进行认证，然后将默认模型设置为 `provider/model`。

正在寻找聊天渠道文档（WhatsApp/Telegram/Discord/Slack/Mattermost（插件）等）？参见[渠道](/channels)。

## 亮点：Venice（Venice AI）

Venice 是我们推荐的 Venice AI 设置，用于隐私优先的推理，并可选择使用 Opus 处理困难任务。

- 默认：`venice/llama-3.3-70b`
- 最佳综合：`venice/claude-opus-45`（Opus 仍然是最强的）

参见 [Venice AI](/providers/venice)。

## 快速开始

1. 与提供商进行认证（通常通过 `openclaw onboard`）。
2. 设置默认模型：

```json5
{
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-5" } } },
}
```

## 提供商文档

- [OpenAI（API + Codex）](/providers/openai)
- [Anthropic（API + Claude Code CLI）](/providers/anthropic)
- [Qwen（OAuth）](/providers/qwen)
- [OpenRouter](/providers/openrouter)
- [Vercel AI Gateway](/providers/vercel-ai-gateway)
- [Moonshot AI（Kimi + Kimi Coding）](/providers/moonshot)
- [OpenCode Zen](/providers/opencode)
- [Amazon Bedrock](/providers/bedrock)
- [Z.AI](/providers/zai)
- [Xiaomi](/providers/xiaomi)
- [GLM 模型](/providers/glm)
- [MiniMax](/providers/minimax)
- [Venice（Venice AI，注重隐私）](/providers/venice)
- [Ollama（本地模型）](/providers/ollama)

## 转录提供商

- [Deepgram（音频转录）](/providers/deepgram)

## 社区工具

- [Claude Max API Proxy](/providers/claude-max-api-proxy) - 将 Claude Max/Pro 订阅作为 OpenAI 兼容的 API 端点使用

有关完整的提供商目录（xAI、Groq、Mistral 等）和高级配置，
参见[模型提供商](/concepts/model-providers)。


---

## heartbeat

---
read_when:
  - 调整心跳频率或消息时
  - 在心跳和 cron 之间选择定时任务方案时
summary: 心跳轮询消息和通知规则
title: 心跳
x-i18n:
  generated_at: "2026-02-03T07:48:57Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: 18b017066aa2c41811b985564dd389834906f4576e85b576fb357a0eff482e69
  source_path: gateway/heartbeat.md
  workflow: 15
---

# 心跳（Gateway 网关）

> **心跳 vs Cron？** 参见 [Cron vs 心跳](/automation/cron-vs-heartbeat) 了解何时使用哪种方案。

心跳在主会话中运行**周期性智能体轮次**，使模型能够在不打扰你的情况下提醒需要关注的事项。

## 快速开始（新手）

1. 保持心跳启用（默认 `30m`，Anthropic OAuth/setup-token 为 `1h`）或设置你自己的频率。
2. 在智能体工作区创建一个简单的 `HEARTBEAT.md` 检查清单（可选但推荐）。
3. 决定心跳消息发送到哪里（默认 `target: "last"`）。
4. 可选：启用心跳推理内容发送以提高透明度。
5. 可选：将心跳限制在活动时段（本地时间）。

配置示例：

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        target: "last",
        // activeHours: { start: "08:00", end: "24:00" },
        // includeReasoning: true, // 可选：同时发送单独的 `Reasoning:` 消息
      },
    },
  },
}
```

## 默认值

- 间隔：`30m`（当检测到的认证模式为 Anthropic OAuth/setup-token 时为 `1h`）。设置 `agents.defaults.heartbeat.every` 或单智能体 `agents.list[].heartbeat.every`；使用 `0m` 禁用。
- 提示内容（可通过 `agents.defaults.heartbeat.prompt` 配置）：
  `Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.`
- 心跳提示**原样**作为用户消息发送。系统提示包含"Heartbeat"部分，运行在内部被标记。
- 活动时段（`heartbeat.activeHours`）按配置的时区检查。在时段外，心跳会被跳过直到下一个时段内的时钟周期。

## 心跳提示的用途

默认提示故意设计得比较宽泛：

- **后台任务**："Consider outstanding tasks"促使智能体审查待办事项（收件箱、日历、提醒、排队工作）并提醒任何紧急事项。
- **人类签到**："Checkup sometimes on your human during day time"促使偶尔发送轻量级的"有什么需要帮助的吗？"消息，但通过使用你配置的本地时区避免夜间打扰（参见 [/concepts/timezone](/concepts/timezone)）。

如果你希望心跳执行非常具体的任务（例如"检查 Gmail PubSub 统计"或"验证 Gateway 网关健康状态"），将 `agents.defaults.heartbeat.prompt`（或 `agents.list[].heartbeat.prompt`）设置为自定义内容（原样发送）。

## 响应约定

- 如果没有需要关注的事项，回复 **`HEARTBEAT_OK`**。
- 在心跳运行期间，当 `HEARTBEAT_OK` 出现在回复的**开头或结尾**时，OpenClaw 将其视为确认。该标记会被移除，如果剩余内容 **≤ `ackMaxChars`**（默认：300），则回复被丢弃。
- 如果 `HEARTBEAT_OK` 出现在回复的**中间**，则不会被特殊处理。
- 对于警报，**不要**包含 `HEARTBEAT_OK`；只返回警报文本。

在心跳之外，消息开头/结尾的意外 `HEARTBEAT_OK` 会被移除并记录日志；仅包含 `HEARTBEAT_OK` 的消息会被丢弃。

## 配置

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m", // 默认：30m（0m 禁用）
        model: "anthropic/claude-opus-4-5",
        includeReasoning: false, // 默认：false（可用时发送单独的 Reasoning: 消息）
        target: "last", // last | none | <channel id>（核心或插件，例如 "bluebubbles"）
        to: "+15551234567", // 可选的渠道特定覆盖
        prompt: "Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.",
        ackMaxChars: 300, // HEARTBEAT_OK 后允许的最大字符数
      },
    },
  },
}
```

### 作用域和优先级

- `agents.defaults.heartbeat` 设置全局心跳行为。
- `agents.list[].heartbeat` 在其之上合并；如果任何智能体有 `heartbeat` 块，**只有这些智能体**运行心跳。
- `channels.defaults.heartbeat` 为所有渠道设置可见性默认值。
- `channels.<channel>.heartbeat` 覆盖渠道默认值。
- `channels.<channel>.accounts.<id>.heartbeat`（多账户渠道）覆盖单渠道设置。

### 单智能体心跳

如果任何 `agents.list[]` 条目包含 `heartbeat` 块，**只有这些智能体**运行心跳。单智能体块在 `agents.defaults.heartbeat` 之上合并（因此你可以设置一次共享默认值，然后按智能体覆盖）。

示例：两个智能体，只有第二个智能体运行心跳。

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        target: "last",
      },
    },
    list: [
      { id: "main", default: true },
      {
        id: "ops",
        heartbeat: {
          every: "1h",
          target: "whatsapp",
          to: "+15551234567",
          prompt: "Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.",
        },
      },
    ],
  },
}
```

### 字段说明

- `every`：心跳间隔（时长字符串；默认单位 = 分钟）。
- `model`：心跳运行的可选模型覆盖（`provider/model`）。
- `includeReasoning`：启用时，也会发送单独的 `Reasoning:` 消息（如果可用）（与 `/reasoning on` 格式相同）。
- `session`：心跳运行的可选会话键。
  - `main`（默认）：智能体主会话。
  - 显式会话键（从 `openclaw sessions --json` 或 [sessions CLI](/cli/sessions) 复制）。
  - 会话键格式：参见[会话](/concepts/session)和[群组](/channels/groups)。
- `target`：
  - `last`（默认）：发送到最后使用的外部渠道。
  - 显式渠道：`whatsapp` / `telegram` / `discord` / `googlechat` / `slack` / `msteams` / `signal` / `imessage`。
  - `none`：运行心跳但**不发送**到外部。
- `to`：可选的收件人覆盖（渠道特定 ID，例如 WhatsApp 的 E.164 或 Telegram 聊天 ID）。
- `prompt`：覆盖默认提示内容（不合并）。
- `ackMaxChars`：`HEARTBEAT_OK` 后在发送前允许的最大字符数。

## 发送行为

- 心跳默认在智能体主会话中运行（`agent:<id>:<mainKey>`），或当 `session.scope = "global"` 时在 `global` 中运行。设置 `session` 可覆盖为特定渠道会话（Discord/WhatsApp 等）。
- `session` 只影响运行上下文；发送由 `target` 和 `to` 控制。
- 要发送到特定渠道/收件人，设置 `target` + `to`。使用 `target: "last"` 时，发送使用该会话的最后一个外部渠道。
- 如果主队列繁忙，心跳会被跳过并稍后重试。
- 如果 `target` 解析为无外部目标，运行仍会发生但不会发送出站消息。
- 仅心跳回复**不会**保持会话活跃；最后的 `updatedAt` 会被恢复，因此空闲过期正常工作。

## 可见性控制

默认情况下，`HEARTBEAT_OK` 确认会被抑制，而警报内容会被发送。你可以按渠道或按账户调整：

```yaml
channels:
  defaults:
    heartbeat:
      showOk: false # 隐藏 HEARTBEAT_OK（默认）
      showAlerts: true # 显示警报消息（默认）
      useIndicator: true # 发出指示器事件（默认）
  telegram:
    heartbeat:
      showOk: true # 在 Telegram 上显示 OK 确认
  whatsapp:
    accounts:
      work:
        heartbeat:
          showAlerts: false # 为此账户抑制警报发送
```

优先级：单账户 → 单渠道 → 渠道默认值 → 内置默认值。

### 各标志的作用

- `showOk`：当模型返回仅 OK 的回复时，发送 `HEARTBEAT_OK` 确认。
- `showAlerts`：当模型返回非 OK 回复时，发送警报内容。
- `useIndicator`：为 UI 状态界面发出指示器事件。

如果**所有三个**都为 false，OpenClaw 会完全跳过心跳运行（不调用模型）。

### 单渠道 vs 单账户示例

```yaml
channels:
  defaults:
    heartbeat:
      showOk: false
      showAlerts: true
      useIndicator: true
  slack:
    heartbeat:
      showOk: true # 所有 Slack 账户
    accounts:
      ops:
        heartbeat:
          showAlerts: false # 仅为 ops 账户抑制警报
  telegram:
    heartbeat:
      showOk: true
```

### 常见模式

| 目标                          | 配置                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| 默认行为（静默 OK，警报开启） | _（无需配置）_                                                                           |
| 完全静默（无消息，无指示器）  | `channels.defaults.heartbeat: { showOk: false, showAlerts: false, useIndicator: false }` |
| 仅指示器（无消息）            | `channels.defaults.heartbeat: { showOk: false, showAlerts: false, useIndicator: true }`  |
| 仅在一个渠道显示 OK           | `channels.telegram.heartbeat: { showOk: true }`                                          |

## HEARTBEAT.md（可选）

如果工作区中存在 `HEARTBEAT.md` 文件，默认提示会告诉智能体读取它。把它想象成你的"心跳检查清单"：小巧、稳定，可以安全地每 30 分钟包含一次。

如果 `HEARTBEAT.md` 存在但实际上是空的（只有空行和 markdown 标题如 `# Heading`），OpenClaw 会跳过心跳运行以节省 API 调用。如果文件不存在，心跳仍会运行，由模型决定做什么。

保持它小巧（简短的检查清单或提醒）以避免提示膨胀。

`HEARTBEAT.md` 示例：

```md
# Heartbeat checklist

- Quick scan: anything urgent in inboxes?
- If it's daytime, do a lightweight check-in if nothing else is pending.
- If a task is blocked, write down _what is missing_ and ask Peter next time.
```

### 智能体可以更新 HEARTBEAT.md 吗？

可以 — 如果你要求它这样做。

`HEARTBEAT.md` 只是智能体工作区中的普通文件，所以你可以在普通聊天中告诉智能体：

- "更新 `HEARTBEAT.md` 添加每日日历检查。"
- "重写 `HEARTBEAT.md`，使其更短并专注于收件箱跟进。"

如果你希望这主动发生，你也可以在心跳提示中包含明确的一行，如："If the checklist becomes stale, update HEARTBEAT.md with a better one."

安全提示：不要在 `HEARTBEAT.md` 中放置密钥（API 密钥、电话号码、私有令牌）— 它会成为提示上下文的一部分。

## 手动唤醒（按需）

你可以排队一个系统事件并触发即时心跳：

```bash
openclaw system event --text "Check for urgent follow-ups" --mode now
```

如果多个智能体配置了 `heartbeat`，手动唤醒会立即运行每个智能体的心跳。

使用 `--mode next-heartbeat` 等待下一个计划的时钟周期。

## 推理内容发送（可选）

默认情况下，心跳只发送最终的"答案"负载。

如果你想要透明度，请启用：

- `agents.defaults.heartbeat.includeReasoning: true`

启用后，心跳还会发送一条以 `Reasoning:` 为前缀的单独消息（与 `/reasoning on` 格式相同）。当智能体管理多个会话/代码库并且你想了解它为什么决定联系你时，这很有用 — 但它也可能泄露比你想要的更多内部细节。在群聊中建议保持关闭。

## 成本意识

心跳运行完整的智能体轮次。更短的间隔消耗更多 token。保持 `HEARTBEAT.md` 小巧，如果你只想要内部状态更新，考虑使用更便宜的 `model` 或 `target: "none"`。


---

## cron-jobs

---
read_when:
  - 调度后台任务或唤醒
  - 配置需要与心跳一起或并行运行的自动化
  - 在心跳和定时任务之间做选择
summary: Gateway网关调度器的定时任务与唤醒
title: 定时任务
x-i18n:
  generated_at: "2026-02-01T19:37:32Z"
  model: claude-opus-4-5
  provider: pi
  source_hash: d43268b0029f1b13d0825ddcc9c06a354987ea17ce02f3b5428a9c68bf936676
  source_path: automation/cron-jobs.md
  workflow: 14
---

# 定时任务（Gateway网关调度器）

> **定时任务还是心跳？** 请参阅[定时任务与心跳对比](/automation/cron-vs-heartbeat)了解何时使用哪种方式。

定时任务是 Gateway网关内置的调度器。它持久化任务、在合适的时间唤醒智能体，并可选择将输出发送回聊天。

如果你想要 _"每天早上运行"_ 或 _"20 分钟后提醒智能体"_，定时任务就是对应的机制。

## 简要概述

- 定时任务运行在 **Gateway网关内部**（而非模型内部）。
- 任务持久化存储在 `~/.openclaw/cron/` 下，因此重启不会丢失计划。
- 两种执行方式：
  - **主会话**：入队一个系统事件，然后在下一次心跳时运行。
  - **隔离式**：在 `cron:<jobId>` 中运行专用智能体轮次，可投递摘要（默认 announce）或不投递。
- 唤醒是一等功能：任务可以请求"立即唤醒"或"下次心跳时"。

## 快速开始（可操作）

创建一个一次性提醒，验证其存在，然后立即运行：

```bash
openclaw cron add \
  --name "Reminder" \
  --at "2026-02-01T16:00:00Z" \
  --session main \
  --system-event "Reminder: check the cron docs draft" \
  --wake now \
  --delete-after-run

openclaw cron list
openclaw cron run <job-id> --force
openclaw cron runs --id <job-id>
```

调度一个带投递功能的周期性隔离任务：

```bash
openclaw cron add \
  --name "Morning brief" \
  --cron "0 7 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Summarize overnight updates." \
  --announce \
  --channel slack \
  --to "channel:C1234567890"
```

## 工具调用等价形式（Gateway网关定时任务工具）

有关规范的 JSON 结构和示例，请参阅[工具调用的 JSON 模式](/automation/cron-jobs#json-schema-for-tool-calls)。

## 定时任务的存储位置

定时任务默认持久化存储在 Gateway网关主机的 `~/.openclaw/cron/jobs.json` 中。Gateway网关将文件加载到内存中，并在更改时写回，因此仅在 Gateway网关停止时手动编辑才是安全的。请优先使用 `openclaw cron add/edit` 或定时任务工具调用 API 进行更改。

## 新手友好概述

将定时任务理解为：**何时**运行 + **做什么**。

1. **选择调度计划**
   - 一次性提醒 → `schedule.kind = "at"`（CLI：`--at`）
   - 重复任务 → `schedule.kind = "every"` 或 `schedule.kind = "cron"`
   - 如果你的 ISO 时间戳省略了时区，将被视为 **UTC**。

2. **选择运行位置**
   - `sessionTarget: "main"` → 在下一次心跳时使用主会话上下文运行。
   - `sessionTarget: "isolated"` → 在 `cron:<jobId>` 中运行专用智能体轮次。

3. **选择负载**
   - 主会话 → `payload.kind = "systemEvent"`
   - 隔离会话 → `payload.kind = "agentTurn"`

可选：一次性任务（`schedule.kind = "at"`）默认会在成功运行后删除。设置
`deleteAfterRun: false` 可保留它（成功后会禁用）。

## 概念

### 任务

定时任务是一条存储记录，包含：

- 一个**调度计划**（何时运行），
- 一个**负载**（做什么），
- 可选的**投递**（输出发送到哪里）。
- 可选的**智能体绑定**（`agentId`）：在指定智能体下运行任务；如果缺失或未知，Gateway网关会回退到默认智能体。

任务通过稳定的 `jobId` 标识（用于 CLI/Gateway网关 API）。
在智能体工具调用中，`jobId` 是规范字段；旧版 `id` 仍可兼容使用。
一次性任务默认会在成功运行后自动删除；设置 `deleteAfterRun: false` 可保留它。

### 调度计划

定时任务支持三种调度类型：

- `at`：一次性时间戳（ISO 8601 字符串）。
- `every`：固定间隔（毫秒）。
- `cron`：5 字段 cron 表达式，可选 IANA 时区。

Cron 表达式使用 `croner`。如果省略时区，将使用 Gateway网关主机的本地时区。

### 主会话与隔离式执行

#### 主会话任务（系统事件）

主会话任务入队一个系统事件，并可选择唤醒心跳运行器。它们必须使用 `payload.kind = "systemEvent"`。

- `wakeMode: "next-heartbeat"`（默认）：事件等待下一次计划心跳。
- `wakeMode: "now"`：事件触发立即心跳运行。

当你需要正常的心跳提示 + 主会话上下文时，这是最佳选择。参见[心跳](/gateway/heartbeat)。

#### 隔离任务（专用定时会话）

隔离任务在会话 `cron:<jobId>` 中运行专用智能体轮次。

关键行为：

- 提示以 `[cron:<jobId> <任务名称>]` 为前缀，便于追踪。
- 每次运行都会启动一个**全新的会话 ID**（不继承之前的对话）。
- 如果未指定 `delivery`，隔离任务会默认以“announce”方式投递摘要。
- `delivery.mode` 可选 `announce`（投递摘要）或 `none`（内部运行）。

对于嘈杂、频繁或"后台杂务"类任务，使用隔离任务可以避免污染你的主聊天记录。

### 负载结构（运行内容）

支持两种负载类型：

- `systemEvent`：仅限主会话，通过心跳提示路由。
- `agentTurn`：仅限隔离会话，运行专用智能体轮次。

常用 `agentTurn` 字段：

- `message`：必填文本提示。
- `model` / `thinking`：可选覆盖（见下文）。
- `timeoutSeconds`：可选超时覆盖。

### 模型和思维覆盖

隔离任务（`agentTurn`）可以覆盖模型和思维级别：

- `model`：提供商/模型字符串（例如 `anthropic/claude-sonnet-4-20250514`）或别名（例如 `opus`）
- `thinking`：思维级别（`off`、`minimal`、`low`、`medium`、`high`、`xhigh`；仅限 GPT-5.2 + Codex 模型）

注意：你也可以在主会话任务上设置 `model`，但这会更改共享的主会话模型。我们建议仅对隔离任务使用模型覆盖，以避免意外的上下文切换。

优先级解析顺序：

1. 任务负载覆盖（最高优先级）
2. 钩子特定默认值（例如 `hooks.gmail.model`）
3. 智能体配置默认值

### 投递（渠道 + 目标）

隔离任务可以通过顶层 `delivery` 配置投递输出：

- `delivery.mode`：`announce`（投递摘要）或 `none`
- `delivery.channel`：`whatsapp` / `telegram` / `discord` / `slack` / `mattermost`（插件）/ `signal` / `imessage` / `last`
- `delivery.to`：渠道特定的接收目标
- `delivery.bestEffort`：投递失败时避免任务失败

当启用 announce 投递时，该轮次会抑制消息工具发送；请使用 `delivery.channel`/`delivery.to` 来指定目标。

如果省略 `delivery.channel` 或 `delivery.to`，定时任务会回退到主会话的“最后路由”（智能体最后回复的位置）。

目标格式提醒：

- Slack/Discord/Mattermost（插件）目标应使用明确前缀（例如 `channel:<id>`、`user:<id>`）以避免歧义。
- Telegram 主题应使用 `:topic:` 格式（见下文）。

#### Telegram 投递目标（主题/论坛帖子）

Telegram 通过 `message_thread_id` 支持论坛主题。对于定时任务投递，你可以将主题/帖子编码到 `to` 字段中：

- `-1001234567890`（仅聊天 ID）
- `-1001234567890:topic:123`（推荐：明确的主题标记）
- `-1001234567890:123`（简写：数字后缀）

带前缀的目标如 `telegram:...` / `telegram:group:...` 也可接受：

- `telegram:group:-1001234567890:topic:123`

## 工具调用的 JSON 模式

直接调用 Gateway网关 `cron.*` 工具（智能体工具调用或 RPC）时使用这些结构。CLI 标志接受人类可读的时间格式如 `20m`，但工具调用应使用 ISO 8601 字符串作为 `schedule.at`，并使用毫秒作为 `schedule.everyMs`。

### cron.add 参数

一次性主会话任务（系统事件）：

```json
{
  "name": "Reminder",
  "schedule": { "kind": "at", "at": "2026-02-01T16:00:00Z" },
  "sessionTarget": "main",
  "wakeMode": "now",
  "payload": { "kind": "systemEvent", "text": "Reminder text" },
  "deleteAfterRun": true
}
```

带投递的周期性隔离任务：

```json
{
  "name": "Morning brief",
  "schedule": { "kind": "cron", "expr": "0 7 * * *", "tz": "America/Los_Angeles" },
  "sessionTarget": "isolated",
  "wakeMode": "next-heartbeat",
  "payload": {
    "kind": "agentTurn",
    "message": "Summarize overnight updates."
  },
  "delivery": {
    "mode": "announce",
    "channel": "slack",
    "to": "channel:C1234567890",
    "bestEffort": true
  }
}
```

说明：

- `schedule.kind`：`at`（`at`）、`every`（`everyMs`）或 `cron`（`expr`，可选 `tz`）。
- `schedule.at` 接受 ISO 8601（可省略时区；省略时按 UTC 处理）。
- `everyMs` 为毫秒数。
- `sessionTarget` 必须为 `"main"` 或 `"isolated"`，且必须与 `payload.kind` 匹配。
- 可选字段：`agentId`、`description`、`enabled`、`deleteAfterRun`、`delivery`。
- `wakeMode` 省略时默认为 `"next-heartbeat"`。

### cron.update 参数

```json
{
  "jobId": "job-123",
  "patch": {
    "enabled": false,
    "schedule": { "kind": "every", "everyMs": 3600000 }
  }
}
```

说明：

- `jobId` 是规范字段；`id` 可兼容使用。
- 在补丁中使用 `agentId: null` 可清除智能体绑定。

### cron.run 和 cron.remove 参数

```json
{ "jobId": "job-123", "mode": "force" }
```

```json
{ "jobId": "job-123" }
```

## 存储与历史

- 任务存储：`~/.openclaw/cron/jobs.json`（Gateway网关管理的 JSON）。
- 运行历史：`~/.openclaw/cron/runs/<jobId>.jsonl`（JSONL，自动清理）。
- 覆盖存储路径：配置中的 `cron.store`。

## 配置

```json5
{
  cron: {
    enabled: true, // 默认 true
    store: "~/.openclaw/cron/jobs.json",
    maxConcurrentRuns: 1, // 默认 1
  },
}
```

完全禁用定时任务：

- `cron.enabled: false`（配置）
- `OPENCLAW_SKIP_CRON=1`（环境变量）

## CLI 快速开始

一次性提醒（UTC ISO，成功后自动删除）：

```bash
openclaw cron add \
  --name "Send reminder" \
  --at "2026-01-12T18:00:00Z" \
  --session main \
  --system-event "Reminder: submit expense report." \
  --wake now \
  --delete-after-run
```

一次性提醒（主会话，立即唤醒）：

```bash
openclaw cron add \
  --name "Calendar check" \
  --at "20m" \
  --session main \
  --system-event "Next heartbeat: check calendar." \
  --wake now
```

周期性隔离任务（投递到 WhatsApp）：

```bash
openclaw cron add \
  --name "Morning status" \
  --cron "0 7 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Summarize inbox + calendar for today." \
  --announce \
  --channel whatsapp \
  --to "+15551234567"
```

周期性隔离任务（投递到 Telegram 主题）：

```bash
openclaw cron add \
  --name "Nightly summary (topic)" \
  --cron "0 22 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Summarize today; send to the nightly topic." \
  --announce \
  --channel telegram \
  --to "-1001234567890:topic:123"
```

带模型和思维覆盖的隔离任务：

```bash
openclaw cron add \
  --name "Deep analysis" \
  --cron "0 6 * * 1" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Weekly deep analysis of project progress." \
  --model "opus" \
  --thinking high \
  --announce \
  --channel whatsapp \
  --to "+15551234567"
```

智能体选择（多智能体配置）：

```bash
# 将任务绑定到智能体 "ops"（如果该智能体不存在则回退到默认智能体）
openclaw cron add --name "Ops sweep" --cron "0 6 * * *" --session isolated --message "Check ops queue" --agent ops

# 切换或清除现有任务的智能体
openclaw cron edit <jobId> --agent ops
openclaw cron edit <jobId> --clear-agent
```

手动运行（调试）：

```bash
openclaw cron run <jobId> --force
```

编辑现有任务（补丁字段）：

```bash
openclaw cron edit <jobId> \
  --message "Updated prompt" \
  --model "opus" \
  --thinking low
```

运行历史：

```bash
openclaw cron runs --id <jobId> --limit 50
```

不创建任务直接发送系统事件：

```bash
openclaw system event --mode now --text "Next heartbeat: check battery."
```

## Gateway网关 API 接口

- `cron.list`、`cron.status`、`cron.add`、`cron.update`、`cron.remove`
- `cron.run`（强制或到期）、`cron.runs`
  如需不创建任务直接发送系统事件，请使用 [`openclaw system event`](/cli/system)。

## 故障排除

### "没有任何任务运行"

- 检查定时任务是否已启用：`cron.enabled` 和 `OPENCLAW_SKIP_CRON`。
- 检查 Gateway网关是否持续运行（定时任务运行在 Gateway网关进程内部）。
- 对于 `cron` 调度：确认时区（`--tz`）与主机时区的关系。

### Telegram 投递到了错误的位置

- 对于论坛主题，使用 `-100…:topic:<id>` 以确保明确无歧义。
- 如果你在日志或存储的"最后路由"目标中看到 `telegram:...` 前缀，这是正常的；定时任务投递接受这些前缀并仍能正确解析主题 ID。


---


