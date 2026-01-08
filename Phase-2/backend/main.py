from fastapi import FastAPI
from backend.api import tasks, auth
from backend.database.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware

# Create tables
create_db_and_tables()

app = FastAPI(title="ToDo App API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(tasks.router, prefix="/api", tags=["tasks"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo App API"}