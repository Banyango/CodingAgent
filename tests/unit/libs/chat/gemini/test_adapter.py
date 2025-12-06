from unittest.mock import AsyncMock

import pytest
from google.genai.types import (
    GenerateContentResponse,
    Candidate,
    Content,
    Part,
    Type,
)

from core.chat.models import (
    FunctionCallReqeustModel,
    FunctionModel,
    ParametersModel,
    PropertyModel,
    ChatMessageModel,
)
from libs.chat.gemini.adapter import GeminiAdapter


@pytest.mark.asyncio
async def test_chat_create_should_add_tool_when_tools_are_defined():
    # Arrange
    mock_client = AsyncMock()
    mock_client.client.models.generate_content = AsyncMock()
    mock_client.client.models.generate_content.return_value = GenerateContentResponse(
        candidates=[
            Candidate(
                content=Content(
                    parts=[
                        Part(
                            text="The current weather in Calgary is sunny with a temperature of 25°C."
                        )
                    ]
                )
            )
        ]
    )

    _sut = GeminiAdapter(client=mock_client)

    # Act
    await _sut.chat_create(
        messages=[ChatMessageModel(role="user", content="Hello")],
        tools=[
            FunctionCallReqeustModel(
                type="object",
                function=FunctionModel(
                    name="test",
                    description="A test function",
                    parameters=ParametersModel(
                        type="object",
                        properties={
                            "test": PropertyModel(
                                type="string",
                                description="A test parameter",
                            )
                        },
                        required=[],
                    ),
                ),
            )
        ],
        format=None,
    )

    # Assert
    mock_client.client.models.generate_content.assert_awaited()
    args, kwargs = mock_client.client.models.generate_content.call_args
    config = kwargs.get("config", [])
    assert len(config.tools) == 1
    function_definitions = config.tools[0].function_declarations
    assert function_definitions[0].name == "test"
    assert function_definitions[0].description == "A test function"
    assert function_definitions[0].parameters.properties["test"].type == Type.STRING


@pytest.mark.asyncio
async def test_chat_create_should_add_tool_call_when_tool_response_exists():
    # Arrange
    mock_client = AsyncMock()
    mock_client.client.models.generate_content = AsyncMock()
    mock_client.client.models.generate_content.return_value = GenerateContentResponse(
        candidates=[Candidate(content=Content(parts=[Part(text="Test response")]))]
    )

    _sut = GeminiAdapter(client=mock_client)

    # Act
    await _sut.chat_create(
        messages=[ChatMessageModel(role="user", content="Hello")],
        tools=[
            FunctionCallReqeustModel(
                type="object",
                function=FunctionModel(
                    name="test",
                    description="A test function",
                    parameters=ParametersModel(
                        type="object",
                        properties={
                            "test": PropertyModel(
                                type="string",
                                description="A test parameter",
                            )
                        },
                        required=[],
                    ),
                ),
            )
        ],
        format=None,
    )

    # Assert
    mock_client.client.models.generate_content.assert_awaited()
    args, kwargs = mock_client.client.models.generate_content.call_args
    contents = kwargs.get("contents", [])
    assert len(contents) == 1
    assert contents[0].role == "user"
    assert contents[0].parts[0].text == "Hello"


@pytest.mark.asyncio
async def test_chat_create_should_add_add_user_and_assistant_messages():
    # Arrange
    mock_client = AsyncMock()
    mock_client.client.models.generate_content = AsyncMock()
    mock_client.client.models.generate_content.return_value = GenerateContentResponse(
        candidates=[
            Candidate(content=Content(parts=[Part(text="I can help you with that!")]))
        ]
    )

    _sut = GeminiAdapter(client=mock_client)

    # Act
    await _sut.chat_create(
        messages=[
            ChatMessageModel(role="user", content="Hello, how are you?"),
            ChatMessageModel(role="assistant", content="I'm doing great!"),
            ChatMessageModel(role="user", content="Can you help me?"),
        ],
        tools=[],
        format=None,
    )

    # Assert
    mock_client.client.models.generate_content.assert_awaited()
    args, kwargs = mock_client.client.models.generate_content.call_args
    contents = kwargs.get("contents", [])
    assert len(contents) == 3
    assert contents[0].role == "user"
    assert contents[0].parts[0].text == "Hello, how are you?"
    assert contents[1].role == "assistant"
    assert contents[1].parts[0].text == "I'm doing great!"
    assert contents[2].role == "user"
    assert contents[2].parts[0].text == "Can you help me?"
