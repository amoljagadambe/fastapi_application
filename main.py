from fastapi import FastAPI, Depends, status
from db.init_db import init_database
from db.session import db_checker
from sqlalchemy.orm import Session
from schemas import users
from curd import users
import uvicorn

app = FastAPI()

# initialise the database
init_database()


@app.post('/user')
def index(request: users.UserBase, db: Session = Depends(db_checker)):
    return users.create(request, db)


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True, debug=True, workers=1)
