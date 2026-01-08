from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Database settings
    database_url: str

    # Auth settings
    better_auth_secret: str
    better_auth_url: str

    # JWT settings
    secret_key: str = "your-secret-key-here"  # In production, use a strong secret
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

    def validate_required_vars(self):
        """Validate that all required environment variables are present"""
        required_vars = ['database_url', 'better_auth_secret', 'better_auth_url']
        for var in required_vars:
            value = getattr(self, var, None)
            if not value or value == "":
                raise ValueError(f"Required environment variable {var} is not set")


settings = Settings()

# Validate settings on import
try:
    settings.validate_required_vars()
except ValueError as e:
    print(f"Configuration error: {e}")
    print("Please check your .env file and ensure all required variables are set.")
    print("You can copy .env.example to .env and update the values.")
    raise