# Platform Configuration Reference

Detailed configuration file templates and examples for all supported deployment platforms.

## Vercel

### vercel.json

Basic configuration:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install",
  "framework": "vite"
}
```

With custom headers and redirects:

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ],
  "redirects": [
    {
      "source": "/old-page",
      "destination": "/new-page",
      "permanent": true
    }
  ],
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://api.example.com/:path*"
    }
  ]
}
```

SPA routing configuration:

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/" }
  ]
}
```

## Netlify

### netlify.toml

Basic static site:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

With custom headers:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/static/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

With environment variables (build-time):

```toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "18"
  NPM_VERSION = "9"
```

With redirects and rewrites:

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

With Netlify Functions:

```toml
[build]
  command = "npm run build"
  publish = "dist"
  functions = "netlify/functions"

[functions]
  node_bundler = "esbuild"
```

## Cloudflare Pages

### wrangler.toml

Cloudflare Pages typically doesn't require configuration (settings in dashboard), but for advanced features:

```toml
name = "my-project"
compatibility_date = "2024-01-01"

[site]
bucket = "./dist"

[[rules]]
type = "Text"
globs = ["**/*.html"]
fallthrough = false
```

For Pages Functions:

```toml
name = "my-pages-project"
compatibility_date = "2024-01-01"

[env.production]
vars = { ENVIRONMENT = "production" }
kv_namespaces = [
  { binding = "MY_KV", id = "your-kv-id" }
]

[[env.production.d1_databases]]
binding = "DB"
database_name = "production-db"
database_id = "your-db-id"
```

### _headers (alternative to wrangler.toml)

```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/static/*
  Cache-Control: public, max-age=31536000, immutable
```

### _redirects (alternative for redirects)

```
/old-path  /new-path  301
/api/*  https://api.example.com/:splat  200
/*  /index.html  200
```

## Railway

### railway.toml

Basic Node.js app:

```toml
[build]
builder = "NIXPACKS"
buildCommand = "npm install && npm run build"

[deploy]
startCommand = "npm start"
restartPolicyType = "on-failure"
restartPolicyMaxRetries = 10
```

With custom Nixpacks:

```toml
[build]
builder = "NIXPACKS"

[build.nixpacksPlan]
providers = ["node"]

[deploy]
startCommand = "node dist/index.js"
healthcheckPath = "/health"
healthcheckTimeout = 30
```

With multiple services:

```toml
[[services]]
name = "web"
startCommand = "npm run start:web"

[[services]]
name = "worker"
startCommand = "npm run start:worker"
```

### nixpacks.toml (advanced Nixpacks configuration)

```toml
[phases.setup]
nixPkgs = ["nodejs-18_x", "python3"]

[phases.install]
cmds = ["npm ci"]

[phases.build]
cmds = ["npm run build"]

[start]
cmd = "npm start"
```

## Render

### render.yaml

Web service:

```yaml
services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production
      - key: DATABASE_URL
        fromDatabase:
          name: postgres-db
          property: connectionString
```

With database:

```yaml
services:
  - type: web
    name: api
    env: node
    buildCommand: npm ci && npm run build
    startCommand: npm start
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: my-db
          property: connectionString

databases:
  - name: my-db
    databaseName: myapp
    user: myapp
```

Background worker:

```yaml
services:
  - type: worker
    name: queue-worker
    env: node
    buildCommand: npm install
    startCommand: npm run worker
    envVars:
      - key: REDIS_URL
        fromService:
          type: redis
          name: my-redis
          property: connectionString

  - type: redis
    name: my-redis
    ipAllowList: []
```

Cron job:

```yaml
services:
  - type: cron
    name: daily-job
    env: node
    buildCommand: npm install
    startCommand: npm run job
    schedule: "0 2 * * *"  # Daily at 2 AM
```

## Fly.io

### fly.toml

Basic Node.js app:

```toml
app = "my-app"
primary_region = "sjc"

[build]
  builder = "heroku/buildpacks:20"

[env]
  PORT = "8080"
  NODE_ENV = "production"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[services]]
  protocol = "tcp"
  internal_port = 8080

  [[services.ports]]
    port = 80
    handlers = ["http"]

  [[services.ports]]
    port = 443
    handlers = ["tls", "http"]

  [[services.http_checks]]
    interval = 10000
    timeout = 2000
    grace_period = "5s"
    method = "get"
    path = "/health"
```

With Dockerfile:

```toml
app = "my-app"
primary_region = "sjc"

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "8080"

[[services]]
  internal_port = 8080
  protocol = "tcp"

  [[services.ports]]
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443
```

Multi-region with replicas:

```toml
app = "global-app"
primary_region = "sjc"

[http_service]
  internal_port = 8080
  force_https = true

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256

[deploy]
  strategy = "rolling"

[[regions]]
  region = "sjc"  # San Jose
  count = 2

[[regions]]
  region = "iad"  # Virginia
  count = 2

[[regions]]
  region = "ams"  # Amsterdam
  count = 1
```

## Environment Variables

### Format by Platform

**Vercel** (in dashboard or CLI):
```bash
vercel env add VARIABLE_NAME
```

**Netlify** (in netlify.toml or dashboard):
```toml
[context.production.environment]
  API_KEY = "production-key"

[context.deploy-preview.environment]
  API_KEY = "preview-key"
```

**Cloudflare Pages** (in dashboard or wrangler.toml):
```toml
[env.production.vars]
API_KEY = "prod-key"
ENVIRONMENT = "production"
```

**Railway** (in dashboard or railway up):
```bash
railway variables set DATABASE_URL=postgresql://...
```

**Render** (in render.yaml):
```yaml
envVars:
  - key: API_KEY
    value: your-api-key
  - key: SECRET_KEY
    sync: false  # Managed in dashboard only
```

### Client-Side Variables

Different frameworks have different naming conventions for client-side variables:

**Next.js**: `NEXT_PUBLIC_*`
```bash
NEXT_PUBLIC_API_URL=https://api.example.com
```

**Vite** (React, Vue, Svelte): `VITE_*`
```bash
VITE_API_ENDPOINT=https://api.example.com
```

**Nuxt**: `NUXT_PUBLIC_*`
```bash
NUXT_PUBLIC_API_BASE=https://api.example.com
```

**Create React App**: `REACT_APP_*`
```bash
REACT_APP_API_URL=https://api.example.com
```

## Node.js Version Specification

### package.json

```json
{
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
```

### .nvmrc (Netlify, Render, some others)

```
18
```

### .node-version (Railway, some others)

```
18.17.0
```

## Build Optimization

### package.json scripts

```json
{
  "scripts": {
    "build": "vite build",
    "build:prod": "NODE_ENV=production vite build --mode production",
    "postbuild": "npm run cleanup",
    "cleanup": "rm -rf node_modules/.cache"
  }
}
```

### .npmrc (for faster builds)

```
# Use npm ci for reproducible builds
package-lock=true

# Cache location
cache=/tmp/npm-cache

# Disable optional dependencies
optional=false

# Production only
production=true
```

### tsconfig.json (TypeScript optimization)

```json
{
  "compilerOptions": {
    "incremental": true,
    "skipLibCheck": true,
    "noEmit": true
  }
}
```
