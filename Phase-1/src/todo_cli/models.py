"""
Data models for Todo CLI Application.

This module defines the Task dataclass representing a single todo item.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single to-do item.

    Attributes:
        id (int): Unique task identifier assigned by TaskList
        title (str): Task description (non-empty string)
        completed (bool): Completion status (False for new tasks)
    """

    id: int
    title: str
    completed: bool = False

    def __str__(self) -> str:
        """Return string representation for display."""
        status_symbol = "[X]" if self.completed else "[ ]"
        return f"{status_symbol} {self.id}: {self.title}"
