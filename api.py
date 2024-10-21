from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///./db.sqlite3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
db = SessionLocal()

class Image(Base):
    __tablename__ = "images_image"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    height = Column(Integer)
    width = Column(Integer)
    publication_date = Column(DateTime)
    tags = Column(String)

class Imagedel(BaseModel):
    names: List[str]

app = FastAPI()

@app.get("/tags")
def all_tags():
    tags = {}
    db_img = db.query(Image).all()
    for img in db_img:
        for tag in img.tags.split():
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
                
    return tags

@app.get("/allimages")
def all_images():
    db_img = db.query(Image).all()
    return {img.name: img.tags for img in db_img}

@app.get("/allimages/{tag}")
def images_by_tag(tag: str):
    db_img = db.query(Image).all()
    return [img.name for img in db_img if tag in img.tags.split()]

@app.post("/allimages/del")
def del_img(imagedel: Imagedel):
    for name in imagedel.names:
        db.query(Image).filter(Image.name == name).delete()
    db.commit()
    return {"deleted": imagedel.names}

db.close()