from fastapi import FastAPI
from .database import engine
from . import models
app= FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def message():
    return {"Message": "Hello welcome to the Blog Website!"}

