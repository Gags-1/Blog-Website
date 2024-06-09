from fastapi import FastAPI
from .routers import post, auth, admin
app= FastAPI()

# models.Base.metadata.create_all(bind=engine)

@app.get("/")
def message():
    return {"Message": "Hello welcome to the Blog Website!"}

app.include_router(post.router)
app.include_router(auth.router)
app.include_router(admin.router)

