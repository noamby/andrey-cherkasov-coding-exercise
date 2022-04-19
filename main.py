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

    def get_todo_by_id(todo_id: int) -> Todo:
        """Returns a Todo instance matching the given id.
        
        Args:
            todo_id: the id of the Todo instance.
        Raises:
            HttpException: if there's no such Todo.
        """
        try:
            # technically we need a uniqueness check here, but when using usual ORM it's guaranteed
            return [todo for todo in todos if todo.id == todo_id][0]
        except IndexError:
            raise HTTPException(status_code=404, detail="Todo not found!")   

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse(url="/docs")

    @app.get("/todos")
    def read_todos():
        return todos

    @app.get("/todos/{todo_id}")
    def read_todo(todo_id: int):
        return get_todo_by_id(todo_id) 

    @app.post("/todos")
    def create_todo(name: str = Body(...), description: str = Body(default=None)):
        todo = Todo(
            id=get_next_id(),
            name=name,
            description=description,
            completed=False
        )
        # TODO: check if further validation is needed
        todos.append(todo)
        return todo

    return app

app = main()



