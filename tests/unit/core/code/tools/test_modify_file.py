from unittest.mock import MagicMock
import tempfile
from pathlib import Path

import pytest

from core.code.tools.modify_file import ModifyFile


@pytest.mark.asyncio
async def test_execute_modifies_file_when_input_is_valid():
    # Arrange
    file_service_mock = MagicMock()
    file_service_mock.validate_file_path.return_value = None

    tool = ModifyFile(file_service=file_service_mock)

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        # create initial file
        file_path = base / "dir" / "file.txt"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("old")

        new_content = "new content"

        # Act
        result = await tool.execute_async(
            str(file_path), new_content, {"project_root": tmpdir}
        )

        # Assert
        assert (
            result == f"ModifyFile - file_path = {file_path} updated to {new_content}"
        )
        assert file_path.read_text(encoding="utf-8") == new_content


@pytest.mark.asyncio
async def test_execute_creates_parent_and_writes_when_parent_missing():
    # Arrange
    file_service_mock = MagicMock()
    file_service_mock.validate_file_path.return_value = None

    tool = ModifyFile(file_service=file_service_mock)

    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        file_path = base / "non" / "existent" / "file.txt"
        new_content = "created content"

        # Act
        await tool.execute_async(str(file_path), new_content, {"project_root": tmpdir})

        # Assert
        assert f"ModifyFile - file_path = {file_path} updated to created content {new_content}"
        assert file_path.exists()
        assert file_path.read_text(encoding="utf-8") == new_content
