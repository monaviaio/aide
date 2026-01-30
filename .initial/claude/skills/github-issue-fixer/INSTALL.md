# Installation Guide

## Quick Install

The skill is already installed at:
```
~/.claude/skills/github-issue-fixer/
```

No additional setup required!

## Prerequisites

### Required
- ✅ Claude Code (with skill support)
- ✅ Git installed and configured
- ✅ GitHub CLI (`gh`) installed and authenticated
- ✅ Working directory is a git repository with GitHub remote

### Optional
- 🔧 LSP server for your language (for diagnostics)
- 🔧 Project-specific tools (npm, pnpm, etc.)

## Verify Installation

### 1. Check Skill Files
```bash
ls -la ~/.claude/skills/github-issue-fixer/
```

Expected output:
```
SKILL.md              # Main skill definition
README.md             # Usage guide
QUICK_REFERENCE.md    # Fast lookup
EXAMPLES.md           # Real examples
CHANGELOG.md          # Version history
WORKFLOW_DIAGRAM.md   # Visual workflow
INSTALL.md            # This file
```

### 2. Check GitHub CLI
```bash
gh --version
gh auth status
```

Expected output:
```
gh version 2.x.x
✓ Logged in to github.com as <your-username>
```

### 3. Test with Sample Issue
```bash
# In your project directory
gh issue list
```

If you see issues, you're ready to use the skill!

## First Use

### Step 1: Navigate to Your Project
```bash
cd /path/to/your/project
```

### Step 2: Ensure Git is Clean (or Stash)
```bash
git status
# If you have uncommitted changes, the skill will stash them
```

### Step 3: Ask Claude to Fix an Issue
```
"Fix issue #3"
"Resolve GitHub issue #42"
"修复 3 号 issue"
```

### Step 4: Review the PR
The skill will provide a PR URL. Review it before merging.

## Troubleshooting

### "gh: command not found"
Install GitHub CLI:
```bash
# macOS
brew install gh

# Linux
sudo apt install gh

# Windows
winget install GitHub.cli
```

Then authenticate:
```bash
gh auth login
```

### "Not a git repository"
```bash
cd /path/to/your/project
git status  # Verify you're in a git repo
```

### "Issue not found"
```bash
gh issue list  # Check issue numbers
gh issue view <number>  # Verify issue exists
```

### "Permission denied"
Ensure you have write access to the repository:
```bash
gh repo view  # Check your permissions
```

### "LSP diagnostics not available"
Install language server for your project:
```bash
# TypeScript/JavaScript
npm install -g typescript typescript-language-server

# Python
pip install python-lsp-server

# Other languages: Check language-specific LSP docs
```

## Configuration

### Skill Customization
Edit the skill file if needed:
```bash
code ~/.claude/skills/github-issue-fixer/SKILL.md
```

### Project-Specific Settings
The skill automatically adapts to:
- Your commit message style
- Your code formatting conventions
- Your i18n setup
- Your testing framework

No configuration needed!

## Upgrading

### Check for Updates
```bash
cat ~/.claude/skills/github-issue-fixer/CHANGELOG.md
```

### Manual Update
1. Backup current version
2. Replace SKILL.md with new version
3. Test with a sample issue

## Uninstallation

To remove the skill:
```bash
rm -rf ~/.claude/skills/github-issue-fixer/
```

To restore:
```bash
# Re-create from the original SKILL.md
```

## Support

### Documentation
- SKILL.md: Complete workflow guide
- QUICK_REFERENCE.md: Fast lookup
- EXAMPLES.md: Real-world examples
- WORKFLOW_DIAGRAM.md: Visual flow

### Getting Help
1. Check EXAMPLES.md for similar scenarios
2. Review QUICK_REFERENCE.md for common tasks
3. Read SKILL.md for detailed explanations
4. Ask Claude: "How do I use the github-issue-fixer skill?"

## Best Practices

### Before Using
- ✅ Ensure issue is clear and actionable
- ✅ Have write access to repository
- ✅ Working directory is clean (or okay to stash)

### During Use
- ✅ Trust the process (don't skip phases)
- ✅ Review changes before committing
- ✅ Verify PR description is accurate

### After Use
- ✅ Review the PR before merging
- ✅ Monitor for any issues after merge
- ✅ Provide feedback for skill improvement

## Performance Tips

### For Faster Fixes
- Keep your working directory clean
- Have GitHub CLI authenticated
- Use LSP for instant error checking
- Trust the automated research (@librarian, @explorer)

### For Better Quality
- Don't rush the understanding phase
- Let the skill research libraries
- Review the quality checklist
- Test thoroughly before committing

## Integration with Other Tools

### CI/CD
The skill creates PRs that work with:
- GitHub Actions
- CircleCI
- Travis CI
- Jenkins
- Any CI/CD that triggers on PR

### Code Review Tools
PRs created by this skill are compatible with:
- GitHub Code Review
- CodeClimate
- SonarQube
- Reviewable

### Project Management
Issue linking works with:
- GitHub Projects
- Jira (via GitHub integration)
- Linear (via GitHub integration)
- Any tool that syncs with GitHub

## FAQ

### Q: Does this work with GitLab/Bitbucket?
A: Currently GitHub only. GitLab/Bitbucket support planned for v2.0.

### Q: Can I customize the commit message format?
A: Yes, edit SKILL.md to change the Conventional Commits format.

### Q: What if my project doesn't use i18n?
A: The skill detects this and skips translation steps automatically.

### Q: Can I use this for private repositories?
A: Yes, as long as `gh` CLI has access to the repo.

### Q: Does this work with monorepos?
A: Yes, navigate to the package directory before using the skill.

### Q: Can I fix multiple issues at once?
A: Use the skill once per issue for clean history. For related issues, create one umbrella issue.

### Q: What if the fix needs architectural changes?
A: Use @oracle for architectural decisions first, then use this skill for implementation.

### Q: How do I report bugs in the skill?
A: Update SKILL.md with improvements or create an issue in your project's meta repo.

---

**Ready to use?** Try: "Fix issue #<number>"
