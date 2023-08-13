from app.api.deps import get_db
from app.crud.crud_good import crud_good
from app.models import Good
from app.schemas import GoodCreate, GoodDBBase, GoodUpdate
from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/good', tags=["Goods"])


@router.get('/', summary='Get goods', response_model=list[GoodDBBase])
async def get_good(db: AsyncSession = Depends(get_db)):
    ret = await crud_good.get_multi(db)
    return ret


@router.put('/', summary='Add good', response_model=StrictBool)
async def add_good(item_in: GoodCreate, db: AsyncSession = Depends(get_db)):
    await crud_good.create(db, obj_in=item_in)
    await db.commit()
    return True


@router.post('/{id_good}', summary='Upd good', response_model=StrictBool)
async def upd_good(id_good: int, item_in: GoodUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_good.get(db, Good.id_good == id_good)
    await crud_good.update(db, db_obj=obj, obj_in=item_in)
    await db.commit()
    return True


@router.delete('/{id_good}', summary='Del good', response_model=StrictBool)
async def del_good(id_good: int, db: AsyncSession = Depends(get_db)):
    await crud_good.remove(db, Good.id_good == id_good)
    await db.commit()
    return True
