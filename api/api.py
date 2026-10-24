from fastapi import FastAPI, Depends
from sqlalchemy import Integer, VARCHAR, create_engine, Column
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel

DATA_BASE_URI = "postgresql://postgres:0208_password@127.0.0.1:8120/news_db"

engine = create_engine(DATA_BASE_URI)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

base = declarative_base()

class c_users(base):
    __tablename__ = "users"

    name = Column(VARCHAR(20), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)

class checker(BaseModel):
    name: str
    id: int

def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post('/p')
async def post(data: checker, db: Session = Depends(get_db)):
    name = data.name
    id = data.id

    check_for_user = db.query(c_users).filter(c_users.id==id,c_users.name==name).first()

    if check_for_user:
        return {"status": f"user with name: {name} already exists"}

    new_user = c_users(name=name, id=id)
    db.add(new_user)
    db.commit()

    return {"status": "success"}

@app.delete('/d')
async def delete(data: checker,db: Session = Depends(get_db)):
    name = data.name
    id = data.id

    check_for_user = db.query(c_users).filter(c_users.name==name, c_users.id==id).first()

    if check_for_user:
        db.delete(check_for_user)
        db.commit()

        return {"status": "success"}
    else:
        return {"status" : f"user with name: {name} not found."}
