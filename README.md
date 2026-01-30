# Aide - AI Coding Assistant Deployment

**monaviaio/aide** is a Docker-based deployment repository for AI coding assistants. [中文文档](./README_zh.md)

## 📦 Overview

A **pre-configured CodeNomad deployment environment** that quickly launches a complete AI coding assistant service through Docker containers.

## 🏗️ Core Components

1. **CodeNomad** - Command center for AI coding assistants
   - Open-source project by NeuralNomadsAI
   - Provides web interface access to AI coding assistants
   - Supports multiple AI models (via OpenRouter API)

2. **oh-my-opencode-slim** - Lightweight AI agent orchestration plugin
   - Upgrades AI assistant from single executor to "manager"
   - Supports multi-agent collaboration (Explorer, Oracle, Librarian, Designer, Fixer, etc.)
   - Optimized version that significantly reduces token consumption

3. **OpenCode** - AI coding toolkit
   - Underlying AI coding engine

## 🚀 Key Features

- **Web Interface**: Access AI coding assistant through browser (default port 8080)
- **Multi-Agent System**: Automatically delegates complex tasks to specialized sub-agents
- **Persistent Storage**: Workspaces and configuration files saved via Docker volumes
- **Authentication Support**: Configurable username/password or skip authentication
- **OpenRouter Integration**: Access multiple LLM models through OpenRouter API

## 📁 Directory Structure

```
.initial/
  config/         # CodeNomad and OpenCode configuration
    auth/
      auth.json   # OpenRouter API key configuration
  claude/skills/  # Claude skill definitions
.storage/
  workspaces/     # Persistent workspaces
```

## 🔧 Usage

1. Configure OpenRouter API key in `.initial/config/auth/auth.json`
2. Set environment variables (username, password, port, etc.)
3. Run `docker-compose up -d` to start the service
4. Access `http://localhost:28080` to use the AI coding assistant

## 💡 Use Cases

- Developers needing quick AI coding assistant deployment
- Teams wanting multi-agent collaboration capabilities
- Organizations requiring self-hosted AI coding environments
- Users wanting to access multiple LLMs through OpenRouter

**Summary**: A **ready-to-use AI coding assistant deployment solution** with advanced multi-agent orchestration capabilities, deployable with one command via docker compose.