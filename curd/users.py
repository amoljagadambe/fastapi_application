from models.users import User
from schemas.users import UserBase
from sqlalchemy.orm import Session


def create(request: UserBase, db: Session):
    new_user = User(email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
