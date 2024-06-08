from fastapi import FastAPI
from .routers import post
app= FastAPI()

# models.Base.metadata.create_all(bind=engine)

@app.get("/")
def message():
    return {"Message": "Hello welcome to the Blog Website!"}

app.include_router(post.router)