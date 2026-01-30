# Free Tier Limits and Quotas

Complete breakdown of free tier limitations and quotas for all major deployment platforms.

## Cloudflare Pages

### Limits
- **Builds**: 500 builds/month
- **Bandwidth**: Unlimited
- **Requests**: Unlimited
- **Build minutes**: Included in builds (no separate limit)
- **Sites**: Unlimited
- **Concurrent builds**: 1
- **File size**: 25 MB per file
- **Total site size**: 20,000 files

### Features Included
- ✅ Custom domains (100 per project)
- ✅ Automatic SSL certificates
- ✅ Preview deployments
- ✅ Cloudflare CDN
- ✅ Pages Functions (500k requests/month)
- ✅ Workers KV (100k reads, 1k writes/day)
- ✅ D1 Database (5 GB storage, 5M rows read/day)
- ✅ R2 Storage (10 GB storage, 1M Class A operations/month)

### Restrictions
- ❌ Build time limit: 20 minutes
- ❌ Function execution: 30 seconds max
- ❌ No team collaboration (Business plan needed)

### Best For
- Static sites with unlimited traffic
- Projects needing edge computing
- International audiences (global CDN)

---

## Vercel

### Limits
- **Bandwidth**: 100 GB/month
- **Build execution**: 6,000 minutes/month
- **Serverless function invocations**: 100 GB-hours/month
- **Edge middleware invocations**: 1 million/month
- **Image optimization**: 1,000 source images
- **Concurrent builds**: 1

### Features Included
- ✅ Unlimited sites/projects
- ✅ Custom domains (50 per project)
- ✅ Automatic SSL
- ✅ Preview deployments (100 per deployment)
- ✅ Analytics (500k events/month)
- ✅ Speed Insights (Unlimited)

### Restrictions
- ❌ Function timeout: 10 seconds
- ❌ Function size: 50 MB
- ❌ Environment variables: 100 per project
- ❌ Team seats: Individual account only
- ❌ Deployment protection: Not available

### Best For
- Next.js applications
- Personal projects with moderate traffic
- Rapid prototyping

---

## Netlify

### Limits
- **Bandwidth**: 100 GB/month
- **Build minutes**: 300 minutes/month
- **Concurrent builds**: 1
- **Sites**: Unlimited (500 max)
- **Form submissions**: 100/month
- **Serverless functions**: 125k requests/month
- **Background functions**: Not available

### Features Included
- ✅ Custom domains (unlimited)
- ✅ Automatic SSL
- ✅ Deploy previews
- ✅ Forms
- ✅ Edge Functions (3M requests/month)
- ✅ Netlify Analytics (Not included - $9/month)

### Restrictions
- ❌ Function timeout: 10 seconds (background: 26s on paid)
- ❌ Function size: 50 MB
- ❌ Build time: 15 minutes max
- ❌ Team members: 1
- ❌ Log retention: 1 day

### Best For
- JAMstack sites
- Projects with forms
- Gatsby/Hugo sites

---

## Railway

### Limits
- **Credit**: $5/month
- **Usage**:
  - vCPU: ~$0.000463/min (100 hours ≈ $2.78)
  - RAM: ~$0.000231/GB/min (1GB for 100 hours ≈ $1.39)
  - Disk: $0.25/GB/month
- **No hard bandwidth limit** (but costs apply)

### Features Included
- ✅ PostgreSQL, MySQL, MongoDB, Redis
- ✅ Automatic SSL
- ✅ Custom domains
- ✅ Environment variables (unlimited)
- ✅ Private networking
- ✅ Metrics and logs

