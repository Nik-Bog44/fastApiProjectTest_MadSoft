from sqlalchemy.orm import Session

from app.schemas import MemeUpdate, MemeCreate
from app.models import Meme


def get_meme(db: Session, meme_id: int) -> Meme:
    return db.query(Meme).filter(Meme.id == meme_id).first()


def get_memes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Meme).offset(skip).limit(limit).all()


def create_meme(db: Session, meme: MemeCreate, image_url: str):
    db_meme = Meme(id=meme.id, title=meme.title, description=meme.description, image_url=image_url)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def update_meme(db: Session, meme_id: int, meme: MemeUpdate):
    db_meme = get_meme(db, meme_id)
    if db_meme is None:
        return None
    for key, value in meme.dict().items():
        setattr(db_meme, key, value)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def delete_meme(db: Session, meme_id: int):
    db_meme = get_meme(db, meme_id)
    if db_meme is None:
        return None
    db.delete(db_meme)
    db.commit()
    return db_meme
