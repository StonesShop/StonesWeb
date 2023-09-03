from app.api.deps import get_db
from app.crud.crud_article import crud_article
from app.models import Article
from app.schemas import ArticleCreate, ArticleDBBase, ArticleUpdate
from fastapi import APIRouter, Depends
from pydantic import StrictBool
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/article', tags=["Article"])


@router.get('/', summary='Get article', response_model=list[ArticleDBBase])
async def get_good(db: AsyncSession = Depends(get_db)):
    ret = await crud_article.get_multi(db)
    return ret


@router.get('/{id_article}', summary='Get article by id', response_model=ArticleDBBase)
async def get_article(id_article: int, db: AsyncSession = Depends(get_db)):
    ret = await crud_article.get(db, Article.id_article == id_article)
    return ret


@router.put('/', summary='Add article', response_model=StrictBool)
async def add_good(item_in: ArticleCreate, db: AsyncSession = Depends(get_db)):
    await crud_article.create(db, obj_in=item_in)
    await db.commit()
    return True


@router.post('/{id_article}', summary='Upd article', response_model=StrictBool)
async def upd_good(id_article: int, item_in: ArticleUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud_article.get(db, Article.id_article == id_article)
    await crud_article.update(db, db_obj=obj, obj_in=item_in)
    await db.commit()
    return True


@router.delete('/{id_article}', summary='Del article', response_model=StrictBool)
async def del_good(id_article: int, db: AsyncSession = Depends(get_db)):
    await crud_article.remove(db, Article.id_article == id_article)
    await db.commit()
    return True
