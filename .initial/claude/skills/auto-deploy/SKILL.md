---
name: auto-deploy
description: Automated application deployment configuration and setup for modern cloud platforms. Use this skill when users want to (1) Deploy applications to platforms like Cloudflare Pages, Vercel, Netlify, Railway, Render, or Fly.io, (2) Set up CI/CD pipelines and auto-deployment, (3) Configure deployment settings, environment variables, and build commands, (4) Choose the best deployment platform for their project type, (5) Troubleshoot deployment issues, (6) Migrate between deployment platforms, or (7) Optimize deployment configurations for performance and cost.
---

# Auto-Deploy Skill

Streamline application deployment to modern cloud platforms with automated configuration, best practices, and platform-specific optimizations.

## Platform Selection Guide

Match project requirements to the optimal platform based on project type and needs:

**Static Sites & Frontend Frameworks**
- **Cloudflare Pages**: Unlimited bandwidth, global CDN, free tier with no limits. Best for static sites and frontend frameworks.
- **Vercel**: Native Next.js support, automatic preview deployments, excellent DX. Best for React/Next.js projects.
- **Netlify**: JAMstack specialist, built-in forms and serverless functions, extensive plugins.

**Full-Stack Applications**
- **Railway**: PostgreSQL/MySQL/Redis included, $5 monthly credit, simple configuration. Best for full-stack apps with databases.
- **Render**: Docker support, background workers, cron jobs. Best for containerized applications.
- **Fly.io**: Global edge deployment, 3 free VMs, low-latency apps. Best for distributed applications.

**Framework-Specific Recommendations**
- Next.js → Vercel or Cloudflare Pages
- Nuxt/Vue → Netlify or Vercel  
- SvelteKit → Vercel or Cloudflare Pages
- Astro → Cloudflare Pages or Netlify
- Express/Node.js → Railway or Render
- Django/Flask → Render or Fly.io

**Common Stacks**
- Frontend + Supabase → Cloudflare Pages or Vercel
- Full-stack with DB → Railway
- Microservices → Fly.io or Render
- Static site → Cloudflare Pages (free unlimited)

## Core Deployment Workflows

### Initial Setup

1. **Connect Repository**
   - Link GitHub/GitLab account
   - Select repository to deploy
   - Configure branch for auto-deployment (usually `main`)

2. **Configure Build Settings**
   - Detect framework automatically or specify manually
   - Set build command (e.g., `npm run build`)
   - Set output directory (e.g., `dist`, `build`, `.next`)
   - Specify install command if needed (e.g., `npm install`)

3. **Set Environment Variables**
   - Add all required API keys and secrets
   - Use platform-specific variable prefixes:
     - Next.js: `NEXT_PUBLIC_*` for client-side
     - Vite: `VITE_*` for client-side  
     - Nuxt: `NUXT_PUBLIC_*` for client-side
   - Never commit secrets to git

4. **Deploy and Verify**
   - Trigger initial deployment
   - Check build logs for errors
   - Test deployed application
   - Configure custom domain if needed

### Configuration Files

Generate platform-specific configuration files when advanced settings are needed. See `references/platform-configs.md` for detailed templates.

**Cloudflare Pages** - `wrangler.toml` (optional, for advanced features)
**Vercel** - `vercel.json` (for routes, headers, redirects)
**Netlify** - `netlify.toml` (for build settings, plugins)
**Railway** - `railway.toml` or `nixpacks.toml` (for custom builds)
**Render** - `render.yaml` (infrastructure as code)

### Environment Variable Management

Common variable patterns:

```bash
# Database connections
DATABASE_URL=postgresql://user:pass@host:5432/db
POSTGRES_URL=postgresql://...
REDIS_URL=redis://...

# API Services
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJ...
STRIPE_SECRET_KEY=sk_...

# Framework-specific (client-side)
NEXT_PUBLIC_API_URL=https://api.example.com
VITE_API_ENDPOINT=https://api.example.com
NUXT_PUBLIC_API_BASE=https://api.example.com

# General
NODE_ENV=production
```

**Security Best Practices**:
- Use different values for production vs preview environments
- Rotate secrets regularly
- Use platform's secret management (not in code)
- Audit who has access to production secrets

### Build Command Optimization

Common build commands by framework:

```bash
# Next.js
npm run build

# Vite/React/Vue
npm run build

# Nuxt
npm run build

# SvelteKit  
npm run build

# Astro
npm run build

# Custom with caching
npm ci && npm run build
```

**Optimization tips**:
- Use `npm ci` instead of `npm install` for faster, reproducible builds
- Enable build caching on platform (usually automatic)
- Minimize dependencies in production
- Use proper `.gitignore` to exclude unnecessary files

## Deployment Troubleshooting

### Build Failures

**Node.js version mismatch**
```bash
# Specify Node version in package.json
{
  "engines": {
    "node": ">=18.0.0"
  }
}
```

Or use `.nvmrc` or `.node-version` file:
```
18
```

