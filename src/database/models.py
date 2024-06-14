from sqlalchemy import Column, Integer, String
from .database import Base

class BlogPost(Base):

    __tablename__ = 'blogposts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)