from models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create(request_data: UserCreate, db: Session) -> User:
    new_user = User(
        email=request_data.email,
        is_active=request_data.is_active,
        is_superuser=request_data.is_superuser,
        name=request_data.name,
        role=request_data.role,
        password=request_data.password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
