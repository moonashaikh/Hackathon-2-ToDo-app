<!--
Sync Impact Report:
- Version change: N/A (initial creation) → 1.0.0
- Modified principles: N/A (new file)
- Added sections: All sections (initial constitution)
- Removed sections: N/A
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->

# Todo App Phase-2 Constitution

## Core Principles

### I. Spec-Driven Development (SDD) Mandate
All development must follow the Spec-Kit Plus workflow: spec → plan → tasks → implementation. No code implementation without approved spec and plan. Features must be fully specified with acceptance criteria, constraints, and test scenarios before any implementation begins.

### II. Zero Manual Coding Tolerance
All code changes must be generated through Claude Code agents following spec-driven tasks. No manual coding, no "vibe-coding", no feature invention beyond the approved spec. Every line of code must trace back to a spec requirement and task.

### III. Security-First Architecture
Security must be designed into every component from the ground up. Authentication and authorization are mandatory for all endpoints. No security shortcuts or afterthoughts. All user data must be properly isolated and protected.

### IV. Technology Stack Compliance
Strict adherence to mandated technology stack: Next.js 16+ (App Router, TypeScript, Tailwind) for frontend; FastAPI + SQLModel for backend; Neon PostgreSQL only for database; Better Auth for authentication. No deviations or alternative technologies.

### V. Multi-User Data Isolation
Every user's data must be completely isolated from other users. Task ownership, access controls, and data boundaries must be enforced at the database and application layers. No cross-user data access or leakage permitted.

### VI. API Contract First
All backend APIs must have clearly defined contracts before implementation. REST API design must follow consistent patterns, include proper error handling, and versioning strategies. Frontend-backend contracts must be explicitly defined and validated.

## Scope & Boundaries

Phase-2 scope includes: secure, multi-user, persistent, full-stack web application with Next.js frontend, FastAPI backend, SQLModel ORM, Neon PostgreSQL database, and Better Auth authentication.

Phase-2 scope excludes: AI chatbot, MCP tools, Kubernetes/Docker, Kafka/Dapr. These belong to Phase-3+ only. No features beyond basic todo management, authentication, and user isolation are permitted.

## Claude Code Authority Rules

Claude Code agents have exclusive authority for all code generation and modification. Agents must follow the authoritative source mandate: prioritize MCP tools and CLI commands for all information gathering. All development tasks must be tracked through the todo system and completed systematically.

## Monorepo & Folder Structure Rules

The project must follow a strict monorepo structure with clear separation between frontend and backend. Frontend code in `frontend/web/`, backend code in `services/api/`, shared types in `packages/types/`. All dependencies must be properly managed through the monorepo structure.

## Feature Rules (Basic Level Only)

Features are limited to core todo functionality: create, read, update, delete tasks; user authentication and session management; basic task filtering and search; task status management (pending, completed). No advanced features like sharing, collaboration, or notifications are permitted in Phase-2.

## Authentication & Security Constitution

Better Auth must be used for frontend authentication with proper JWT verification in the backend. All API endpoints must validate user authentication and authorization. Passwords must be properly hashed, sessions managed securely, and CSRF protection implemented. Multi-user isolation is mandatory.

## API Constitution

All backend APIs must be RESTful with consistent URL patterns and HTTP method usage. Proper error handling with appropriate HTTP status codes is required. Rate limiting and input validation must be implemented. API documentation must be comprehensive and up-to-date.

## Database & Data Ownership Rules

SQLModel must be used exclusively for database operations with proper model definitions. All database queries must respect user ownership and implement proper access controls. Data retention policies must be followed, and proper indexing implemented for performance. Database migrations must be version-controlled and tested.

## Frontend Rules

Next.js App Router must be used with TypeScript throughout. Tailwind CSS for styling with consistent design system. All components must be properly typed and follow accessibility standards. State management must be handled through proper patterns (Context, Server Actions, etc.). Client-side and server-side rendering decisions must be deliberate and documented.

## Testing & Validation Rules

All code must be accompanied by appropriate tests: unit tests for business logic, integration tests for API endpoints, and end-to-end tests for critical user flows. Test coverage must meet minimum thresholds (80% for backend, 70% for frontend). All tests must pass before any code can be merged.

## Prohibited Actions

Manual coding outside of Claude Code agents is strictly prohibited. Feature invention beyond approved spec is forbidden. Security shortcuts or bypasses are not allowed. Deviations from the mandated technology stack are prohibited. Direct database access without proper ORM layers is forbidden. Hardcoding secrets or credentials is strictly prohibited.

## Definition of Phase-2 Completion

Phase-2 is complete when: all spec requirements are implemented, all tests pass, security review is completed, multi-user isolation is validated, API documentation is complete, frontend is fully functional with proper authentication, database schema is finalized with proper constraints, and all code is generated through Claude Code agents following SDD workflow.

## Forward Compatibility (Phase-3 Readiness)

Code must be written to support future Phase-3 requirements without blocking additions. Database schema should accommodate future extensions. API design should allow for future feature additions. Authentication system should support future identity provider additions. Architecture should support potential microservices decomposition in Phase-3.

## Governance

This constitution supersedes all other development practices and guidelines. All code changes must comply with these rules. Amendments require formal documentation and approval process. All pull requests and code reviews must verify constitution compliance. Complexity must be justified against these principles. Use this constitution as the ultimate authority for all development decisions.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04