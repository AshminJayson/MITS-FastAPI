from datetime import date
from fastapi import APIRouter, Form, status

from schemas.todo import Todo
from data.todo import toDOS

router = APIRouter(prefix='/todos')


@router.get("/{user_id}", response_model=list[Todo])
def get_user_todos(user_id: int, limit: int, isNotCompleted: bool):
    user_todos = [todo for todo in toDOS if todo['user_id'] == user_id]
    if isNotCompleted:
        user_todos = [
            todo for todo in user_todos if todo['is_completed'] is False]
    return user_todos[:limit]


@router.post("/{user_id}", response_model=Todo, status_code=status.HTTP_201_CREATED)
def add_new_todo(user_id: int, title: str = Form(...), description: str = Form(...), due_date: date = Form(...)):
    newTask = {
        'id': 232,
        'user_id': user_id,
        'title': title,
        'description': description,
        'due_date': due_date,
        'is_completed': False
    }

    toDOS.append(newTask)
    return newTask
