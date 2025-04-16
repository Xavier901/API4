from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import List

import oauth2
import models,schemas
from database import get_db


router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)
#user_id:int=Depends(oauth2.get_current_user)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post: schemas.PostCreate,db:Session=Depends(get_db),
                user_id:int=Depends(oauth2.get_current_user)):  
    
    print("Post" , user_id)
    new_post=models.Post(
        **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    #print(new_post) 
    return new_post