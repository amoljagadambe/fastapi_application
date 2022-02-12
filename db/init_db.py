from db import base     # DO NOT REMOVE: Important line in order to import all the tables
from db.base_class import Base
from db.session import engine


def init_database():
    Base.metadata.create_all(bind=engine)
