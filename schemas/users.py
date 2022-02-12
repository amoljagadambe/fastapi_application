from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr = None
    # is_active: bool = True
    # is_superuser: bool = False
    # full_name: Optional[str] = None
    # client_id: Optional[int] = None
    # role: str = None
