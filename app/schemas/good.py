from pydantic import BaseModel


class GoodDBBase(BaseModel):
    id_good: int
    name: str

    class Config:
        orm_mode = True


class GoodCreate(BaseModel):
    name: str


class GoodUpdate(BaseModel):
    name: str
