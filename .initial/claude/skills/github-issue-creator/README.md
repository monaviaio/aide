# GitHub Issue Creator Skill

Transform vague problem descriptions into high-quality, actionable GitHub issues following industry best practices.

## Installation

This skill is already installed at:
```
~/.claude/skills/github-issue-creator/
```

## Usage

Simply describe the problem or feature you want to report:

```
"Create an issue for the login bug"
"Write an issue: forgot password returns 404"
"创建一个 issue：需要添加暗黑模式"
"Help me report this bug: dashboard is slow"
```

Claude will:
1. ✅ Ask clarifying questions if needed
2. ✅ Research the codebase for context
3. ✅ Structure the information properly
4. ✅ Format with professional Markdown
5. ✅ Add relevant labels and metadata
6. ✅ Create the issue on GitHub
7. ✅ Provide the issue URL

## What Makes This Skill Different

### Industry Best Practices
- **Joel Spolsky**: Painless Bug Tracking (3 essential elements)
- **Jeff Atwood**: Complaint-Driven Development (report symptoms, not diagnoses)
- **Simon Tatham**: Effective Bug Reporting (show, don't tell)
- **GitHub**: Official issue template standards

### Complete Information Extraction
Most people write vague issues. This skill ensures:
- Specific, observable facts
- Clear reproduction steps (for bugs)
- Motivation and context (for features)
- Environment details
- Visual evidence

### Professional Formatting
Every issue includes:
- Clear, descriptive title
- Well-structured sections
- Markdown formatting
- Code blocks for logs
- Sanitized sensitive data

## Example: From Vague to Excellent

### User Input (Vague)
```
"忘记密码功能404"
```

### Created Issue (Excellent)
```markdown
# Bug: Forgot password page returns 404 error

## Bug Description
When users click "Forgot password?" on the login page, they are 
redirected to `/forgot-password` which returns a 404 error.

## Steps to Reproduce
1. Go to `/login`
2. Click "Forgot password?" link
3. Observe 404 error

## Expected Behavior
- User should see forgot password form
- User should be able to enter email
- User should receive reset link

## Actual Behavior
- 404 error page is displayed

## Environment
- **App Version**: Current main
- **Browser**: All browsers
- **Route**: `/forgot-password`

## Affected Components
- `src/app/(auth)/login/page.tsx`
- `src/app/(auth)/forgot-password/`

## Impact
- **Severity**: High
- **Affected Users**: All users
- **Frequency**: Always

## Suggested Labels
- `bug`, `auth`, `high-priority`
```

**Time**: 2-3 minutes (vs 15+ minutes manually)

## Issue Types Supported

### Bug Reports
Perfect for:
- Crashes and errors
- Unexpected behavior
- UI glitches
- Performance issues

Includes:
- Reproduction steps
- Expected vs actual behavior
- Environment details
- Error messages and logs

### Feature Requests
Perfect for:
- New functionality
- User stories
- Product improvements

Includes:
- Problem/motivation
- Proposed solution
- User flow
- Success criteria
- Alternatives considered

### Enhancements
Perfect for:
- Improving existing features
- Performance optimization
- UX improvements

Includes:
- Current behavior
- Problems with it
- Proposed improvements
- Success metrics

## Quality Standards

### The "Definition of Ready"
An issue is ready when a developer can:
- ✅ Understand without clarification
- ✅ Reproduce the bug (if applicable)
- ✅ Know the success criteria
- ✅ Estimate the effort
- ✅ Start working immediately

### Quality Checklist
Every issue includes:
- ✅ Specific title (50-80 chars)
- ✅ Clear problem description
- ✅ Reproduction steps (bugs)
- ✅ Motivation (features)
- ✅ Environment details
- ✅ Visual evidence
- ✅ Professional formatting
- ✅ Sanitized data
- ✅ Suggested labels

## Common Problems Solved

### Problem 1: Vague Descriptions
**Before**: "Login is broken"
**After**: "Login fails with 403 error when password contains @ symbol"

### Problem 2: Missing Context
**Before**: "App crashes"
**After**: "App crashes when clicking Save after entering >100 chars in bio"

### Problem 3: No Reproduction Steps
**Before**: "Sometimes it doesn't work"
**After**: Detailed 5-step reproduction with environment details

### Problem 4: Poor Formatting
**Before**: Wall of text
**After**: Structured sections with Markdown, code blocks, lists

### Problem 5: Solutioneering
**Before**: "The auth token variable is null"
**After**: "I get logged out immediately after logging in"

## Integration with Other Skills

### Works with github-issue-fixer
1. **Create issue** with this skill
2. **Fix issue** with github-issue-fixer skill
3. Complete workflow from problem to solution

### Uses Specialists
- **@explorer**: Find affected files and components
- **@librarian**: Check library documentation
- **@designer**: For UI/UX feature requests

## Configuration

No configuration needed! The skill:
- Detects your repository context
- Adapts to your issue templates
- Follows your labeling conventions
- Matches your project style

## Best Practices

### Before Creating
1. Search for existing issues (avoid duplicates)
2. Gather all relevant information
3. Take screenshots if applicable
4. Note environment details

### During Creation
1. Answer clarifying questions honestly
2. Provide specific examples
3. Include error messages
4. Be collaborative, not demanding

### After Creation
1. Monitor for maintainer questions
2. Provide additional context if asked
3. Test proposed fixes
4. Close issue when resolved

## Tips for Best Results

### Be Specific
❌ "It's broken"
✅ "Login fails with 403 when password has special chars"

### Show, Don't Tell
❌ "The button doesn't work"
✅ "Clicking Save button does nothing, no error shown"

### Report Symptoms, Not Diagnoses
❌ "The auth token is null"
✅ "I get logged out right after logging in"

### Provide Context
❌ "Dashboard is slow"
✅ "Dashboard takes 10s to load when I have >1000 transactions"

## Troubleshooting

### "Issue already exists"
The skill will find duplicates and suggest adding to existing issue instead.

### "Need more information"
The skill will ask clarifying questions - answer them for better issues.

### "Can't reproduce"
Provide more specific steps, environment details, or screenshots.

## Success Metrics

High-quality issues achieve:
- ✅ **Fast triage**: <2 min for maintainer to understand
- ✅ **No clarification**: Developer can start immediately
- ✅ **Clear success**: Everyone knows when it's done
- ✅ **Quick fix**: Better issues get fixed faster

## Real-World Impact

### For Users
- 🎯 Problems get fixed faster
- 💬 Better communication with team
- 📝 Professional issue reports
- 😌 Less back-and-forth

### For Maintainers
- ⚡ Faster triage
- 🎯 Clear priorities
- 📊 Better planning
- 😊 Happier community

### For Projects
- 📈 Higher quality issues
- 🔄 Faster resolution
- 📚 Better documentation
- 💪 Healthier backlog

## Methodology Sources

This skill is based on proven methodologies:

- **Painless Bug Tracking** (Joel Spolsky)
  - *Source*: Joel on Software blog
  - *Principle*: 3 essential elements for every bug

- **Complaint-Driven Development** (Jeff Atwood)
  - *Source*: Coding Horror blog
  - *Principle*: Report symptoms, not theories

- **How to Report Bugs Effectively** (Simon Tatham)
  - *Source*: chiark.greenend.org.uk
  - *Principle*: Show, don't tell

- **GitHub Issue Templates**
  - *Source*: GitHub official documentation
  - *Principle*: Structured, consistent reports

## Examples

See `EXAMPLES.md` for:
- Real bug reports
- Feature requests
- Enhancement proposals
- Before/after comparisons

## Quick Reference

See `QUICK_REFERENCE.md` for:
- Issue type decision tree
- Template quick lookup
- Common mistake fixes
- Formatting cheat sheet

---

**Created by**: Claude Code
**Methodology**: Joel Spolsky, Jeff Atwood, Simon Tatham, GitHub
**Companion to**: github-issue-fixer skill
