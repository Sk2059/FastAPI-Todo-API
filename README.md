# 🚀 FastAPI Todo API

A production-style Todo API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **JWT Authentication**.

This project goes beyond a simple CRUD application and implements many of the patterns used in real backend systems including authentication, authorization, database migrations, protected routes, dependency injection, pagination, and ownership-based access control.

---

# 📌 Project Goal

The goal of this project is to learn and implement modern backend development practices using FastAPI while building a realistic API that resembles production systems.

Unlike traditional Todo applications, this API ensures that:

* Users can only access their own tasks.
* Passwords are never stored in plain text.
* Routes can be protected using JWT tokens.
* Database schema changes are version controlled.
* APIs are scalable and maintainable using proper architecture.

---

# 🛠 Tech Stack

## Backend Framework

* FastAPI

## Database

* PostgreSQL

## ORM

* SQLAlchemy 2.0

## Database Migration Tool

* Alembic

## Authentication

* JWT Authentication
* OAuth2 Password Flow

## Password Hashing

* Passlib + Bcrypt

## Validation

* Pydantic

## Server

* Uvicorn

---

# 📂 Project Structure

```text
app/
│
├── api/
│   └── router/
│       ├── user.py
│       └── task.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
│
├── dependencies/
│   ├── auth.py
│   └── current_user.py
│
├── models/
│   ├── user.py
│   └── task.py
│
├── schemas/
│   ├── user.py
│   └── task.py
│
└── main.py
```

---

# 🔐 Authentication System

The project uses JWT Authentication with OAuth2 Password Flow.

Authentication process:

```text
User Login
    ↓
Email + Password Verification
    ↓
JWT Access Token Generation
    ↓
Client stores token
    ↓
Protected Endpoint Access
```

Example token:

```text
Authorization: Bearer <jwt_token>
```

Protected endpoints require a valid token.

---

# 👤 User Features

## User Registration

Creates a new account after validating:

* Email uniqueness
* Username uniqueness
* Password hashing

Endpoint:

```http
POST /users/register
```

Example Request:

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
}
```

---

## User Login

Authenticates a user and returns a JWT access token.

Endpoint:

```http
POST /users/login
```

Response:

```json
{
    "access_token": "jwt_token_here",
    "token_type": "bearer"
}
```

---

## Current User Endpoint

Returns the authenticated user information.

Endpoint:

```http
GET /users/me
```

This endpoint demonstrates:

* OAuth2 integration
* Dependency Injection
* JWT decoding
* Protected routes

---

# ✅ Task Features

## Create Task

Creates a new task for the authenticated user.

Endpoint:

```http
POST /tasks
```

Example:

```json
{
    "title": "Learn FastAPI",
    "description": "Complete CRUD section",
    "priority": "high"
}
```

The API automatically assigns ownership:

```text
owner_id = current_user.id
```

Users cannot create tasks for other users.

---

## Get All Tasks

Returns all tasks belonging to the authenticated user.

Endpoint:

```http
GET /tasks
```

Security:

```text
User A -> Sees User A tasks only
User B -> Sees User B tasks only
```

---

## Get Single Task

Returns a single task if the authenticated user owns it.

Endpoint:

```http
GET /tasks/{task_id}
```

If the task belongs to another user:

```text
404 Task Not Found
```

This prevents unauthorized access.

---

## Update Task

Allows partial updates of task information.

Endpoint:

```http
PUT /tasks/{task_id}
```

Example:

```json
{
    "completed": true
}
```

Implemented using:

```python
exclude_unset=True
```

This ensures only provided fields are updated.

---

## Delete Task

Deletes a task owned by the current user.

Endpoint:

```http
DELETE /tasks/{task_id}
```

Ownership validation is performed before deletion.

---

## Pagination

Supports pagination to efficiently retrieve large datasets.

Example:

```http
GET /tasks?skip=0&limit=10
```

This prevents loading thousands of records at once.

---

# 🧠 Concepts Covered

This project covers:

## FastAPI

* Routing
* Path Parameters
* Query Parameters
* Request Body Validation
* Response Models
* Dependency Injection
* Status Codes

## Pydantic

* Request Validation
* Response Serialization
* Schema Design

## Authentication

* JWT Tokens
* OAuth2 Password Flow
* Protected Routes

## Database

* SQLAlchemy ORM
* Relationships
* Foreign Keys
* Sessions

## Database Migrations

* Alembic
* Version Controlled Schema Changes

## Security

* Password Hashing
* Authorization
* Ownership Validation

## Production Practices

* Project Structure
* Separation of Concerns
* Dependency Injection
* Environment Variables

---

# 🔗 API Endpoints

## User Endpoints

| Method | Endpoint        | Description                |
| ------ | --------------- | -------------------------- |
| POST   | /users/register | Register user              |
| POST   | /users/login    | Login user                 |
| GET    | /users/me       | Current authenticated user |

---

## Task Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /tasks      | Create task     |
| GET    | /tasks      | Get all tasks   |
| GET    | /tasks/{id} | Get single task |
| PUT    | /tasks/{id} | Update task     |
| DELETE | /tasks/{id} | Delete task     |

---

# ⚙️ Installation

Clone repository:

```bash
git clone <repository_url>
cd fastapi-todo-api
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run migrations:

```bash
alembic upgrade head
```

Start server:

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎯 Learning Outcomes

By building this project, the following backend concepts were practiced:

* Building REST APIs with FastAPI
* Database design and relationships
* Authentication and authorization
* JWT implementation
* API security best practices
* Pagination and filtering
* Dependency Injection
* Database migrations
* Production-style project structure

---

# 🚧 Future Improvements

Planned features:

* Task filtering
* Task searching
* Task sorting
* Centralized exception handling
* Logging middleware
* Unit tests using Pytest
* Docker support
* CI/CD pipeline
* Deployment to cloud providers
* Redis caching
* Background jobs

---

# 👨‍💻 Author

Developed as part of a backend engineering learning journey focused on modern Python API development using FastAPI and PostgreSQL.
