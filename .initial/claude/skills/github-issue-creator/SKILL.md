---
name: github-issue-creator
description: Create high-quality, detailed GitHub issues from user input. Use this skill when the user wants to report a bug, request a feature, or create any type of GitHub issue. This skill transforms vague descriptions into structured, actionable issues following industry best practices from Joel Spolsky, Jeff Atwood, and open source maintainer standards.
---

# GitHub Issue Creator

Transform vague problem descriptions into high-quality, actionable GitHub issues using proven methodologies from Joel Spolsky (Painless Bug Tracking), Jeff Atwood (Complaint-Driven Development), and Simon Tatham (How to Report Bugs Effectively).

## When to Use This Skill

Trigger this skill when the user wants to:
- **Report a bug**: "Create an issue for the login bug"
- **Request a feature**: "Write an issue for adding dark mode"
- **Propose enhancement**: "Create issue for improving dashboard performance"
- **Document problem**: "I found a bug, help me write an issue"
- **Quick report**: "创建一个 issue：忘记密码功能404"

Do NOT trigger for:
- Fixing existing issues (use github-issue-fixer skill)
- General questions about the project
- Discussion topics (use GitHub Discussions instead)

## Core Philosophy

This skill embodies three proven methodologies:

### 1. Joel Spolsky's Painless Bug Tracking
**Three Essential Elements**: Every bug report needs:
1. Steps to reproduce
2. What you expected to see
3. What you saw instead

**Golden Rule**: "A bug report is a test case waiting to happen."

### 2. Jeff Atwood's Complaint-Driven Development
**Key Insight**: Don't "solutioneer" - describe the visible failure, not your theory of the root cause.

**Advice**: Report symptoms, not diagnoses. Let developers investigate.

### 3. Simon Tatham's Effective Bug Reporting
**Core Concept**: "Show, don't tell."

**Principle**: Specific, observable facts beat vague descriptions.

## The Issue Creation Workflow

Follow these phases to create a high-quality issue.

### Phase 1: Understand the Problem (CRITICAL)

**Goal**: Extract complete information from the user's description.

1. **Classify Issue Type**
   Determine what kind of issue this is:
   - **Bug**: Something is broken or behaves incorrectly
   - **Feature**: New functionality is needed
   - **Enhancement**: Existing functionality needs improvement
   - **Documentation**: Docs are missing or unclear
   - **Question**: Need clarification (suggest Discussion instead)

2. **Extract Key Information**
   
   **For Bugs**:
   - What were you trying to do?
   - What steps did you take?
   - What did you expect to happen?
   - What actually happened?
   - When did this start? (always? after update?)
   - Can you reproduce it consistently?
   
   **For Features**:
   - What problem are you trying to solve?
   - Who would benefit from this?
   - How do you imagine it working?
   - Have you seen this elsewhere?
   - What's the business value?
   
   **For Enhancements**:
   - What's the current behavior?
   - What's the problem with it?
   - How should it be improved?
   - What's the expected benefit?

3. **Identify Missing Information**
   If the user's description is vague, ask clarifying questions:
   - "Can you describe the exact steps to reproduce this?"
   - "What error message did you see?"
   - "What browser/OS are you using?"
   - "Can you provide a screenshot?"

4. **Explore Context** (Use @explorer)
   Before writing the issue, understand the codebase:
   - Does this feature/component already exist?
   - Are there related issues?
   - What files/modules are involved?
   
   ```
   Use @explorer to:
   - Search for related files
   - Find similar implementations
   - Identify affected components
   ```

5. **Avoid the XY Problem**
   If the user is asking for a specific solution, probe for the underlying problem:
   - ❌ User: "Add a button to clear cache"
   - ✅ Ask: "What problem are you experiencing that needs cache clearing?"
   - ✅ Real issue: "I see stale data after updating my profile"

### Phase 2: Structure the Issue

**Goal**: Organize information into a clear, actionable format.

