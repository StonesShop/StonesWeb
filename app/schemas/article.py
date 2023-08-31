from pydantic import BaseModel


class ArticleDBBase(BaseModel):
    id_article: int
    name: str

    class Config:
        orm_mode = True


class ArticleCreate(BaseModel):
    name: str


class ArticleUpdate(BaseModel):
    name: str
