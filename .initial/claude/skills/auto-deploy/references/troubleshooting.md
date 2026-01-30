# Deployment Troubleshooting Guide

Common deployment issues, error messages, and their solutions.

## Build Failures

### Node.js Version Mismatch

**Error:**
```
error: The engine "node" is incompatible with this module
```

**Solution:**
Specify Node version in `package.json`:
```json
{
  "engines": {
    "node": ">=18.0.0"
  }
}
```

Or create `.nvmrc`:
```
18
```

### Missing Dependencies

**Error:**
```
Module not found: Can't resolve 'package-name'
```

**Solutions:**
1. Check if dependency is in `dependencies` (not `devDependencies`):
```bash
npm install --save package-name
```

2. For TypeScript projects, ensure `typescript` is installed:
```bash
npm install --save-dev typescript @types/node
```

3. Clear cache and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Build Command Failed

**Error:**
```
npm ERR! Missing script: "build"
```

**Solution:**
Add build script to `package.json`:
```json
{
  "scripts": {
    "build": "vite build"  // or appropriate build command
  }
}
```

### Out of Memory

**Error:**
```
FATAL ERROR: Ineffective mark-compacts near heap limit
```

**Solution:**
Increase Node memory limit in build command:
```json
{
  "scripts": {
    "build": "NODE_OPTIONS='--max-old-space-size=4096' vite build"
  }
}
```

Or configure in platform settings:
- **Vercel**: Automatic scaling
- **Netlify**: Contact support for upgrade
- **Railway**: Increase memory in service settings

### TypeScript Errors

**Error:**
```
error TS2307: Cannot find module 'X' or its corresponding type declarations
```

**Solutions:**
1. Install type definitions:
```bash
npm install --save-dev @types/package-name
```

2. Add to `tsconfig.json`:
```json
{
  "compilerOptions": {
    "skipLibCheck": true
  }
}
```

### Environment Variable Not Found

**Error:**
```
ReferenceError: process is not defined
```

**Solution:**
Use framework-specific prefixes for client-side variables:

Next.js:
```javascript
// Use NEXT_PUBLIC_ prefix
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
```

Vite:
```javascript
// Use VITE_ prefix  
const apiUrl = import.meta.env.VITE_API_URL;
```

## Runtime Errors

### 404 on Page Refresh (SPA)

**Problem:**
Routes work on initial load but return 404 on refresh.

**Solution:**

**Vercel** (`vercel.json`):
```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/" }
  ]
}
```

