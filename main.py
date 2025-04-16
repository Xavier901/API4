from database import engine,get_db
import models,schemas
from routers import auth,user
from fastapi import FastAPI




models.Base.metadata.create_all(bind=engine)
app=FastAPI()


app.include_router(user.router)
app.include_router(auth.router)

@app.get('/')
def index():
    return{"Responce":"Welcome to API4"}