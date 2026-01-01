---

description: "Task list for feature implementation"
---

# Tasks: In-Memory Todo Console Application

**Input**: Design documents from `/specs/001-in-memory-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are NOT included - not explicitly requested in feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project folder structure per implementation plan (src/todo_cli/, tests/)
- [ ] T002 Initialize Python package in src/todo_cli/__init__.py
- [ ] T003 Create placeholder files: src/todo_cli/cli.py, src/todo_cli/models.py, src/todo_cli/services.py
- [ ] T004 Create tests package with placeholder files: tests/__init__.py, tests/test_cli.py, tests/test_models.py, tests/test_services.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 [P] Define Task dataclass in src/todo_cli/models.py with id (int), title (str), completed (bool) attributes
- [ ] T006 Define TaskList service class skeleton in src/todo_cli/services.py with tasks list and next_id counter
- [ ] T007 Implement TaskList.add_task method in src/todo_cli/services.py with validation for non-empty title
- [ ] T008 Implement TaskList.get_all_tasks method in src/todo_cli/services.py returning list of Task objects
- [ ] T009 Implement TaskList.get_task_by_id method in src/todo_cli/services.py with linear search and None return

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can create new tasks with unique sequential IDs

**Independent Test**: Can create one or more tasks and verify they are stored with unique IDs without requiring view, update, delete, or complete features

### Implementation for User Story 1

- [ ] T010 [P] [US1] Implement CLI menu option 1 in src/todo_cli/cli.py for adding new task
- [ ] T011 [US1] Implement CLI input prompt for task title in src/todo_cli/cli.py with empty input validation
- [ ] T012 [US1] Connect CLI add option to TaskList.add_task service method in src/todo_cli/cli.py
- [ ] T013 [US1] Add success message display after task creation in src/todo_cli/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional - tasks can be added and stored with unique IDs

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Users can view all tasks with ID, title, and completion status

**Independent Test**: Can add tasks and then view them to verify correct display without requiring update, delete, or complete features

### Implementation for User Story 2

- [ ] T014 [P] [US2] Implement CLI menu option 2 in src/todo_cli/cli.py for viewing all tasks
- [ ] T015 [US2] Implement task display format in src/todo_cli/cli.py showing ID, title, completion status with [ ] or [✓] indicator
- [ ] T016 [US2] Implement "No tasks found" message in src/todo_cli/cli.py when task list is empty
- [ ] T017 [US2] Connect CLI view option to TaskList.get_all_tasks service method in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - add and view tasks

---

## Phase 5: User Story 3 - Update Task Title (Priority: P3)

**Goal**: Users can update task titles by ID

**Independent Test**: Can create a task, update its title, and verify updated result without requiring delete or complete features

### Implementation for User Story 3

- [ ] T018 [P] [US3] Implement TaskList.update_task_title method in src/todo_cli/services.py with task validation and title validation
- [ ] T019 [US3] Implement CLI menu option 3 in src/todo_cli/cli.py for updating task title
- [ ] T020 [US3] Implement CLI input prompts for task ID and new title in src/todo_cli/cli.py with validation for non-numeric ID and empty title
- [ ] T021 [US3] Add error message for task not found in src/todo_cli/cli.py
- [ ] T022 [US3] Connect CLI update option to TaskList.update_task_title service method in src/todo_cli/cli.py
- [ ] T023 [US3] Add success confirmation message in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P4)

**Goal**: Users can delete tasks by ID

**Independent Test**: Can create tasks, delete one, and verify it no longer appears in task list

### Implementation for User Story 4

- [ ] T024 [P] [US4] Implement TaskList.delete_task method in src/todo_cli/services.py with task validation
- [ ] T025 [US4] Implement CLI menu option 4 in src/todo_cli/cli.py for deleting task
- [ ] T026 [US4] Implement CLI input prompt for task ID in src/todo_cli/cli.py with validation for non-numeric ID
- [ ] T027 [US4] Add error message for task not found in src/todo_cli/cli.py
- [ ] T028 [US4] Connect CLI delete option to TaskList.delete_task service method in src/todo_cli/cli.py
- [ ] T029 [US4] Add success confirmation message in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete (Priority: P5)

**Goal**: Users can mark tasks as completed by ID

**Independent Test**: Can create a task, mark it complete, and view updated status

### Implementation for User Story 5

- [ ] T030 [P] [US5] Implement TaskList.mark_task_complete method in src/todo_cli/services.py with task validation
- [ ] T031 [US5] Implement CLI menu option 5 in src/todo_cli/cli.py for marking task complete
- [ ] T032 [US5] Implement CLI input prompt for task ID in src/todo_cli/cli.py with validation for non-numeric ID
- [ ] T033 [US5] Add error message for task not found in src/todo_cli/cli.py
- [ ] T034 [US5] Connect CLI complete option to TaskList.mark_task_complete service method in src/todo_cli/cli.py
- [ ] T035 [US5] Add success confirmation message in src/todo_cli/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Application Entry Point

**Purpose**: Wire CLI and service together, enable app execution

- [ ] T036 Implement main application loop in src/todo_cli/cli.py with continuous menu display until exit option chosen
- [ ] T037 Implement menu display function in src/todo_cli/cli.py showing 6 options (Add, View, Update, Delete, Complete, Exit)
- [ ] T038 Add option 6 (Exit) in src/todo_cli/cli.py to terminate application loop
- [ ] T039 Create app.py at repository root importing and calling main function from src/todo_cli/cli.py

**Checkpoint**: Application can run from terminal and perform all five operations

---

## Phase 9: Documentation

**Purpose**: Setup, run, usage documentation and Claude Code guidance

- [ ] T040 [P] Write README.md at repository root with project description, setup instructions (Python 3.13+, UV), run instructions, usage examples
- [ ] T041 [P] Update CLAUDE.md at repository root with project-specific instructions (verify existing content is preserved)
- [ ] T042 [P] Verify specs/history directory structure is populated (already exists from spec-plan-workflow)

**Checkpoint**: Documentation complete, project ready for use

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T043 Add type hints to all functions in src/todo_cli/cli.py, src/todo_cli/models.py, src/todo_cli/services.py
- [ ] T044 Add docstrings to all public functions in src/todo_cli/models.py and src/todo_cli/services.py (Google-style or numpy-style)
- [ ] T045 Ensure PEP 8 compliance: 100 character line limit, proper import grouping in all source files
- [ ] T046 Run quickstart validation: python app.py and verify all 5 operations work end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can proceed sequentially in priority order (P1 → P2 → P3 → P4 → P5)
  - Stories 2-5 can be worked on after Story 1 is complete, but sequential is recommended
- **App Entry Point (Phase 8)**: Depends on all user stories being complete
- **Documentation (Phase 9)**: Depends on app.py being created (Phase 8)
- **Polish (Phase 10)**: Depends on all code being complete (through Phase 9)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) and Story 1 - Integrates with TaskList service but independent story
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) and Story 1 - Uses add_task to create test scenarios, but can be tested independently
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) and Story 1 - Uses add_task to create test scenarios, but can be tested independently
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) and Story 1 - Uses add_task to create test scenarios, but can be tested independently

### Within Each Phase

- Phase 1: Tasks T002-T004 can run in parallel (different files)
- Phase 2: Tasks T005-T009 can run in parallel (different files)
- Phase 3: Tasks T010 and T011 can run in parallel (different sections of cli.py)
- Phase 4: Tasks T014 and T015 can run in parallel (different sections of cli.py)
- Phase 5: Tasks T018 and T019 can run in parallel (different files)
- Phase 6: Tasks T024 and T025 can run in parallel (different files)
- Phase 7: Tasks T030 and T031 can run in parallel (different files)
- Phase 8: Tasks T037 and T038 can run in parallel (different sections of cli.py)
- Phase 9: Tasks T040-T042 can run in parallel (different files)
- Phase 10: Tasks T043-T045 can run in parallel (different files)

### Parallel Opportunities

**Parallel Launch Example - Phase 2**:
```bash
# Launch all foundational tasks together:
Task: "Define Task dataclass in src/todo_cli/models.py"
Task: "Define TaskList service class skeleton in src/todo_cli/services.py"
```

**Parallel Launch Example - Phase 3**:
```bash
# Launch CLI and input tasks together:
Task: "Implement CLI menu option 1 in src/todo_cli/cli.py for adding new task"
Task: "Implement CLI input prompt for task title in src/todo_cli/cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test adding tasks by running app.py
5. Can demonstrate core functionality (create tasks)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP complete!
3. Add User Story 2 → Test independently → Add feature (view tasks)
4. Add User Story 3 → Test independently → Add feature (update titles)
5. Add User Story 4 → Test independently → Add feature (delete tasks)
6. Add User Story 5 → Test independently → Add feature (mark complete)
7. Complete App Entry Point → Full application wiring
8. Complete Documentation → Ready for users
9. Complete Polish → Production-ready code

