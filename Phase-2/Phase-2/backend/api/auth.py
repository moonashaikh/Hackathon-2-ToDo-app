from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from backend.database.database import get_session
from backend.schemas.auth import UserRegister, UserLogin, Token
from backend.models.user import User, UserCreate
from backend.utils.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta
from typing import Optional
from uuid import UUID
from backend.core.auth_deps import get_current_active_user
from backend.schemas.auth import TokenData


router = APIRouter()


@router.post("/register", response_model=Token)
def register(user_data: UserRegister, session: Session = Depends(get_session)):
    """Register a new user"""
    # Check if user already exists
    existing_user = session.query(User).filter(
        (User.username == user_data.username) | (User.email == user_data.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    # Create access token
    access_token_expires = timedelta(minutes=30)  # This could come from settings
    access_token = create_access_token(
        data={"user_id": str(db_user.id), "username": db_user.username},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    """Login an existing user"""
    # Find user by username
    db_user = session.query(User).filter(User.username == user_data.username).first()

    if not db_user or not verify_password(user_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=30)  # This could come from settings
    access_token = create_access_token(
        data={"user_id": str(db_user.id), "username": db_user.username},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/profile")
def get_profile(current_user: TokenData = Depends(get_current_active_user), session: Session = Depends(get_session)):
    """Get the current user's profile information"""
    # Fetch the full user from the database using the user_id from the token
    db_user = session.get(User, current_user.user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Return user profile data
    return {
        "id": str(db_user.id),
        "username": db_user.username,
        "email": db_user.email,
        "created_at": db_user.created_at
    }


@router.post("/logout")
def logout():
    """Logout the current user (client-side token removal is sufficient)"""
    return {"message": "Successfully logged out"}