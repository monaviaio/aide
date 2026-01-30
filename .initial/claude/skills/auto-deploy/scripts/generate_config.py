#!/usr/bin/env python3
"""
Generate platform-specific configuration files for deployment.

Usage:
    python generate_config.py <platform> <framework> [--output-dir .]
    
Platforms: vercel, netlify, cloudflare, railway, render
Frameworks: nextjs, react, vue, nuxt, svelte, astro, node
"""

import argparse
import json
import sys
from pathlib import Path


CONFIGS = {
    "vercel": {
        "nextjs": {
            "filename": "vercel.json",
            "content": {
                "buildCommand": "npm run build",
                "outputDirectory": ".next",
                "framework": "nextjs",
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
                                "key": "X-XSS-Protection",
                                "value": "1; mode=block"
                            }
                        ]
                    }
                ]
            }
        },
        "react": {
            "filename": "vercel.json",
            "content": {
                "buildCommand": "npm run build",
                "outputDirectory": "dist",
                "rewrites": [
                    {"source": "/(.*)", "destination": "/"}
                ]
            }
        },
        "vue": {
            "filename": "vercel.json",
            "content": {
                "buildCommand": "npm run build",
                "outputDirectory": "dist",
                "rewrites": [
                    {"source": "/(.*)", "destination": "/"}
                ]
            }
        }
    },
    "netlify": {
        "nextjs": {
            "filename": "netlify.toml",
            "content": """[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
"""
        },
        "react": {
            "filename": "netlify.toml",
            "content": """[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""
        },
        "vue": {
            "filename": "netlify.toml",
            "content": """[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""
        }
    },
    "railway": {
        "node": {
            "filename": "railway.toml",
            "content": """[build]
cmd = "npm install && npm run build"

[deploy]
startCommand = "npm start"
restartPolicyType = "on-failure"
restartPolicyMaxRetries = 10
"""
        },
        "nextjs": {
            "filename": "railway.toml",
            "content": """[build]
cmd = "npm install && npm run build"

[deploy]
startCommand = "npm start"
"""
        }
    },
    "render": {
        "node": {
            "filename": "render.yaml",
            "content": """services:
  - type: web
    name: my-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production
"""
        },
        "nextjs": {
            "filename": "render.yaml",
            "content": """services:
  - type: web
    name: nextjs-app
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_ENV
        value: production
"""
        }
    }
}


def generate_config(platform: str, framework: str, output_dir: Path):
    """Generate configuration file for the specified platform and framework."""
    
    if platform not in CONFIGS:
        print(f"Error: Platform '{platform}' not supported.")
        print(f"Supported platforms: {', '.join(CONFIGS.keys())}")
        return False
    
    if framework not in CONFIGS[platform]:
        print(f"Error: Framework '{framework}' not supported for {platform}.")
        print(f"Supported frameworks for {platform}: {', '.join(CONFIGS[platform].keys())}")
        return False
    
    config = CONFIGS[platform][framework]
    filename = config["filename"]
    content = config["content"]
    
    output_path = output_dir / filename
    
    # Write configuration file
    with open(output_path, "w") as f:
        if isinstance(content, dict):
            json.dump(content, f, indent=2)
        else:
            f.write(content)
    
    print(f"✅ Generated {filename} for {platform} ({framework})")
    print(f"   Location: {output_path}")
    print(f"\n📝 Next steps:")
    print(f"   1. Review and customize the configuration")
    print(f"   2. Add environment variables in your {platform} dashboard")
    print(f"   3. Commit {filename} to your repository")
    print(f"   4. Push to deploy!")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate platform-specific deployment configuration files"
    )
    parser.add_argument(
        "platform",
        choices=["vercel", "netlify", "cloudflare", "railway", "render"],
        help="Deployment platform"
    )
    parser.add_argument(
        "framework",
        choices=["nextjs", "react", "vue", "nuxt", "svelte", "astro", "node"],
        help="Framework or runtime"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Output directory (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    success = generate_config(args.platform, args.framework, args.output_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
