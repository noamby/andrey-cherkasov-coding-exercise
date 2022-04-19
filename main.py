from fastapi import FastAPI, Body
from fastapi.responses import RedirectResponse


def main():
    app = FastAPI()

    memory = []

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse(url="/docs")

    @app.get("/todo")
    def return_todo(all=None, _id=None):
        if all:
            return memory
        
        if not all:
            if not _id:
                return
            else:
                for x in memory:
                    if x["_id"] == _id:
                        return x

    @app.post("/todo")
    def create_todo(sent_by_user = Body(...)):
        if sent_by_user["name"]:
            if sent_by_user["description"]:
                next_id = len(memory) + 1
                sent_by_user["_id"] = next_id
                memory.append(sent_by_user)
                return sent_by_user





    return app

app = main()



