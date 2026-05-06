# To-Do API (FastAPI)

This is a REST API built with FastAPI and SQLite.

## Features

- Create, Read, Update, Delete TODOs
- Toggle completion status
- Filtering and pagination
- Timestamps (created_at, updated_at)

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Installation

### Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/todo-api.git
```

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run API

```bash
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Example Request

POST /todos

```json
{
  "title": "ToDo-1",
  "description": "Learn Python"
}
```

## Future Improvements

- JWT Authentication
- Docker support
- PostgreSQL
- Alembic migrations
- Unit testing
- CI/CD
