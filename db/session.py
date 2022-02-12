from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./sftp.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
    "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False )

# Base = declarative_base()


def db_checker():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
