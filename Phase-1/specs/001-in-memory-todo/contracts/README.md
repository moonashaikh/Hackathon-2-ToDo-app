# Contracts: In-Memory Todo Console Application

**Feature**: 001-in-memory-todo
**Date**: 2025-12-31

## Note

This contracts directory is **not applicable** for this CLI application.

## Rationale

This feature uses:
- **CLI interface only** (Constitution Principle II: CLI-First Design)
- **No external APIs or network communication**
- **No REST or GraphQL endpoints** (web frameworks out of scope)
- **Internal service methods only** (documented in data-model.md)

Contract definitions (OpenAPI, GraphQL schema) are typically used for:
- Web APIs with HTTP endpoints
- Microservice communication
- External integrations

Since this is a single-command-line application:
- All service methods are internal (within the same Python process)
- No external consumers need to understand our API
- Service interfaces are documented in `data-model.md` (TaskList methods)
- CLI contracts are defined in quickstart.md (user-facing interface)

## Alternative Documentation

For this CLI application, see:
- **[data-model.md](../data-model.md)**: TaskList service method signatures and contracts
- **[quickstart.md](../quickstart.md)**: User-facing CLI interface and menu contracts
- **[spec.md](../spec.md)**: Functional requirements and user scenarios

## Future Considerations

If the application evolves to include:
- Web API (e.g., Flask, FastAPI, FastAPI)
- Remote access (networked multi-user)
- External integrations

Then this directory should contain:
- OpenAPI/Swagger specification
- GraphQL schema
- Protocol buffer definitions
- API versioning documentation

For now (Phase I), contracts are internal-only and documented in `data-model.md`.
