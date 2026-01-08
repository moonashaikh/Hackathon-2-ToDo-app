# Quickstart Guide: Phase-II Backend

## Prerequisites

- Python 3.8 or higher
- pip package manager
- PostgreSQL-compatible database (Neon recommended)
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Navigate to Backend Directory
```bash
cd Phase-2
```

### 3. Create Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the Phase-2 directory with the following variables:

```env
NEON_DB_URL=your_neon_database_connection_string
BETTER_AUTH_SECRET=your_better_auth_secret
BETTER_AUTH_URL=http://localhost:8000
```

### 5. Database Setup
The application will use the PostgreSQL database specified in `NEON_DB_URL`. Ensure your Neon database is created and accessible.

### 6. Run the Application

For development:
```bash
uvicorn main:app --reload
```

For production:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000` (or the port specified in your environment).

## API Testing

Once the server is running, you can test the API endpoints:

### Register a New User
```bash
curl -X POST http://localhost:8000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'
```

### Login
```bash
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}'
```

### Create a Todo (with authentication token)
```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"title": "My first todo", "description": "A sample todo item"}'
```

## Environment Variables

- `NEON_DB_URL`: Connection string for PostgreSQL database
- `BETTER_AUTH_SECRET`: Secret key for authentication
- `BETTER_AUTH_URL`: URL for authentication service

## Database Schema

The application will automatically connect to your PostgreSQL database. The required tables will be created based on the models defined in the application.

## Development

### Using Uvicorn for Development
```bash
uvicorn main:app --reload
```

This will restart the server automatically when code changes are detected.

## Troubleshooting

### Common Issues

1. **Database Connection Error**: Verify your `NEON_DB_URL` is correct and the database is accessible
2. **Missing Environment Variables**: Ensure all required environment variables are set in your `.env` file
3. **Port Already in Use**: Use a different port with the `--port` option in uvicorn

### Getting Help

Check the API documentation at `/docs` when the server is running, or review the API contracts in the `specs/001-phase-ii-backend/contracts/` directory.