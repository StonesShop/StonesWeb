from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Good(Base):
    __tablename__ = 't_good'
    __table_args__ = ({'schema': 'stone', 'comment': 'Goods'})

    id_good = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
