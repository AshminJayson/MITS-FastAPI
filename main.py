from fastapi import FastAPI

from routers.todos import router as todosRouter
from routers.users import router as usersRouter

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API move to /docs for swagger documentation"}


app.include_router(usersRouter)
app.include_router(todosRouter)
