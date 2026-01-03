from fastapi import APIRouter
from dotenv import load_dotenv
import psycopg2
import os
from app.repositories import user_repository

load_dotenv()

router = APIRouter(tags=["Users"])

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT"),
)

cursor = conn.cursor()


@router.get("/users")
def users():
    return user_repository.get_all_users()


@router.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    if user:
        return user
    else:
        return {"message": "User not found"}


@router.post("/users")
def create_user(name: str, email: str):
    user = user_repository.create_user(name, email)
    return {
        "data": user,
        "message": "User created successfully",
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = user_repository.delete_user_by_id(user_id)
    if success:
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
