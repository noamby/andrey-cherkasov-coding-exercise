from typing import Optional

from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    name: str
    description: Optional[str]
    completed: bool


next_id = 1


def get_next_id() -> int:
    global next_id
    current_id = next_id
    next_id += 1
    return current_id


def main():
    app = FastAPI()

    todos = []

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse(url="/docs")

    @app.get("/todos")
    def read_todos():
        return todos

    @app.get("/todos/{todo_id}")
    def read_todo(todo_id: int):
        try:
            # technically we need a uniqueness check here, but when using usual ORM it's guaranteed
            todo = [todo for todo in todos if todo.id == todo_id][0]
        except IndexError:
            raise HTTPException(status_code=404, detail="Todo not found!")

    @app.post("/todos")
    def create_todo(name: str = Body(...), description: str = Body(default=None)):
        todo = Todo(
            id=get_next_id(),
            name=name,
            description=description,
            completed=False
        )
        todos.append(todo)
        return todo


    return app

app = main()



