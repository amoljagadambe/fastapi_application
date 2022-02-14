from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr = None
    is_active: bool = True
    is_superuser: bool = False
    name: Optional[str] = None
    # client_id: Optional[int] = None
    role: str = None


class UserCreate(UserBase):
    email: EmailStr
    password: str
    role: str = None
    is_active: Optional[bool] = False


class ShowUser(UserBase):
    email: str
    role: str

    class Config:
        orm_mode = True
