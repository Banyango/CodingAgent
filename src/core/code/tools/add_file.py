import asyncio
from pathlib import Path
from typing import Dict, Any

from loguru import logger
from wireup import service

from core.agent.interfaces import Tool
from core.code.models import ToolErrorModel
from core.code.services import FileService


@service
class AddFile(Tool):
    description = "Adds a file to the specified directory."

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    async def execute_async(
        self, file_path: str, file_name: str, context: Dict[str, Any]
    ) -> str | ToolErrorModel:
        """Create the directory (if needed) and touch the target file.

        Args:
            file_path (str): The directory path where the file will be added.
            file_name (str): The name of the file to be added.
            context (Dict[str, Any]): Additional context for the operation.
        """
        error = self.file_service.validate_file_path(
            tool_name="AddFile",
            file_path=file_path,
            project_root=context["project_root"],
            target_type="dir",
        )
        if error:
            return error

        dir_path = Path(context["project_root"]) / Path(file_path)
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            target = dir_path / file_name
            # Run the blocking touch in a thread
            await asyncio.to_thread(target.touch, True)

            return f"File {file_name} added at {file_path}"
        except Exception as exc:
            logger.error(f"Failed to add file {file_name} at {file_path}: {exc}")
            return f"Failed to add file {file_name} at {file_path}: {exc}"
