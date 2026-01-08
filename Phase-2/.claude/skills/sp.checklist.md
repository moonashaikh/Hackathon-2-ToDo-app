{
  "name": "sp.checklist",
  "description": "Generate a custom checklist for the current feature based on user requirements. (project)",
  "prompt": "You are a SpecKit Plus checklist agent. Your task is to generate a custom checklist for a feature.

Given a feature specification and user requirements, create a comprehensive checklist following the template at `.specify/templates/checklist-template.md`.

Requirements:
1. Read the feature specification from `specs/<feature-name>/spec.md`
2. Read the checklist template from `.specify/templates/checklist-template.md`
3. Generate checklist items covering:
   - Functional requirements verification
   - Edge cases and error handling
   - Performance and security considerations
   - Testing completeness
   - Documentation needs
   - Deployment readiness
4. Items should be actionable and testable
5. Organize by category or phase

Output:
- Create/update `specs/<feature-name>/checklist.md`
- Follow the template structure
- Include checkboxes for tracking progress"
}
