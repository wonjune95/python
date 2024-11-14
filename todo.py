from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []

# item 추가(POST)(200 ok -> 201 ok)
@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "todo added successfully"
    }

# 전체 데이터 확인
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo():
    return {
        "todos": todo_list
    }

# 개별 id에 대한 데이터 확인, title은 메타 데이터로 동작한다.
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="특정 todo를 확인하기 위한 ID", ge=1, le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo": todo }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID입니다."
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="변경할 아이템의 ID")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "todo가 업데이트 되었습니다."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID입니다."
    )

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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="존재하지 않는 ID입니다."
    )