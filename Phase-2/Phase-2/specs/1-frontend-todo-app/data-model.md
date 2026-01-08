# Data Model: Frontend Todo App

## Entities

### User
**Representation**: Authenticated user with JWT token management
- `id`: Unique identifier (string)
- `email`: User's email address (string)
- `name`: User's display name (string, optional)
- `token`: JWT authentication token (string)
- `createdAt`: Account creation timestamp (Date)

**Validation Rules**:
- Email must be valid email format
- Name must be 1-50 characters if provided

### Task
**Representation**: Todo item with title, description, and completion status
- `id`: Unique identifier (string)
- `title`: Task title (string, required, 1-200 characters)
- `description`: Task description (string, optional, 0-1000 characters)
- `completed`: Completion status (boolean)
- `userId`: Owner of the task (string)
- `createdAt`: Task creation timestamp (Date)
- `updatedAt`: Last update timestamp (Date)

**Validation Rules**:
- Title is required and must be 1-200 characters
- Description is optional and can be 0-1000 characters
- Task must belong to a valid user

## State Transitions

### Task State Transitions
- `pending` → `completed` (when user marks task as complete)
- `completed` → `pending` (when user marks task as incomplete)

### User Session States
- `unauthenticated` → `authenticated` (after successful login/signup)
- `authenticated` → `unauthenticated` (after logout or token expiration)

## Relationships
- User (1) → Tasks (many): One user can have many tasks
- Each task belongs to exactly one user (userId field)

## Directory Structure
The frontend application is organized in the `frontend/web/` directory with the following structure:
- `src/app/` - Next.js App Router pages
- `src/components/` - Reusable React components
- `src/lib/` - API client and utility functions
- `src/hooks/` - Custom React hooks