from fastapi import APIRouter
from .routers import medicines

api_router = APIRouter()
# app = FastAPI()

api_router.include_router(medicines.router, prefix="", tags=["medicine"])

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}