from abc import ABC, abstractmethod

from core.code.models import ToolErrorModel


class Tool(ABC):
    description: str

    @abstractmethod
    async def execute_async(self, *args, **kwargs) -> str | ToolErrorModel:
        pass
