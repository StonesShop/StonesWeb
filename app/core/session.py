from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
