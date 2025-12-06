from pydantic_settings import BaseSettings
from wireup import service


class OpenRouterSettings(BaseSettings):
    # load settings from environment variables with the OPEN_ROUTER_ prefix
    model_config = {"env_prefix": "OPEN_ROUTER_"}

    api_key: str | None = None
    base_url: str = "http://localhost:11434/"
    model: str = "gpt-oss:20b"


@service
def get_open_router_settings() -> OpenRouterSettings:
    settings = OpenRouterSettings()
    if not settings.api_key:
        raise RuntimeError("OPEN_ROUTER_API_KEY must be set in the environment")
    return settings
