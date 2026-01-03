from fastapi import APIRouter
from app.repositories import user_repository
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(tags=["Users"])


@router.get("/users", response_model=list[UserResponse])
def users():
    return user_repository.get_all_users()


@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    if user:
        return user
    else:
        return {"message": "User not found"}


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    created_user = user_repository.create_user(user.email, user.full_name)
    return created_user


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    deleted_user = user_repository.delete_user_by_id(user_id)
    if deleted_user:
        return deleted_user
    else:
        return {"message": "User not found"}
