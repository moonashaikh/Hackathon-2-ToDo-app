---
id: 1
title: Create Phase2 Constitution
stage: constitution
date: 2026-01-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: sp.constitution
labels: [constitution,spec-driven,phase-2]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Context:
This project is "Hackathon II – Evolution of Todo (Spec-Driven Development)".

Phase-1 (In-Memory Python Console App) is COMPLETE.
Now we are working on **Phase-2: Full-Stack Web Application**.

Your task:
Create a **COMPLETE, STRICT, and PRODUCTION-GRADE `speckit.constitution`**
for **Phase-2 ONLY**.

This constitution is the highest authority and must define:
- Non-negotiable principles
- Architectural constraints
- Security rules
- Tech-stack enforcement
- Spec-Driven workflow rules
- Quality bars
- Prohibited actions

⚠️ This constitution will be used by Claude Code, Copilot, and other agents.
It must PREVENT:
- Manual coding
- Vibe-coding
- Feature invention
- Security shortcuts

---

### PHASE-2 CONTEXT (YOU MUST FOLLOW EXACTLY)

Phase-2 Goal:
Transform the Phase-1 console todo app into a **secure, multi-user, persistent, full-stack web application**.

Scope INCLUDES:
- Frontend: Next.js 16+ (App Router, TypeScript, Tailwind)
- Backend: FastAPI (Python)
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth (Frontend) + JWT verification (Backend)
- REST API
- Multi-user task isolation
- Spec-Kit Plus workflow
- Monorepo structure

Scope EXCLUDES (VERY IMPORTANT):
- AI chatbot
- MCP tools
- Kubernetes / Docker
- Kafka / Dapr
These belong to Phase-3+ ONLY.

---

### MANDATORY TECHNOLOGY (NO DEVIATION)

Frontend:
- Next.js 16+
- App Router
- TypeScript
- Tailwind CSS
- Better Auth

Backend:
- FastAPI
- SQLModel
- JWT middleware

Database:
- Neon PostgreSQL ONLY

Specs:
- GitHub Spec-Kit Plus
- Organized specs folder

---

### REQUIRED OUTPUT FORMAT

Generate **ONLY** the constitution file content in Markdown.

File name:
`speckit.constitution`

Structure it with clear sections such as (you may improve wording but not remove intent):

1. Purpose of Phase-2
2. Scope & Boundaries
3. Core Principles (Binding)
4. Spec-Driven Development Rules
5. Claude Code Authority Rules
6. Monorepo & Folder Structure Rules
7. Feature Rules (Basic Level Only)
8. Authentication & Security Constitution
9. API Constitution
10. Database & Data Ownership Rules
11. Frontend Rules
12. Testing & Validation Rules
13. Prohibited Actions
14. Definition of Phase-2 Completion
15. Forward Compatibility (Phase-3 readiness)

---

### HARD RUL
```

## Response snapshot

A complete, strict, and production-grade constitution for Phase-2 of the Todo app project has been created at `.specify/memory/constitution.md`. The constitution includes 15 sections covering core principles, scope boundaries, Claude Code authority rules, monorepo structure, feature rules, authentication and security, API constitution, database rules, frontend rules, testing requirements, prohibited actions, completion definition, forward compatibility, and governance.

## Outcome

- ✅ Impact: Created comprehensive constitution file for Phase-2 project governance
- 🧪 Tests: none required for this task
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Ready for Phase-2 development following the new constitution
- 🧠 Reflection: The constitution establishes clear boundaries and rules to prevent scope creep and ensure compliance with the tech stack requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A