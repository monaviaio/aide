# GitHub Issue Creator - Real Examples

## Example 1: From Vague to Excellent Bug Report

### User Input (Vague)
```
"忘记密码功能404"
```

### Skill Process

**Step 1: Clarification**
```
I understand you're seeing a 404 error with the forgot password feature. 
Let me ask a few questions to create a detailed issue:

1. When do you see the 404? After clicking a link, or when typing the URL?
2. What page are you on when this happens?
3. Do you see any error messages besides 404?
```

**Step 2: User Response**
```
When I click "Forgot password?" on the login page, it goes to /forgot-password 
and shows 404. No other error messages.
```

**Step 3: Research** (via @explorer)
```
Found:
- src/app/(auth)/login/page.tsx has link to /forgot-password
- src/app/(auth)/forgot-password/ directory exists but is empty
- No page.tsx file in forgot-password directory
```

**Step 4: Draft Issue**

### Created Issue

```markdown
# Bug: Forgot password page returns 404 error

## Bug Description
When users click the "Forgot password?" link on the login page, they are redirected to `/forgot-password` which displays a 404 error page. This prevents users from accessing the password reset functionality.

## Steps to Reproduce
1. Navigate to the login page at `/login`
2. Locate and click the "Forgot password?" link below the password field
3. Observe the 404 error page

## Expected Behavior
- User should be redirected to a forgot password form
- Form should allow user to enter their email address
- User should receive a password reset link via email

## Actual Behavior
- Browser navigates to `/forgot-password`
- 404 error page is displayed
- No password reset functionality is available

## Environment
- **App Version**: Current production (main branch)
- **Browser**: All browsers (Chrome, Safari, Firefox)
- **Route**: `/forgot-password`
- **Reproducibility**: 100% - happens every time

## Root Cause Analysis
Upon investigation, the issue appears to be a missing implementation rather than a broken feature:
- The login page contains a link to `/forgot-password`
- The route directory `src/app/(auth)/forgot-password/` exists
- However, no `page.tsx` file exists in this directory
- This is a missing feature that needs to be implemented

## Affected Components
- **Frontend**: `src/app/(auth)/login/page.tsx` (line 155) - Contains the link
- **Missing**: `src/app/(auth)/forgot-password/page.tsx` - Needs to be created
- **Backend**: `src/lib/auth.ts` - May need password reset configuration

## Screenshots
![404 Error on Forgot Password Page](screenshot-404.png)
![Login Page with Forgot Password Link](screenshot-login-link.png)

## Impact Assessment
- **Severity**: High
- **Affected Users**: All users who forget their password
- **Frequency**: Always (100% reproduction rate)
- **Workaround**: None - users must contact support for password reset
- **Business Impact**: Poor user experience, increased support tickets

## Suggested Implementation
To fix this issue, the following components need to be created:
1. Forgot password page (`/forgot-password`) with email input form
2. Reset password page (`/reset-password`) with new password form
3. Email service configuration for sending reset links
4. Integration with authentication library's password reset flow

## Related Issues
- None found (this is a new issue)

## Suggested Labels
- `bug`
- `auth`
- `missing-feature`
- `high-priority`
- `user-experience`

## Additional Notes
This appears to be a planned feature that was not yet implemented. The directory structure suggests it was set up but the implementation was not completed.

---

**Reporter**: [Your Name]
**Date**: 2026-01-30
**Assigned to**: To be triaged
```

**Result**: ✅ Complete, actionable issue ready for development

---

## Example 2: Feature Request with Research

### User Input
```
"We need dark mode"
```

### Skill Process

**Step 1: Clarification**
```
I'd like to create a detailed feature request for dark mode. Let me ask:

1. Who would primarily use this feature?
2. What's the main problem you're trying to solve?
3. How do you envision it working? (toggle, auto-detect, etc.)
4. Have you seen dark mode implementations you like?
```

**Step 2: User Response**
```
All users would benefit, especially those working at night. 
I work late and the bright white screen hurts my eyes.
I'd like a toggle in settings, similar to GitHub's implementation.
```

**Step 3: Research** (via @librarian)
```
Checking next-themes library for dark mode implementation...
Found: next-themes is a popular solution for Next.js apps
```

### Created Issue

