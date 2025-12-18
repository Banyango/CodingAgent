from fastapi import APIRouter

from app.apis.v1.conversations.router import router as conversations_router


def build_api_v1_routes() -> APIRouter:
    """
    Builds the routes for the API v1.
    """
    router = APIRouter(prefix="/api/v1")

    # conversations
    router.include_router(conversations_router)

    return router