1. **Draft a Clear Title**
   
   **Format**: `[Type] Specific, observable problem or feature`
   
   **Good Titles**:
   - ✅ "Bug: Login fails with 403 when password contains special characters"
   - ✅ "Feature: Add dark mode toggle to settings page"
   - ✅ "Enhancement: Improve dashboard load time for large datasets"
   
   **Poor Titles**:
   - ❌ "It's broken"
   - ❌ "Fix bug"
   - ❌ "Add feature"
   - ❌ "Help!"
   
   **Title Guidelines**:
   - 50-80 characters ideal
   - Start with issue type (Bug/Feature/Enhancement)
   - Be specific and observable
   - Include key context (component, error, action)

2. **Choose the Right Template**
   
   Select the appropriate structure based on issue type:

   **A. Bug Report Template**
   ```markdown
   ## Bug Description
   [Clear, concise description of the bug]
   
   ## Steps to Reproduce
   1. Go to [page/component]
   2. Click on [button/element]
   3. Enter [data/input]
   4. Observe [unexpected behavior]
   
   ## Expected Behavior
   [What should happen]
   
   ## Actual Behavior
   [What actually happens]
   
   ## Environment
   - **OS**: [e.g., macOS Sonoma 14.2]
   - **Browser**: [e.g., Chrome 120.0]
   - **App Version**: [e.g., v2.1.0]
   - **Device**: [e.g., Desktop, iPhone 15]
   
   ## Screenshots / Logs
   [Attach visual evidence or error logs]
   
   ## Additional Context
   - First noticed: [when did this start?]
   - Frequency: [always / sometimes / rarely]
   - Workaround: [any temporary solution?]
   
   ## Possible Solution (Optional)
   [If you have insights, share them - but focus on symptoms first]
   ```
   
   **B. Feature Request Template**
   ```markdown
   ## Feature Summary
   [One-sentence description of the feature]
   
   ## Problem / Motivation
   **As a** [type of user]
   **I want to** [action/capability]
   **So that** [benefit/value]
   
   ### Current Situation
   [What's the current state? What's missing?]
   
   ### Pain Points
   - [Specific problem 1]
   - [Specific problem 2]
   
   ## Proposed Solution
   [How you envision this working]
   
   ### User Flow
   1. User does [action]
   2. System responds with [behavior]
   3. User sees [result]
   
   ### UI/UX Mockup (Optional)
   [Sketch, wireframe, or description of interface]
   
   ## Alternatives Considered
   [Other ways to solve this - why did you reject them?]
   
   ## Success Criteria
   - [ ] [Measurable outcome 1]
   - [ ] [Measurable outcome 2]
   
   ## Additional Context
   - **Priority**: [High / Medium / Low]
   - **Impact**: [How many users affected?]
   - **Examples**: [Similar features in other apps]
   ```
   
   **C. Enhancement Template**
   ```markdown
   ## Enhancement Summary
   [What needs to be improved]
   
   ## Current Behavior
   [How it works now]
   
   ## Problems with Current Approach
   - [Issue 1]
   - [Issue 2]
   
   ## Proposed Improvement
   [How it should work instead]
   
   ### Benefits
   - [Benefit 1]
   - [Benefit 2]
   
   ### Implementation Ideas (Optional)
   [Technical suggestions if you have them]
   
   ## Success Metrics
   [How will we know this is better?]
   - Performance: [e.g., 50% faster load time]
   - UX: [e.g., 2 fewer clicks]
   - Maintainability: [e.g., less code complexity]
   ```

3. **Add Rich Context**
   
   Enhance the issue with:
   
   **Visual Evidence**:
   - Screenshots showing the problem
   - Screen recordings of reproduction steps
   - Before/after mockups for features
   - Error messages (formatted as code blocks)
   
   **Technical Details**:
   - Error stack traces (sanitized!)
   - Console logs
   - Network request/response
   - Browser DevTools output
   
   **Environment Info**:
   - OS version
   - Browser/app version
   - Screen size (for UI bugs)
   - Network conditions (for performance issues)

