from fastapi import APIRouter, Form, status

from schemas.todo import Todo
from data.todo import toDOS
import random
from datetime import date

router = APIRouter(prefix="/todos")


@router.get("/{user_id}", response_model=list[Todo])
# /{user_id} is path parameter ?limit= is a query parameter
def get_todos_for_user(user_id: int, limit: int):
    validTodos = []
    print(toDOS)
    for toDoItem in toDOS:
        if toDoItem['user_id'] == user_id:
            validTodos.append(toDoItem)

    return validTodos[:limit]


@router.post("/{user_id}", response_model=Todo, status_code=status.HTTP_201_CREATED)
def add_new_todo_item(user_id: int, title: str = Form(...), description: str = Form(...), due_date: date = Form(...)):
    newTask = {
        "id": random.randint(100, 1000),
        "user_id": user_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "is_completed": False
    }

    toDOS.append(newTask)
    return newTask
