# GitHub Issue Fixer - Real Examples

This document shows real-world examples of how the skill works in practice.

## Example 1: Missing Feature (Issue #3)

### Issue Description
```
Title: 忘记密码 404
Body: 忘记密码 404
```

### User Input
```
"创建一个新的分支，然后再创建一个PR，然后自动修复3号问题。github上面的。"
```

### Skill Execution

#### Phase 1: Understand
1. **Fetched issue**: `gh issue view 3`
2. **Analysis**:
   - Type: Feature (missing functionality)
   - Problem: /forgot-password returns 404
   - Root cause: Page doesn't exist

3. **Exploration** (via @explorer):
   - Found login page linking to /forgot-password
   - Found empty directory: src/app/(auth)/forgot-password/
   - Identified auth library: better-auth

4. **Research** (via @librarian):
   - Method: `authClient.requestPasswordReset()`
   - Required: `sendResetPassword` callback in auth.ts
   - Flow: request → email → reset page

#### Phase 2: Plan
Created todo list:
```
1. Create branch fix-forgot-password-404
2. Stash uncommitted changes
3. Create forgot-password page
4. Create reset-password page
5. Configure auth.ts callback
6. Add translations (en, zh, th)
7. Commit and push
8. Create PR
```

#### Phase 3: Prepare
```bash
git stash push -m "Temp stash before fix-forgot-password branch"
git checkout -b fix-forgot-password-404
```

#### Phase 4: Implement
Created files:
1. `src/app/(auth)/forgot-password/page.tsx`
   - Email input form
   - Success state with instructions
   - Error handling

2. `src/app/(auth)/reset-password/page.tsx`
   - Token validation from URL
   - New password form with confirmation
   - Password strength requirements
   - Success/error states

3. Updated `src/lib/auth.ts`:
   ```typescript
   emailAndPassword: {
     enabled: true,
     autoSignIn: true,
     sendResetPassword: async ({ user, url, token }, request) => {
       // Console log for dev, TODO for production
       console.log("Password reset:", url)
     }
   }
   ```

4. Added translations to:
   - `messages/en.json`
   - `messages/zh.json`
   - `messages/th.json`

#### Phase 5: Test
- ✅ LSP diagnostics: Fixed method name error (forgetPassword → requestPasswordReset)
- ✅ Manual test: Form renders correctly
- ✅ Flow test: Email → reset link → new password

#### Phase 6: Commit
```bash
git add messages/ src/lib/auth.ts src/app/(auth)/forgot-password/ src/app/(auth)/reset-password/
git commit -m "feat(auth): implement forgot password and reset password flow

- Add /forgot-password page with email input form
- Add /reset-password page with new password form
- Configure auth.ts with sendResetPassword callback
- Add i18n translations (en, zh, th)

Fixes #3"
```

#### Phase 7: PR
```bash
git push -u origin fix-forgot-password-404
gh pr create --title "Fix: Implement forgot password and reset password functionality (Fixes #3)" --body "..."
```

**Result**: https://github.com/minliacom/wealth/pull/5

### Metrics
- **Time**: ~15 minutes
- **Files changed**: 6
- **Lines added**: 434
- **Commits**: 1 (clean, atomic)
- **Tests**: Manual verification
- **Documentation**: PR description, code comments, translations

### What Made This Fix High Quality

1. **Complete Understanding**
   - Used @explorer to map the codebase
   - Used @librarian to research better-auth API
   - Understood the full flow before coding

2. **Comprehensive Implementation**
   - Both pages (forgot + reset)
   - Configuration (sendResetPassword)
   - All translations (en, zh, th)
   - Error handling and edge cases

3. **Clean Git History**
   - Single, focused commit
   - Clear Conventional Commits format
   - Proper issue linking

4. **Excellent PR**
   - Summary of changes
   - How it works
   - Testing instructions
   - Production setup notes
   - Properly linked issue

## Example 2: Bug Fix (Hypothetical)

### Issue Description
```
Title: Login timeout after 5 minutes
Body: Users are logged out after 5 minutes of inactivity, but session should last 7 days.
```

### Skill Execution Flow

#### Phase 1: Understand
1. Fetch issue
2. Classify: Bug (incorrect behavior)
3. Expected: 7 days session
4. Actual: 5 minutes timeout
5. Explore: Find session configuration

#### Phase 2: Plan
```
1. Create branch fix/123/login-timeout
2. Find session config in auth.ts
3. Update session expiry
4. Test session persistence
5. Commit with fix message
6. Create PR
```

