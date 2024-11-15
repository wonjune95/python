from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

# /signup 라우트
user_router = APIRouter(
    tags=["User"],
)

users = {}

# 가입(/signup)
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 등록된 사용자입니다"
        )
    users[data.email] = data
    return {
        "message": "가입되었습니다"
    }

# 로그인(/singin)
@user_router.post("/signin")
async def sign_user_in(user:UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="등록되지 않은 사용자입니다"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="잘못된 패스워드입니다"
        )
    
    return {
        "message": "로그인되었습니다"
    }
