from sqlmodel import Session, select
from backend.models.task import Task, TaskCreate, TaskUpdate
from backend.models.user import User
from typing import List, Optional
from uuid import UUID
from datetime import datetime


def create_task(session: Session, task_data: TaskCreate, user_id: UUID) -> Task:
    """Create a new task for a user"""
    db_task = Task(
        title=task_data.title,
        description=task_data.description,
        is_completed=task_data.is_completed,
        user_id=user_id
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def get_task_by_id(session: Session, task_id: UUID, user_id: UUID) -> Optional[Task]:
    """Get a task by its ID for a specific user"""
    return session.get(Task, task_id) if session.get(Task, task_id) and session.get(Task, task_id).user_id == user_id else None


def get_tasks_by_user(session: Session, user_id: UUID) -> List[Task]:
    """Get all tasks for a specific user"""
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return tasks


def update_task(session: Session, task_id: UUID, task_data: TaskUpdate, user_id: UUID) -> Optional[Task]:
    """Update a task for a specific user"""
    db_task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not db_task or db_task.user_id != user_id:
        return None

    # Update task fields
    task_update_data = task_data.dict(exclude_unset=True)
    for field, value in task_update_data.items():
        setattr(db_task, field, value)

    # Update the updated_at timestamp
    db_task.updated_at = datetime.utcnow()

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def delete_task(session: Session, task_id: UUID, user_id: UUID) -> bool:
    """Delete a task for a specific user"""
    db_task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not db_task or db_task.user_id != user_id:
        return False

    session.delete(db_task)
    session.commit()
    return True


def toggle_task_completion(session: Session, task_id: UUID, user_id: UUID, is_completed: bool) -> Optional[Task]:
    """Toggle the completion status of a task for a specific user"""
    db_task = session.get(Task, task_id)

    # Check if task exists and belongs to the user
    if not db_task or db_task.user_id != user_id:
        return None

    db_task.is_completed = is_completed

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task