4. **Ensure Actionability**
   
   The "Definition of Ready" - a developer should be able to:
   - ✅ Understand the problem without asking questions
   - ✅ Reproduce the bug (if applicable)
   - ✅ Know when the issue is resolved
   - ✅ Estimate effort required
   
   **Checklist**:
   - [ ] Title is specific and clear
   - [ ] Type is identified (Bug/Feature/Enhancement)
   - [ ] Problem is well-described
   - [ ] Steps to reproduce are included (for bugs)
   - [ ] Expected vs actual behavior is clear
   - [ ] Environment details are provided
   - [ ] Visual evidence is attached (if applicable)
   - [ ] Success criteria are defined

### Phase 3: Enhance with Research

**Goal**: Add valuable context from the codebase and documentation.

1. **Search for Related Issues**
   ```bash
   gh issue list --search "keyword"
   ```
   
   Check if:
   - This issue already exists (avoid duplicates)
   - There are related issues to reference
   - Similar problems have been reported
   
   If duplicates exist:
   - Link to the existing issue
   - Add your unique context as a comment instead

2. **Find Relevant Code** (Use @explorer)
   ```
   Ask @explorer to:
   - Locate the affected component/file
   - Find related functionality
   - Identify potential impact areas
   ```
   
   Add to issue:
   ```markdown
   ## Affected Components
   - `src/app/(auth)/login/page.tsx` - Login form
   - `src/lib/auth.ts` - Authentication logic
   ```

3. **Check Documentation** (Use @librarian if library-related)
   ```
   If the issue involves a library:
   - Check if this is expected behavior
   - Look for known issues in library docs
   - Find relevant API documentation
   ```
   
   Add to issue:
   ```markdown
   ## References
   - [Library docs on authentication](https://...)
   - [Related API documentation](https://...)
   ```

### Phase 4: Format with Markdown

**Goal**: Make the issue scannable and professional.

1. **Use Markdown Formatting**
   
   ```markdown
   # Headers for major sections
   ## Sub-headers for subsections
   
   **Bold** for emphasis
   *Italic* for subtle emphasis
   
   `inline code` for variable names, file names
   
   ```code blocks for logs and code```
   
   - Bullet lists for options
   1. Numbered lists for steps
   
   > Blockquotes for important notes
   
   [Links](https://...) for references
   
   ![Images](url) for screenshots
   ```

2. **Structure for Scannability**
   
   - Use headers to create clear sections
   - Keep paragraphs short (3-4 lines max)
   - Use lists instead of long paragraphs
   - Add blank lines between sections
   - Use code blocks for technical content

3. **Sanitize Sensitive Data**
   
   ⚠️ **CRITICAL**: Before including logs or screenshots:
   - Remove API keys and tokens
   - Redact passwords
   - Hide internal IP addresses
   - Mask email addresses (if sensitive)
   - Remove company-specific data
   
   ```markdown
   ❌ BAD:
   Authorization: Bearer sk_live_abc123xyz...
   
   ✅ GOOD:
   Authorization: Bearer [REDACTED]
   ```

### Phase 5: Add Metadata

**Goal**: Help with triage and prioritization.

1. **Suggest Labels**
   
   Based on issue type and content:
   - **Type**: `bug`, `feature`, `enhancement`, `documentation`
   - **Component**: `auth`, `dashboard`, `api`, `ui`
   - **Priority**: `high`, `medium`, `low`
   - **Status**: `needs-triage`, `needs-reproduction`, `needs-design`
   - **Effort**: `good-first-issue`, `help-wanted`
   
   ```markdown
   ## Suggested Labels
   - `bug`
   - `auth`
   - `needs-reproduction`
   ```

2. **Estimate Priority** (if clear)
   
   **High Priority**:
   - Security vulnerabilities
   - Data loss bugs
   - Complete feature breakage
   - Blocking issues
   
   **Medium Priority**:
   - Significant UX problems
   - Performance issues
   - Missing key features
   
   **Low Priority**:
   - Minor UI glitches
   - Nice-to-have features
   - Edge cases

