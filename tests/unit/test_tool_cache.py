from core.agent.providers import ToolsProvider
from core.agent.interfaces import Tool
from core.code.models import ToolErrorModel


class FakeTool(Tool):
    description = "A fake tool for testing"

    async def execute_async(
        self,
        count: int,
        name: str = "bob",
        active: bool = True,
        data: dict | None = None,
        items: list | None = None,
    ) -> str | ToolErrorModel:
        """A simple async method used to test signature serialization."""
        return ""


def test_get_tools_should_return_serialized_tool():
    # Arrange
    tool_cache = ToolsProvider([FakeTool])

    # Act
    tools = tool_cache.get_tools()

    # Assert
    assert tools[0].function is not None
    assert tools[0].function.name == "FakeTool"
    assert tools[0].function.description == "A fake tool for testing"
    assert tools[0].function.parameters is not None
    assert tools[0].function.parameters.type == "object"

    assert set(tools[0].function.parameters.required) == {"count"}

    assert len(tools[0].function.parameters.properties) == 5

    assert tools[0].function.parameters.properties["count"].type == "integer"
    assert tools[0].function.parameters.properties["name"].type == "string"
    assert tools[0].function.parameters.properties["active"].type == "boolean"
    assert tools[0].function.parameters.properties["data"].type == ["object", "null"]
    assert tools[0].function.parameters.properties["items"].type == ["array", "null"]


def test_get_tool_by_name_should_return_tool_when_name_is_valid():
    # Arrange
    tool_cache = ToolsProvider([FakeTool])

    # Act
    tools = tool_cache.get_tool_by_name("FakeTool")

    # Assert
    assert tools == FakeTool


def test_get_tool_by_name_should_return_none_when_name_is_invalid():
    # Arrange
    tool_cache = ToolsProvider([FakeTool])

    # Act
    result = tool_cache.get_tool_by_name("NonExistentTool")

    # Assert
    assert result is None
