from pathlib import Path
from unittest.mock import MagicMock
import tempfile

import pytest

from core.code.models import ToolErrorModel, CodeContext
from core.code.tools.list_dir import ListDir


@pytest.mark.asyncio
async def test_execute_lists_directory_entries_when_input_is_valid():
    # Arrange
    file_service_mock = MagicMock()
    file_service_mock.validate_file_path.return_value = None
    tool = ListDir(file_service=file_service_mock)

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        sub = base / "subdir"
        sub.mkdir()
        # create files
        files = [sub / "a.txt", sub / "b.txt", sub / "c.md"]
        for f in files:
            f.write_text("content")

        file_path = tmpdir + "/subdir"
        context = CodeContext(project_root=tmpdir)

        # Act
        result = await tool.execute_async(file_path, context)

        # Assert
        assert f"\nListDir at {sub.as_posix()}:\nc.md, b.txt, a.txt\n" == result


@pytest.mark.asyncio
async def test_execute_returns_error_when_path_outside_project_root():
    # Arrange
    file_service_mock = MagicMock()
    error_model = ToolErrorModel(
        tool_name="ModifyFile", error_message="Path is outside of project root"
    )
    file_service_mock.validate_file_path.return_value = error_model

    tool = ListDir(file_service=file_service_mock)

    # Act
    result = await tool.execute_async("/irrelevant", {"project_root": "/project"})

    # Assert
    assert result == error_model
