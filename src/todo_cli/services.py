"""
Business logic for Todo CLI Application.

This module defines the TaskList service class managing task storage
and operations (add, view, update, delete, mark complete).
"""

from typing import List, Optional

from .models import Task


class TaskList:
    """
    Service class managing collection of tasks in memory.

    Attributes:
        tasks (List[Task]): Python list storing Task objects
        next_id (int): Auto-increment counter for unique IDs
    """

    def __init__(self) -> None:
        """Initialize empty task list with ID counter starting at 1."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str) -> Task:
        """
        Create and store a new task.

        Args:
            title: Non-empty task title

        Returns:
            Task: Created Task object with assigned ID

        Raises:
            ValueError: If title is empty after stripping whitespace
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = Task(id=self.next_id, title=title.strip(), completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in memory.

        Returns:
            List[Task]: List of all Task objects (empty if none exist)
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find task by ID.

        Args:
            task_id: Positive integer task ID

        Returns:
            Optional[Task]: Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task_title(self, task_id: int, new_title: str) -> bool:
        """
        Update task title by ID.

        Args:
            task_id: Positive integer task ID
            new_title: Non-empty new task title

        Returns:
            bool: True on success

        Raises:
            ValueError: If task not found or title is empty
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")

        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty.")

        task.title = new_title.strip()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove task from memory by ID.

        Args:
            task_id: Positive integer task ID

        Returns:
            bool: True on success

        Raises:
            ValueError: If task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")

        self.tasks = [t for t in self.tasks if t.id != task_id]
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark task as completed by ID.

        Args:
            task_id: Positive integer task ID

        Returns:
            bool: True on success (idempotent - can mark already complete task)

        Raises:
            ValueError: If task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found.")

        task.completed = True
        return True
