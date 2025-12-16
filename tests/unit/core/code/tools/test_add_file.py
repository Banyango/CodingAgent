import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from core.code.models import ToolErrorModel, CodeContext
from core.code.tools.add_file import AddFile


@pytest.mark.asyncio
async def test_execute_adds_file_when_input_is_valid():
    # Arrange
    file_service = MagicMock()
    file_service.validate_file_path.return_value = None
    tool = AddFile(file_service=file_service)

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = tmpdir
        file_name = "test.txt"
        context = CodeContext(project_root=tmpdir)

        # Act
        result = await tool.execute_async(file_path, file_name, "contents", context)

        # Assert
        target = Path(file_path) / file_name
        assert target.exists(), "Expected the file to be created on disk"
        assert (
            result == f"File {file_name} added at {file_path} and added the contents."
        )


@pytest.mark.asyncio
async def test_execute_returns_error_when_path_outside_project_root():
    # Arrange
    file_service = MagicMock()

    error_model = ToolErrorModel(
        tool_name="test", error_message="Path is outside of project root"
    )
    file_service.validate_file_path.return_value = error_model

    tool = AddFile(file_service=file_service)

    # Act
    result = await tool.execute_async(
        "/some/path", "file.txt", "contents", {"project_root": "/project"}
    )

    # Assert
    assert isinstance(result, ToolErrorModel)
    assert result == error_model
    assert result.error_message == "Path is outside of project root"


@pytest.mark.asyncio
async def test_execute_should_add_file_when_sub_dir_doesnt_exist():
    # Arrange
    file_service = MagicMock()
    file_service.validate_file_path.return_value = None
    tool = AddFile(file_service=file_service)

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = "subdir1/subdir2/subdir3"
        file_name = "test.txt"
        context = CodeContext(project_root=tmpdir)

        # Act
        result = await tool.execute_async(file_path, file_name, "contents", context)

        # Assert
        target = Path(tmpdir) / file_path / file_name
        assert target.exists(), "Expected the file to be created on disk"
        assert (
            result == f"File {file_name} added at {file_path} and added the contents."
        )
