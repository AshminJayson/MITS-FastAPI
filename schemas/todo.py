from pydantic import BaseModel
from datetime import date


class Todo(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    due_date: date
    is_completed: bool
