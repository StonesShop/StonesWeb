from app.crud.base import CRUDBase
from app.models import Good
from app.schemas import GoodCreate, GoodUpdate


class CRUDGood(CRUDBase[Good, GoodCreate, GoodUpdate]):
    pass


crud_good = CRUDGood(Good)
