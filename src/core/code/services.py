from pathlib import Path
from typing import Literal

from wireup import service

from core.code.models import ToolErrorModel


@service
class FileService:
    @staticmethod
    def validate_file_path(
        tool_name: str,
        file_path: str,
        project_root: str,
        target_type: Literal["file", "dir"] = "file",
    ) -> None | ToolErrorModel:
        """Validate that the given file_path is within the project_root and exists as the specified target_type.

        Args:
            tool_name (str): The name of the tool requesting validation.
            file_path (str): The file path to validate (relative to project_root).
            project_root (str): The root directory of the project.
            target_type (Literal["file", "dir"]): The expected type of the target path ("file" or "dir").
        """
        path = Path(file_path)
        project_root_path = Path(project_root)

        # Build the target path: if path is absolute use it directly, otherwise join with project_root
        if path.is_absolute():
            return ToolErrorModel(
                tool_name=tool_name, error_message="Absolute paths are not allowed."
            )

        target = project_root_path / path

        try:
            root_resolved = project_root_path.resolve(strict=False)
            target_resolved = target.resolve(strict=False)
        except Exception as exc:
            return ToolErrorModel(
                tool_name=tool_name, error_message=f"Error resolving paths: {exc}"
            )

        try:
            target_resolved.relative_to(root_resolved)
        except Exception:
            return ToolErrorModel(
                tool_name=tool_name,
                error_message="Access to paths outside the project root is not allowed.",
            )

        if not target_resolved.exists():
            return ToolErrorModel(
                tool_name=tool_name,
                error_message=f"The file {file_path} does not exist.",
            )

        if target_type == "file" and not target_resolved.is_file():
            return ToolErrorModel(
                tool_name=tool_name,
                error_message=f"The path {file_path} is not a file.",
            )

        if target_type == "dir" and not target_resolved.is_dir():
            return ToolErrorModel(
                tool_name=tool_name,
                error_message=f"The path {file_path} is not a directory.",
            )

        return None
