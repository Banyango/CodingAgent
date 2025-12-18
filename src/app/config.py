from pydantic.v1 import BaseSettings
from wireup import service


class APIConfig(BaseSettings):
    app_port: int = 8000
    app_host: str = "localhost"
    api_version: str = "1.0.0"
    log_level: str = "INFO"
    path_prefix: str = "/api"


@service
def api_config_provider() -> APIConfig:
    return APIConfig()  # type: ignore
