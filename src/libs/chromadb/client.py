from chromadb import PersistentClient
from chromadb.api import ClientAPI
from pydantic_settings import BaseSettings
from wireup import service


class ChromaConfig(BaseSettings):
    persist_directory: str = "./chroma_db"
    anonymized_telemetry: bool = False


@service
def chroma_config() -> ChromaConfig:
    return ChromaConfig()


@service
class ChromaClient:
    def __init__(self, config: ChromaConfig):
        self.config = config
        self.connection: ClientAPI = PersistentClient(
            path=config.persist_directory
        )
