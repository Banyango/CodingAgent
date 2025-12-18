import contextlib

from fastapi import FastAPI

from app.apis.v1.routes import build_api_v1_routes
from app.health.router import router as health_router

from app.config import APIConfig
from wireup.integration import fastapi

from libs.container import on_app_startup
from src.app.container import container


@contextlib.asynccontextmanager
async def on_app_lifecycle(app: FastAPI):
    fastapi.setup(container, app)
    await on_app_startup(container)
    yield


def create_api(config: APIConfig) -> FastAPI:
    app = FastAPI(
        version=config.api_version,
        docs_url=f"{config.path_prefix}/docs",
        lifespan=on_app_lifecycle,
    )

    app.include_router(health_router)
    app.include_router(build_api_v1_routes())

    return app