3. **Identify Affected Users**
   
   ```markdown
   ## Impact
   - **Severity**: [Critical / High / Medium / Low]
   - **Affected Users**: [All users / Specific user group / Edge case]
   - **Frequency**: [Always / Often / Sometimes / Rarely]
   ```

### Phase 6: Review and Refine

**Goal**: Ensure the issue meets quality standards.

1. **Self-Review Checklist**
   
   **Clarity**:
   - [ ] Title is specific and descriptive
   - [ ] Problem is clearly stated
   - [ ] No jargon or assumptions
   
   **Completeness**:
   - [ ] All required sections filled
   - [ ] Evidence provided (screenshots/logs)
   - [ ] Environment details included
   
   **Actionability**:
   - [ ] Developer can start work immediately
   - [ ] Success criteria are clear
   - [ ] No follow-up questions needed
   
   **Professionalism**:
   - [ ] Tone is collaborative, not demanding
   - [ ] Formatting is clean and scannable
   - [ ] Sensitive data is sanitized

2. **Apply Quality Criteria**
   
   Compare against the "Good vs Poor" standard:
   
   | Aspect | Poor | Good |
   |--------|------|------|
   | **Title** | "It's broken" | "Login fails with 403 on special chars" |
   | **Reproduction** | "Sometimes happens" | "Consistent with steps 1-4" |
   | **Context** | "App crashed" | "Crashed after clicking Save on Profile" |
   | **Evidence** | None | Stack trace + screenshot |
   | **Tone** | "Fix this now!" | "Happy to help test the fix" |

3. **Improve Weak Areas**
   
   If any section is weak:
   - Ask user for more details
   - Use @explorer to add code context
   - Use @librarian to add documentation links
   - Enhance with research findings

### Phase 7: Create the Issue

**Goal**: Submit the issue to GitHub.

1. **Present Draft to User**
   
   Show the complete issue draft:
   ```markdown
   Here's the issue I've drafted:
   
   ---
   
   [FULL ISSUE CONTENT]
   
   ---
   
   Does this accurately capture the problem? Any changes needed?
   ```

2. **Iterate if Needed**
   
   If user requests changes:
   - Update the relevant sections
   - Re-present for approval
   - Don't create until user confirms

3. **Create the Issue**
   
   ```bash
   gh issue create --title "[Title]" --body "[Body]"
   ```
   
   Or if labels are needed:
   ```bash
   gh issue create \
     --title "[Title]" \
     --body "[Body]" \
     --label "bug,auth,needs-triage"
   ```

4. **Return Issue URL**
   
   Provide the issue URL to the user:
   ```
   ✅ Issue created successfully!
   
   🔗 https://github.com/owner/repo/issues/123
   
   You can track progress and add comments at the link above.
   ```

## Quality Standards

### The "Definition of Ready"

An issue is ready when a developer can:
1. ✅ Understand the problem without clarification
2. ✅ Reproduce the bug (if applicable)
3. ✅ Know the success criteria
4. ✅ Estimate the effort
5. ✅ Start working immediately

### Quality Checklist

Before creating the issue, verify:

**Content Quality**:
- [ ] Title is specific (50-80 chars)
- [ ] Type is clearly identified
- [ ] Problem is well-described
- [ ] Context is sufficient
- [ ] Evidence is provided

**For Bugs**:
- [ ] Reproduction steps are detailed
- [ ] Expected vs actual behavior is clear
- [ ] Environment details are complete
- [ ] Error messages are included

**For Features**:
- [ ] Motivation is explained (Why?)
- [ ] User story is provided (As a... I want... So that...)
- [ ] Success criteria are defined
- [ ] Alternatives are considered

**Formatting**:
- [ ] Markdown is properly used
- [ ] Sections are well-organized
- [ ] Content is scannable
- [ ] Code/logs use code blocks

**Safety**:
- [ ] No API keys or tokens
- [ ] No passwords
- [ ] No sensitive data
- [ ] Logs are sanitized

