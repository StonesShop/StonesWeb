from pydantic import BaseModel
from typing import Optional


class ArticleDBBase(BaseModel):
    id_article: int
    name: str
    price: int

    class Config:
        orm_mode = True


class ArticleCreate(BaseModel):
    name: str
    price: int


class ArticleUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int]
