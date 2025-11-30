from pydantic_settings import BaseSettings
from wireup import service


class OpenRouterSettings(BaseSettings):
    base_url: str = "http://localhost:11434/"
    model: str = "gpt-oss:20b"


@service
def get_open_router_settings() -> OpenRouterSettings:
    return OpenRouterSettings()