**Netlify** (`netlify.toml`):
```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

**Cloudflare Pages** (`_redirects`):
```
/*  /index.html  200
```

### API Routes Not Working

**Error:**
```
404: API route not found
```

**Solutions:**

For **Vercel** (Next.js):
- API routes must be in `pages/api/` or `app/api/`
- Check file naming: `pages/api/hello.js` → `/api/hello`

For **Netlify**:
- Serverless functions in `netlify/functions/`
- File must export handler:
```javascript
exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Hello" })
  };
};
```

For **Cloudflare Pages**:
- Functions in `functions/` directory
- Use `export async function onRequest(context)`:
```javascript
export async function onRequest(context) {
  return new Response("Hello");
}
```

### Function Timeout

**Error:**
```
Task timed out after 10.00 seconds
```

**Solutions:**

1. Optimize function code (reduce processing time)
2. Use background jobs for long-running tasks
3. Upgrade to paid plan for longer timeouts:
   - Vercel: 10s free, 60s+ paid
   - Netlify: 10s free, 26s+ paid
   - Cloudflare: No timeout (but CPU limit)

### CORS Errors

**Error:**
```
Access to fetch at 'X' from origin 'Y' has been blocked by CORS policy
```

**Solution:**

Add CORS headers in configuration:

**Vercel** (`vercel.json`):
```json
{
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        { "key": "Access-Control-Allow-Methods", "value": "GET,POST,OPTIONS" }
      ]
    }
  ]
}
```

**Netlify** (`netlify.toml`):
```toml
[[headers]]
  for = "/api/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
    Access-Control-Allow-Methods = "GET, POST, OPTIONS"
```

Or in serverless function:
```javascript
return {
  statusCode: 200,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type'
  },
  body: JSON.stringify(data)
};
```

### Static Assets 404

**Error:**
```
GET /static/css/main.css 404
```

**Solutions:**

1. Check `outputDirectory` matches actual build output:
   - Vite: `dist`
   - Create React App: `build`
   - Next.js: `.next` (but auto-detected)

2. Use relative paths or public URL:
```javascript
// Wrong
<img src="/assets/logo.png" />

// Right (for Vite)
<img src={new URL('./assets/logo.png', import.meta.url).href} />

// Or use public directory
// public/logo.png → /logo.png
<img src="/logo.png" />
```

3. Check `.gitignore` doesn't exclude assets:
```gitignore
# Wrong - excludes all dist content
dist/

# Right - dist itself but not during build
/dist
```

## Database Connection Issues

### Connection Refused

**Error:**
```
Error: connect ECONNREFUSED
```

**Solutions:**

1. Verify `DATABASE_URL` format:
```bash
# PostgreSQL
postgresql://user:password@host:5432/database

# MySQL
mysql://user:password@host:3306/database
```

2. Check database is accessible from platform:
   - Railway: Use internal URL if same project
   - Render: Use internal connection string
   - External DB: Allow platform IPs in firewall

3. Enable SSL if required:
```javascript
// Prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
  // Add this
  ssl      = true
}

// Sequelize
new Sequelize(process.env.DATABASE_URL, {
  dialectOptions: {
    ssl: {
      require: true,
      rejectUnauthorized: false
    }
  }
});
```

### Too Many Connections

**Error:**
```
Error: too many connections for role
```

**Solutions:**

1. Use connection pooling:
```javascript
// Prisma
datasource db {
  url = env("DATABASE_URL")
  connection_limit = 5
}

// Or use connection pool URL
DATABASE_URL="postgresql://user:pass@host:5432/db?connection_limit=5"
```

2. Use external connection pooler:
   - Supabase: Use pooler connection string
   - PlanetScale: Built-in pooling
   - External: PgBouncer, Supavisor

### Migration Failures

**Error:**
```
Migration failed: relation already exists
```

**Solutions:**

1. Reset database (dev only):
```bash
npx prisma migrate reset
```

2. Generate migration without applying:
```bash
npx prisma migrate dev --create-only
```

3. For production, use:
```bash
npx prisma migrate deploy
```

## Platform-Specific Issues

### Vercel

**Preview Deployment Taking Forever**
- Check if function is in infinite loop
- Review function logs in dashboard
- Set timeout in `vercel.json`:
```json
{
  "functions": {
    "api/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

**Edge Runtime Incompatibility**
- Some Node.js APIs unavailable in Edge runtime
- Check compatibility: https://edge-runtime.vercel.app
- Use Node.js runtime instead:
```javascript
export const config = {
  runtime: 'nodejs'
};
```

### Netlify

**Build Plugins Not Running**
- Verify plugin configuration in `netlify.toml`:
```toml
[[plugins]]
  package = "@netlify/plugin-nextjs"
```

**Deploy Preview Not Updating**
- Clear deploy cache in Netlify UI
- Force rebuild: `netlify build --clear-cache`

### Cloudflare Pages

**Functions Not Deploying**
- Ensure functions are in `functions/` directory
- Check file naming (underscores create routes)
- Verify no syntax errors in functions

**KV Binding Not Working**
- Bind KV namespace in dashboard
- Access via `context.env.MY_KV` not `process.env`

### Railway

**Service Not Starting**
- Check `startCommand` in `railway.toml`
- Verify port binding:
```javascript
const PORT = process.env.PORT || 3000;
app.listen(PORT);
```

**Out of Credit**
- Monitor usage in dashboard
- Upgrade plan or optimize resources
- Use sleep schedule for non-production

### Render

**Service Sleeping**
- Free tier services sleep after 15 min inactivity
- Upgrade to prevent sleep
- Or use external ping service (cron-job.org)

**Build Stuck**
- Check for infinite loops in build script
- Verify dependencies aren't too large
- Contact support if persistent

## Performance Issues

### Slow Initial Load

**Solutions:**

1. Enable code splitting:
```javascript
// React lazy loading
const Component = lazy(() => import('./Component'));

// Dynamic imports
const module = await import('./module.js');
```

2. Optimize images:
```javascript
// Next.js Image
import Image from 'next/image';
<Image src="/photo.jpg" width={500} height={300} />

// Or use Cloudflare Images, Imgix
```

3. Add caching headers:
```json
{
  "headers": [
    {
      "source": "/static/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

### High Bandwidth Usage

**Solutions:**

1. Enable compression (usually automatic)
2. Optimize assets:
   - Images: WebP format, proper sizing
   - JavaScript: Tree-shaking, minification
   - CSS: PurgeCSS, minification

3. Use CDN (built-in on most platforms)

4. Implement lazy loading for below-fold content

## Debugging Tips

### Enable Debug Logs

**Vercel:**
```bash
vercel dev --debug
```

**Netlify:**
```bash
netlify dev --debug
```

**Railway:**
```bash
railway logs --follow
```

### Check Build Logs

All platforms provide detailed build logs:
- Look for first error (not last)
- Check environment variables are set
- Verify all files are committed to git
- Review warnings (they can become errors)

### Test Locally

```bash
# Install dependencies
npm ci

# Build locally
npm run build

# Serve production build
npx serve dist  # or appropriate directory
```

### Common Debugging Commands

```bash
# Check Node version
node --version

# Check package versions
npm list

# Verify environment
env | grep -i node

# Test build with verbose output
npm run build --verbose

# Clear all caches
rm -rf node_modules .next dist
npm ci
```