Each story adds value without breaking previous stories.

### Sequential Team Strategy

Recommended execution order for single developer:

1. **Setup (Phase 1)**: Create structure and placeholder files
2. **Foundational (Phase 2)**: Implement Task and TaskList core
3. **Story 1 (Phase 3)**: Add task functionality
4. **Story 2 (Phase 4)**: View tasks functionality
5. **Story 3 (Phase 5)**: Update task titles functionality
6. **Story 4 (Phase 6)**: Delete tasks functionality
7. **Story 5 (Phase 7)**: Mark complete functionality
8. **App Entry (Phase 8)**: Wire everything together
9. **Documentation (Phase 9)**: Write README and verify CLAUDE.md
10. **Polish (Phase 10)**: Code quality and validation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Tests were NOT explicitly requested in spec, so no test tasks included
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Follow constitution principles: CLI-only, in-memory storage, SOLID, defensive programming

## Task Summary

- **Total Tasks**: 46
- **Setup Tasks**: 4 (T001-T004)
- **Foundational Tasks**: 5 (T005-T009)
- **User Story 1 Tasks**: 4 (T010-T013)
- **User Story 2 Tasks**: 4 (T014-T017)
- **User Story 3 Tasks**: 6 (T018-T023)
- **User Story 4 Tasks**: 6 (T024-T029)
- **User Story 5 Tasks**: 6 (T030-T035)
- **App Entry Point Tasks**: 4 (T036-T039)
- **Documentation Tasks**: 3 (T040-T042)
- **Polish Tasks**: 4 (T043-T046)

**Parallel Opportunities**: 19 tasks marked [P] can be run in parallel across phases
