# In-Memory Todo Console Application

A command-line todo application in Python that allows users to manage tasks entirely in memory.

## Features

- ✅ Add new tasks with unique sequential IDs
- ✅ View all tasks with ID, title, and completion status
- ✅ Update task titles by ID
- ✅ Delete tasks by ID
- ✅ Mark tasks as completed
- 🚀 Fast startup and execution (< 2 seconds)
- 💾 In-memory storage (no files or databases)

## Project Status

Phase I (Basic Level) - Complete ✅

All five core features implemented:
1. Add Task
2. View Tasks
3. Update Task Title
4. Delete Task
5. Mark Task as Complete

## Prerequisites

- **Python 3.13 or higher**: Download from [python.org](https://www.python.org/downloads/)
- **UV** (recommended): Python package and environment manager
  - Install: `pip install uv` or see [uv installation guide](https://github.com/astral-sh/uv)

## Setup

### 1. Clone or Navigate to Repository

```bash
cd E:\hackathon-2\ToDo-App
```

### 2. Create Virtual Environment (Optional but Recommended)

Using **UV** (recommended):
```bash
# Create virtual environment
uv venv

# Activate environment (Windows PowerShell)
.venv\Scripts\activate

# Activate environment (macOS/Linux)
source .venv/bin/activate
```

Using **venv** (standard library):
```bash
# Create virtual environment
python -m venv .venv

# Activate environment (Windows PowerShell)
.venv\Scripts\activate

# Activate environment (macOS/Linux)
source .venv/bin/activate
```

### 3. Verify Python Version

```bash
python --version
```

Expected output: `Python 3.13.x` or higher

### 4. Install Dependencies

This application uses Python standard library only, so no external packages are required.

## Running the Application

### Start Todo Application

```bash
python app.py
```

Or with full path:
```bash
python E:\hackathon-2\ToDo-App\app.py
```

## Usage

### Interactive Menu

When you run the application, you'll see:

```
====================
  TODO MANAGER
====================

1. Add a new task
2. View all tasks
3. Update task title
4. Delete a task
5. Mark task as complete
6. Exit

Enter your choice (1-6): _
```

### Adding a Task

1. Select option `1` from menu
2. Enter task title when prompted
3. Task is created with next available ID

**Example**:
```
Enter your choice (1-6): 1
Enter task title: Buy groceries
Task added: [ ] 1: Buy groceries
```

### Viewing All Tasks

1. Select option `2` from menu
2. All tasks display with ID, title, and completion status

**Example**:
```
Enter your choice (1-6): 2

--- Your Tasks ---
[ ] 1: Buy groceries
[✓] 2: Walk the dog 🐕
[ ] 3: Pay bills
--------------------
Total: 3 tasks
```

### Updating a Task Title

1. Select option `3` from menu
2. Enter task ID to update
3. Enter new task title

**Example**:
```
Enter your choice (1-6): 3
Enter task ID to update: 2
Enter new title: Walk the dog 🐕
Task updated: [✓] 2: Walk the dog 🐕
```

### Deleting a Task

1. Select option `4` from menu
2. Enter task ID to delete

**Example**:
```
Enter your choice (1-6): 4
Enter task ID to delete: 3
Task deleted: Pay bills
```

### Marking a Task Complete

1. Select option `5` from menu
2. Enter task ID to mark as complete

**Example**:
```
Enter your choice (1-6): 5
Enter task ID to mark complete: 1
Task marked complete: [✓] 1: Buy groceries
```

### Exiting the Application

1. Select option `6` from menu
2. Application exits

**Note**: All tasks are lost when you exit the application (in-memory storage only).

## Common Error Messages

### Empty Task Title

```
Error: Task title cannot be empty. Please try again.
```

**Solution**: Enter a non-empty task title.

### Invalid Task ID

```
Error: Please enter a valid number for task ID.
```

**Solution**: Enter a positive integer (e.g., 1, 2, 3).

### Task Not Found

```
Error: Task with ID 99 not found.
```

**Solution**: Check the task ID from "View all tasks" and enter a valid ID.

### No Tasks Exist

```
No tasks found. Add a task to get started!
```

**Solution**: Use "Add a new task" option to create your first task.

## Project Structure

```
E:\hackathon-2\ToDo-App\
├── app.py                  # Application entry point (run this!)
├── src/
│   └── todo_cli/
│       ├── __init__.py        # Package initialization
│       ├── cli.py             # CLI interaction layer
│       ├── models.py          # Task data structure
│       └── services.py       # Business logic
├── tests/
│   └── __init__.py          # Test package (tests not included in Phase I)
├── README.md                 # This file
├── CLAUDE.md                 # Claude Code usage instructions
└── specs/
    └── 001-in-memory-todo/ # Spec-Kit Plus artifacts
```

## Architecture

The application follows clean architecture with clear separation of concerns:

### Layers

1. **Models** (`src/todo_cli/models.py`)
   - `Task` dataclass with id, title, completed attributes

2. **Services** (`src/todo_cli/services.py`)
   - `TaskList` service class managing in-memory storage
   - Methods: add_task, get_all_tasks, get_task_by_id, update_task_title, delete_task, mark_task_complete

3. **CLI** (`src/todo_cli/cli.py`)
   - Interactive menu with 6 options
   - Input validation and error handling
   - Routes commands to service layer

4. **App Entry** (`app.py`)
   - Simple entry point importing and calling main()

### Design Principles

- **CLI-First**: All functionality via command-line interface
- **In-Memory Storage**: No files, databases, or persistence
- **SOLID Principles**: Clear separation of concerns
- **Defensive Programming**: Input validation with clear error messages
- **Smallest Viable Change**: Only specified features, no overengineering

## Limitations

- **Session-Based**: All data is lost when application exits
- **Single-User**: No authentication or multi-user support
- **No Persistence**: No file or database storage
- **No Search/Filtering**: Basic functionality only (Phase I)

## Development

### Code Quality Standards

- **PEP 8 Compliance**: Follow Python style guide
- **Type Hints**: Used for all function signatures
- **Docstrings**: Google-style docstrings for public functions
- **Line Length**: Maximum 100 characters
- **Imports**: Grouped (stdlib, third-party, local)

### Running Tests

Tests are not included in Phase I (not explicitly requested in specification).

To add tests in Phase II:
1. Install pytest: `pip install pytest`
2. Create test files in `tests/` directory
3. Run tests: `pytest tests/`

## Documentation

- **[Quick Start Guide](specs/001-in-memory-todo/quickstart.md)** - Detailed setup and usage
- **[Data Model](specs/001-in-memory-todo/data-model.md)** - Entity definitions and validation
- **[Research](specs/001-in-memory-todo/research.md)** - Technical decisions
- **[Implementation Plan](specs/001-in-memory-todo/plan.md)** - Architecture decisions
- **[Tasks](specs/001-in-memory-todo/tasks.md)** - Implementation task breakdown

## Constitution

This project follows the [ToDo CLI App Constitution](.specify/memory/constitution.md) with 7 core principles:

1. Spec-Driven Development (NON-NEGOTIABLE)
2. CLI-First Design
3. In-Memory Storage Only
4. SOLID Principles and Separation of Concerns
5. Test-First Development
6. Defensive Programming
7. Smallest Viable Change

## Contributing

When contributing to this project:

1. Follow the constitution principles
2. Use Spec-Kit Plus workflow: `/sp.specify` → `/sp.plan` → `/sp.tasks` → `/sp.implement`
3. Ensure code quality standards (PEP 8, type hints, docstrings)
4. Keep changes small and focused on approved tasks

## License

This project is created for educational/hackathon purposes.

## Acknowledgments

- Spec-Kit Plus for spec-driven development workflow
- Claude Code for AI-assisted development
