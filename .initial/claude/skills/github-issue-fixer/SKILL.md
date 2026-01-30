---
name: github-issue-fixer
description: Systematically fix GitHub issues following industry best practices. Use this skill when the user asks to fix, resolve, or implement a GitHub issue by number (e.g., "fix issue #3", "implement #42"). This skill guides you through the complete workflow from understanding the issue to creating a merged PR, ensuring quality, completeness, and proper git hygiene.
---

# GitHub Issue Fixer

Systematically fix GitHub issues using proven methodologies from Kent Beck (TDD), Martin Fowler (Refactoring), and GitHub Flow. This skill ensures every fix is complete, tested, documented, and follows industry standards.

## When to Use This Skill

Trigger this skill when the user provides:
- **Explicit issue number**: "Fix issue #3", "Resolve #42", "Implement issue 123"
- **Issue reference with action**: "修复 3 号 issue", "处理 GitHub issue #5"

Do NOT trigger for:
- General bug reports without issue numbers
- Feature requests not yet tracked as issues
- Questions about how to fix something

## Core Philosophy

This skill embodies three proven methodologies:

### 1. Kent Beck's Test-Driven Development (TDD)
**Red-Green-Refactor**: Never write production code until you have a reproduction case or test that demonstrates the issue. This ensures:
- You've actually understood the problem
- The fix can be verified
- Regressions are prevented

### 2. Martin Fowler's Refactoring Principle
**Leave the campground cleaner**: Fixes should not just patch symptoms but improve code structure. A good fix:
- Addresses the root cause, not symptoms
- Improves code clarity
- Reduces future maintenance burden

### 3. GitHub Flow
**Branch-based workflow**: Every fix follows a consistent, safe workflow:
1. Create feature branch
2. Make changes with atomic commits
3. Push and create PR
4. Review and merge

## The Complete Fix Workflow

Follow these phases in order. Do not skip steps.

### Phase 1: Understand & Triage (CRITICAL)

**Goal**: Fully understand the issue before writing any code.

1. **Fetch the Issue**
   ```bash
   gh issue view <number>
   ```
   
2. **Parse the Issue**
   - What is the expected behavior?
   - What is the actual behavior?
   - What are the reproduction steps?
   - Are there any error messages or logs?

3. **Classify the Issue Type**
   - **Bug**: Existing functionality is broken
   - **Feature**: New functionality is missing (like forgot-password 404)
   - **Enhancement**: Existing functionality needs improvement
   - **Refactor**: Code structure needs improvement

4. **Identify Dependencies**
   Use @explorer to discover:
   - Related files and components
   - Existing similar implementations
   - Dependencies and libraries involved
   
   Example: For a "forgot password 404" issue, search for:
   - Authentication files
   - Existing password-related routes
   - Email service configuration

5. **Research Solution Approach**
   For features requiring library integration, use @librarian:
   - Check official documentation
   - Find implementation examples
   - Understand API methods and patterns
   
   Example: For forgot-password, research:
   - Auth library's password reset methods
   - Required configuration
   - Complete flow (request → email → reset)

6. **Clarify Ambiguities**
   If the issue is vague or incomplete:
   - Comment on the issue asking for clarification
   - DO NOT proceed with assumptions
   - Wait for user confirmation

### Phase 2: Plan the Fix

**Goal**: Create a clear implementation plan before coding.

1. **Create a Todo List**
   Use the todowrite tool to break down the fix into specific tasks:
   ```
   - Create new branch
   - Implement component A
   - Implement component B
   - Configure service C
   - Add translations (if applicable)
   - Write/update tests
   - Update documentation
   - Commit and push
   - Create PR
   ```

2. **Identify Scope**
   - What files need to be created?
   - What files need to be modified?
   - What new dependencies are required?
   - What configuration changes are needed?

3. **Consider Edge Cases**
   - Error handling
   - Validation
   - Loading states
   - Empty states
   - Internationalization

### Phase 3: Prepare Environment

**Goal**: Set up a clean working environment.

1. **Check Current State**
   ```bash
   git status
   git branch --show-current
   ```

2. **Stash Uncommitted Changes** (if any)
   ```bash
   git stash push -m "Temp stash before issue-<number> fix"
   ```

3. **Create Feature Branch**
   **Branch Naming Convention**: `<type>/<issue-number>/<short-description>`
   
   Examples:
   - `fix/123/login-timeout`
   - `feature/42/forgot-password`
   - `bug/456/header-alignment`
   
   ```bash
   git checkout -b <branch-name>
   ```

### Phase 4: Implement the Fix (Red-Green-Refactor)

**Goal**: Implement a complete, tested solution.

1. **Read Relevant Files First**
   Use the read tool to understand existing code before modifying:
   - Related components
   - Configuration files
   - Similar implementations

2. **Implement Incrementally**
   Follow the todo list created in Phase 2. For each task:
   
   a. **Mark as in_progress**
   ```
   todowrite: Mark current task as in_progress
   ```
   
   b. **Implement the change**
   - Create new files if needed
   - Modify existing files
   - Follow existing code style and patterns
   
   c. **Verify immediately**
   - Check for LSP errors: `lsp_diagnostics`
   - Fix any type errors or linting issues
   
   d. **Mark as completed**
   ```
   todowrite: Mark task as completed
   ```

