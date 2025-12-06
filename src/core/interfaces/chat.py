from abc import ABC, abstractmethod
from typing import List, Optional

from wireup import abstract

from core.chat.models import (
    ChatOptionsModel,
    ChatMessageModel,
    FunctionCallReqeustModel,
)


@abstract
class ChatClient(ABC):
    @abstractmethod
    async def chat(
        self,
        messages: List[ChatMessageModel],
        tools: Optional[List[FunctionCallReqeustModel]],
        options: ChatOptionsModel,
    ) -> ChatMessageModel:
        pass
