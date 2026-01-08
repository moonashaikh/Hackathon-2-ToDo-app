from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

if TYPE_CHECKING:
    from backend.models.user import User


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: bool = Field(default=False)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)


class Task(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default=func.now(), sa_column=Column(DateTime(timezone=True), onupdate=func.now()))

    # Relationship to user
    owner: "User" = Relationship(back_populates="tasks")


class TaskCreate(TaskBase):
    title: str = Field(min_length=1, max_length=255)


class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: Optional[bool] = Field(default=None)


class TaskRead(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    user_id: uuid.UUID