**Metadata**:
- [ ] Appropriate labels suggested
- [ ] Priority is indicated (if clear)
- [ ] Impact is described

## Common Mistakes to Avoid

### ❌ The XY Problem
**Mistake**: Asking for a specific solution instead of describing the problem.

**Example**:
- ❌ "Add a button to clear cache"
- ✅ "I see stale data after updating my profile"

**Solution**: Always extract the underlying problem first.

### ❌ "It Doesn't Work"
**Mistake**: Vague statements without specifics.

**Example**:
- ❌ "Login is broken"
- ✅ "Login fails with 403 error when password contains @ symbol"

**Solution**: Probe for specific, observable facts.

### ❌ Missing Reproduction Steps
**Mistake**: Assuming the developer knows how to trigger the bug.

**Example**:
- ❌ "The app crashes sometimes"
- ✅ "App crashes when clicking Save after entering >100 characters in bio field"

**Solution**: Always include step-by-step reproduction.

### ❌ No Environment Details
**Mistake**: Reporting bugs without version/platform info.

**Example**:
- ❌ "Button is misaligned"
- ✅ "Button is misaligned on mobile Safari iOS 17.2, iPhone 14"

**Solution**: Always include OS, browser, app version.

### ❌ The Wall of Text
**Mistake**: Writing paragraphs without formatting.

**Solution**: Use headers, lists, and code blocks.

### ❌ Solutioneering
**Mistake**: Diagnosing the code instead of reporting symptoms.

**Example**:
- ❌ "The auth token variable is null"
- ✅ "I get logged out immediately after logging in"

**Solution**: Report what you see, not what you think is wrong.

### ❌ Demanding Tone
**Mistake**: Being aggressive or entitled.

**Example**:
- ❌ "Fix this NOW! This is unacceptable!"
- ✅ "This is blocking my work. Happy to provide more details or help test."

**Solution**: Be collaborative and respectful.

## Specialist Delegation

### Use @explorer when:
- Need to find affected files/components
- Looking for related issues
- Understanding codebase structure
- Identifying impact areas

### Use @librarian when:
- Issue involves a third-party library
- Need to check if behavior is expected
- Looking for official documentation
- Understanding API usage

### Use @designer when:
- Feature request involves UI/UX
- Need mockups or wireframes
- Discussing visual design
- Proposing interface changes

## Advanced Features

### For Complex Issues

1. **Break Down Large Issues**
   
   If the issue is too large:
   - Create a parent "Epic" issue
   - Break into smaller sub-issues
   - Link them with task lists:
   
   ```markdown
   ## Implementation Tasks
   - [ ] #123 - Create login form
   - [ ] #124 - Add validation logic
   - [ ] #125 - Integrate with backend
   ```

2. **Add Acceptance Criteria**
   
   For features, define clear acceptance:
   ```markdown
   ## Acceptance Criteria
   - [ ] User can click dark mode toggle
   - [ ] Theme persists across sessions
   - [ ] All components support dark mode
   - [ ] Accessible (WCAG 2.1 AA)
   ```

3. **Include Technical Context**
   
   If you have technical insights:
   ```markdown
   ## Technical Notes
   - Likely related to the `validatePassword` function in `src/lib/auth.ts`
   - May need to update regex pattern to allow special characters
   - Should check if backend API also needs updating
   ```

### For Urgent Issues

If the issue is critical:

1. **Mark as High Priority**
   ```markdown
   ## ⚠️ URGENT - Production Issue
   
   **Severity**: Critical
   **Impact**: All users unable to log in
   **Started**: 2026-01-30 10:30 UTC
   ```

2. **Add Workaround** (if known)
   ```markdown
   ## Temporary Workaround
   Users can log in by:
   1. Clearing browser cache
   2. Using incognito mode
   ```

3. **Tag Relevant People** (if appropriate)
   ```markdown
   @team-lead @security-team - This affects authentication
   ```

## Examples

### Example 1: Bug Report

**User Input**: "忘记密码功能404"

**Created Issue**:

