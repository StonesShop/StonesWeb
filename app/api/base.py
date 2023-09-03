from app.api.endpoints import article
from fastapi import APIRouter
from app.api.endpoints import catalog

api_router = APIRouter()
api_router.include_router(article.router)
api_router.include_router(catalog.router)
