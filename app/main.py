from fastapi import FastAPI
from pathlib import Path
import uvicorn
from api import api_router


# def configure_apps(app: FastAPI):
#     configure_routers(app=app)

# def configure_routers(app: FastAPI):
#     app.include_router(api_router)

# def create_app():
#     app = FastAPI()
#     configure_apps(app=app)
#     return app

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
