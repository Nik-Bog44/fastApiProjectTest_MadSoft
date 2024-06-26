from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud


def get_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme
