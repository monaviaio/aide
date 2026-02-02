<div align="center">

# 🚀 Aide - AI Coding Assistant Deployment

**One-Command Deployment | Multi-Agent Collaboration | Production-Ready**

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange)](https://opencode.ai)

[English](#) | [简体中文](./README_zh.md)

</div>

---

## 📦 Overview

**monaviaio/aide** is a production-ready Docker deployment for AI coding assistants. Deploy a complete AI development environment with **multi-agent collaboration** in one command.

## 🎯 What You Get
- 🌐 **Web-Based IDE**: Access AI coding assistant through browser (port 8080)
- 🤖 **Multi-Agent System**: 6+ specialized AI agents working together
- 💾 **Persistent Workspaces**: All your work saved via Docker volumes
- 🔐 **Secure Authentication**: Configurable username/password protection
- 🎨 **Model Flexibility**: Mix and match any LLM models via OpenRouter
- ⚡ **Pre-Configured**: Optimal agent setups out of the box

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User (Browser)                        │
│                   http://localhost:8080                  │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                     CodeNomad                            │
│              (Web Interface Layer)                       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  oh-my-opencode-slim                     │
│           (Multi-Agent Orchestration Layer)              │
│                                                           │
│  ┌─────────────┐  ┌──────────┐  ┌──────────────┐       │
│  │Orchestrator │  │ Explorer │  │   Oracle     │       │
│  │   (Chief)   │  │(Recon)   │  │  (Advisor)   │       │
│  └─────────────┘  └──────────┘  └──────────────┘       │
│                                                           │
│  ┌─────────────┐  ┌──────────┐  ┌──────────────┐       │
│  │  Librarian  │  │ Designer │  │    Fixer     │       │
│  │ (Research)  │  │  (UI/UX) │  │ (Implement)  │       │
│  └─────────────┘  └──────────┘  └──────────────┘       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  newtype-profile                         │
│            (Configuration Management)                    │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                     OpenCode                             │
│              (AI Coding Engine)                          │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   OpenRouter API                         │
│     (Claude Opus 4.5, Sonnet 4.5, Gemini 3 Pro...)     │
└─────────────────────────────────────────────────────────┘
```

---
## 🚀 Quick Start
### Prerequisites
- **Docker** and **Docker Compose** installed
- **OpenRouter API Key** ([Get one here](https://openrouter.ai/keys))
### Installation

**1. Clone the repository**

```bash
git clone https://github.com/monaviaio/aide.git
cd aide
```

**2. Configure OpenRouter API Key**

Edit `.initial/config/auth/auth.json`:

```json
{
    "openrouter": {
        "type": "api",
        "key": "sk-or-v1-YOUR-API-KEY-HERE"
    }
}
```

**3. Set environment variables**

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Required: Set a secure password
CODENOMAD_PASSWORD=your_secure_password_here

# Optional: Customize these
CODENOMAD_USERNAME=codenomad
CODENOMAD_PORT=8080
CODENOMAD_SKIP_AUTH=false
```

**4. Start the service**

```bash
docker-compose up -d
```

**5. Access the web interface**

Open your browser and navigate to:

```
http://localhost:8080
```

Login with your configured username and password.

**6. Verify agents are working**

In the CodeNomad interface, type:

```
ping all agents
```

You should see responses from all 6 agents.

---

## 🏛️ Core Components

### 1. CodeNomad - Command Center

**What it does:**
- Provides web-based access to AI coding assistants
- Manages workspaces and file operations
- Handles authentication and security

**Key Features:**
- Browser-based IDE experience
- Multi-workspace support
- Persistent storage via Docker volumes

**Project:** [NeuralNomadsAI/CodeNomad](https://github.com/NeuralNomadsAI)

---

### 2. oh-my-opencode-slim - The Pantheon

**What it does:**
- Transforms your AI assistant from a single executor into a team manager
- Automatically delegates complex tasks to specialized agents
- Optimizes token usage through intelligent routing

**The 6 Agents:**
<table>
  <tr>
    <th>Agent</th>
    <th>Role</th>
    <th>When to Use</th>
    <th>Default Model</th>
  </tr>
  <tr>
    <td><b>Orchestrator</b></td>
    <td>Master delegator and strategic coordinator</td>
    <td>Complex multi-step tasks, architecture decisions</td>
    <td>Claude Sonnet 4.5</td>
  </tr>
  <tr>
    <td><b>Explorer</b></td>
    <td>Codebase reconnaissance specialist</td>
    <td>Understanding unfamiliar codebases, finding patterns</td>
    <td>Gemini 3 Flash</td>
  </tr>
  <tr>
    <td><b>Oracle</b></td>
    <td>Strategic advisor and debugger of last resort</td>
    <td>Critical bugs, architectural reviews, deep analysis</td>
    <td>Claude Opus 4.5</td>
  </tr>
  <tr>
    <td><b>Librarian</b></td>
    <td>External knowledge retrieval</td>
    <td>Research APIs, frameworks, best practices</td>
    <td>Gemini 3 Flash</td>
  </tr>
  <tr>
    <td><b>Designer</b></td>
    <td>UI/UX implementation and visual excellence</td>
    <td>Frontend work, styling, user interfaces</td>
    <td>Gemini 3 Flash</td>
  </tr>
  <tr>
    <td><b>Fixer</b></td>
    <td>Fast implementation specialist</td>
    <td>Quick fixes, straightforward implementations</td>
    <td>Claude Opus 4.5</td>
  </tr>
</table>

**Key Features:**
- 🎯 Automatic Task Delegation: Orchestrator routes tasks to the right specialist
- 💰 Cost Optimization: Use expensive models only when needed
- ⚡ Parallel Execution: Multiple agents can work simultaneously
- 🎨 Customizable Presets: Pre-configured optimal setups
- 🔧 Model Flexibility: Assign any model to any agent

**Configuration Presets:**

This deployment includes two presets:
1. strongest-coding-2026-optimized (Default)
   - Uses Claude Opus 4.5 for critical thinking (Oracle, Fixer)
   - Uses Gemini 3 Pro for fast operations (Explorer, Librarian, Designer)
   - Balanced for cost and performance
2. **zen-free**
   - Uses only free-tier models
   - Great for learning and experimentation

**Project:** [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)

---

### 3. newtype-profile - Configuration Management

**What it does:**
- Manages user preferences and agent configurations
- Provides content creation workflows (adapted from oh-my-opencode)
- Includes additional agents for content work (researcher, writer, editor, fact-checker)

**Additional Agents:**
| Agent | Role | Use Case |
|-------|------|----------|
| Researcher | Intelligence gathering | Web research, trend analysis |
| Writer | Content creation | Documentation, articles, copy |
| Editor | Content refinement | Polish, structure, clarity |
| Fact-Checker | Verification | Source validation, accuracy checks |
| Archivist | Knowledge base | Internal documentation retrieval |
| Extractor | Format processing | PDF/image content extraction |

**Key Features:**
- 🎭 Dual-Mode Chief: Thought partner + execution coordinator
- 📚 Memory System: Cross-session knowledge persistence
- 🔄 Auto-Configuration: Smart setup on first run
- 🎨 Built-in Skills: Super-analyst, super-writer, playwright

**Project:** [newtype-01/newtype-profile](https://github.com/newtype-01/newtype-profile)

---

### 4. OpenCode - The Engine

**What it does:**
- Core AI coding engine
- Tool integration layer
- MCP (Model Context Protocol) support

**Project:** [OpenCode.ai](https://opencode.ai)

---

## ⚙️ Configuration Guide

### Directory Structure

```
aide/
├── .initial/                    # Initial configuration (copied to container)
│   ├── config/
│   │   ├── auth/
│   │   │   └── auth.json       # OpenRouter API key
│   │   ├── codenomad/          # CodeNomad settings
│   │   └── opencode/
│   │       ├── opencode.json   # Model configurations
│   │       └── oh-my-opencode-slim.json  # Agent presets
│   └── claude/
│       └── skills/             # Custom skills
├── .storage/
│   └── workspaces/             # Persistent workspaces (mounted)
├── docker-compose.yml          # Service definition
├── Dockerfile                  # Container image
├── .env                        # Environment variables
└── README.md
```

### Environment Variables

Edit `.env` to customize:
| Variable | Default | Description |
|----------|---------|-------------|
| CODENOMAD_PASSWORD | required | Password for web access |
| CODENOMAD_USERNAME | codenomad | Username for web access |
| CODENOMAD_PORT | 8080 | External port mapping |
| CODENOMAD_SKIP_AUTH | false | Skip authentication (use only behind VPN/proxy) |

### Model Configuration

**Available Models (via OpenRouter):**

Edit `.initial/config/opencode/opencode.json` to add or modify models:

```json
{
  "provider": {
    "openrouter": {
      "models": {
        "anthropic/claude-sonnet-4.5": {
          "name": "Claude Sonnet 4.5",
          "attachment": true,
          "limit": {
            "context": 200000,
            "output": 32000
          }
        },
        "google/gemini-3-pro-preview": {
          "name": "Gemini 3 Pro Preview",
          "thinking": true,
          "attachment": true,
          "limit": {
            "context": 1048576,
            "output": 65535
          }
        }
      }
    }
  }
}
```

### Agent Configuration

**Customize Agent Models:**

Edit `.initial/config/opencode/oh-my-opencode-slim.json`:

```json
{
  "preset": "strongest-coding-2026-optimized",
  "presets": {
    "strongest-coding-2026-optimized": {
      "orchestrator": {
        "model": "openrouter/anthropic/claude-sonnet-4.5",
        "temperature": 0.7,
        "variant": "high"
      },
      "oracle": {
        "model": "openrouter/anthropic/claude-opus-4.5",
        "temperature": 0.3,
        "variant": "high"
      }
      // ... other agents
    }
  }
}
```

**Create Custom Presets:**

Add your own preset configuration:

```json
{
  "preset": "my-custom-preset",
  "presets": {
    "my-custom-preset": {
      "orchestrator": {
        "model": "openrouter/anthropic/claude-sonnet-4.5",
        "skills": ["*"],
        "mcps": ["websearch"]
      }
      // ... configure other agents
    }
  }
}
```

---

## 💡 Usage Examples

### Basic Workflow

**1. Start a coding session**

```
I need to build a REST API for user authentication
```

**2. Orchestrator analyzes and delegates**
   - Calls Librarian to research best practices
   - Calls Fixer to implement the code
   - Calls Oracle to review security

**3. Review and iterate**

```
Can you add rate limiting to the login endpoint?
```

### Advanced Usage

**Parallel Research:**

```
Research these three topics simultaneously:
1. JWT vs session-based auth
2. Rate limiting strategies
3. Password hashing best practices
```

**UI/UX Work:**

```
Design a modern login page with dark mode support
```
→ Automatically routed to Designer agent

**Deep Debugging:**

```
This authentication bug only happens in production. Help me debug it.
```
→ Escalated to Oracle for deep analysis

---

## 🔧 Advanced Configuration

### Custom Skills

Add custom skills to `.initial/claude/skills/`:

```
.initial/claude/skills/
└── my-custom-skill/
    ├── SKILL.md          # Skill definition
    └── README.md         # Documentation
```

Skills are automatically loaded on container start.

### Tmux Integration

Enable real-time agent monitoring:

Edit `.initial/config/opencode/oh-my-opencode-slim.json`:

```json
{
  "tmux": {
    "enabled": true,
    "layout": "main-vertical",
    "main_pane_size": 60
  }
}
```

See [oh-my-opencode-slim tmux docs](https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/docs/tmux-integration.md) for details.

### MCP Server Configuration

Enable additional capabilities via MCP servers:

```json
{
  "mcp": {
    "tavily": {
      "api_key": "tvly-your-api-key"
    },
    "firecrawl": {
      "api_key": "fc-your-api-key"
    }
  }
}
```

**Available MCP servers:**
- websearch (Exa) - Built-in web search
- sequential-thinking - Structured problem-solving
- tavily - Advanced web search and crawling
- firecrawl - Web scraping
- filesystem - Local file access

---

## 🐛 Troubleshooting

### Port Already in Use

**Error:** `Bind for 0.0.0.0:8080 failed: port is already allocated`

**Solution:** Change the port in `.env`:

```env
CODENOMAD_PORT=28080
```

Then restart:

```bash
docker-compose down
docker-compose up -d
```

### Authentication Failed

**Error:** Cannot login with username/password

**Solution:**
1. Check `.env` has correct `CODENOMAD_PASSWORD`
2. Restart the container:
   ```bash
   docker-compose restart
   ```

### Agent Not Responding

**Error:** Agent doesn't respond or times out

**Solution:**
1. Check OpenRouter API key in `.initial/config/auth/auth.json`
2. Verify API key has credits: https://openrouter.ai/credits
3. Check logs:
   ```bash
   docker-compose logs -f codenomad
   ```

### Model API Errors

**Error:** Model not found or Insufficient credits

**Solution:**
1. Verify model name in configuration matches OpenRouter models
2. Check OpenRouter credits
3. Switch to a different model in agent configuration

### Container Won't Start

**Error:** Container exits immediately

**Solution:**
1. Check logs:
   ```bash
   docker-compose logs codenomad
   ```
2. Verify all required files exist:
   - `.initial/config/auth/auth.json`
   - `.env`
3. Rebuild the image:
   ```bash
   docker-compose build --no-cache
   docker-compose up -d
   ```

---

## 📚 Use Cases

### For Individual Developers
- Rapid Prototyping: Orchestrator + Fixer for quick implementations
- Learning: Explorer helps understand unfamiliar codebases
- Code Review: Oracle provides expert-level feedback

### For Teams
- Onboarding: New developers use Explorer to understand the codebase
- Architecture Decisions: Oracle provides strategic guidance
- Documentation: Writer + Editor create and maintain docs

### For Organizations
- Self-Hosted: Full control over data and infrastructure
- Cost Control: Optimize model usage per task type
- Customization: Tailor agents to your tech stack

### For Content Creators
- Research: Researcher + Librarian gather information
- Writing: Writer drafts, Editor polishes
- Fact-Checking: Fact-checker validates sources

---

## 🔄 Updating

### Update Docker Image

```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose build --no-cache
docker-compose up -d
```

### Update Plugins

Plugins are installed during image build. To update:

```bash
# Edit Dockerfile to specify version
# RUN bun add -g oh-my-opencode-slim@1.2.3

# Rebuild
docker-compose build --no-cache
docker-compose up -d
```

---

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

For bugs or feature requests, please [open an issue](https://github.com/monaviaio/aide/issues).

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

This project integrates and builds upon:

- [CodeNomad](https://github.com/NeuralNomadsAI) - Web interface for AI coding
- [oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) - Multi-agent orchestration
- [newtype-profile](https://github.com/newtype-01/newtype-profile) - Configuration management
- [OpenCode](https://opencode.ai) - AI coding platform
- [OpenRouter](https://openrouter.ai) - Unified LLM API

Special thanks to the open-source community for making this possible.

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/monaviaio/aide/issues)
- **Discussions:** [GitHub Discussions](https://github.com/monaviaio/aide/discussions)
- **Documentation:** [Wiki](https://github.com/monaviaio/aide/wiki)

---

<div align="center">

Built with ❤️ by the Monavia team

[⭐ Star this repo](https://github.com/monaviaio/aide) if you find it useful!

</div>