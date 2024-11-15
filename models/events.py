from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int             # 자동 생성되는 고유 식별자
    title: str          # 이벤트 타이틀
    image: str          # 이벤트 이미지 배너의 링크
    description: str    # 이벤트 설명
    tags: List[str]     # 그룹화를 위한 이벤트 태그
    location: str       # 이벤트 위치 

    class Config:
        json_schema_extra = {
            "title": "fastapi study",
            "image": "http://www.test.com/1.jpg",
            "description": "간단한 설명을 추가해주세요.",
            "tags": ["python", "fastapi", "study"],
            "location": "Google Meet"
        }