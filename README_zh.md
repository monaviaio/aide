# Aide - AI 编码助手部署方案

**monaviaio/aide** 是一个基于 Docker 的 AI 编码助手部署仓库。[English Documentation](./README.md)

## 📦 项目概述

这是一个**预配置的 CodeNomad 部署环境**，通过 Docker 容器快速启动一个完整的 AI 编码助手服务。

## 🏗️ 核心组件

1. **CodeNomad** - AI 编码助手的命令中心
   - 由 NeuralNomadsAI 开发的开源项目
   - 提供 Web 界面访问 AI 编码助手
   - 支持多种 AI 模型（通过 OpenRouter API）

2. **oh-my-opencode-slim** - 轻量级 AI 代理编排插件
   - 将 AI 助手从单一执行者升级为"管理者"
   - 支持多代理协作（Explorer、Oracle、Librarian、Designer、Fixer 等）
   - 大幅减少 token 消耗的优化版本

3. **OpenCode** - AI 编码工具
   - 底层 AI 编码引擎

## 🚀 主要功能

- **Web 界面**：通过浏览器访问 AI 编码助手（默认端口 8080）
- **多代理系统**：自动将复杂任务委派给专门的子代理
- **持久化存储**：工作空间和配置文件通过 Docker volumes 保存
- **认证支持**：可配置用户名/密码或跳过认证
- **OpenRouter 集成**：使用 OpenRouter API 访问多种 LLM 模型

## 📁 目录结构

```
.initial/
  config/         # CodeNomad 和 OpenCode 配置
    auth/
      auth.json   # OpenRouter API 密钥配置
  claude/skills/  # Claude 技能定义
.storage/
  workspaces/     # 持久化工作空间
```

## 🔧 使用方式

1. 配置 `.initial/config/auth/auth.json` 中的 OpenRouter API 密钥
2. 设置环境变量（用户名、密码、端口等）
3. 运行 `docker-compose up -d` 启动服务
4. 访问 `http://localhost:28080` 使用 AI 编码助手

## 💡 适用场景

- 需要快速部署 AI 编码助手的开发者
- 想要多代理协作能力的团队
- 需要自托管 AI 编码环境的组织
- 希望通过 OpenRouter 使用多种 LLM 的用户

**总结**：这是一个**开箱即用的 AI 编码助手部署方案**，集成了先进的多代理编排能力，通过 docker compose 实现一键部署。
