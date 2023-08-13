from app.api.endpoints import good
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(good.router)
