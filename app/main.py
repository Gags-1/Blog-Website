from fastapi import FastAPI
from .routers import post, auth, admin
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

# models.Base.metadata.create_all(bind=engine)

origins=[
   "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def message():
    return {"Message": "Hello welcome to the Blog Website!"}

app.include_router(post.router)
app.include_router(auth.router)
app.include_router(admin.router)

