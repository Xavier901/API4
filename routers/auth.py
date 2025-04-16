from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import database,schemas,models


router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login():    
    return{"X":"xxxx"}