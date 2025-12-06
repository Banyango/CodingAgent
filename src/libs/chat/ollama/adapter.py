from typing import Union, Sequence, Mapping, Any, List, Optional, Literal

import ollama
from pydantic.json_schema import JsonSchemaValue

from wireup import service

from core.chat.models import FunctionCallReqeustModel, ChatMessageModel, FunctionCallResponseModel
from libs.chat.ollama.config import OllamaAISettings
from libs.chat.types import Message
from dataclasses import asdict, is_dataclass


@service
class OllamaAdapter:
    def __init__(self, config: OllamaAISettings):
        self.client = ollama.AsyncClient(config.base_url)
        self.model = config.model

    async def chat_create(
        self,
        messages: Sequence[Union[Mapping[str, Any], Message]],
        tools: List[FunctionCallReqeustModel],
        format: Optional[Union[Literal["", "json"], JsonSchemaValue]],
        think: Optional[bool] = None,
    ) -> ChatMessageModel:
        """
        Create a chat completion

        Args:
            messages (Sequence[Union[Mapping[str, Any], Message]]): The messages to send to the chat model.
            tools (List[FunctionCallReqeustModel]): The tools available for function calling.
            format (Optional[Union[Literal['', 'json'], JsonSchemaValue]]): The format for the response.
            think (Optional[bool]): Whether to enable thinking mode.
        """
        if tools is None:
            tools = []

        prepared_messages = [
            {
                "content": m.content,
                "thinking": m.thinking,
                "tool_name": m.tool_name,
                "tool_calls": m.tool_calls or [],
                "role": m.role,
            }
            if is_dataclass(m)
            else m
            for m in messages
        ]
        prepared_tools = [asdict(t) if is_dataclass(t) else t for t in tools]

        response = await self.client.chat(
            model=self.model,
            messages=prepared_messages,
            tools=prepared_tools,
            format=format,
            think=think,
        )

        return ChatMessageModel(
            role="assistant",
            content=response.message.content or "",
            thinking=response.message.thinking or "",
            tool_name=response.message.tool_name or "",
            tool_calls=[
                FunctionCallResponseModel(
                    name=tool_call.function.name,
                    arguments=dict(tool_call.function.arguments),
                )
                for tool_call in (response.message.tool_calls or [])
            ],
        )