```markdown
# Feature: Add dark mode support with theme toggle

## Feature Summary
Add a dark mode theme option that users can toggle in the settings page, reducing eye strain for users working in low-light environments.

## Problem / Motivation

**As a** user who frequently works during evening hours  
**I want to** switch the application interface to a dark theme  
**So that** I can reduce eye strain and work more comfortably in low-light conditions

### Current Situation
The application currently only supports a light theme with bright white backgrounds and dark text. There is no way for users to customize the visual theme.

### Pain Points
- **Eye Strain**: Bright white backgrounds cause discomfort during extended use, especially in low-light environments
- **No Customization**: Users have no control over the application's appearance
- **Battery Drain**: Light themes consume more power on OLED screens (mobile devices)
- **Accessibility**: Some users with light sensitivity conditions struggle with bright interfaces

### User Impact
- **Primary Users**: All users, especially those working evenings/nights
- **Estimated Percentage**: 40-60% of users would benefit (based on industry data)
- **Use Cases**: Late-night work, dark office environments, light-sensitive users

## Proposed Solution

Add a theme toggle feature that allows users to switch between light and dark modes.

### User Flow

1. **Access Settings**
   - User navigates to Settings page
   - User sees a new "Appearance" or "Theme" section

2. **Select Theme**
   - Options displayed: Light / Dark / System (auto-detect)
   - User clicks their preferred option
   - App immediately applies the selected theme

3. **Persistence**
   - User's preference is saved to local storage
   - Theme persists across browser sessions
   - Theme syncs across devices (if user is logged in)

### UI/UX Design

**Settings Page Addition**:
```
┌─────────────────────────────────┐
│ Appearance                      │
├─────────────────────────────────┤
│ Theme                           │
│ ○ Light                         │
│ ● Dark                          │
│ ○ System (auto)                 │
└─────────────────────────────────┘
```

**Visual Specifications**:
- Toggle should be easily accessible
- Smooth transition animation (0.3s fade)
- Clear visual feedback when switching
- Icons: Sun (light), Moon (dark), Monitor (system)

### Technical Implementation (Suggested)

**Library**: Use `next-themes` package
```typescript
// Example implementation
import { ThemeProvider } from 'next-themes'

// In root layout
<ThemeProvider attribute="class">
  {children}
</ThemeProvider>

// In settings component
import { useTheme } from 'next-themes'

const { theme, setTheme } = useTheme()
```

**Color Palette** (Suggested):
```css
/* Light Mode */
--background: #ffffff
--text: #1a1a1a
--border: #e5e5e5

/* Dark Mode */
--background: #1a1a1a
--text: #ffffff
--border: #404040
```

## Alternatives Considered

### 1. Time-Based Auto Dark Mode
**Rejected**: Users should have explicit control. Some work nights, some prefer dark mode always.

### 2. Multiple Theme Options (Blue, Green, etc.)
**Rejected for v1**: Adds complexity. Start with light/dark, expand later if needed.

### 3. Browser Preference Only (No Toggle)
**Rejected**: Users may want different settings per device or context.

### 4. CSS Media Query Only
**Rejected**: Doesn't allow user override or persistence.

## Success Criteria

The feature is complete when:

- [ ] User can access theme settings from the Settings page
- [ ] Three options available: Light, Dark, System (auto-detect)
- [ ] Theme changes apply immediately (no page refresh)
- [ ] Theme preference persists across browser sessions
- [ ] Theme preference syncs across devices (if logged in)
- [ ] All UI components support both themes
- [ ] Transition between themes is smooth (0.3s animation)
- [ ] Accessible contrast ratios maintained (WCAG 2.1 AA)
- [ ] No visual bugs or broken components in dark mode
- [ ] Documentation updated with theme customization info

## Acceptance Criteria

### Functional Requirements
- [ ] Toggle appears in Settings page
- [ ] Clicking Light/Dark/System changes theme
- [ ] Theme persists after browser close/reopen
- [ ] System option respects OS dark mode preference
- [ ] Theme applies to all pages and components

### Visual Requirements
- [ ] All text is readable in both themes
- [ ] All components have appropriate dark mode styles
- [ ] Images/icons adapt to theme (if needed)
- [ ] Loading states work in both themes
- [ ] Modals and overlays work in both themes

### Technical Requirements
- [ ] No console errors when switching themes
- [ ] Performance impact < 50ms for theme switch
- [ ] Works in all supported browsers
- [ ] Mobile responsive in both themes

## Additional Context

### Priority
**Medium-High**: Not critical for core functionality, but high user demand and relatively straightforward to implement.

### Impact Assessment
- **User Satisfaction**: High positive impact
- **Development Effort**: Medium (2-3 days)
- **Maintenance**: Low ongoing maintenance
- **Risk**: Low technical risk

### Examples & References
- **GitHub**: Excellent dark mode implementation with smooth transitions
- **Twitter**: Clean toggle in settings
- **Discord**: System-aware dark mode by default
- **VS Code**: Multiple theme options (inspiration for future enhancement)

### Industry Data
- 70% of users prefer dark mode in low-light conditions
- 40% of users use dark mode exclusively
- Dark mode reduces eye strain by 20-30% (various studies)

## Technical Notes

### Files Likely to Change
- `src/app/layout.tsx` - Add ThemeProvider
- `src/app/(dashboard)/settings/page.tsx` - Add theme toggle UI
- `src/styles/globals.css` - Define dark mode CSS variables
- `tailwind.config.ts` - Configure dark mode
- `package.json` - Add next-themes dependency

### Potential Challenges
- Ensuring all components support dark mode (may need component audit)
- Handling images that don't work well in dark mode
- Testing across all pages and edge cases

### Future Enhancements (Out of Scope for v1)
- Custom theme colors
- High contrast mode
- Scheduled theme switching (e.g., dark mode after 6 PM)
- Per-page theme overrides

## Suggested Labels
- `feature`
- `ui`
- `enhancement`
- `user-experience`
- `medium-priority`
- `good-first-issue` (for basic implementation)

## Suggested Assignee
Frontend team / UI team

---

**Reporter**: [Your Name]
**Date**: 2026-01-30
**Estimated Effort**: 2-3 days
**Dependencies**: None
```

