from fastapi import HTTPException, Depends, APIRouter
from .. import models
from typing import Optional
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import or_
from .. import schemas


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=list[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ""
):
    query = db.query(models.Post)
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                models.Post.title.ilike(search_term),
                models.Post.content.ilike(search_term)
            )
        )
        
    results = query.limit(limit).offset(skip).all()
    return results

    