
from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session

import models,schemas
from database import get_db

router=APIRouter(
    prefix="/users",
    tags=['Users']
    )




@router.post('/create_user')
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    
    new_user=models.User(**user.dict()) # get user query from schemas data
    db.add(new_user)                    #add it to database
    db.commit()                         #save changes to database
    db.refresh(new_user)                #update the new user
    
    return new_user                     #return the new user

