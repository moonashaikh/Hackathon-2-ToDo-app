# Research: In-Memory Todo Console Application

**Feature**: 001-in-memory-todo
**Date**: 2025-12-31
**Purpose**: Document technical decisions and alternatives considered for Phase 0 research

## Decision 1: Architecture Pattern

**Decision**: Layered architecture with clear separation of concerns (Models, Services, CLI, App Entry)

**Rationale**:
- Aligns with constitution's SOLID principles and separation of concerns
- Each layer has single responsibility, making code testable and maintainable
- CLI layer handles user interaction only, no business logic
- Services layer contains business rules and validation
- Models layer defines data structures
- App entry point orchestrates the application lifecycle

**Alternatives Considered**:
1. **Monolithic single file**: All code in one file
   - Rejected because: Violates separation of concerns, difficult to test, hard to maintain
2. **Functional programming approach**: Pure functions without classes
   - Rejected because: User strategy specifies service class, less intuitive for managing state
3. **Plugin architecture**: Extensible command pattern
   - Rejected because: Overengineering, violates smallest viable change principle

**References**: Constitution Principle IV (SOLID Principles), Clean Architecture principles

## Decision 2: Data Model Design

**Decision**: Task dataclass with id (int), title (str), completed (bool) attributes

**Rationale**:
- Dataclass provides automatic `__init__`, `__repr__`, equality checks
- Type hints enable IDE support and static analysis
- Simple, immutable-like structure (fields can be modified but dataclass encourages immutability patterns)
- Matches spec requirements exactly (ID, Title, Completion Status)

**Alternatives Considered**:
1. **Dictionary-based storage**: Tasks stored as `{'id': 1, 'title': '...', 'completed': False}`
   - Rejected because: No type safety, more error-prone, harder to validate
2. **NamedTuple**: Similar to dataclass but immutable
   - Rejected because: Cannot update fields (tasks need title/status updates)
3. **Custom class with properties**: Full class with getters/setters
   - Rejected because: Unnecessary complexity for simple data structure

**References**: Python 3.7+ dataclasses documentation, spec FR-002, Key Entities section

## Decision 3: In-Memory Storage Strategy

**Decision**: TaskList service class managing Python list with auto-incrementing counter

**Rationale**:
- Python list provides O(1) append and O(n) search, acceptable for in-memory use
- Auto-increment counter ensures unique sequential IDs (spec FR-002, assumption 1)
- Deleted task IDs not reused (spec assumption 2), simplifies implementation
- Service class encapsulates storage logic, following separation of concerns
- List-based storage allows iteration for "view all tasks" operation

**Alternatives Considered**:
1. **Dictionary with ID as key**: `{1: Task(...), 2: Task(...)}`
   - Rejected because: Requires maintaining order separately, doesn't support sequential gap tracking
2. **Linked list implementation**: Custom linked list structure
   - Rejected because: Unnecessary complexity, Python list is optimized for this use case
3. **Auto-incrementing ID generator using itertools.count()**:
   - Considered for ID generation, but simple counter variable is clearer

**Implementation Notes**:
- Counter starts at 1, increments after each task creation
- Task removal uses list comprehension or filter to rebuild list without deleted task
- Search operations (find by ID) use list iteration with early exit on match

**References**: Spec FR-002, assumptions 1-2, Constitution Principle III (In-Memory Storage Only)

## Decision 4: CLI Interaction Design

**Decision**: Interactive menu-driven CLI with numbered options and prompt-based input

**Rationale**:
- Interactive menu is intuitive for single-session applications
- Numbered options simplify user input (type number, select action)
- Prompt-based input allows per-action data collection (task title, task ID)
- Aligns with spec requirement for "clear prompts and messages"
- Supports deterministic behavior: same inputs produce same outputs

**Alternatives Considered**:
1. **Command-line arguments**: `python app.py add "Buy groceries"`, `python app.py complete 1`
   - Rejected because: Less interactive, requires multiple invocations per session
2. **Keyboard shortcuts**: Press 'a' to add, 'v' to view, etc.
   - Rejected because: Less discoverable, requires learning curve
3. **GUI with tkinter**: Simple graphical interface
   - Rejected because: Constitution prohibits UI frameworks, CLI-only design

**Implementation Notes**:
- Menu displays continuously until user chooses "exit" option
- Each action prompts for required input (title or ID)
- Input validation occurs before calling service methods
- Error messages displayed to user with next action prompt

**References**: Spec non-functional requirements (CLI-based interaction, clear prompts), Constitution Principle II (CLI-First Design)

