from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.models import BlogPost
from database.database import get_db
import logging
from fastapi.responses import JSONResponse

router = APIRouter()
logger = logging.getLogger(__name__)

class Post(BaseModel):
    title: str
    content: str

@router.post("/", response_model=Post)
def create_blog_post(blog_post: Post, db: Session = Depends(get_db)):
    new_blog_post = BlogPost(title=blog_post.title, content=blog_post.content)
    db.add(new_blog_post)
    db.commit()
    db.refresh(new_blog_post)
    logger.info(f"Blog post created: {blog_post}")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": "success"})

@router.get("/", response_model=list[Post])
def get_blog_posts(db: Session = Depends(get_db)):
    posts = db.query(BlogPost).all()

    json = []

    for post in posts:
        json.append({"title": post.title, "content": post.content})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"posts": json})

@router.get("/{blog_post_id}", response_model=Post)
def get_blog_post(blog_post_id: int, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.id == blog_post_id).first()
    if post is None:
        logging.warning(f"Blog post not found: {blog_post_id}")
        raise HTTPException(status_code=404, detail="Blog post not found")
    
    post = {"title": post.title, "content": post.content}

    return JSONResponse(status_code=status.HTTP_200_OK, content={"post": post})

@router.delete("/{blog_post_id}", response_model=None)
def delete_blog_post(blog_post_id: int, db: Session = Depends(get_db)):

    if db.query(BlogPost).filter(BlogPost.id == blog_post_id).first() is None:
        logging.warning(f"Blog post not found: {blog_post_id}")
        raise HTTPException(status_code=404, detail="Post not found")

    db.query(BlogPost).filter(BlogPost.id == blog_post_id).delete()
    db.commit()
    logger.info(f"Blog post deleted: {blog_post_id}")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "success"})

@router.put("/{blog_post_id}", response_model=Post)
def update_blog_post(blog_post_id: int, blog_post: Post, db: Session = Depends(get_db)):
    if blog_post.title is None and blog_post.content is None:
        logging.warning(f"Title or content required")
        raise HTTPException(status_code=400, detail="Invalid request")

    if db.query(BlogPost).filter(BlogPost.id == blog_post_id).first() is None:
        logging.warning(f"Blog post not found: {blog_post_id}")
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.query(BlogPost).filter(BlogPost.id == blog_post_id).update({"title": blog_post.title, "content": blog_post.content})

    db.commit()

    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "success"})