from fastapi import FastAPI, Form
from data.user import users
from data.todo import toDOS

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API move to /docs for swagger documentation"}


@app.get("/users/{user_id}")
def get_user_data(user_id: int):
    print("Fetching user data with user ID", user_id)
    for user in users:
        if user["id"] == user_id:
            print("User found:", user)
            return user

    print("User not found with ID", user_id)
    return {"error": "User not found"}


@app.get("/todos/{user_id}")
def get_user_todos(user_id: int, limit: int, isNotCompleted: bool):
    user_todos = [todo for todo in toDOS if todo['user_id'] == user_id]
    if isNotCompleted:
        user_todos = [
            todo for todo in user_todos if todo['is_completed'] is False]
    return user_todos[:limit]


@app.post("/todos/{user_id}")
def add_new_todo(user_id: int, title: str = Form(...), description: str = Form(...), due_date: str = Form(...)):
    newTask = {
        'id': 232,
        'user_id': user_id,
        'title': title,
        'description': description,
        'due_date': due_date,
        'is_completed': False
    }

    toDOS.append(newTask)
    return {"message": "New task created", "data": newTask}
