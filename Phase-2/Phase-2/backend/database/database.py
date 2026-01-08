from sqlmodel import create_engine, Session
from backend.core.config import settings
from typing import Generator


# Create database engine
engine = create_engine(settings.database_url, echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    """Create database tables - this should be called on app startup"""
    # Import models to register them with SQLModel
    from backend.models.user import User
    from backend.models.task import Task
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)