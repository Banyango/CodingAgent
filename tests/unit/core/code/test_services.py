import tempfile
from pathlib import Path

from core.code.services import FileService


def test_validate_file_path_should_return_error_when_path_outside_project_root():
    # Arrange
    tool = FileService()

    # Act
    result = tool.validate_file_path("test", "../path/to/file.txt", "/project")

    # Assert
    assert result is not None
    assert (
        "Access to paths outside the project root is not allowed."
        in result.error_message
    )
    assert result.tool_name == "test"


def test_validate_file_path_should_respond_with_error_when_file_does_not_exist():
    # Arrange
    tool = FileService()

    # Act
    result = tool.validate_file_path("test", "file.txt", "/project")

    # Assert
    assert result is not None
    assert "The file file.txt does not exist." in result.error_message


def test_validate_file_path_should_respond_with_error_when_path_exists_but_is_not_file():
    # Arrange
    tool = FileService()
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        dir_name = "mydir"
        (base / dir_name).mkdir()

        # Act
        result = tool.validate_file_path("test", "mydir", tmpdir)

        # Assert
        assert result is not None
        assert "The path mydir is not a file." in result.error_message


def test_validate_file_path_should_respond_with_error_when_path_is_absolute():
    # Arrange
    tool = FileService()

    # Act
    result = tool.validate_file_path(
        "test",
        "/absolute/path/to/file.txt",
        "/some/project",
    )

    # Assert
    assert result is not None
    assert "Absolute paths are not allowed." in result.error_message
    assert result.tool_name == "test"
