from fastapi import APIRouter
from .routers import medicines

api_router = APIRouter()

api_router.include_router(medicines.router, prefix="", tags=["medicine"])
