# GitHub Issue Fixer - Workflow Diagram

## Visual Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INPUT                                   │
│              "Fix issue #3" / "修复 3 号 issue"                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 1: UNDERSTAND                             │
├─────────────────────────────────────────────────────────────────┤
│  1. Fetch Issue                                                  │
│     ├─ gh issue view <number>                                    │
│     └─ Parse: title, body, labels                                │
│                                                                   │
│  2. Classify Type                                                │
│     ├─ Bug: Broken functionality                                 │
│     ├─ Feature: Missing functionality                            │
│     └─ Enhancement: Improvement needed                           │
│                                                                   │
│  3. Explore Codebase (@explorer)                                 │
│     ├─ Find related files                                        │
│     ├─ Locate similar implementations                            │
│     └─ Identify dependencies                                     │
│                                                                   │
│  4. Research Solution (@librarian)                               │
│     ├─ Check library documentation                               │
│     ├─ Find API methods                                          │
│     └─ Understand best practices                                 │
│                                                                   │
│  5. Clarify Ambiguities                                          │
│     └─ Ask user if issue is vague                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 2: PLAN                                  │
├─────────────────────────────────────────────────────────────────┤
│  1. Create Todo List                                             │
│     ├─ Break down into specific tasks                            │
│     ├─ Identify files to create/modify                           │
│     └─ Note configuration needs                                  │
│                                                                   │
│  2. Identify Scope                                               │
│     ├─ What needs to be implemented?                             │
│     ├─ What edge cases to handle?                                │
│     └─ What documentation to update?                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 3: PREPARE                                │
├─────────────────────────────────────────────────────────────────┤
│  1. Check Current State                                          │
│     └─ git status, git branch                                    │
│                                                                   │
│  2. Stash Uncommitted Changes (if any)                           │
│     └─ git stash push -m "..."                                   │
│                                                                   │
│  3. Create Feature Branch                                        │
│     └─ git checkout -b <type>/<number>/<description>             │
│         Examples:                                                │
│         - fix/123/login-timeout                                  │
│         - feature/42/forgot-password                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                 PHASE 4: IMPLEMENT                               │
├─────────────────────────────────────────────────────────────────┤
│  For each todo item:                                             │
│                                                                   │
│  1. Mark as in_progress                                          │
│     └─ todowrite: Update status                                  │
│                                                                   │
│  2. Read Relevant Files                                          │
│     └─ Understand existing patterns                              │
│                                                                   │
│  3. Implement Change                                             │
│     ├─ Create new files                                          │
│     ├─ Modify existing files                                     │
│     ├─ Follow code style                                         │
│     └─ Handle edge cases                                         │
│                                                                   │
│  4. Verify Immediately                                           │
│     ├─ lsp_diagnostics: Check errors                             │
│     └─ Fix any issues                                            │
│                                                                   │
│  5. Mark as completed                                            │
│     └─ todowrite: Update status                                  │
│                                                                   │
│  Special Considerations:                                         │
│  ├─ i18n: Add translations to all language files                 │
│  ├─ Config: Document required setup                              │
│  └─ Quality: Follow existing patterns                            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 5: TEST                                   │
├─────────────────────────────────────────────────────────────────┤
│  1. Manual Verification                                          │
│     ├─ Test happy path                                           │
│     ├─ Test error cases                                          │
│     └─ Test edge cases                                           │
│                                                                   │
│  2. Automated Tests (if applicable)                              │
│     ├─ Run test suite                                            │
│     └─ Add new tests                                             │
│                                                                   │
│  3. LSP Diagnostics                                              │
│     └─ Verify no type errors                                     │
│                                                                   │
│  4. Self-Review                                                  │
│     ├─ Root cause addressed?                                     │
│     ├─ Error handling included?                                  │
│     ├─ Follows conventions?                                      │
│     └─ No unnecessary changes?                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 6: COMMIT                                │
├─────────────────────────────────────────────────────────────────┤
│  1. Review Changes                                               │
│     ├─ git status                                                │
│     └─ git diff                                                  │
│                                                                   │
│  2. Stage Relevant Files                                         │
│     └─ git add <specific-files>                                  │
│                                                                   │
│  3. Write Commit Message (Conventional Commits)                  │
│     Format:                                                      │
│     <type>(<scope>): <description>                               │
│                                                                   │
│     [optional body]                                              │
│                                                                   │
│     Fixes #<number>                                              │
│                                                                   │
│     Types: fix, feat, refactor, docs, test, chore                │
│                                                                   │
│  4. Commit                                                       │
│     └─ git commit -m "..."                                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 7: PR                                   │
├─────────────────────────────────────────────────────────────────┤
│  1. Push Branch                                                  │
│     └─ git push -u origin <branch-name>                          │
│                                                                   │
│  2. Analyze Full Context                                         │
│     ├─ git log --oneline                                         │
│     └─ git diff main...HEAD                                      │
│                                                                   │
│  3. Draft PR Description                                         │
│     Template:                                                    │
│     - Summary                                                    │
│     - Changes (bullet points)                                    │
│     - How It Works                                               │
│     - Testing Instructions                                       │
│     - Notes (config, limitations)                                │
│     - Closes: Fixes #<number>                                    │
│                                                                   │
│  4. Create PR                                                    │
│     └─ gh pr create --title "..." --body "..."                   │
│                                                                   │
│  5. Return PR URL                                                │
│     └─ Provide link to user                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SUCCESS                                     │
│                                                                   │
│  ✅ Issue resolved                                               │
│  ✅ Clean git history                                            │
│  ✅ Comprehensive PR                                             │
│  ✅ Ready for review                                             │
└─────────────────────────────────────────────────────────────────┘
```

## Specialist Delegation Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 1: UNDERSTAND                           │
└───────────┬─────────────────────────────────────────────────────┘
            │
            ├─► @explorer
            │   ├─ Find related files
            │   ├─ Locate patterns
            │   └─ Map dependencies
            │
            └─► @librarian
                ├─ Library docs
                ├─ API methods
                └─ Best practices

┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 4: IMPLEMENT                             │
└───────────┬─────────────────────────────────────────────────────┘
            │
            ├─► @designer (if UI work)
            │   ├─ Visual design
            │   ├─ Responsive layout
            │   └─ User experience
            │
            └─► @fixer (if 3+ parallel tasks)
                ├─ Independent task 1
                ├─ Independent task 2
                └─ Independent task 3
```