#### Phase 3-4: Implement
```typescript
// src/lib/auth.ts
session: {
  expiresIn: 60 * 60 * 24 * 7, // Changed from 60 * 5
  updateAge: 60 * 60 * 24,
}
```

#### Phase 5: Test
- Verify session lasts 7 days
- Check cookie expiration
- Test "remember me" behavior

#### Phase 6: Commit
```
fix(auth): correct session expiry to 7 days

Session was incorrectly set to 5 minutes (300 seconds)
instead of 7 days (604800 seconds). Updated expiresIn
to match product requirements.

Fixes #123
```

#### Phase 7: PR
**Title**: `Fix: Correct session expiry to 7 days (Fixes #123)`

**Body**:
```markdown
## Summary
Fixes session timeout bug where users were logged out after 5 minutes.

## Root Cause
The `session.expiresIn` value was set to `60 * 5` (5 minutes)
instead of `60 * 60 * 24 * 7` (7 days).

## Changes
- ✅ Updated `src/lib/auth.ts` session configuration
- ✅ Changed `expiresIn` from 300s to 604800s

## Testing
1. Log in to the application
2. Wait 10 minutes (previously would log out)
3. Verify session is still active
4. Check cookie expiration in DevTools

## Closes
Fixes #123
```

## Example 3: Feature Enhancement (Hypothetical)

### Issue Description
```
Title: Add CSV export for transactions
Body: Users need to export their transactions as CSV for accounting software.
```

### Skill Execution Flow

#### Phase 1: Understand
1. Feature type: Enhancement
2. Requirements: Export transactions to CSV
3. Research: Check for existing export functionality
4. Explore: Find transaction data model

#### Phase 2: Plan
```
1. Create branch feature/42/csv-export
2. Create CSV export utility function
3. Add export button to transactions page
4. Implement download logic
5. Add loading state
6. Add translations
7. Write tests
8. Commit and PR
```

#### Phase 3-4: Implement
Files created/modified:
- `src/lib/csv-export.ts` (utility)
- `src/app/(dashboard)/transactions/page.tsx` (UI)
- `messages/*.json` (translations)

#### Phase 5: Test
- Export with 0 transactions
- Export with 1 transaction
- Export with 1000 transactions
- Verify CSV format
- Test in Excel/Google Sheets

#### Phase 6: Commit
```
feat(transactions): add CSV export functionality

- Create CSV export utility with proper escaping
- Add export button to transactions page
- Include all transaction fields in export
- Add loading state during export
- Add i18n translations

Fixes #42
```

#### Phase 7: PR
Complete PR with screenshots of the export button and sample CSV file.

## Comparison: Before vs After

### Before (Manual Process)
1. ❌ Read issue (5 min)
2. ❌ Google for solutions (15 min)
3. ❌ Start coding without plan (10 min)
4. ❌ Hit library API issues (20 min)
5. ❌ Realize need translations (10 min)
6. ❌ Debug and fix errors (15 min)
7. ❌ Write vague commit message (2 min)
8. ❌ Create minimal PR (5 min)
9. ❌ Back-and-forth in review (30 min)

**Total**: ~2 hours, multiple iterations

### After (With Skill)
1. ✅ Systematic understanding (3 min)
2. ✅ Automated research (@librarian, 2 min)
3. ✅ Clear plan with todos (2 min)
4. ✅ Guided implementation (5 min)
5. ✅ Quality checks built-in (1 min)
6. ✅ Proper commit message (1 min)
7. ✅ Comprehensive PR (1 min)
8. ✅ Fast merge (minimal review needed)

**Total**: ~15 minutes, one iteration

## Key Takeaways

### What Makes Fixes High Quality
1. **Complete understanding** before coding
2. **Research** for library integrations
3. **Planning** with clear todos
4. **Incremental** implementation with verification
5. **Clean** git history
6. **Comprehensive** PR descriptions

### Why This Skill Works
- **Systematic**: Never skip critical steps
- **Researched**: Uses @librarian for libraries
- **Tested**: LSP diagnostics + manual verification
- **Documented**: Clear commits and PRs
- **Complete**: Handles edge cases, i18n, config

### When to Use This Skill
- ✅ User provides issue number
- ✅ Issue is on GitHub
- ✅ You have write access to repo
- ✅ Issue is actionable and clear

### When NOT to Use
- ❌ Issue is vague (ask for clarification first)
- ❌ Requires architectural decisions (use @oracle)
- ❌ Just exploring the problem
- ❌ No GitHub issue exists yet

---

**Remember**: Quality fixes take the same time as rushed fixes, but they:
- Merge faster (less review back-and-forth)
- Cause fewer regressions
- Are easier to maintain
- Build team trust