**Missing dependencies**
- Check that all dependencies are in `package.json`, not just `devDependencies`
- For TypeScript projects, ensure `typescript` is in dependencies

**Environment variable errors**
- Verify all required variables are set in platform dashboard
- Check for typos in variable names
- Ensure client-side variables use correct prefix

### Runtime Errors

**API routes not working**
- Verify serverless function configuration
- Check function timeout limits (usually 10s on free tiers)
- Review function logs in platform dashboard

**Static assets 404**
- Verify output directory setting matches build output
- Check asset paths use relative URLs
- Ensure assets are included in build (not in `.gitignore`)

**Database connection issues**
- Verify connection string format
- Check database is accessible from platform
- Ensure SSL/TLS settings are correct

See `references/troubleshooting.md` for comprehensive debugging guide.

## Platform-Specific Features

### Automatic Preview Deployments

All major platforms support preview URLs for pull requests:

- **Vercel**: Automatic preview for every commit in PR
- **Netlify**: Deploy previews with custom subdomain
- **Cloudflare Pages**: Preview deployments for branches
- **Railway**: PR environments with temporary databases
- **Render**: Preview instances (paid plans)

Configure in platform settings or `vercel.json`/`netlify.toml`.

### Custom Domains

**DNS Configuration**:

For apex domain (example.com):
```
A record: @ → Platform IP or use CNAME flattening
```

For subdomain (www.example.com or app.example.com):
```
CNAME record: subdomain → platform-provided domain
```

**SSL Certificates**: Automatic on all platforms (Let's Encrypt)

### Edge Functions & Middleware

**Cloudflare Pages Functions**:
- Create `functions/` directory
- Files automatically become edge functions
- Runs on Cloudflare's global network

**Vercel Edge Functions**:
- Use Next.js middleware or Edge API routes
- Ultra-fast edge runtime

**Netlify Edge Functions**:
- Deno-based edge functions
- Deploy in `netlify/edge-functions/`

## Cost Optimization Strategies

### Free Tier Recommendations

**Best completely free options**:
1. **Cloudflare Pages** - Unlimited bandwidth, 500 builds/month, unlimited sites
2. **Vercel** - 100GB bandwidth, unlimited personal projects
3. **Netlify** - 100GB bandwidth, 300 build minutes

**Best value with databases**:
1. **Railway** - $5/month credit (enough for 1-2 small apps)
2. **Render** - Free tier with limitations (apps sleep after inactivity)

**Database-only free options**:
- Supabase: 500MB PostgreSQL, 5GB storage
- Neon: 3GB PostgreSQL (serverless)
- PlanetScale: 5GB MySQL (free tier limited)
- MongoDB Atlas: 512MB

### Staying Within Free Limits

**Reduce bandwidth usage**:
- Optimize images (use WebP, proper sizing)
- Enable compression
- Use CDN caching headers
- Lazy load resources

**Reduce build minutes**:
- Cache node_modules
- Use incremental builds
- Minimize build frequency (don't deploy every commit)

**Monitor usage**:
- Set up usage alerts in platform dashboard
- Review analytics monthly
- Upgrade only when necessary

## Migration Between Platforms

### Migration Checklist

1. **Export current configuration**
   - Document all environment variables
   - Note custom domain settings
   - Export deployment settings

2. **Prepare target platform**
   - Create new project
   - Set environment variables
   - Configure build settings

3. **Test deployment**
   - Deploy to preview URL first
   - Test all functionality
   - Check performance

4. **Switch traffic**
   - Update DNS records to point to new platform
   - Wait for DNS propagation (up to 48 hours)
   - Monitor for issues

5. **Cleanup**
   - Keep old deployment for rollback (1-2 weeks)
   - Cancel old platform subscription if applicable

### Common Migration Paths

**Heroku → Railway/Render**:
- Export `DATABASE_URL` and other config vars
- Update Procfile if needed
- Railway auto-detects most Heroku projects

**Netlify → Cloudflare Pages**:
- Export `netlify.toml` settings
- Adapt redirects to Cloudflare format
- Rewrite functions if using Netlify Functions

**Vercel → Netlify/Cloudflare**:
- Export `vercel.json` routes
- Adapt serverless functions
- Update environment variables

## Bundled Resources

### Scripts

- `scripts/generate_config.py` - Generate platform-specific configuration files based on project type
- `scripts/check_compatibility.py` - Verify framework/platform compatibility and suggest optimal settings
- `scripts/env_template.py` - Generate .env.example from project dependencies

### References

- `references/platform-configs.md` - Detailed configuration file templates and examples for all platforms
- `references/troubleshooting.md` - Common deployment issues, error messages, and solutions
- `references/free-tier-limits.md` - Complete breakdown of free tier limitations and quotas

### Assets

- `assets/config-templates/` - Ready-to-use configuration files (vercel.json, netlify.toml, etc.)
- `assets/github-actions/` - CI/CD workflow templates for GitHub Actions
- `assets/docker/` - Dockerfile templates for containerized deployments
