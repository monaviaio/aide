#!/usr/bin/env python3
"""
Check framework and platform compatibility for deployment.

Usage:
    python check_compatibility.py [--framework <framework>] [--platform <platform>]
"""

import argparse
import json
import sys
from pathlib import Path


COMPATIBILITY_MATRIX = {
    "nextjs": {
        "recommended": ["vercel", "cloudflare-pages", "netlify"],
        "supported": ["railway", "render", "fly-io"],
        "features": {
            "ssr": True,
            "ssg": True,
            "edge": True,
            "serverless": True
        },
        "notes": "Best on Vercel (native support) or Cloudflare Pages (edge runtime)"
    },
    "react": {
        "recommended": ["vercel", "cloudflare-pages", "netlify"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": False,
            "ssg": True,
            "edge": False,
            "serverless": False
        },
        "notes": "Use Vite for modern builds. All static hosts work well."
    },
    "vue": {
        "recommended": ["vercel", "netlify", "cloudflare-pages"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": False,
            "ssg": True,
            "edge": False,
            "serverless": False
        },
        "notes": "Vite-based builds recommended. Consider Nuxt for SSR."
    },
    "nuxt": {
        "recommended": ["vercel", "netlify", "cloudflare-pages"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": True,
            "ssg": True,
            "edge": True,
            "serverless": True
        },
        "notes": "Full SSR support. Edge runtime available on Cloudflare/Vercel."
    },
    "svelte": {
        "recommended": ["vercel", "netlify", "cloudflare-pages"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": False,
            "ssg": True,
            "edge": False,
            "serverless": False
        },
        "notes": "Use SvelteKit for SSR capabilities"
    },
    "sveltekit": {
        "recommended": ["vercel", "cloudflare-pages", "netlify"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": True,
            "ssg": True,
            "edge": True,
            "serverless": True
        },
        "notes": "Excellent adapter system for different platforms"
    },
    "astro": {
        "recommended": ["cloudflare-pages", "vercel", "netlify"],
        "supported": ["railway", "render"],
        "features": {
            "ssr": True,
            "ssg": True,
            "edge": True,
            "serverless": True
        },
        "notes": "Best for content-heavy sites. Excellent SSG performance."
    },
    "express": {
        "recommended": ["railway", "render", "fly-io"],
        "supported": ["vercel", "netlify"],
        "features": {
            "ssr": True,
            "ssg": False,
            "edge": False,
            "serverless": True
        },
        "notes": "Traditional Node.js app. Needs always-on server or serverless adapter."
    }
}

PLATFORM_INFO = {
    "vercel": {
        "best_for": ["nextjs", "react", "sveltekit"],
        "free_tier": "100GB bandwidth, unlimited projects",
        "build_minutes": "6000/month",
        "edge_functions": True,
        "serverless": True
    },
    "cloudflare-pages": {
        "best_for": ["astro", "nextjs", "react"],
        "free_tier": "Unlimited bandwidth and requests",
        "build_minutes": "500 builds/month",
        "edge_functions": True,
        "serverless": True
    },
    "netlify": {
        "best_for": ["react", "vue", "nuxt"],
        "free_tier": "100GB bandwidth, 300 build minutes",
        "build_minutes": "300/month",
        "edge_functions": True,
        "serverless": True
    },
    "railway": {
        "best_for": ["express", "nextjs", "any-with-db"],
        "free_tier": "$5 credit/month",
        "build_minutes": "Included in credit",
        "edge_functions": False,
        "serverless": False,
        "databases": ["postgresql", "mysql", "redis", "mongodb"]
    },
    "render": {
        "best_for": ["express", "django", "docker"],
        "free_tier": "750 hours/month (with sleep)",
        "build_minutes": "Unlimited",
        "edge_functions": False,
        "serverless": False
    },
    "fly-io": {
        "best_for": ["docker", "global-apps", "express"],
        "free_tier": "3 shared VMs, 3GB storage",
        "build_minutes": "Unlimited",
        "edge_functions": True,
        "serverless": False
    }
}


def detect_framework(project_dir: Path = Path(".")):
    """Detect framework from package.json or other indicators."""
    
    package_json = project_dir / "package.json"
    
    if not package_json.exists():
        return None
    
    with open(package_json) as f:
        data = json.load(f)
    
    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
    
    # Check for framework-specific dependencies
    if "next" in deps:
        return "nextjs"
    elif "nuxt" in deps or "@nuxt/kit" in deps:
        return "nuxt"
    elif "@sveltejs/kit" in deps:
        return "sveltekit"
    elif "svelte" in deps:
        return "svelte"
    elif "astro" in deps:
        return "astro"
    elif "vue" in deps:
        return "vue"
    elif "react" in deps:
        return "react"
    elif "express" in deps:
        return "express"
    
    return None


def check_compatibility(framework: str, platform: str = None):
    """Check compatibility and provide recommendations."""
    
    if framework not in COMPATIBILITY_MATRIX:
        print(f"❌ Framework '{framework}' not recognized.")
        print(f"Supported frameworks: {', '.join(COMPATIBILITY_MATRIX.keys())}")
        return False
    
    info = COMPATIBILITY_MATRIX[framework]
    
    print(f"\n🔍 Compatibility Check: {framework.upper()}")
    print("=" * 60)
    
    print(f"\n✅ Recommended Platforms:")
    for p in info["recommended"]:
        print(f"   • {p}")
    
    print(f"\n⚠️  Supported (with limitations):")
    for p in info["supported"]:
        print(f"   • {p}")
    
    print(f"\n🎯 Features:")
    for feature, supported in info["features"].items():
        status = "✅" if supported else "❌"
        print(f"   {status} {feature.upper()}")
    
    print(f"\n💡 Notes: {info['notes']}")
    
    if platform:
        if platform in PLATFORM_INFO:
            print(f"\n📊 Platform Details: {platform.upper()}")
            print("-" * 60)
            pinfo = PLATFORM_INFO[platform]
            print(f"Best for: {', '.join(pinfo['best_for'])}")
            print(f"Free tier: {pinfo['free_tier']}")
            print(f"Build minutes: {pinfo['build_minutes']}")
            
            if framework in pinfo.get("best_for", []):
                print(f"\n✅ {framework} is HIGHLY compatible with {platform}")
            elif platform in info["recommended"]:
                print(f"\n✅ {platform} is recommended for {framework}")
            elif platform in info["supported"]:
                print(f"\n⚠️  {platform} supports {framework} but may have limitations")
            else:
                print(f"\n❌ {platform} is not recommended for {framework}")
                print(f"   Consider: {', '.join(info['recommended'])}")
        else:
            print(f"\n❌ Platform '{platform}' not recognized.")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Check deployment platform compatibility"
    )
    parser.add_argument(
        "--framework",
        help="Framework to check (auto-detected if not specified)"
    )
    parser.add_argument(
        "--platform",
        choices=["vercel", "cloudflare-pages", "netlify", "railway", "render", "fly-io"],
        help="Platform to check against (optional)"
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path("."),
        help="Project directory (default: current directory)"
    )
    
    args = parser.parse_args()
    
    framework = args.framework
    
    if not framework:
        print("🔎 Auto-detecting framework...")
        framework = detect_framework(args.project_dir)
        
        if framework:
            print(f"✅ Detected: {framework}")
        else:
            print("❌ Could not detect framework. Please specify with --framework")
            sys.exit(1)
    
    success = check_compatibility(framework, args.platform)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
