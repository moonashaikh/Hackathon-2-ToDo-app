from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from backend.database.database import get_session
from backend.schemas.task import TaskCreate, TaskUpdate, TaskToggle, TaskResponse, TaskListResponse
from backend.utils.task_service import (
    create_task, get_task_by_id, get_tasks_by_user,
    update_task, delete_task, toggle_task_completion
)
from backend.core.auth_deps import get_current_active_user
from backend.schemas.auth import TokenData
from uuid import UUID
from typing import List


router = APIRouter()


@router.get("/tasks", response_model=TaskListResponse)
def read_tasks(
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Get all tasks for the authenticated user"""
    tasks = get_tasks_by_user(session, current_user.user_id)
    task_responses = [TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        user_id=task.user_id,
        created_at=task.created_at,
        updated_at=task.updated_at
    ) for task in tasks]

    return TaskListResponse(tasks=task_responses, total=len(task_responses))


@router.post("/tasks", response_model=TaskResponse)
def create_task_endpoint(
    task_data: TaskCreate,
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the authenticated user"""
    db_task = create_task(session, task_data, current_user.user_id)

    return TaskResponse(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        is_completed=db_task.is_completed,
        user_id=db_task.user_id,
        created_at=db_task.created_at,
        updated_at=db_task.updated_at
    )


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: UUID,
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Get a specific task by ID for the authenticated user"""
    db_task = get_task_by_id(session, task_id, current_user.user_id)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or you don't have permission to access it"
        )

    return TaskResponse(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        is_completed=db_task.is_completed,
        user_id=db_task.user_id,
        created_at=db_task.created_at,
        updated_at=db_task.updated_at
    )


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_endpoint(
    task_id: UUID,
    task_data: TaskUpdate,
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Update a specific task for the authenticated user"""
    db_task = update_task(session, task_id, task_data, current_user.user_id)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or you don't have permission to update it"
        )

    return TaskResponse(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        is_completed=db_task.is_completed,
        user_id=db_task.user_id,
        created_at=db_task.created_at,
        updated_at=db_task.updated_at
    )


@router.delete("/tasks/{task_id}")
def delete_task_endpoint(
    task_id: UUID,
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Delete a specific task for the authenticated user"""
    success = delete_task(session, task_id, current_user.user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or you don't have permission to delete it"
        )

    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/toggle", response_model=TaskResponse)
def toggle_task_endpoint(
    task_id: UUID,
    toggle_data: TaskToggle,
    current_user: TokenData = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a task for the authenticated user"""
    db_task = toggle_task_completion(session, task_id, current_user.user_id, toggle_data.is_completed)
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or you don't have permission to update it"
        )

    return TaskResponse(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        is_completed=db_task.is_completed,
        user_id=db_task.user_id,
        created_at=db_task.created_at,
        updated_at=db_task.updated_at
    )