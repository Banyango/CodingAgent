from dataclasses import asdict
from typing import Iterable, AsyncIterator, List, Optional

from wireup import service

from core.chat.client import ChatClient
from core.chat.models import ChatMessageModel, ChatOptionsModel, FunctionCallToolModel
from libs.chat.model_adapter import ModelAdapter
from libs.chat.types import ChatResponse


@service
class MultiModelChatClient(ChatClient):
    def __init__(self, client: ModelAdapter):
        self._client = client

    async def chat(
        self,
        messages: Iterable[ChatMessageModel],
        options: ChatOptionsModel,
        tools: Optional[List[FunctionCallToolModel]],
    ) -> ChatResponse:

        payload_messages = [asdict(m) | {"content": m.content} for m in messages]

        return await self._client.chat_create(
            messages=payload_messages, tools=tools, format=options.format
        )

    async def stream(
        self,
        messages: Iterable[ChatMessageModel],
        options: ChatOptionsModel,
        tools: Optional[List[FunctionCallToolModel]],
    ) -> AsyncIterator[str]:

        payload_messages = [asdict(m) | {"content": m.content} for m in messages]

        async with self._client.chat_with_streaming_response(
            messages=payload_messages, tools=tools
        ) as stream:
            for event in stream.iter_lines():
                yield event
