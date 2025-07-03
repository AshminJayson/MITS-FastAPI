from fastapi import APIRouter, Form, HTTPException, status

from schemas.todo import Todo
from data.todo import toDOS
import random
from datetime import date

router = APIRouter(prefix="/todos")


@router.get("/")
def get_all_todos():
    return toDOS


@router.get("/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):
    for todo in toDOS:
        if todo['id'] == todo_id:
            return todo

    raise HTTPException(status.HTTP_404_NOT_FOUND, "Todo item not found")


@router.get("/u/{user_id}", response_model=list[Todo])
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


@router.put("/{todo_id}", response_model=Todo)
def update_todo_item(todo_id: int, title: str = Form(None), description: str = Form(None), due_date: date = Form(None), is_completed: bool = Form(None)):
    for idx, todo in enumerate(toDOS):
        if todo['id'] == todo_id:
            if title is not None:
                todo['title'] = title
            if description is not None:
                todo['description'] = description
            if due_date is not None:
                todo['due_date'] = due_date
            if is_completed is not None:
                todo['is_completed'] = is_completed

            toDOS[idx] = todo
            return todo

    raise HTTPException(status.HTTP_404_NOT_FOUND, "Todo item not found")


@router.delete("/{todo_id}")
def delete_todo_item(todo_id: int):
    validIndex = -1
    for idx, todo in enumerate(toDOS):
        if todo['id'] == todo_id:
            validIndex = idx
            break

    if validIndex == -1:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Todo item not found")

    del toDOS[validIndex]
    return {"message": "Todo item deleted successfully"}
