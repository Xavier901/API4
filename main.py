from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def index():
    return{"Responce":"Welcome to API4"}