### Restrictions
- ❌ Credit expires monthly (doesn't roll over)
- ❌ Services scale down when credit exhausted
- ❌ 1 concurrent deploy

### Best For
- Full-stack apps with databases
- Backend APIs
- Projects under $5/month usage

---

## Render

### Free Tier (Web Services)
- **Hours**: 750 hours/month per service
- **Instances**: Unlimited free services
- **RAM**: 512 MB per instance
- **Auto-sleep**: After 15 minutes of inactivity
- **Cold start**: Can take 30-60 seconds

### Free Tier (Databases)
- **PostgreSQL**: 90 days free, then $7/month
- **Redis**: Not available on free tier

### Static Sites (Free Forever)
- **Bandwidth**: 100 GB/month
- **Sites**: Unlimited
- **Custom domains**: Unlimited

### Features Included
- ✅ Automatic SSL
- ✅ Deploy previews (paid plans)
- ✅ Custom domains
- ✅ Private services

### Restrictions
- ❌ Services sleep after 15 min inactivity
- ❌ Slower build machines
- ❌ Limited to 1 region
- ❌ No persistent disk on free tier

### Best For
- Hobby projects (with sleep acceptable)
- Static sites
- Testing/development

---

## Fly.io

### Free Tier
- **Compute**: 3 shared-cpu-1x VMs (256 MB RAM each)
- **Volumes**: 3 GB persistent storage (across all volumes)
- **Bandwidth**: 160 GB outbound/month
- **IPv4**: 1 free (additional $2/month each)

### Features Included
- ✅ Anycast routing
- ✅ Automatic SSL
- ✅ Global deployment
- ✅ Private networking
- ✅ Metrics

### Restrictions
- ❌ Shared CPU (not dedicated)
- ❌ 256 MB RAM per VM
- ❌ Limited IPv4 addresses
- ❌ No object storage on free tier

### Best For
- Docker containers
- Global edge applications
- Low-latency requirements

---

## Database Services (Free Tiers)

### Supabase
- **Database**: 500 MB PostgreSQL
- **Storage**: 1 GB files
- **Bandwidth**: 5 GB
- **Auth**: 50,000 monthly active users
- **API requests**: Unlimited
- **Projects**: Pause after 7 days inactivity

### Neon
- **Storage**: 3 GB
- **Compute**: 1 vCPU
- **Active time**: 100 hours/month
- **Branches**: 10
- **Databases**: Unlimited
- **Auto-suspend**: After 5 minutes inactivity

### PlanetScale (Hobby - Recently Updated)
- **Storage**: 5 GB
- **Row reads**: 1 billion/month
- **Row writes**: 10 million/month
- **Databases**: 1
- **Branches**: 1 production + 1 development

### MongoDB Atlas
- **Storage**: 512 MB
- **RAM**: Shared
- **Connections**: 500 max
- **Backups**: Not included
- **Clusters**: 1 M0 cluster per project

### Turso (LibSQL)
- **Databases**: 500
- **Rows read**: 9 billion/month
- **Rows written**: 500k/month
- **Storage**: 9 GB total
- **Locations**: 3

---

## Comparison Table

| Platform | Best For | Monthly Bandwidth | Build Minutes | Database | Serverless |
|----------|----------|-------------------|---------------|----------|------------|
| **Cloudflare Pages** | Static + Edge | Unlimited | 500 builds | KV, D1, R2 | Yes (500k) |
| **Vercel** | Next.js | 100 GB | 6000 min | External | Yes (100 GB-h) |
| **Netlify** | JAMstack | 100 GB | 300 min | External | Yes (125k) |
| **Railway** | Full-stack | Usage-based ($5) | Usage-based | Yes (Postgres, MySQL, Redis) | No |
| **Render** | General | 100 GB (static) | Unlimited | Postgres (90 days) | Limited |
| **Fly.io** | Docker/Global | 160 GB | Unlimited | External | No |

---

## Recommended Combinations

### Free Static Site
- **Frontend**: Cloudflare Pages (unlimited bandwidth)
- **Database**: Supabase (500 MB)
- **Storage**: Cloudflare R2 (10 GB)
- **Cost**: $0/month

### Free Full-Stack
- **App**: Railway ($5 credit)
- **Database**: Railway Postgres (included)
- **Cost**: $0/month if usage under $5

### Free with Scale
- **Frontend**: Cloudflare Pages
- **API**: Vercel Serverless (100 GB-hours)
- **Database**: Neon (3 GB)
- **Cost**: $0/month

### Budget Full-Stack ($5/month)
- **Everything**: Railway ($5 credit)
  - Web service
  - PostgreSQL
  - Redis
  - Worker service
- **Backup DB**: Neon (free backup)

---

## Tips to Stay Within Free Limits

### Reduce Bandwidth
1. **Optimize images**:
   - Use WebP/AVIF formats
   - Proper sizing (don't serve 4K images for thumbnails)
   - Lazy loading
   
2. **Enable compression**:
   - Gzip/Brotli (usually automatic)
   - Minify JS/CSS
   
3. **Use CDN caching**:
   - Set proper Cache-Control headers
   - Use immutable for versioned assets

### Reduce Build Minutes
1. **Cache dependencies**:
   - Most platforms cache `node_modules` automatically
   - Use `npm ci` instead of `npm install`
   
2. **Optimize build**:
   - Skip unnecessary steps in preview builds
   - Use incremental builds (Next.js, etc.)
   
3. **Limit builds**:
   - Don't trigger build on every commit
   - Use branch deployments wisely

### Reduce Database Usage
1. **Optimize queries**:
   - Use indexes
   - Limit result sets
   - Use connection pooling
   
2. **Clean up data**:
   - Archive old data
   - Remove unused tables
   
3. **Use caching**:
   - Redis for hot data
   - In-memory caching

### Reduce Serverless Costs
1. **Optimize functions**:
   - Reduce cold starts
   - Minimize dependencies
   - Keep functions small and focused
   
2. **Use caching**:
   - Cache API responses
   - Use CDN for static responses
   
3. **Batch operations**:
   - Combine multiple requests
   - Use webhooks instead of polling

---

## Monitoring Usage

### Cloudflare
- Dashboard → Analytics
- Check builds used
- Monitor function invocations

### Vercel
- Dashboard → Usage
- Real-time bandwidth graph
- Build minutes breakdown

### Netlify
- Team Settings → Billing
- Current month usage
- Alerts available

### Railway
- Project → Usage
- Real-time credit burn
- Set up usage alerts

### Render
- Dashboard → Account
- Service metrics
- No alerts on free tier

## When to Upgrade

### You've Outgrown Free Tier If:

1. **Traffic exceeded**:
   - Consistently hitting bandwidth limits
   - Need more than 100 GB/month
   - → Upgrade Vercel ($20) or stay on Cloudflare

2. **Build time insufficient**:
   - Using all 300-6000 minutes
   - Need faster builds
   - → Upgrade Netlify ($19) or Vercel ($20)

3. **Database too small**:
   - Need more than 500 MB - 3 GB
   - Need better performance
   - → Railway ($5+), Supabase ($25), or Neon ($19)

4. **Need team features**:
   - Collaboration required
   - RBAC needed
   - → Upgrade to team plans ($20-50/month)

5. **Serverless limits hit**:
   - Need longer timeouts (>10s)
   - More invocations
   - → Vercel Pro or Netlify Pro
