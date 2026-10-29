import os
import sys
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Integer, Column, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///./test.db')

engine = create_engine(DATABASE_URI)
sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()

class cc_users(base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)

base.metadata.create_all(bind=engine)

class checker(BaseModel):
    id: int

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post('/p')
async def post(data: checker, db: Session = Depends(get_db)):
    user_id = data.id
    
    if_user_exists = db.query(cc_users).filter(cc_users.id == user_id).first()
    
    if if_user_exists:
        return {'status': 'already exists'}
    else:
        create_user = cc_users(id=user_id)
        db.add(create_user)
        db.commit()
        return {'status': 'created'}

@app.get('/g')
async def get_checkerVersion():
    return {"status": "succesfully got a your fetch request!"}

@app.delete('/d')
async def delete(data: checker, db: Session = Depends(get_db)):
    user_id = data.id
    
    if_user_exists = db.query(cc_users).filter(cc_users.id == user_id).first()
    
    if if_user_exists:
        db.delete(if_user_exists)
        db.commit()

        return {'status': 'succesfully deleted'}
    else:
        return {'status': 'not exists'}