**Result**: ✅ Comprehensive feature request with clear scope and success criteria

---

## Example 3: Enhancement with Metrics

### User Input
```
"Dashboard is slow"
```

### Skill Process

**Step 1: Clarification**
```
I understand the dashboard has performance issues. To create a detailed enhancement issue:

1. How slow is it? (seconds to load?)
2. When is it slow? (always, or with certain data?)
3. What actions feel slow? (initial load, interactions, etc.)
4. How many transactions/data do you typically have?
```

**Step 2: User Response**
```
Takes about 10 seconds to load when I have over 1000 transactions.
Initial load is the main problem. Interactions are fine once loaded.
I have about 2000 transactions currently.
```

### Created Issue

```markdown
# Enhancement: Improve dashboard load time for large datasets

## Enhancement Summary
Optimize dashboard initial load time to handle large transaction datasets (1000+ items) more efficiently, reducing load time from ~10 seconds to <2 seconds.

## Current Behavior

### Performance Metrics
- **Current Load Time**: ~10 seconds with 2000 transactions
- **Acceptable Load Time**: <2 seconds
- **Performance Gap**: 5x slower than target

### User Experience
When users have large transaction histories (1000+ transactions):
1. User navigates to dashboard
2. Page shows loading spinner for ~10 seconds
3. All data loads at once
4. Dashboard becomes interactive

This creates a poor user experience, especially for power users with extensive transaction histories.

## Problems with Current Approach

### Technical Issues
- **No Pagination**: All transactions loaded at once
- **No Virtualization**: All DOM nodes rendered immediately
- **Heavy Computations**: Statistics calculated on full dataset client-side
- **No Caching**: Data refetched on every navigation

### User Impact
- **Frustration**: 10-second wait feels broken
- **Abandonment**: Users may think app crashed
- **Productivity Loss**: Frequent dashboard visits = frequent waits
- **Poor First Impression**: New users see slow performance

## Proposed Improvements

### 1. Implement Pagination (High Priority)
Load transactions in batches of 50-100 items:
```typescript
// Example API change
GET /api/transactions?page=1&limit=50
```

**Benefits**:
- Faster initial load
- Lower memory usage
- Better perceived performance

### 2. Add Virtual Scrolling (High Priority)
Use react-virtual or similar to render only visible items:
```typescript
import { useVirtualizer } from '@tanstack/react-virtual'
```

**Benefits**:
- Render only ~20 visible items
- Smooth scrolling even with 10,000+ items
- Minimal DOM nodes

### 3. Optimize Statistics Calculation (Medium Priority)
Move heavy computations to backend:
```typescript
// Instead of client-side calculation:
const total = transactions.reduce(...)

// Use pre-computed API response:
GET /api/dashboard/stats
```

**Benefits**:
- Faster load (no client-side computation)
- More accurate (server-side precision)
- Cacheable

### 4. Implement Smart Caching (Medium Priority)
Use SWR or React Query for data caching:
```typescript
import useSWR from 'swr'

