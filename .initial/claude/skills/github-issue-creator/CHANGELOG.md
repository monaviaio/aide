# Changelog

All notable changes to the GitHub Issue Creator skill will be documented in this file.

## [1.0.0] - 2026-01-30

### Added
- Initial release of GitHub Issue Creator skill
- Complete 7-phase workflow (Understand → Structure → Research → Format → Metadata → Review → Create)
- Three issue type templates (Bug Report, Feature Request, Enhancement)
- Integration with @explorer for codebase research
- Integration with @librarian for library documentation
- Integration with @designer for UI/UX features
- Quality assurance checklist (20+ verification points)
- Markdown formatting automation
- Sensitive data sanitization
- Label and priority suggestions

### Methodology
Based on proven industry practices:
- Joel Spolsky's Painless Bug Tracking (3 essential elements)
- Jeff Atwood's Complaint-Driven Development (report symptoms)
- Simon Tatham's Effective Bug Reporting (show, don't tell)
- GitHub's official issue template standards

### Documentation
- SKILL.md: Complete workflow guide (21,071 characters)
- README.md: Usage and quick start guide
- QUICK_REFERENCE.md: Fast lookup cheat sheet
- EXAMPLES.md: Real-world issue examples
- CHANGELOG.md: Version history

### Real-World Validation
Skill design based on successful issue creation patterns:
- Bug reports with complete reproduction steps
- Feature requests with clear motivation and success criteria
- Enhancements with metrics and implementation plans

### Quality Standards
- ✅ "Definition of Ready" - developer can start work immediately
- ✅ Complete information extraction
- ✅ Professional formatting
- ✅ Research-backed context
- ✅ Collaborative tone

### Known Limitations
- Requires GitHub CLI (`gh`) to be installed and authenticated
- Assumes git repository with GitHub remote
- Best suited for clear, actionable problems
- May need user clarification for vague descriptions

### Future Enhancements (Planned)
- [ ] Automated duplicate detection
- [ ] Screenshot annotation tools
- [ ] Issue template customization
- [ ] Multi-issue creation (for epics)
- [ ] Integration with project management tools
- [ ] Analytics on issue quality metrics

---

## Version History

### v1.0.0 (2026-01-30)
First stable release. Companion skill to github-issue-fixer.

---

## Contributing

To suggest improvements:
1. Create issues using this skill (dogfooding!)
2. Note any gaps or inefficiencies
3. Update SKILL.md with improvements
4. Test the updated workflow
5. Document changes in this CHANGELOG

---

## Credits

**Created by**: Claude Code (Anthropic)
**Companion to**: github-issue-fixer skill
**Methodology sources**:
- Joel Spolsky - "Painless Bug Tracking"
- Jeff Atwood - "Complaint-Driven Development"
- Simon Tatham - "How to Report Bugs Effectively"
- GitHub - Official issue template documentation
- Open source maintainer best practices

**Special thanks to**:
- The open source community (for establishing issue standards)
- GitHub (for excellent documentation)
- All the maintainers who taught us what makes a good issue