## Decision 5: Error Handling Strategy

**Decision**: Try-except blocks with specific exception types and user-friendly error messages

**Rationale**:
- Validates user input (empty titles, non-numeric IDs) per spec FR-007
- Catches non-existent task IDs before attempting operations
- Provides clear, actionable error messages per spec requirements
- Prevents crashes and unexpected exits
- Aligns with Constitution Principle VI (Defensive Programming)

**Error Types to Handle**:
1. **Empty task title**: User presses Enter without input
   - Action: Display "Error: Task title cannot be empty. Please try again."
2. **Non-numeric task ID**: User enters "abc" instead of "1"
   - Action: Display "Error: Please enter a valid number for task ID."
3. **Non-existent task ID**: User enters ID 99 when only tasks 1-5 exist
   - Action: Display "Error: Task with ID 99 not found."
4. **No tasks to display**: User selects "view all tasks" when task list is empty
   - Action: Display "No tasks found. Add a task to get started!"

**Alternatives Considered**:
1. **Return None/null for errors**: Let CLI handle missing results
   - Rejected because: Inconsistent error handling, harder to provide specific messages
2. **Raise custom exceptions**: Define `TaskNotFoundError`, `EmptyTitleError`
   - Rejected because: Unnecessary complexity for CLI application, try-except sufficient
3. **Exit on error**: Application terminates on any error
   - Rejected because: Poor user experience, should recover and continue

**References**: Spec FR-007, edge cases section, Constitution Principle VI

## Decision 6: Testing Strategy (If Tests Requested)

**Decision**: pytest for unit tests, manual testing for integration

**Rationale**:
- pytest is de facto standard for Python testing
- Supports fixtures for test setup/teardown
- Easy to run (`pytest` command)
- Unit tests for models and services (test data structures, business logic)
- Integration tests for CLI (test user flows)
- Tests written BEFORE implementation (Red-Green-Refactor)

**Test Coverage**:
- `test_models.py`: Task dataclass creation, field validation
- `test_services.py`: Add task, view tasks, update title, delete task, mark complete
- `test_cli.py`: Menu flow, input handling, error display

**Alternatives Considered**:
1. **unittest module**: Python built-in testing framework
   - Rejected because: More verbose than pytest, less common in modern Python
2. **doctest**: Documentation-based testing
   - Rejected because: Less comprehensive, doesn't cover all scenarios
3. **No tests**: Rely on manual testing only
   - Rejected because: Constitution emphasizes test-first development principle

**Note**: Tests will be generated in `/sp.tasks` phase if explicitly requested in tasks document.

**References**: Constitution Principle V (Test-First Development), spec acceptance scenarios

## Decision 7: Documentation Strategy

**Decision**: README.md for setup/usage, CLAUDE.md for Claude Code guidance, specs/history for evolution tracking

**Rationale**:
- README.md provides user-facing documentation: setup, run, usage examples
- CLAUDE.md contains project-specific Claude Code instructions per constitution
- specs/history/ preserves spec evolution as spec documents
- Aligns with user strategy requirement for documentation

**Documentation Content**:
1. **README.md**:
   - Project description
   - Setup instructions (Python 3.13+, UV for env management)
   - Run instructions (how to execute app.py)
   - Usage examples (how to use each feature)
   - Known limitations (in-memory, single-session)

2. **CLAUDE.md**:
   - Already exists with SpecKit Plus instructions
   - Add project-specific guidance if needed
   - Reference constitution for coding standards

3. **specs/history/**:
   - Automatically populated by SpecKit Plus workflow
   - Each phase creates its own document (spec, plan, tasks)
   - Tracks evolution of requirements and design

**Alternatives Considered**:
1. **Docstrings only**: Only use inline documentation
   - Rejected because: Doesn't provide user-facing guide or setup instructions
2. **Wiki/external docs**: Use GitHub Wiki or external site
   - Rejected because: Overengineering, docs should live with code
3. **No documentation**: Rely on code only
   - Rejected because: Users need setup/usage guide, Claude Code needs instructions

**References**: User strategy section 6, spec acceptance criteria ("Spec-Kit Plus workflow artifacts are present")

## Summary

All technical decisions aligned with:
- **Constitution**: All 7 principles satisfied
- **Specification**: All functional requirements addressed
- **User Strategy**: All implementation strategy items covered
- **Smallest Viable Change**: No overengineering, simple solutions chosen

**Next Step**: Proceed to Phase 1 (Design) to create data-model.md and quickstart.md.