const { data } = useSWR('/api/transactions', {
  revalidateOnFocus: false,
  dedupingInterval: 60000
})
```

**Benefits**:
- Instant load on return visits
- Background revalidation
- Reduced server load

### 5. Add Loading Skeletons (Low Priority)
Replace spinner with skeleton UI for better perceived performance.

## Implementation Priority

### Phase 1 (Week 1)
- [ ] Add pagination to transactions API
- [ ] Implement pagination in dashboard UI
- [ ] Add loading skeletons

**Expected Improvement**: 10s → 3s (70% improvement)

### Phase 2 (Week 2)
- [ ] Implement virtual scrolling
- [ ] Move statistics to backend API
- [ ] Add caching with SWR

**Expected Improvement**: 3s → 1.5s (85% improvement)

### Phase 3 (Future)
- [ ] Optimize database queries
- [ ] Add CDN caching
- [ ] Implement service worker

**Expected Improvement**: 1.5s → <1s (90%+ improvement)

## Success Metrics

### Performance Targets
- **Initial Load**: <2 seconds (currently ~10s)
- **Time to Interactive**: <3 seconds
- **Largest Contentful Paint**: <2.5 seconds
- **Cumulative Layout Shift**: <0.1

### User Experience Targets
- **Perceived Speed**: Users feel dashboard is "fast"
- **Abandonment Rate**: <5% (currently ~15%)
- **User Satisfaction**: >4.5/5 rating

### Technical Metrics
- **DOM Nodes**: <500 (currently ~2000)
- **Memory Usage**: <50MB (currently ~200MB)
- **API Response Time**: <500ms
- **Bundle Size Impact**: <10KB added

## Testing Plan

### Performance Testing
1. Test with 100, 1000, 5000, 10000 transactions
2. Measure load time for each dataset size
3. Test on slow 3G network
4. Test on mobile devices
5. Use Lighthouse for metrics

### User Testing
1. A/B test with 10% of users
2. Collect feedback via survey
3. Monitor analytics for improvements
4. Measure task completion time

## Additional Context

### Affected Users
- **Percentage**: ~30% of users have >1000 transactions
- **Growth**: Number growing as app matures
- **Power Users**: Most affected are most engaged users

### Technical Debt
This optimization will also:
- Improve code maintainability
- Reduce server costs (less data transferred)
- Enable future features (real-time updates)

### References
- [Web Vitals](https://web.dev/vitals/)
- [React Virtualization Guide](https://react-virtual.tanstack.com/)
- [SWR Documentation](https://swr.vercel.app/)

## Suggested Labels
- `enhancement`
- `performance`
- `dashboard`
- `high-priority`
- `technical-debt`

## Estimated Effort
- Phase 1: 3-5 days
- Phase 2: 5-7 days
- Total: 2 weeks

---

**Reporter**: [Your Name]
**Date**: 2026-01-30
**Impact**: High (affects 30% of users)
**Priority**: High (degrades user experience)
```

**Result**: ✅ Detailed enhancement with metrics, implementation plan, and success criteria

---

## Key Takeaways from Examples

### What Makes These Issues Excellent

1. **Specific and Measurable**
   - "10 seconds with 2000 transactions" vs "slow"
   - Clear success criteria
   - Quantifiable improvements

2. **Complete Context**
   - Environment details
   - User impact assessment
   - Technical analysis

3. **Actionable**
   - Clear implementation steps
   - Priority guidance
   - Testing plan

4. **Professional**
   - Well-structured
   - Proper formatting
   - Collaborative tone

5. **Research-Backed**
   - Codebase analysis
   - Library recommendations
   - Industry best practices

### Time Comparison

| Approach | Time | Quality |
|----------|------|---------|
| **Manual (rushed)** | 5 min | Poor - vague, incomplete |
| **Manual (careful)** | 20-30 min | Good - but time-consuming |
| **With This Skill** | 3-5 min | Excellent - fast + complete |

### Impact on Development

Issues created with this skill:
- ✅ Get triaged faster (<2 min vs 10+ min)
- ✅ Need fewer clarification questions (0-1 vs 3-5)
- ✅ Get fixed faster (clear scope)
- ✅ Have higher acceptance rate (well-researched)

---

**Remember**: Quality issues are an investment that pays dividends in faster development and better outcomes.
