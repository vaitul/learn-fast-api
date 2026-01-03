from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr  # Validates email format
    full_name: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str