3. **Handle Internationalization**
   If the project uses i18n:
   - Add translation keys to all language files
   - Use consistent key naming
   - Provide translations for all supported languages

4. **Configuration Updates**
   If new services or features require configuration:
   - Update configuration files
   - Add TODO comments for production setup
   - Document required environment variables

5. **Code Quality Checks**
   - Follow existing patterns and conventions
   - Keep functions focused and small
   - Add comments for complex logic
   - Use meaningful variable names

### Phase 5: Test & Verify

**Goal**: Ensure the fix works and doesn't break anything.

1. **Manual Verification**
   - Test the happy path
   - Test error cases
   - Test edge cases
   - Verify UI/UX if applicable

2. **Automated Tests** (if project has tests)
   - Run existing test suite
   - Add new tests for the fix
   - Ensure all tests pass

3. **LSP Diagnostics**
   ```bash
   lsp_diagnostics <file-path>
   ```
   Verify no type errors or warnings.

4. **Code Review Self-Check**
   Before committing, review your changes:
   - [ ] Addresses the root cause, not symptoms
   - [ ] Includes error handling
   - [ ] Follows project conventions
   - [ ] No unnecessary changes (formatting, unrelated fixes)
   - [ ] Clear and maintainable

### Phase 6: Commit with Quality

**Goal**: Create a clean, understandable git history.

1. **Review Changes**
   ```bash
   git status
   git diff
   ```

2. **Stage Changes**
   ```bash
   git add <relevant-files>
   ```
   
   **Important**: Only stage files related to this fix. Do not include:
   - Unrelated formatting changes
   - Debug code
   - Temporary files

3. **Write Commit Message**
   Follow **Conventional Commits** format:
   ```
   <type>(<scope>): <description>
   
   [optional body]
   
   [optional footer]
   ```
   
   **Types**:
   - `fix`: Bug fix
   - `feat`: New feature
   - `refactor`: Code restructuring
   - `docs`: Documentation only
   - `test`: Adding tests
   - `chore`: Maintenance tasks
   
   **Example**:
   ```
   feat(auth): implement forgot password and reset password flow
   
   - Add /forgot-password page with email input form
   - Add /reset-password page with new password form  
   - Configure auth.ts with sendResetPassword callback
   - Add i18n translations (en, zh, th)
   
   Fixes #3
   ```
   
   **Quality Criteria**:
   - First line ≤ 72 characters
   - Imperative mood ("Add feature" not "Added feature")
   - Body explains WHY, not WHAT (code shows what)
   - Reference issue number: "Fixes #123" or "Closes #456"

4. **Commit**
   ```bash
   git commit -m "<message>"
   ```

### Phase 7: Create Pull Request

**Goal**: Submit the fix for review and merge.

1. **Push Branch**
   ```bash
   git push -u origin <branch-name>
   ```

2. **Analyze Full Context**
   Before creating PR, review:
   ```bash
   git log --oneline
   git diff main...HEAD
   ```
   
   Understand ALL changes that will be included in the PR, not just the latest commit.

3. **Draft PR Description**
   Use this template:
   
   ```markdown
   ## Summary
   Brief explanation of what this PR does (1-2 sentences)
   
   ## Changes
   - ✅ Bullet list of key changes
   - ✅ What was added/modified/removed
   - ✅ Any configuration updates
   
   ## How It Works
   Explain the implementation approach (especially for complex fixes)
   
   ## Testing
   How to test this fix:
   1. Step-by-step instructions
   2. Expected behavior
   3. Edge cases covered
   
   ## Screenshots/Logs (if applicable)
   Visual proof that it works
   
   ## Notes
   - Any production setup required
   - Known limitations
   - Follow-up tasks
   
   ## Closes
   Fixes #<issue-number>
   ```

4. **Create PR**
   ```bash
   gh pr create --title "<title>" --body "<body>"
   ```
   
   **Title Format**: `<Type>: <Description> (Fixes #<number>)`
   
   Examples:
   - `Fix: Implement forgot password flow (Fixes #3)`
   - `Feature: Add user export functionality (Fixes #42)`

5. **Return PR URL**
   Always provide the PR URL to the user so they can review it.

## Quality Checklist

Before marking the fix as complete, verify ALL of these:

### Completeness
- [ ] Issue is fully understood (not assumed)
- [ ] Root cause is addressed (not symptoms)
- [ ] All edge cases are handled
- [ ] Error handling is included
- [ ] Loading/empty states are considered (if UI)

### Code Quality
- [ ] Follows project conventions and patterns
- [ ] Code is readable and maintainable
- [ ] No unnecessary changes or debugging code
- [ ] LSP diagnostics show no errors
- [ ] Comments explain WHY, not WHAT

### Testing
- [ ] Manual testing completed
- [ ] Automated tests added/updated (if applicable)
- [ ] All tests pass