```markdown
# Bug: Forgot password page returns 404 error

## Bug Description
When users click "Forgot password?" on the login page, they are redirected to `/forgot-password` which returns a 404 error. This prevents users from resetting their passwords.

## Steps to Reproduce
1. Go to the login page at `/login`
2. Click on "Forgot password?" link
3. Observe 404 error page

## Expected Behavior
- User should see a forgot password form
- User should be able to enter their email
- User should receive a password reset link

## Actual Behavior
- 404 error page is displayed
- No forgot password functionality available

## Environment
- **App Version**: Current main branch
- **Browser**: All browsers
- **Route**: `/forgot-password`

## Screenshots
[Screenshot of 404 error page]

## Additional Context
- The login page has a link to `/forgot-password`
- The route exists in the directory structure but has no `page.tsx`
- This is a missing feature rather than a broken one

## Affected Components
- `src/app/(auth)/login/page.tsx` - Contains the link
- `src/app/(auth)/forgot-password/` - Empty directory

## Suggested Labels
- `bug`
- `auth`
- `missing-feature`
- `high-priority`

## Impact
- **Severity**: High
- **Affected Users**: All users who forget their password
- **Frequency**: Always
```

### Example 2: Feature Request

**User Input**: "We need dark mode"

**Created Issue**:

```markdown
# Feature: Add dark mode support

## Feature Summary
Add a dark mode theme option that users can toggle in settings.

## Problem / Motivation
**As a** user who works in low-light environments
**I want to** switch the app to dark mode
**So that** I can reduce eye strain and save battery on OLED screens

### Current Situation
The app only supports light mode, which can be harsh on the eyes in dark environments.

### Pain Points
- Bright white backgrounds cause eye strain at night
- No way to customize the theme
- Battery drain on mobile devices with OLED screens

## Proposed Solution
Add a dark mode toggle in the user settings page.

### User Flow
1. User navigates to Settings
2. User sees "Theme" section with options: Light / Dark / System
3. User selects "Dark"
4. App immediately switches to dark theme
5. Preference is saved and persists across sessions

### UI/UX Mockup
- Toggle switch in Settings page
- All components adapt to dark theme
- Smooth transition animation (0.3s)

## Alternatives Considered
1. **Auto dark mode based on time**: Rejected because users should have control
2. **Multiple themes**: Rejected for v1 to keep scope manageable
3. **Browser preference only**: Rejected because users may want different settings per device

## Success Criteria
- [ ] User can toggle dark mode in settings
- [ ] Theme persists across browser sessions
- [ ] All components support dark mode
- [ ] Accessible contrast ratios (WCAG 2.1 AA)
- [ ] Smooth transition between themes

## Additional Context
- **Priority**: Medium
- **Impact**: Would benefit all users, especially mobile users
- **Examples**: 
  - GitHub's dark mode implementation
  - Twitter's theme switcher

## Technical Notes
- Consider using CSS variables for theme colors
- May need to update all component styles
- Should integrate with next-themes library

## Suggested Labels
- `feature`
- `ui`
- `enhancement`
- `good-first-issue` (for basic implementation)
```

## Success Metrics

A high-quality issue achieves:

1. **Fast Triage**: Maintainer can prioritize in <2 minutes
2. **No Clarification Needed**: Developer can start work immediately
3. **Clear Success**: Everyone knows when issue is resolved
4. **Collaborative Tone**: Encourages team participation

## Continuous Improvement

After creating issues:
- Note which sections needed most clarification
- Track which issues got implemented fastest
- Learn from maintainer feedback
- Update this skill based on patterns

---

**Remember**: A good issue is a gift to the development team. It saves time, prevents misunderstandings, and moves the project forward. Invest time in creating quality issues - it pays dividends.

**Credits**: This skill synthesizes methodologies from:
- Joel Spolsky (Painless Bug Tracking)
- Jeff Atwood (Complaint-Driven Development)
- Simon Tatham (How to Report Bugs Effectively)
- GitHub's issue template best practices
- Open source maintainer guidelines
