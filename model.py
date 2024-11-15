from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

class Beomtaek(BaseModel):
    id: int
    item: str

class Config:
    json_schema_extra = {
        "example": {
            "id": 1,
            "item": "Example schema"
            }
        }
    
# todo의 item을 변경하기 위한 모델
class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "item": "변경할 아이템 작성"
            }
        }

# todo_list의 item만 리턴하기 위한 모델
class TodoItems(BaseModel):
    todos: list[TodoItem]
    class Config:
        json_schema_extra = {
            "example": [
                {"item": "첫번째 아이템"},
                {"item": "두번째 아이템"}
                ]
        }