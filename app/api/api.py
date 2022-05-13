from fastapi import APIRouter


from .routers import medicines, order, permissions, roles, users, login

api_router = APIRouter()

api_router.include_router(login.router, prefix="", tags=["login"])
api_router.include_router(users.router, prefix="", tags=["user"])
api_router.include_router(medicines.router, prefix="", tags=["medicine"])
api_router.include_router(order.router, prefix="", tags=["order"])
api_router.include_router(permissions.router, prefix="", tags=["permission"])
api_router.include_router(roles.router, prefix="", tags=["role"])