## Decision Tree

```
User says "Fix issue #N"
    │
    ├─ Issue exists? ──No──► Ask user to verify issue number
    │                         or create issue first
    └─ Yes
        │
        ├─ Issue clear? ──No──► Comment on issue asking
        │                        for clarification
        └─ Yes
            │
            ├─ Type: Bug
            │   ├─ Can reproduce? ──No──► Ask for repro steps
            │   └─ Yes ──► Red-Green-Refactor
            │
            ├─ Type: Feature
            │   ├─ Needs research? ──Yes──► Use @librarian
            │   └─ No ──► Implement directly
            │
            └─ Type: Enhancement
                ├─ Needs design? ──Yes──► Use @designer
                └─ No ──► Implement directly
```

## Quality Gates

```
Each phase has exit criteria:

PHASE 1 ✓
├─ Issue fully understood
├─ Type classified
├─ Dependencies identified
└─ Solution approach clear

PHASE 2 ✓
├─ Todo list created
├─ Scope identified
└─ Edge cases noted

PHASE 3 ✓
├─ Clean working directory
├─ Feature branch created
└─ Ready to code

PHASE 4 ✓
├─ All todos completed
├─ LSP diagnostics clean
├─ i18n translations added
└─ Configuration documented

PHASE 5 ✓
├─ Manual testing passed
├─ Automated tests passed
├─ Self-review completed
└─ Quality checklist verified

PHASE 6 ✓
├─ Relevant files staged
├─ Commit message clear
└─ Issue referenced

PHASE 7 ✓
├─ Branch pushed
├─ PR description complete
├─ Issue linked
└─ PR URL provided
```

## Time Estimates

```
Typical fix timeline:

Simple Bug Fix:
├─ Understand: 2 min
├─ Plan: 1 min
├─ Prepare: 1 min
├─ Implement: 3 min
├─ Test: 2 min
├─ Commit: 1 min
└─ PR: 1 min
Total: ~10-15 minutes

Feature Implementation:
├─ Understand: 3 min (with @librarian)
├─ Plan: 2 min
├─ Prepare: 1 min
├─ Implement: 5-10 min
├─ Test: 2 min
├─ Commit: 1 min
└─ PR: 1 min
Total: ~15-20 minutes

Complex Enhancement:
├─ Understand: 5 min (with @explorer + @librarian)
├─ Plan: 3 min
├─ Prepare: 1 min
├─ Implement: 10-15 min (with @designer/@fixer)
├─ Test: 5 min
├─ Commit: 2 min
└─ PR: 2 min
Total: ~30-40 minutes
```

## Success Metrics

```
Quality Indicators:

High Quality Fix:
├─ ✅ First-time merge rate: >80%
├─ ✅ Review comments: <3
├─ ✅ Time to merge: <24 hours
├─ ✅ Regression rate: <5%
└─ ✅ Code review score: >8/10

Medium Quality Fix:
├─ ⚠️ First-time merge rate: 50-80%
├─ ⚠️ Review comments: 3-10
├─ ⚠️ Time to merge: 24-72 hours
├─ ⚠️ Regression rate: 5-15%
└─ ⚠️ Code review score: 6-8/10

Low Quality Fix:
├─ ❌ First-time merge rate: <50%
├─ ❌ Review comments: >10
├─ ❌ Time to merge: >72 hours
├─ ❌ Regression rate: >15%
└─ ❌ Code review score: <6/10
```

---

**Remember**: Each phase builds on the previous. Don't skip steps!
