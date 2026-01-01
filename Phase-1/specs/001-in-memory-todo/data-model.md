# Data Model: In-Memory Todo Console Application

**Feature**: 001-in-memory-todo
**Date**: 2025-12-31
**Purpose**: Define entity structures, relationships, and validation rules

## Entity: Task

Represents a single to-do item with three core attributes.

### Attributes

| Attribute | Type | Description | Validation Rules | Notes |
|-----------|------|-------------|-----------------|-------|
| id | int | Must be unique, positive integer | Auto-assigned by TaskList service |
| title | str | Non-empty string | Must contain at least one non-whitespace character |
| completed | bool | True or False | Defaults to False for new tasks |

### State Transitions

```
[Not Complete] --- mark_complete() ---> [Complete]
```

**Transition Rules**:
- Can transition from Not Complete to Complete only
- Can transition from Complete to Complete again (idempotent)
- Cannot transition from Complete to Not Complete (not in scope per spec)
- Initial state is always Not Complete for new tasks

### Validation

**Title Validation**:
- Must not be empty or whitespace-only
- Can contain any printable characters (spaces, emoji, special characters)
- No maximum length enforced (spec assumption 4: unlimited tasks, implies unlimited titles)

**ID Validation**:
- Managed exclusively by TaskList service (auto-increment)
- Deleted task IDs are not reused (spec assumption 2)
- Must be positive integer when provided by user for operations

### Example Instance

```python
Task(id=1, title="Buy groceries", completed=False)
Task(id=2, title="Walk the dog 🐕", completed=True)
```

## Entity: TaskList

Service class managing collection of tasks in memory.

### Attributes

| Attribute | Type | Description | Notes |
|-----------|------|-------------|-------|
| tasks | list[Task] | Python list storing Task objects | List order preserved, supports O(n) iteration |
| next_id | int | Auto-increment counter for unique IDs | Starts at 1, increments after each add |

### Methods

#### add_task(title: str) -> Task

**Purpose**: Create and store a new task.

**Behavior**:
1. Validate title is non-empty (raise ValueError if empty)
2. Create new Task with `id=next_id`, `title`, `completed=False`
3. Append task to `tasks` list
4. Increment `next_id` by 1
5. Return the created Task

**Validation**:
- `title` must be non-empty string (after stripping whitespace)

**Returns**: Created Task object with assigned ID

**Raises**: `ValueError` if title is empty

#### get_all_tasks() -> list[Task]

**Purpose**: Retrieve all tasks in memory.

**Behavior**:
- Return copy of `tasks` list (or original, no mutation needed)
- Empty list if no tasks exist

**Returns**: List of all Task objects

#### get_task_by_id(task_id: int) -> Task | None

**Purpose**: Find task by ID.

**Behavior**:
1. Iterate through `tasks` list
2. Return task where `task.id == task_id`
3. Return None if no match found

**Validation**:
- `task_id` must be positive integer

**Returns**: Task object if found, None otherwise

#### update_task_title(task_id: int, new_title: str) -> bool

**Purpose**: Update task title by ID.

**Behavior**:
1. Find task using `get_task_by_id()`
2. Raise ValueError if task not found
3. Validate `new_title` is non-empty (raise ValueError if empty)
4. Update task.title to `new_title`
5. Return True

**Validation**:
- `task_id` must be positive integer
- `new_title` must be non-empty string (after stripping whitespace)

**Returns**: True on success

**Raises**: `ValueError` if task not found or title is empty

#### delete_task(task_id: int) -> bool

**Purpose**: Remove task from memory by ID.

**Behavior**:
1. Find task using `get_task_by_id()`
2. Raise ValueError if task not found
3. Remove task from `tasks` list using list comprehension
4. Task ID is not reused (next_id counter continues incrementing)
5. Return True

**Validation**:
- `task_id` must be positive integer

**Returns**: True on success

**Raises**: `ValueError` if task not found

#### mark_task_complete(task_id: int) -> bool

**Purpose**: Mark task as completed by ID.

**Behavior**:
1. Find task using `get_task_by_id()`
2. Raise ValueError if task not found
3. Set `task.completed = True`
4. Return True (idempotent: can mark already complete task again)

**Validation**:
- `task_id` must be positive integer

**Returns**: True on success

**Raises**: `ValueError` if task not found

## Relationships

```
TaskList (1) ── manages ── (0..N) Task
```

- TaskList has zero or more Task objects
- Task objects belong to exactly one TaskList
- No direct relationships between Task objects

## Validation Rules Summary

### Input Validation (Service Layer)

All service methods validate inputs before operations:

1. **Task Titles**: Must be non-empty after stripping whitespace
2. **Task IDs**: Must be positive integers
3. **Task Existence**: Operations require task exists in TaskList

### Output Validation (CLI Layer)

CLI layer handles service-level validation and displays user-friendly messages:

1. **Empty Title Error**: "Error: Task title cannot be empty. Please try again."
2. **Invalid ID Error**: "Error: Please enter a valid number for task ID."
3. **Task Not Found Error**: "Error: Task with ID {task_id} not found."
4. **No Tasks Message**: "No tasks found. Add a task to get started!"

## Performance Considerations

- **Add Task**: O(1) - append to list
- **Get All Tasks**: O(n) - iterate all tasks (n = task count)
- **Find Task by ID**: O(n) - linear search (acceptable for in-memory, < 1000 tasks)
- **Update/Delete/Complete**: O(n) - find task + O(1) list rebuild for delete

**Performance Goal**: All operations complete in < 1 second for up to 1000 tasks (spec SC-003, FR-008)

## Implementation Notes

1. Use `dataclass` decorator for Task to reduce boilerplate
2. Use type hints for all method signatures (Python 3.13+)
3. Implement clear, descriptive error messages for all validation failures
4. No external storage: All data lost when TaskList object is destroyed
5. Thread-safety not required: Single-user, single-session application
