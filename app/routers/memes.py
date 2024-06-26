from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db


router = APIRouter()


@router.get("/memes", response_model=List[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        memes = crud.get_memes(db, skip=skip, limit=limit)
        return memes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/memes/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = crud.get_meme(db, meme_id)
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return meme


@router.post("/memes", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    image_url = "http://minio:9000/bucketname/filename"  # Placeholder, should be implemented
    return crud.create_meme(db=db, meme=meme, image_url=image_url)


@router.put("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    updated_meme = crud.update_meme(db, meme_id, meme)
    if updated_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return updated_meme


@router.delete("/memes/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    deleted_meme = crud.delete_meme(db, meme_id)
    if deleted_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return deleted_meme
