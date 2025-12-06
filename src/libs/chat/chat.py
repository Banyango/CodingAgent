from typing import List, Optional

from wireup import service

from core.interfaces.chat import ChatClient
from core.chat.models import (
    ChatMessageModel,
    ChatOptionsModel,
    FunctionCallReqeustModel,
)

from libs.chat.model_adapter import ModelAdapter


@service
class MultiModelChatClient(ChatClient):
    def __init__(self, client: ModelAdapter):
        self._client = client

    async def chat(
        self,
        messages: List[ChatMessageModel],
        tools: Optional[List[FunctionCallReqeustModel]],
        options: ChatOptionsModel,
    ) -> ChatMessageModel:
        return await self._client.chat_create(
            messages=messages, tools=tools or [], format=options.format
        )
