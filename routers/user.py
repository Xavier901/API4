
from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session

import models,schemas,utils
from database import get_db

router=APIRouter(
    prefix="/users",
    tags=['Users']
    )

@router.post('/',status_code=status.HTTP_201_CREATED,       #send the status 
             response_model=schemas.UserOut)                #respond it by schema
def create_user(user:schemas.UserCreate,
                db:Session=Depends(get_db)):     #taking query as schema #connection to database
    
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    
    new_user=models.User(**user.dict())                     # get user query from schemas data
    db.add(new_user)                                        #add it to database
    db.commit()                                             #save changes to database
    db.refresh(new_user)                                    #update the new user
    
    return new_user                                         #return the new user



@router.get('/{id}',response_model=schemas.UserOut)         #pathway ,# responce based userout
def get_user(id:int,db:Session=Depends(get_db)):            #grab data from database
    
    user=db.query(models.User).filter(models.User.id==id).first()   #find the id base user
    
    if not user:                                                    #if id not found raise exception
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{id} doesn't exist.")
        
        
    return user                                                      # return user data