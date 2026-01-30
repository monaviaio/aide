# GitHub Issue Fixer - Quick Reference

## 🚀 Quick Start

```bash
"Fix issue #<number>"
```

## 📋 The 7-Phase Workflow

```
1. UNDERSTAND → Fetch issue, classify type, research approach
2. PLAN       → Create todo list, identify scope
3. PREPARE    → Stash changes, create branch
4. IMPLEMENT  → Code with quality, handle edge cases
5. TEST       → Verify manually and with LSP
6. COMMIT     → Conventional Commits format
7. PR         → Comprehensive description, link issue
```

## 🏷️ Branch Naming

```
<type>/<issue-number>/<short-description>

Examples:
fix/123/login-timeout
feature/42/forgot-password
bug/456/header-alignment
```

## 📝 Commit Format

```
<type>(<scope>): <description>

[optional body]

Fixes #<issue-number>

Example:
feat(auth): implement forgot password flow

- Add /forgot-password page
- Add /reset-password page
- Configure email callback

Fixes #3
```

### Commit Types
- `fix`: Bug fix
- `feat`: New feature
- `refactor`: Code restructuring
- `docs`: Documentation
- `test`: Tests
- `chore`: Maintenance

## 📄 PR Template

```markdown
## Summary
Brief explanation (1-2 sentences)

## Changes
- ✅ Key change 1
- ✅ Key change 2
- ✅ Key change 3

## How It Works
Implementation approach

## Testing
1. Step-by-step test instructions
2. Expected behavior

## Notes
- Production setup required
- Known limitations

## Closes
Fixes #<number>
```

## ✅ Quality Checklist

Before submitting:
- [ ] Root cause addressed (not symptoms)
- [ ] Edge cases handled
- [ ] Error handling included
- [ ] Follows project conventions
- [ ] LSP diagnostics clean
- [ ] i18n translations added
- [ ] Configuration documented
- [ ] Commit message clear
- [ ] PR description complete
- [ ] Issue properly linked

## 🎯 Specialist Delegation

| Specialist | When to Use |
|-----------|-------------|
| @explorer | Discover files, find patterns |
| @librarian | Library docs, API research |
| @designer | UI/UX, responsive layouts |
| @fixer | 3+ parallel independent tasks |

## ⚠️ Common Mistakes

| ❌ Mistake | ✅ Solution |
|-----------|-----------|
| Shotgun changes | Use @explorer first |
| No reproduction | Red-Green-Refactor |
| Unrelated changes | Focused commits |
| Vague PR | Use template |
| Assumptions | Ask for clarity |
| Skip research | Use @librarian |
| Missing config | Document TODOs |

## 🔄 Red-Green-Refactor

```
1. RED    → Create failing test/reproduction
2. GREEN  → Minimal code to pass
3. REFACTOR → Clean up and improve
```

## 📊 Success Metrics

- ✅ Issue completely resolved
- ✅ No regressions
- ✅ Code maintainable
- ✅ Tests pass
- ✅ Documentation updated
- ✅ Clean git history
- ✅ Fast merge

## 🎓 Methodology Credits

- **Kent Beck**: Test-Driven Development
- **Martin Fowler**: Refactoring
- **GitHub**: GitHub Flow
- **Google**: Code Review Standards
- **Conventional Commits**: Commit format

---

**Pro Tip**: Trust the process. Each phase builds on the previous one. Don't skip steps!
