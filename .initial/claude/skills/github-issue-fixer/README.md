# GitHub Issue Fixer Skill

A systematic workflow for fixing GitHub issues following industry best practices from Kent Beck (TDD), Martin Fowler (Refactoring), and GitHub Flow.

## Installation

This skill is already installed in your Claude Code environment at:
```
~/.claude/skills/github-issue-fixer/
```

## Usage

Simply ask Claude to fix an issue by number:

```
"Fix issue #3"
"Resolve GitHub issue #42"
"修复 3 号 issue"
"Implement issue 123"
```

Claude will automatically:
1. ✅ Fetch and understand the issue
2. ✅ Research the solution approach
3. ✅ Create a feature branch
4. ✅ Implement the fix with proper code quality
5. ✅ Add tests and documentation
6. ✅ Create a clean commit with Conventional Commits format
7. ✅ Submit a well-documented PR
8. ✅ Link the PR to close the issue automatically

## What Makes This Skill Different

### Industry Best Practices
- **Kent Beck's TDD**: Red-Green-Refactor approach ensures fixes are verifiable
- **Martin Fowler's Refactoring**: Fixes improve code structure, not just patch symptoms
- **GitHub Flow**: Consistent, safe branch-based workflow
- **Conventional Commits**: Clean, parseable commit history

### Complete Workflow
Most developers skip steps. This skill ensures:
- Issue is fully understood before coding
- Research is done for library integrations
- Edge cases and error handling are considered
- i18n translations are added
- Configuration is documented
- PR descriptions are comprehensive

### Quality Assurance
Every fix includes:
- LSP diagnostics check
- Code style consistency
- Atomic, focused commits
- Proper issue linking
- Testing verification

## Example: Real Fix

Here's how this skill fixed issue #3 (forgot password 404):

**Input**: "修复 3 号 issue"

**Process**:
1. Fetched issue: "忘记密码 404"
2. Used @explorer to find auth files
3. Used @librarian to research better-auth password reset
4. Created branch: `fix/forgot-password-404`
5. Implemented:
   - `/forgot-password` page
   - `/reset-password` page
   - Auth configuration
   - Translations (en, zh, th)
6. Committed with clear message
7. Created PR with comprehensive description

**Output**: [PR #5](https://github.com/minliacom/wealth/pull/5)

**Time**: ~15 minutes (vs 1+ hour manually)

## Configuration

No configuration needed! The skill adapts to your project:
- Detects existing conventions
- Follows your code style
- Uses your i18n setup
- Matches your commit patterns

## Methodology Sources

This skill is based on proven methodologies:

- **Test-Driven Development** (Kent Beck)
  - *Book*: "Test Driven Development: By Example"
  - *Principle*: Red-Green-Refactor

- **Refactoring** (Martin Fowler)
  - *Book*: "Refactoring: Improving the Design of Existing Code"
  - *Principle*: Leave code better than you found it

- **GitHub Flow**
  - *Source*: GitHub official documentation
  - *Principle*: Branch-based workflow for safe deployments

- **Conventional Commits**
  - *Source*: conventionalcommits.org
  - *Principle*: Structured, parseable commit messages

- **Google Engineering Practices**
  - *Source*: Google's Code Review Guidelines
  - *Principle*: Code health over feature velocity

## Quality Metrics

A fix is considered complete when:
- ✅ Issue is resolved (not just symptoms)
- ✅ No regressions introduced
- ✅ Code is maintainable and readable
- ✅ Tests pass (if applicable)
- ✅ Documentation is updated
- ✅ Git history is clean
- ✅ PR is well-documented
- ✅ Issue is properly linked

## Common Use Cases

### Bug Fixes
```
"Fix issue #42 - login timeout"
```
- Reproduces the bug
- Identifies root cause
- Implements fix with tests
- Verifies no regressions

### Missing Features
```
"Implement issue #3 - forgot password"
```
- Researches implementation approach
- Checks library documentation
- Implements complete flow
- Adds configuration

### Enhancements
```
"Resolve issue #15 - improve dashboard performance"
```
- Profiles current performance
- Identifies bottlenecks
- Implements optimizations
- Measures improvements

## Tips for Best Results

### Be Specific
❌ "Fix the bug"
✅ "Fix issue #42"

### Trust the Process
The skill follows a proven workflow. Don't skip phases.

### Review Before Merge
Always review the PR before merging. The skill creates quality PRs, but human review adds context.

### Iterate
If the fix isn't perfect, the skill can iterate based on feedback.

## Troubleshooting

### "Issue not found"
- Ensure you're in a git repository with GitHub remote
- Check that `gh` CLI is authenticated
- Verify the issue number exists

### "Too many uncommitted changes"
- The skill will stash changes automatically
- Or commit your work first, then run the skill

### "Library not found"
- The skill will use @librarian to research
- May need to install dependencies first

## Contributing

Found a way to improve this skill? The skill itself can be updated:
1. Edit `~/.claude/skills/github-issue-fixer/SKILL.md`
2. Test with a real issue
3. Share improvements with the community

## License

This skill is based on publicly available methodologies and best practices. Use freely in your projects.

---

**Created by**: Claude Code
**Based on**: Real-world issue fix (issue #3, forgot password 404)
**Methodology**: Kent Beck (TDD), Martin Fowler (Refactoring), GitHub Flow
