"""
Command-line interface for Todo CLI Application.

This module provides interactive menu-driven CLI for managing tasks.
Handles user input, validation, and routes commands to TaskList service.
"""

from typing import Optional

from .services import TaskList
from .models import Task


def display_menu() -> None:
    """Display main application menu with 6 options."""
    print("\n" + "=" * 20)
    print("  TODO MANAGER")
    print("=" * 20)
    print("\n1. Add a new task")
    print("2. View all tasks")
    print("3. Update task title")
    print("4. Delete a task")
    print("5. Mark task as complete")
    print("6. Exit")


def get_menu_choice() -> int:
    """
    Get and validate user's menu choice.

    Returns:
        int: Validated menu choice (1-6)
    """
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            if not choice:
                print("Error: Please enter a number between 1 and 6.")
                continue

            choice_int = int(choice)
            if 1 <= choice_int <= 6:
                return choice_int
            else:
                print("Error: Please enter a number between 1 and 6.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_task_title(prompt: str = "Enter task title: ") -> str:
    """
    Get and validate task title from user.

    Args:
        prompt: Input prompt message

    Returns:
        str: Validated non-empty task title
    """
    while True:
        title = input(prompt).strip()
        if title:
            return title
        print("Error: Task title cannot be empty. Please try again.")


def get_task_id(prompt: str = "Enter task ID: ") -> int:
    """
    Get and validate task ID from user.

    Args:
        prompt: Input prompt message

    Returns:
        int: Validated positive integer task ID
    """
    while True:
        try:
            task_id = input(prompt).strip()
            if not task_id:
                print("Error: Task ID cannot be empty. Please try again.")
                continue

            task_id_int = int(task_id)
            if task_id_int > 0:
                return task_id_int
            else:
                print("Error: Task ID must be a positive number.")
        except ValueError:
            print("Error: Please enter a valid number.")


def add_task_workflow(task_list: TaskList) -> None:
    """User Story 1: Add a new task."""
    print("\n--- Add New Task ---")
    title = get_task_title()
    task = task_list.add_task(title)
    print(f"Task added: {task}")


def view_tasks_workflow(task_list: TaskList) -> None:
    """User Story 2: View all tasks."""
    print("\n--- Your Tasks ---")
    tasks = task_list.get_all_tasks()

    if not tasks:
        print("No tasks found. Add a task to get started!")
    else:
        for task in tasks:
            print(str(task))
        print("-------------------")
        print(f"Total: {len(tasks)} tasks")


def update_task_title_workflow(task_list: TaskList) -> None:
    """User Story 3: Update task title."""
    print("\n--- Update Task Title ---")
    task_id = get_task_id("Enter task ID to update: ")
    new_title = get_task_title("Enter new title: ")

    try:
        task_list.update_task_title(task_id, new_title)
        task = task_list.get_task_by_id(task_id)
        print(f"Task updated: {task}")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_workflow(task_list: TaskList) -> None:
    """User Story 4: Delete a task."""
    print("\n--- Delete Task ---")
    task_id = get_task_id("Enter task ID to delete: ")

    try:
        task = task_list.get_task_by_id(task_id)
        task_list.delete_task(task_id)
        print(f"Task deleted: {task.title}")
    except ValueError as e:
        print(f"Error: {e}")


def mark_task_complete_workflow(task_list: TaskList) -> None:
    """User Story 5: Mark task as complete."""
    print("\n--- Mark Task Complete ---")
    task_id = get_task_id("Enter task ID to mark complete: ")

    try:
        task_list.mark_task_complete(task_id)
        task = task_list.get_task_by_id(task_id)
        print(f"Task marked complete: {task}")
    except ValueError as e:
        print(f"Error: {e}")


def handle_menu_choice(choice: int, task_list: TaskList) -> bool:
    """
    Route menu choice to appropriate workflow.

    Args:
        choice: Validated menu choice (1-6)
        task_list: TaskList service instance

    Returns:
        bool: True to continue application, False to exit
    """
    if choice == 1:
        add_task_workflow(task_list)
    elif choice == 2:
        view_tasks_workflow(task_list)
    elif choice == 3:
        update_task_title_workflow(task_list)
    elif choice == 4:
        delete_task_workflow(task_list)
    elif choice == 5:
        mark_task_complete_workflow(task_list)
    elif choice == 6:
        print("\nThank you for using Todo Manager!")
        return False

    return True


def main() -> None:
    """Main application loop - run continuously until user chooses exit."""
    task_list = TaskList()

    print("Welcome to Todo Manager!")
    print("All tasks are stored in memory and will be lost when you exit.\n")

    while True:
        display_menu()
        choice = get_menu_choice()
        should_continue = handle_menu_choice(choice, task_list)

        if not should_continue:
            break


if __name__ == "__main__":
    main()
