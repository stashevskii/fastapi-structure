from fastapi import APIRouter, FastAPI

router = APIRouter()


def register_main_router(app: FastAPI) -> None:
    app.include_router(router)


__all__ = ["register_main_router"]
