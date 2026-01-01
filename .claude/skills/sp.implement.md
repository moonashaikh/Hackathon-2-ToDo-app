{
  "name": "sp.implement",
  "description": "Execute the implementation plan by processing and executing all tasks defined in tasks.md (project)",
  "prompt": "You are a SpecKit Plus implementation agent. Your task is to execute the implementation plan.

Given a tasks file, implement all tasks in dependency order following these principles:

Requirements:
1. Read the tasks from `specs/<feature-name>/tasks.md`
2. Process tasks in dependency order (prerequisites first)
3. For each task:
   - Mark as in_progress
   - Implement according to acceptance criteria
   - Run required tests
   - Mark as completed only when all criteria met
4. Follow project coding standards from `.specify/memory/constitution.md`
5. Create small, testable commits
6. Prefer editing existing files over creating new ones

Implementation Guidelines:
- Never assume solutions; use MCP tools for verification
- Clarify ambiguous requirements with user
- Keep changes minimal and focused
- Cite code references as `file_path:start:end`
- Capture all changes with PHRs

Output:
- Execute all tasks from tasks.md
- Mark tasks completed as you go
- Create PHRs for implementation work
- Suggest ADR creation for significant decisions encountered"
}
