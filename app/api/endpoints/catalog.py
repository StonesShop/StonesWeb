from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.crud.crud_article import crud_article

router = APIRouter(prefix='/catalog')


@router.get('/', summary='Get Catalog')
async def get_catalog(db: AsyncSession = Depends(get_db)):
    ret = await crud_article.get_multi(db)
    return ret
