from abc import abstractmethod, ABC
from typing import Union, List, Optional, Literal

from pydantic.json_schema import JsonSchemaValue
from wireup import abstract

from core.chat.models import FunctionCallReqeustModel, ChatMessageModel


@abstract
class ModelAdapter(ABC):
    @abstractmethod
    async def chat_create(
        self,
        messages: List[ChatMessageModel],
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
        pass
