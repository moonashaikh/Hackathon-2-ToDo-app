# Quick Start Guide: In-Memory Todo Console Application

**Feature**: 001-in-memory-todo
**Date**: 2025-12-31
**Purpose**: Get the todo CLI application running quickly

## Prerequisites

- **Python 3.13 or higher**: Download from [python.org](https://www.python.org/downloads/)
- **UV** (recommended): Python package and environment manager
  - Install: `pip install uv` or see [uv installation guide](https://github.com/astral-sh/uv)
- **Command-line terminal**: PowerShell (Windows), Terminal (macOS/Linux), or Git Bash

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

### 3. Install Dependencies

This application uses Python standard library only, so no external packages are required.

**Optional**: If you want to run tests, install pytest:
```bash
uv add pytest
# or
pip install pytest
```

### 4. Verify Python Version

```bash
python --version
```

Expected output: `Python 3.13.x` or higher

## Running the Application

### Start the Todo Application

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
Task added: [1] Buy groceries (not complete)
```

### Viewing All Tasks

1. Select option `2` from menu
2. All tasks display with ID, title, and completion status

**Example**:
```
Enter your choice (1-6): 2

--- Your Tasks ---
[ ] 1: Buy groceries
[✓] 2: Walk the dog
[ ] 3: Pay bills
-------------------
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
│       ├── __init__.py
│       ├── cli.py            # CLI interaction layer
│       ├── models.py          # Task data structure
│       └── services.py       # Business logic
├── tests/
│   ├── test_cli.py          # CLI tests (optional)
│   ├── test_models.py        # Model tests (optional)
│   └── test_services.py     # Service tests (optional)
├── specs/
│   └── 001-in-memory-todo/ # Spec-Kit Plus artifacts
├── README.md
├── CLAUDE.md
└── .specify/
```

## Tips and Tricks

- **Emoji Support**: Task titles can contain emoji (e.g., "Walk the dog 🐕")
- **Long Titles**: Task titles can be any length (no maximum)
- **Rapid Operations**: Operations complete in under 1 second for up to 1000 tasks
- **Keyboard Shortcuts**: None available (use numbered menu options)
- **Session-Based**: All tasks are lost when you exit the application

## Troubleshooting

### "python: command not found"

**Solution**: Install Python 3.13+ from python.org and add to PATH.

### "ModuleNotFoundError: No module named 'todo_cli'"

**Solution**:
- Ensure you're in the correct directory: `E:\hackathon-2\ToDo-App`
- Ensure `src/todo_cli/__init__.py` exists
- Run from project root: `python app.py`

### Application Doesn't Respond

**Solution**:
- Press Enter (might be waiting for input)
- Press Ctrl+C to exit the application

### Data Lost After Restart

**Expected Behavior**: This is correct! The application uses in-memory storage only (no files or databases). All tasks are lost when you exit.

## Next Steps

- Customize the application by editing `src/todo_cli/` files
- Add new features following the existing architecture
- Refer to `README.md` for detailed documentation
- Review `CLAUDE.md` for Claude Code usage instructions

## Support

For issues or questions:
- Check the `specs/001-in-memory-todo/` directory for specifications and design documents
- Review the constitution at `.specify/memory/constitution.md`
- Refer to Spec-Kit Plus documentation for workflow questions
