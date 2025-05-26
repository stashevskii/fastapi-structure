from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.app.api.routes import register_main_router
from src.app.infrastructure.config import config
from src.app.infrastructure.persistence.db import engine
from src.app.core.base import Base


@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield


def create_app() -> FastAPI:
    application = FastAPI(
        debug=config.app_config.app_debug,
        title=config.app_config.app_title,
        version=config.app_config.app_version,
        description=config.app_config.app_description,
        lifespan=lifespan
    )
    register_main_router(application)
    return application


def run():
    uvicorn.run(
        app="src.app.main:app",
        host=config.app_config.app_host,
        port=config.app_config.app_port,
        reload=True
    )


app = create_app()
