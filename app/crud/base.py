from typing import Any, Generic, Type, TypeVar, Union

from app.models.base import Base
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, *args):
        return (await db.execute(select(self.model).filter(*args))).scalar_one()

    async def get_multi(
        self, db: AsyncSession, *args, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        return (await db.execute(select(self.model).filter(*args).offset(skip).limit(limit))).scalars()

    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: AsyncSession,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.flush()
        db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *args) -> bool:
        await db.execute(delete(self.model).filter(*args))
        await db.flush()
        return True

    async def update_multi(
        self,
        db: AsyncSession,
        obj_dict: dict[str, Any],
        *args
    ) -> bool:
        await db.execute(update(self.model).where(args).values(*obj_dict))
        await db.flush()
        return True
