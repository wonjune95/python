from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "todo added successfully"
    }

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="특정 todo를 확인하기 위한 ID", ge=1, le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    return {
        "message": "Todo with supplied ID doesn't exist"
    }

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="변경할 아이템의 ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "todo가 업데이트 되었습니다."
            }
    return {
        "message": "Todo with supplied ID doesn't exist"
    }

# 전체 목록 삭제하기(DELETE)
@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {
        "message": "모든 todos가 삭제되었습니다."
    }

# 특정 item 삭제하기(DELETE)
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(..., title="삭제할 아이템의 ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.remove(todo)
            return {
                "message": "todo가 삭제되었습니다."
            }
    return {
        "message": "Todo with supplied ID doesn't exist"
    }