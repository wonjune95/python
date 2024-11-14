from fastapi import FastAPI
from todo import todo_router  # todo.py 파일에서 todo_router 가져오기

app = FastAPI()

@app.get("/")
async def welcome() -> dict: 
    return {
        "hello": "world"
}

app.include_router(todo_router)