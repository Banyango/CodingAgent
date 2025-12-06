import pytest
import wireup

import core
import libs
from core.chat.models import (
    FunctionCallReqeustModel,
    FunctionModel,
    ParametersModel,
    PropertyModel, ChatMessageModel,
)
from libs.chat.gemini.adapter import GeminiAdapter


@pytest.mark.asyncio
async def test_gemini_adapter_chat_create_should_get_response_with_message():
    # Arrange
    headless_app = wireup.create_async_container(
        service_modules=[
            core,
            libs,
        ]
    )

    gemini = await headless_app.get(GeminiAdapter)

    # Call chat_create with a simple message and no tools
    response = await gemini.chat_create(
        messages=[ChatMessageModel(role="user", content="hello")], tools=[], format=None
    )

    # Assertions
    assert response is not None
    assert response.role == "assistant"
    assert response.content is not None


@pytest.mark.asyncio
async def test_gemini_adapter_chat_create_should_get_response_with_tools():
    # Arrange
    headless_app = wireup.create_async_container(
        service_modules=[
            core,
            libs,
        ]
    )

    gemini = await headless_app.get(GeminiAdapter)

    # Call chat_create with a simple message and no tools
    response = await gemini.chat_create(
        messages=[
            ChatMessageModel(role="user", content="what is the current weather in Calgary")
        ],
        tools=[
            FunctionCallReqeustModel(
                type="function",
                function=FunctionModel(
                    name="get_current_weather",
                    description="Get the current weather in a given location",
                    parameters=ParametersModel(
                        type="object",
                        properties={
                            "location": PropertyModel(
                                type="string",
                                description="The city and state, e.g. San Francisco, CA",
                            ),
                            "unit": PropertyModel(
                                type="string",
                                description="The unit of temperature. 'celsius' or 'fahrenheit'.",
                            ),
                        },
                        required=["location"],
                    ),
                ),
            )
        ],
        format=None,
    )

    # Assertions
    assert response is not None
    assert response.role == "assistant"
    assert response.tool_calls is not None
    assert len(response.tool_calls) > 0
