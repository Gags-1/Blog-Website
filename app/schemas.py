from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
#This is BaseModel used to set parameters in the posts that the user will create
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
class UserReponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True


#for reposne to user
class Post(PostBase):
    id: int
    created_at: datetime
    class config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post

    class config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]