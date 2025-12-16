from typing import Union, List, Optional, Literal

from google.genai import types
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    GenerateContentResponse,
    Part,
    Content,
    Tool,
    Schema,
    Type,
)
from pydantic.json_schema import JsonSchemaValue

from wireup import service

from google import genai

from core.chat.models import (
    FunctionCallReqeustModel,
    ChatMessageModel,
    FunctionCallResponseModel,
)
from libs.chat.gemini.config import GeminiAISettings
from libs.chat.model_adapter import ModelAdapter


class GeminiClient:
    def __init__(self, config: GeminiAISettings):
        self.client = genai.client.AsyncClient(
            api_client=genai.client.BaseApiClient(api_key=config.api_key)
        )
        self.model = config.model


@service
def gemini_client_factory(
    config: GeminiAISettings,
) -> GeminiClient:
    return GeminiClient(config=config)


@service
class GeminiAdapter(ModelAdapter):
    def __init__(self, client: GeminiClient):
        self.client = client

    async def chat_create(
        self,
        messages: List[ChatMessageModel],
        tools: List[FunctionCallReqeustModel],
        format: Optional[Union[Literal["", "json"], JsonSchemaValue]],
        think: Optional[bool] = None,
    ) -> ChatMessageModel:
        """Create a chat completion

        Args:
            messages (Sequence[Union[Mapping[str, Any], Message]]): The messages to send to the chat model.
            tools (List[FunctionCallReqeustModel]): The tools available for function calling.
            format (Optional[Union[Literal['', 'json'], JsonSchemaValue]]): The format for the response.
            think (Optional[bool]): Whether to enable thinking mode.
        """
        function_definitions = []
        for tool in tools:
            function_definitions.append(
                FunctionDeclaration(
                    name=tool.function.name,
                    description=tool.function.description,
                    parameters=Schema(
                        type=Type(tool.function.parameters.type),
                        properties={
                            k: Schema(**v.model_dump())
                            for k, v in tool.function.parameters.properties.items()
                        },
                        required=tool.function.parameters.required,
                    ),
                )
            )

        prepared_messages = []
        system_instruction = []
        for message in messages:
            if message.role == "tool":
                prepared_messages.append(
                    Content(
                        role="user",
                        parts=[
                            types.Part.from_function_response(
                                name=message.tool_name or "unknown_tool",
                                response={"result": message.content},
                            )
                        ],
                    )
                )
            elif message.role == "system":
                system_instruction = Content(parts=[Part(text=message.content)])
            elif message.role == "assistant":
                prepared_messages.append(
                    Content(
                        role="model",
                        parts=[
                            Part(
                                text=message.content,
                                thought_signature=message.thinking
                                if isinstance(message.thinking, bytes)
                                else None,
                            )
                        ],
                    )
                )
            else:
                prepared_messages.append(
                    Content(role="user", parts=[Part(text=message.content)])
                )

        if len(prepared_messages) == 0:
            raise ValueError(
                "At least one user message is required to generate a chat response."
            )

        response: GenerateContentResponse = (
            await self.client.client.models.generate_content(
                model=self.client.model,
                contents=prepared_messages,
                config=GenerateContentConfig(
                    tools=[Tool(function_declarations=function_definitions)],
                    thinking_config=types.ThinkingConfig(include_thoughts=think),
                    system_instruction=system_instruction,
                ),
            )
        )

        return ChatMessageModel(
            role="assistant",
            content=response.text or "",
            thinking=response.parts[0].thought_signature if response.parts else None,
            tool_calls=[
                FunctionCallResponseModel(
                    name=function_call.name or "unknown_function",
                    arguments=function_call.args or {},
                )
                for function_call in response.function_calls or []
            ],
        )
