FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 安装git curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 安装node 方便后续启动 前端应用
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# check node 版本 和 npm版本
RUN node -v && npm -v

# 将当前源代码 copy 到 app 目录
COPY . /app
WORKDIR /app

# 创建uv python包 虚拟环境
ENV VIRTUAL_ENV=/app/.venv
RUN uv venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 安装依赖包
RUN uv pip install . && rm -rf ~/.cache

EXPOSE 8888

# 服务启动
ENTRYPOINT ["python", "server.py"]