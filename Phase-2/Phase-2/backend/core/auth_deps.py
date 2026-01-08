from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.utils.auth import verify_token
from backend.schemas.auth import TokenData
from typing import Optional


security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """Dependency to get the current authenticated user from the token"""
    token_data = verify_token(credentials.credentials)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_data


def get_current_active_user(current_user: TokenData = Depends(get_current_user)) -> TokenData:
    """Dependency to get the current active user (can be extended for additional checks)"""
    # Here you could add additional checks like if the user is active, etc.
    return current_user