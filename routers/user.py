
from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session

import models,schemas
from database import get_db

router=APIRouter(
    prefix="/users",
    tags=['Users']
    )




@router.get('/create_user')
def create_user():
    return{"user":"user"}

