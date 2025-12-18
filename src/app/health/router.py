from fastapi import APIRouter
from pydantic import BaseModel
from wireup import Injected, inject_from_container

from app.config import APIConfig
from app.container import container

router = APIRouter()


class ServiceStatusResource(BaseModel):
    """Resource for the health status of the service."""

    message: str
    version: str


@router.get("/health", response_model=ServiceStatusResource, tags=["health"])
@inject_from_container(container=container)
async def get_health_status(config: Injected[APIConfig]):
    return ServiceStatusResource(message="Service is OK", version=config.api_version)
