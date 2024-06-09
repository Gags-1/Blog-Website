from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]