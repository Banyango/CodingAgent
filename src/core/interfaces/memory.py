from abc import ABC, abstractmethod
from typing import List

from wireup import abstract

from core.chat.models import ChatMessageModel


@abstract
class AgentMemoryService(ABC):
    @abstractmethod
    async def save_messages(self, messages: List[ChatMessageModel]):
        pass

    @abstractmethod
    async def load_messages(self) -> List[ChatMessageModel]:
        pass
