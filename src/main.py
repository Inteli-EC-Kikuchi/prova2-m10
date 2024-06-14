import logging
from fastapi import FastAPI, Request
from database.database import Base, engine
import routes.blog as blog_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

app.include_router(blog_routes.router, prefix="/blog", tags=["blog"])