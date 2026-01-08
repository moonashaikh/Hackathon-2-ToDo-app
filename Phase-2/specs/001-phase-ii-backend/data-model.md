# Data Model: Phase-II Backend

## Entity: User
**Description**: Represents a registered user in the system

**Fields**:
- `id` (UUID, Primary Key): Unique identifier for the user
- `email` (VARCHAR(255), Unique, Not Null): User's email address for login
- `password` (VARCHAR(255), Not Null): Hashed password (never exposed in API responses)
- `created_at` (TIMESTAMP, Not Null): Timestamp when user was created
- `updated_at` (TIMESTAMP, Not Null): Timestamp when user was last updated

**Constraints**:
- Email must be unique across all users
- Email must be valid email format
- Password must be properly hashed before storage

**Relationships**:
- One-to-Many with Todo (via user_id foreign key)

## Entity: Todo
**Description**: Represents a todo item owned by a user

**Fields**:
- `id` (UUID, Primary Key): Unique identifier for the todo
- `title` (VARCHAR(255), Not Null): Title of the todo item
- `description` (TEXT, Optional): Detailed description of the todo
- `completed` (BOOLEAN, Not Null, Default: false): Completion status
- `user_id` (UUID, Foreign Key, Not Null): Reference to the owning user
- `created_at` (TIMESTAMP, Not Null): Timestamp when todo was created
- `updated_at` (TIMESTAMP, Not Null): Timestamp when todo was last updated

**Constraints**:
- user_id must reference a valid user in the users table
- Title must not be empty

**Relationships**:
- Many-to-One with User (via user_id foreign key)

## Database Schema SQL

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Todos table
CREATE TABLE todos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_todos_user_id ON todos(user_id);
CREATE INDEX idx_users_email ON users(email);
```

## Validation Rules

### User Validation
- Email: Must be a valid email format
- Password: Must be at least 6 characters long (will be hashed)
- Uniqueness: Email must be unique

### Todo Validation
- Title: Must be provided and not empty
- User ownership: Todos can only be accessed by their owner
- Completed: Boolean value, defaults to false

## State Transitions

### Todo State Transitions
- `created` → `incomplete`: New todo is created with completed = false
- `incomplete` → `completed`: User marks todo as completed
- `completed` → `incomplete`: User unmarks todo as completed
- `any state` → `deleted`: User deletes the todo (cascading delete also removes from database)

## Access Control Rules

### User Data Isolation
- Users can only access their own todos
- Attempting to access another user's todo results in 403 Forbidden or 404 Not Found
- Foreign key constraints ensure referential integrity
- Authentication required for all todo operations