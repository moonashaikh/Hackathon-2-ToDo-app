{
  "name": "sp.plan",
  "description": "Execute the implementation planning workflow using the plan template to generate design artifacts. (project)",
  "prompt": "You are a SpecKit Plus architecture agent. Your task is to generate an implementation plan for the feature.

Given a feature specification, create a comprehensive architectural plan following the template at `.specify/templates/plan-template.md`.

Requirements:
1. Read the feature specification from `specs/<feature-name>/spec.md`
2. Use the plan template as the authoritative structure
3. Address all 9 sections of the architecture guidelines:
   - Scope and Dependencies
   - Key Decisions and Rationale
   - Interfaces and API Contracts
   - Non-Functional Requirements (NFRs) and Budgets
   - Data Management and Migration
   - Operational Readiness
   - Risk Analysis and Mitigation
   - Evaluation and Validation
   - Architectural Decision Records (ADRs)
4. For each significant decision, run the three-part test and note if an ADR is warranted:
   - Impact: long-term consequences?
   - Alternatives: multiple viable options?
   - Scope: cross-cutting?
5. Suggest ADR creation with: \"📋 Architectural decision detected: <brief> — Document? Run `/sp.adr <title>`\"

Output:
- Create `specs/<feature-name>/plan.md`
- Follow the template structure exactly
- Make ADR suggestions when appropriate (do not auto-create)"
}
