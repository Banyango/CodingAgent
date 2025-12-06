from typing import Union, Sequence, Mapping, Any, List, Optional, Literal

from openai import AsyncOpenAI
from pydantic.json_schema import JsonSchemaValue

from wireup import service

from core.chat.models import FunctionCallReqeustModel, ChatMessageModel

from libs.chat.open_router.config import OpenRouterSettings
from libs.chat.types import Message



@service
class OpenRouterAdapter:
    def __init__(self, config: OpenRouterSettings):
        self.client = AsyncOpenAI(base_url=config.base_url, api_key=config.api_key)
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
        # todo
        # if tools is None:
        #     tools = []
        #
        # prepared_messages = cast(
        #     List[ChatCompletionMessageParam],
        #     [
        #         {
        #             "content": m.content or "",
        #             "role": m.role,
        #         }
        #         if is_dataclass(m)
        #         else m
        #         for m in messages
        #     ],
        # )
        #
        # prepared_tools = [
        #     ChatCompletionFunctionToolParam(
        #         function=FunctionDefinition(
        #             name=t.function.name,
        #             description=t.function.description or "",
        #             parameters=asdict(t.function.parameters),
        #         ),
        #         type="function",
        #     )
        #     if is_dataclass(t)
        #     else t
        #     for t in tools
        # ]
        #
        # response = await self.client.chat.completions.create(
        #     messages=prepared_messages,
        #     model=self.model,
        #     tools=prepared_tools,
        # )
        #
        # parsed_tool_calls = []
        # for tool_call in response.choices[0].message.tool_calls or []:
        #     parsed_tool_calls.append(
        #         ToolCall(
        #             id=tool_call.id,
        #             function=Function(
        #                 name=tool_call.function.name,
        #                 arguments=json.loads(tool_call.function.arguments),
        #             ),
        #         )
        #     )

        return ChatMessageModel(
            role="assistant",
            content="none",
        )
