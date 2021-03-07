__version__ = '0.1.0'

from fastapi import FastAPI

from .routers import fan
from .settings import settings

origins = ["*"]

OPENAPI_URL = "/openapi.json" if settings.debug else None
ROOT_PATH = "/" if settings.debug else "/api"

app = FastAPI(root_path=ROOT_PATH, openapi_url=OPENAPI_URL)


app.include_router(fan.router)
