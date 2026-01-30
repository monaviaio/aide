# GitHub Issue Creator - Quick Reference

## 🚀 Quick Start

```
"Create an issue for [problem]"
"Write an issue: [description]"
"创建 issue：[问题描述]"
```

## 📋 Issue Type Decision Tree

```
What are you reporting?
│
├─ Something is BROKEN → Bug Report
│  ├─ Crashes/errors
│  ├─ Unexpected behavior
│  └─ UI glitches
│
├─ Something is MISSING → Feature Request
│  ├─ New functionality
│  ├─ User capability
│  └─ Product gap
│
├─ Something needs IMPROVEMENT → Enhancement
│  ├─ Performance
│  ├─ UX refinement
│  └─ Code quality
│
└─ Something is UNCLEAR → Documentation
   ├─ Missing docs
   ├─ Confusing docs
   └─ Outdated docs
```

## 🏷️ Title Format

```
[Type] Specific, observable problem or feature

Good Examples:
✅ Bug: Login fails with 403 when password contains @
✅ Feature: Add dark mode toggle to settings
✅ Enhancement: Reduce dashboard load time by 50%

Bad Examples:
❌ It's broken
❌ Fix bug
❌ Help!
```

## 📝 Bug Report Template (Quick)

```markdown
## Bug Description
[What's wrong in 1-2 sentences]

## Steps to Reproduce
1. Go to...
2. Click...
3. See error

## Expected vs Actual
Expected: [what should happen]
Actual: [what happens instead]

## Environment
- OS: [macOS 14.2]
- Browser: [Chrome 120]
- Version: [v2.1.0]

## Screenshots
[Attach evidence]
```

## 🎯 Feature Request Template (Quick)

```markdown
## Feature Summary
[One sentence description]

## Problem / Motivation
As a [user type]
I want to [action]
So that [benefit]

## Proposed Solution
[How it should work]

## Success Criteria
- [ ] Outcome 1
- [ ] Outcome 2
```

## ✨ Enhancement Template (Quick)

```markdown
## Enhancement Summary
[What needs improvement]

## Current Behavior
[How it works now]

## Proposed Improvement
[How it should work]

## Benefits
- [Benefit 1]
- [Benefit 2]
```

## 🎯 3 Essential Elements (Joel Spolsky)

Every bug report needs:
1. **Steps to reproduce**
2. **What you expected**
3. **What you saw instead**

## 🚫 Common Mistakes & Fixes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| "It's broken" | "Login fails with 403 on special chars" |
| "Sometimes happens" | "Happens every time I do X, Y, Z" |
| "App crashed" | "App crashed after clicking Save" |
| No screenshot | Include visual evidence |
| "Fix this NOW!" | "Happy to help test the fix" |
| Wall of text | Use headers, lists, code blocks |

## 📊 Quality Checklist

Before submitting:
- [ ] Title is specific (50-80 chars)
- [ ] Type is identified (Bug/Feature/Enhancement)
- [ ] Problem is clearly described
- [ ] Steps to reproduce (for bugs)
- [ ] Motivation explained (for features)
- [ ] Environment details included
- [ ] Screenshots/logs attached
- [ ] Markdown formatting used
- [ ] Sensitive data sanitized
- [ ] Labels suggested

## 🎨 Markdown Cheat Sheet

```markdown
# H1 Header
## H2 Header
### H3 Header

**Bold text**
*Italic text*

`inline code`

```code block```

- Bullet list
1. Numbered list

> Blockquote

[Link text](url)
![Image](url)
```

## 🔍 Information to Gather

### For Bugs
- [ ] What were you doing?
- [ ] Exact steps to reproduce
- [ ] What did you expect?
- [ ] What actually happened?
- [ ] Error messages
- [ ] Screenshots
- [ ] OS/Browser/Version
- [ ] When did this start?

### For Features
- [ ] What problem does this solve?
- [ ] Who needs this?
- [ ] How should it work?
- [ ] What's the business value?
- [ ] Any examples elsewhere?
- [ ] What are alternatives?

### For Enhancements
- [ ] Current behavior
- [ ] What's wrong with it?
- [ ] How to improve it?
- [ ] Expected benefits
- [ ] How to measure success?

## 🏷️ Label Suggestions

### Type Labels
- `bug` - Something is broken
- `feature` - New functionality
- `enhancement` - Improvement
- `documentation` - Docs issue

### Component Labels
- `auth` - Authentication
- `ui` - User interface
- `api` - Backend API
- `performance` - Speed/efficiency
- `security` - Security issue

### Priority Labels
- `critical` - Urgent fix needed
- `high` - Important
- `medium` - Normal priority
- `low` - Nice to have

### Status Labels
- `needs-triage` - Needs review
- `needs-reproduction` - Can't reproduce yet
- `needs-design` - Needs design work
- `good-first-issue` - Easy for newcomers
- `help-wanted` - Community help needed

## 🎯 Priority Guidelines

### Critical
- Security vulnerabilities
- Data loss
- Complete breakage
- All users affected

### High
- Major functionality broken
- Significant UX problem
- Many users affected

### Medium
- Minor functionality issue
- Moderate UX problem
- Some users affected

### Low
- Cosmetic issues
- Edge cases
- Few users affected

## 💡 Pro Tips

### Show, Don't Tell
❌ "Button doesn't work"
✅ "Clicking Save does nothing, no error shown"

### Report Symptoms, Not Diagnoses
❌ "Auth token is null"
✅ "Get logged out right after login"

### Be Specific
❌ "Dashboard is slow"
✅ "Dashboard takes 10s with >1000 transactions"

### Avoid the XY Problem
❌ "Add cache clear button"
✅ "I see stale data after profile update"

### Be Collaborative
❌ "Fix this NOW!"
✅ "Blocking my work, happy to help test"

## 🔄 Workflow

```
1. Describe problem
   ↓
2. Skill asks clarifying questions
   ↓
3. Skill researches codebase
   ↓
4. Skill drafts issue
   ↓
5. You review and approve
   ↓
6. Skill creates issue
   ↓
7. Get issue URL
```

## 📈 Success Metrics

Good issue = Developer can:
- ✅ Understand in <2 min
- ✅ Start work immediately
- ✅ Know when it's done
- ✅ Estimate effort

## 🎓 Methodology Credits

- **Joel Spolsky**: 3 essential elements
- **Jeff Atwood**: Report symptoms
- **Simon Tatham**: Show, don't tell
- **GitHub**: Template standards

---

**Pro Tip**: Invest time in creating quality issues - they get fixed faster!
