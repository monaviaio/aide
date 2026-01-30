FROM node:20-slim

# 设置工作目录
WORKDIR /workspaces

# 一次性安装所有系统依赖（镜像构建时执行，不会每次启动都执行）
RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    python3-full \
    procps \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*


# 安装 CodeNomad 和 OpenCode
RUN npm install -g @neuralnomads/codenomad@latest opencode-ai@latest

# 安装包管理工具（按优先级顺序：bun > pnpm > yarn）
# 1. 安装 Bun（最高优先级）
RUN curl -fsSL https://bun.sh/install | bash && \
    ln -s /root/.bun/bin/bun /usr/local/bin/bun

# 2. 安装 pnpm（第二优先级）
RUN npm install -g pnpm

RUN bun add -g oh-my-opencode-slim@latest

# 设置环境变量
ENV CODENOMAD_WORK_DIR=/workspaces
ENV PATH="/root/.bun/bin:${PATH}"

# 暴露端口
EXPOSE 8080

# 启动命令
ENTRYPOINT ["codenomad"]
CMD ["--host", "0.0.0.0", "--port", "8080", "--workspace-root", "/workspaces"]
