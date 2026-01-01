<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0 (Initial ratification)
- Modified principles: N/A (new constitution)
- Added sections: All sections (Core Principles, Architecture Constraints, Development Workflow, Governance)
- Removed sections: N/A (new constitution)
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (Constitution Check section aligned)
  - ✅ .specify/templates/spec-template.md (User stories and acceptance criteria aligned)
  - ✅ .specify/templates/tasks-template.md (Task organization and testing aligned)
- Follow-up TODOs: None
-->

# ToDo CLI App Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

No implementation occurs without an approved specification. The development lifecycle MUST follow this strict order:
1. **Specification** (WHAT and WHY): Define user stories, acceptance criteria, and requirements in `/specs/<feature>/spec.md`
2. **Plan** (HOW): Document architecture decisions in `/specs/<feature>/plan.md`
3. **Tasks**: Create actionable, testable tasks in `/specs/<feature>/tasks.md`
4. **Implementation**: Write code ONLY after tasks are approved

**Rationale**: Prevents rework, ensures alignment with business intent, and makes every change traceable to requirements.

### II. CLI-First Design

All functionality MUST be accessible via command-line interface. No web frameworks, UI frameworks, or graphical interfaces are permitted.

**Requirements**:
- Text in/out protocol: stdin/arguments → stdout, errors → stderr
- Support both human-readable and structured output (JSON) where appropriate
- Commands should be intuitive, with help text for every operation
- Deterministic behavior: same inputs produce same outputs

**Rationale**: Ensures simplicity, composability with Unix tools, and focus on core functionality over presentation.

### III. In-Memory Storage Only

Tasks and data MUST be stored exclusively in memory using Python data structures. No files, databases, or external storage mechanisms are permitted.

**Requirements**:
- Use Python lists, dictionaries, or custom data structures for task storage
- All data is ephemeral and lost on application exit
- No persistence layer, no file I/O for data storage

**Rationale**: Simplifies architecture, eliminates storage complexity, focuses on business logic and CLI interaction.

### IV. SOLID Principles and Separation of Concerns

Code MUST follow SOLID principles with clear separation between CLI logic and business logic.

**Requirements**:
- CLI layer: Argument parsing, user interaction, output formatting
- Business logic layer: Task operations, validation, domain rules
- No mixing of concerns: CLI code should not contain business rules
- Meaningful function and variable names that express intent
- Single Responsibility: Each function/class has one reason to change

**Rationale**: Maintains testability, readability, and makes future changes easier without side effects.

### V. Test-First Development

Tests MUST be written before implementation. Red-Green-Refactor cycle is strictly enforced when tests are required.

**Requirements**:
- Write test cases that FAIL before implementing the feature
- Tests verify acceptance criteria from the specification
- Tests are independent and can run in any order
- Unit tests for individual functions, integration tests for user journeys

**Rationale**: Validates requirements, ensures implementation correctness, provides living documentation.

### VI. Defensive Programming

All user input MUST be validated with clear, user-friendly error messages.

**Requirements**:
- Validate all CLI arguments and input data
- Never trust user input without validation
- Provide descriptive error messages that guide users to correct usage
- Handle edge cases gracefully (empty lists, missing arguments, invalid IDs)
- Use type hints and runtime validation where appropriate

**Rationale**: Prevents crashes, provides good user experience, catches errors early.

### VII. Smallest Viable Change

All changes must be the minimum necessary to meet requirements. No overengineering or "future-proofing."

**Requirements**:
- Implement only what's specified in the approved tasks
- Don't add features "just in case"
- Don't refactor unrelated code while implementing a feature
- Prefer simple solutions over clever ones
- YAGNI (You Aren't Gonna Need It) principle

**Rationale**: Reduces complexity, maintains clarity, prevents technical debt from unused features.

## Architecture Constraints

### Technology Stack

- **Language**: Python 3.13 or higher
- **Project Structure**: Single Python package with `src/` and `tests/` directories
- **No External Dependencies for Storage**: Pure Python data structures only
- **No Web Frameworks**: CLI application only
- **No UI Frameworks**: Command-line interface only

### Project Structure

```
src/
├── todo_cli/          # Main package
│   ├── __init__.py
│   ├── cli.py         # CLI argument parsing and commands
│   ├── models.py      # Data structures (Task, TaskList)
│   └── services.py    # Business logic (add, complete, list, etc.)
tests/
├── __init__.py
├── test_cli.py        # CLI interface tests
├── test_models.py      # Data structure tests
└── test_services.py   # Business logic tests
```

### Code Quality Standards

- **PEP 8 Compliance**: Follow Python style guide
- **Type Hints**: Use type annotations for all function signatures
- **Docstrings**: Google-style or numpy-style docstrings for public functions
- **Maximum Line Length**: 100 characters
- **Imports**: Group imports (stdlib, third-party, local) in that order

## Development Workflow

### Feature Development Process

1. **Specification Phase** (`/sp.specify`)
   - Define user stories with priorities (P1, P2, P3)
   - Write acceptance scenarios in Given-When-Then format
   - Document functional requirements and success criteria
   - No implementation details in spec

2. **Planning Phase** (`/sp.plan`)
   - Research technical approaches
   - Design data models and service interfaces
   - Document architecture decisions
   - Identify dependencies and constraints

3. **Task Generation** (`/sp.tasks`)
   - Create actionable, dependency-ordered tasks
   - Organize tasks by user story for independent implementation
   - Specify exact file paths and implementation details
   - Mark parallel-executable tasks with [P]

4. **Implementation** (`/sp.implement`)
   - Execute tasks in dependency order
   - Write tests first (if tests required)
   - Implement feature code
   - Verify acceptance criteria

### Quality Gates

Before any implementation begins:
- [ ] Specification approved with clear acceptance criteria
- [ ] Plan document complete with architecture decisions
- [ ] Tasks document created with file paths and dependencies
- [ ] Constitution compliance verified

### Code Review Standards

- Every change must align with an approved task
- Changes must be small and focused (one logical unit)
- Tests must pass before merging
- Code must follow SOLID principles
- No breaking changes without spec update

## Governance

### Amendment Procedure

Constitution amendments require:
1. Documentation of the proposed change with rationale
2. Review by project maintainers
3. Migration plan if existing code or workflows are affected
4. Version bump following semantic versioning:
   - MAJOR: Backward-incompatible changes (principle removal/redefinition)
   - MINOR: New principle or section addition
   - PATCH: Clarifications, wording fixes, non-semantic changes

### Compliance Review

All pull requests and code reviews must verify compliance with this constitution. The constitution supersedes all other development practices.

### Complexity Justification

If a design appears to violate simplicity or smallest-viable-change principles, it MUST be documented with:
- The specific problem being solved
- Why simpler alternatives are insufficient
- Trade-offs explicitly stated

### Reference Documents

- **Runtime Guidance**: `CLAUDE.md` for Claude Code interactions and agent workflows
- **Templates**: `.specify/templates/` for spec, plan, and task document structure
- **Project Documentation**: `README.md` for setup and usage instructions

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
