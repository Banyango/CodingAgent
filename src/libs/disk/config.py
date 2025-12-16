from pydantic_settings import BaseSettings
from wireup import service


class MemoryConfig(BaseSettings):
    use_memory: bool = False


@service
def memory_config_factory() -> MemoryConfig:
    return MemoryConfig()
