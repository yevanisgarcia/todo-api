from pydantic import BaseModel
from datetime import datetime


class TodoCreate(BaseModel):
    title: str
    description: str | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
