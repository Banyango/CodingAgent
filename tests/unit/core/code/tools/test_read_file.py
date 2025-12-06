import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from core.code.models import ToolErrorModel
from core.code.tools.read_file import ReadFile


@pytest.mark.asyncio
async def test_execute_async_returns_file_contents_when_input_is_valid():
    # Arrange
    file_service_mock = MagicMock()
    file_service_mock.validate_file_path.return_value = None
    tool = ReadFile(file_service=file_service_mock)

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        file_name = "sample.txt"
        content = "hello world\nthis is a test"
        (base / file_name).write_text(content, encoding="utf-8")

        file_path = file_name
        context = {"project_root": tmpdir}

        # Act
        result = await tool.execute_async(file_path, context)  # type: ignore

        # Assert
        assert isinstance(result, str)
        assert content in result


@pytest.mark.asyncio
async def test_execute_async_returns_file_error_when_validation_fails():
    # Arrange
    file_service_mock = MagicMock()
    file_service_mock.validate_file_path.return_value = ToolErrorModel(
        tool_name="test", error_message="validation error"
    )
    tool = ReadFile(file_service=file_service_mock)

    # Act
    result = await tool.execute_async("test", {"project_root": "/project"})

    # Assert
    assert isinstance(result, ToolErrorModel)
    assert result.error_message == "validation error"
