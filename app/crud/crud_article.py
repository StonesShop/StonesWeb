from app.crud.base import CRUDBase
from app.models import Article
from app.schemas import ArticleCreate, ArticleUpdate


class CRUDGood(CRUDBase[Article, ArticleCreate, ArticleUpdate]):
    pass


crud_article = CRUDGood(Article)
