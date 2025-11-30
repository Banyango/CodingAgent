from typing import Union, Sequence, Mapping, Any, List, Optional, Literal

import ollama
from pydantic.json_schema import JsonSchemaValue

from wireup import service

from core.chat.models import FunctionCallToolModel
from libs.chat.model_adapter import ModelAdapter
from libs.chat.open_router.config import OpenRouterSettings
from libs.chat.types import ChatResponse, Message
from dataclasses import asdict, is_dataclass


@service(qualifier="openrouter")
class OpenRouterAdapter(ModelAdapter):
    def __init__(self, config: OpenRouterSettings):
        self.client = ollama.AsyncClient(config.base_url)
        self.model = config.model

    async def chat_create(
        self,
        messages: Sequence[Union[Mapping[str, Any], Message]],
        tools: List[FunctionCallToolModel],
        format: Optional[Union[Literal["", "json"], JsonSchemaValue]],
        think: Optional[bool] = None,
    ) -> ChatResponse:
        """
        Create a chat completion

        Args:
            messages (Sequence[Union[Mapping[str, Any], Message]]): The messages to send to the chat model.
            tools (List[FunctionCallToolModel]): The tools available for function calling.
            format (Optional[Union[Literal['', 'json'], JsonSchemaValue]]): The format for the response.
            think (Optional[bool]): Whether to enable thinking mode.
        """
        if tools is None:
            tools = []

        prepared_messages = [OllamaMessage(content=m.content, thinking=m.thinking, tool_name=m.tool_name, tool_calls=m.tool_calls, role=m.role).model_dump_json() if is_dataclass(m) else m for m in messages]
        prepared_tools = [asdict(t) if is_dataclass(t) else t for t in tools]

        response = await self.client.chat(
            model=self.model,
            messages=prepared_messages,
            tools=prepared_tools,
            format=format,
            think=think,
        )

        return ChatResponse(
            message=Message(
                role=response.message.role,
                content=response.message.content,
                thinking=response.message.thinking,
                tool_name=response.message.tool_name,
                tool_calls=response.message.tool_calls,
            ),
            done=response.done,
        )

    async def chat_with_streaming_response(
        self,
        messages: Sequence[Union[Mapping[str, Any], Message]],
        tools: List[FunctionCallToolModel],
        format: Optional[Union[Literal["", "json"], JsonSchemaValue]] = None,
        think: Optional[bool] = None,
    ):
        """
        Chat with streaming response

        Args:
            messages (Sequence[Union[Mapping[str, Any], Message]]): The messages to send to the chat model.
            tools (List[FunctionCallToolModel]): The tools available for function calling.
            format (Optional[Union[Literal['', 'json'], JsonSchemaValue]]): The format for the response.
            think (Optional[bool]): Whether to enable thinking mode.
        """
        prepared_messages = [asdict(m) if is_dataclass(m) else m for m in messages]
        prepared_tools = [asdict(t) if is_dataclass(t) else t for t in tools]

        return self.client.chat(
            stream=True,
            model=self.model,
            messages=prepared_messages,
            tools=prepared_tools,
            format=format,
            think=think,
        )
