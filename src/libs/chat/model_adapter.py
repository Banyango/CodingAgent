from abc import abstractmethod, ABC
from typing import Union, Sequence, Mapping, Any, List, Optional, Literal

from pydantic.json_schema import JsonSchemaValue
from wireup import abstract

from core.chat.models import FunctionCallToolModel
from libs.chat.types import ChatResponse, Message

@abstract
class ModelAdapter(ABC):
    @abstractmethod
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
        pass

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
        pass