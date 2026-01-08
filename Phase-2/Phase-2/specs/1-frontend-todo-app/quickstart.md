# Quickstart: Frontend Todo App

## Development Setup

1. **Prerequisites**
   - Node.js 18+
   - pnpm (recommended) or npm

2. **Installation**
   ```bash
   # Clone the repository
   git clone <repository-url>

   # Navigate to the frontend directory
   cd frontend/web

   # Install dependencies
   pnpm install
   ```

3. **Environment Configuration**
   ```bash
   # Copy the environment file
   cp .env.example .env.local

   # Update the environment variables
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
   ```

4. **Running the Application**
   ```bash
   # Start the development server
   pnpm dev

   # The application will be available at http://localhost:3000
   ```

## Key Features

### Authentication
- User signup and login via Better Auth
- Protected routes using authentication provider
- Automatic token management

### Task Management
- Create tasks with required title and optional description
- Mark tasks as complete/incomplete
- Edit existing tasks
- Delete tasks with confirmation

### UI States
- Loading states during API calls
- Empty state for no tasks
- Error handling for network issues
- Disabled states for form validation

## Project Structure

```
frontend/web/
├── src/
│   ├── app/              # Next.js App Router pages
│   ├── components/       # Reusable UI components
│   ├── lib/             # Utility functions and API clients
│   └── hooks/           # Custom React hooks
```

## API Integration

The frontend communicates with the backend via REST API endpoints following the contract specifications:
- Authentication endpoints through Better Auth
- Task management endpoints following REST conventions
- Proper JWT token handling for authorization