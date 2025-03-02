from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr
    city: str
    interests: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str = None
    age: int = None
    gender: str = None
    email: EmailStr = None
    city: str = None
    interests: str = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
