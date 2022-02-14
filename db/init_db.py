from db import base     # DO NOT REMOVE: Important line in order to import all the models (noqa: F401)
from db.base_class import Base
from db.session import engine


def init_database():
    Base.metadata.create_all(bind=engine)

    '''
    Below code will create one super user and add it into user table
    in order to run it import session first
    '''
    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #         role= "admin"
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841

