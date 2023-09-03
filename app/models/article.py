from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Article(Base):
    __tablename__ = 't_article'
    __table_args__ = ({'schema': 'stone', 'comment': 'Article'})

    id_article = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