### Documentation
- [ ] Code comments for complex logic
- [ ] README updated (if behavior changed)
- [ ] i18n translations added (if applicable)
- [ ] Configuration documented (if needed)

### Git Hygiene
- [ ] Branch name follows convention
- [ ] Commits are atomic and focused
- [ ] Commit messages follow Conventional Commits
- [ ] PR description is clear and complete
- [ ] Issue is properly linked (Fixes #N)

### Collaboration
- [ ] Todo list was maintained throughout
- [ ] User was kept informed of progress
- [ ] Ambiguities were clarified before coding
- [ ] PR URL was provided to user

## Common Mistakes to Avoid

### ❌ The Shotgun Fix
**Mistake**: Changing many files hoping one fixes the bug.
**Solution**: Use @explorer to understand the codebase first. Make targeted changes.

### ❌ Ghost Fixes
**Mistake**: Fixing without reproduction or tests.
**Solution**: Always create a test case or reproduction first (Red-Green-Refactor).

### ❌ Dirty PRs
**Mistake**: Including unrelated changes (formatting, other fixes).
**Solution**: Keep PRs focused. Use `git add <specific-files>`, not `git add .`.

### ❌ Vague Descriptions
**Mistake**: PR description says "Fixes bug" with no details.
**Solution**: Use the PR template. Explain WHAT, WHY, and HOW.

### ❌ Assumption-Driven Development
**Mistake**: Making assumptions about vague issues.
**Solution**: Ask for clarification. Comment on the issue if unclear.

### ❌ Skipping Research
**Mistake**: Implementing without checking docs or examples.
**Solution**: Use @librarian for library integrations. Research before coding.

### ❌ Configuration Oversights
**Mistake**: Forgetting to configure services (like email for password reset).
**Solution**: Check for required configuration. Add TODO comments for production.

## Example: Complete Fix Flow

Here's how the workflow looked for fixing issue #3 (forgot password 404):

### 1. Understand (Phase 1)
```bash
gh issue view 3
# Output: "忘记密码 404"
```

**Analysis**:
- Issue type: Feature (missing functionality)
- Problem: /forgot-password route returns 404
- Root cause: Page doesn't exist

### 2. Explore (Phase 1)
Used @explorer to find:
- Login page has link to /forgot-password
- Directory exists but is empty (no page.tsx)
- Auth library is better-auth

### 3. Research (Phase 1)
Used @librarian to understand:
- better-auth has requestPasswordReset() method
- Requires sendResetPassword callback in auth.ts
- Need both forgot-password and reset-password pages

### 4. Plan (Phase 2)
Created todo list:
1. Create new branch
2. Create forgot-password page
3. Create reset-password page
4. Configure auth.ts callback
5. Add translations
6. Commit and push
7. Create PR

### 5. Implement (Phase 3-4)
- Created branch: `fix/forgot-password-404`
- Implemented forgot-password page with form
- Implemented reset-password page with token handling
- Added sendResetPassword callback (console.log for dev)
- Added translations for en, zh, th

### 6. Verify (Phase 5)
- Checked LSP diagnostics (fixed method name error)
- Verified all pages render correctly
- Tested happy path flow

### 7. Commit (Phase 6)
```
feat(auth): implement forgot password and reset password flow

- Add /forgot-password page with email input form
- Add /reset-password page with new password form
- Configure auth.ts with sendResetPassword callback
- Add i18n translations (en, zh, th)

Fixes #3
```

### 8. PR (Phase 7)
Created PR with:
- Clear summary
- Bullet points of changes
- Testing instructions
- Production setup notes
- Link to issue: "Fixes #3"

**Result**: Complete, tested, documented fix merged successfully.

## Delegation Strategy

This skill coordinates multiple specialists:

### Use @explorer when:
- Need to discover related files
- Finding similar implementations
- Understanding codebase structure
- Locating configuration files

### Use @librarian when:
- Integrating third-party libraries
- Understanding API methods
- Finding implementation examples
- Checking documentation

### Use @designer when:
- Issue involves UI/UX
- Need responsive layouts
- Creating user-facing forms
- Ensuring visual consistency

### Use @fixer when:
- Have 3+ independent parallel tasks
- Clear specifications for each task
- Can split implementation work

## Success Metrics

A successful fix achieves:

1. **Issue Resolution**: Original problem is completely solved
2. **No Regressions**: Existing functionality still works
3. **Code Quality**: Maintainable, readable, follows conventions
4. **Documentation**: Future developers understand the change
5. **Clean History**: Clear commits and PR description
6. **Fast Merge**: Minimal back-and-forth in review

## Continuous Improvement

After each fix:
- Reflect on what went well
- Note any repeated patterns
- Update this skill if process gaps are found
- Share learnings with the team

---

**Remember**: A good fix is not just about making the code work. It's about making the codebase better, the team more productive, and the project more maintainable.

**Credits**: This skill synthesizes methodologies from:
- Kent Beck (Test-Driven Development)
- Martin Fowler (Refactoring)
- GitHub Flow (Branch-based workflow)
- Google Engineering Practices (Code review standards)
- Conventional Commits (Commit message format)
