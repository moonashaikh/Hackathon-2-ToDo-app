# API Contracts: Todo Application Backend

## Authentication Endpoints

### POST /api/auth/register
**Description**: Register a new user

**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (201 Created)**:
```json
{
  "token": "jwt-token-string",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com"
  }
}
```

**Response (400 Bad Request)**:
```json
{
  "msg": "Email already exists"
}
```

### POST /api/auth/login
**Description**: Login existing user

**Request**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK)**:
```json
{
  "token": "jwt-token-string",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com"
  }
}
```

**Response (401 Unauthorized)**:
```json
{
  "msg": "Invalid credentials"
}
```

### POST /api/auth/logout
**Description**: Logout user (future implementation)

**Headers**:
- x-auth-token: "jwt-token-string"

**Response (200 OK)**:
```json
{
  "msg": "User logged out"
}
```

### GET /api/auth/me
**Description**: Get current user info

**Headers**:
- x-auth-token: "jwt-token-string"

**Response (200 OK)**:
```json
{
  "user": {
    "id": "uuid-string",
    "email": "user@example.com"
  }
}
```

## Todo Endpoints

### GET /api/todos
**Description**: Get all todos for the authenticated user

**Headers**:
- x-auth-token: "jwt-token-string"

**Response (200 OK)**:
```json
[
  {
    "id": "uuid-string",
    "title": "Todo title",
    "description": "Todo description",
    "completed": false,
    "user_id": "user-uuid-string",
    "created_at": "2023-01-01T00:00:00.000Z",
    "updated_at": "2023-01-01T00:00:00.000Z"
  }
]
```

### POST /api/todos
**Description**: Create a new todo for the authenticated user

**Headers**:
- x-auth-token: "jwt-token-string"

**Request**:
```json
{
  "title": "New todo",
  "description": "Todo description"
}
```

**Response (201 Created)**:
```json
{
  "id": "uuid-string",
  "title": "New todo",
  "description": "Todo description",
  "completed": false,
  "user_id": "user-uuid-string",
  "created_at": "2023-01-01T00:00:00.000Z",
  "updated_at": "2023-01-01T00:00:00.000Z"
}
```

### PUT /api/todos/:id
**Description**: Update a specific todo for the authenticated user

**Headers**:
- x-auth-token: "jwt-token-string"

**Request**:
```json
{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```

**Response (200 OK)**:
```json
{
  "id": "uuid-string",
  "title": "Updated title",
  "description": "Updated description",
  "completed": true,
  "user_id": "user-uuid-string",
  "created_at": "2023-01-01T00:00:00.000Z",
  "updated_at": "2023-01-02T00:00:00.000Z"
}
```

### DELETE /api/todos/:id
**Description**: Delete a specific todo for the authenticated user

**Headers**:
- x-auth-token: "jwt-token-string"

**Response (200 OK)**:
```json
{
  "msg": "Todo removed"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "msg": "Validation error message"
}
```

### 401 Unauthorized
```json
{
  "msg": "Token is not valid"
}
```

### 403 Forbidden
```json
{
  "msg": "Access denied"
}
```

### 404 Not Found
```json
{
  "msg": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "msg": "Server error occurred"
}
```

## Security Requirements

1. All endpoints except `/api/auth/register` and `/api/auth/login` require authentication
2. Users can only access their own todos
3. JWT tokens must be validated on each authenticated request
4. Passwords must never be returned in API responses
5. All user input must be validated and sanitized