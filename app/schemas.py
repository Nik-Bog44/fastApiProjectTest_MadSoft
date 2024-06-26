from typing import Optional

from pydantic import BaseModel


class MemeBase(BaseModel):
    id: int
    title: str
    description: str
    image_url: str


class MemeCreate(MemeBase):
    title: str
    description: str


class MemeUpdate(MemeBase):
    description: Optional[str] = None
    tags: Optional[str] = None


class Meme(MemeBase):
    id: int
    title: str
    description: str
    image_url: str

    class Config:
        from_attributes = True
