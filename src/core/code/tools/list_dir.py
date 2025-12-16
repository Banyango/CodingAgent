import asyncio
from pathlib import Path

from loguru import logger
from wireup import service

from core.interfaces.tool import Tool
from core.code.models import CodeContext, ToolErrorModel
from core.code.services import FileService


@service
class ListDir(Tool):
    description = "Lists the contents of a specified directory."

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    async def execute_async(
        self, file_path: str, context: CodeContext
    ) -> str | ToolErrorModel:
        """List and return the contents of the specified directory.

        Args:
            file_path (str): The directory path where the target directory is located.
            context (CodeContext): Additional context for the operation.
        """
        error = self.file_service.validate_file_path(
            tool_name="ListDir",
            file_path=file_path,
            project_root=context["project_root"],
        )
        if error:
            return error

        target = Path(context["project_root"]) / Path(file_path)

        try:
            # Run the blocking iterdir in a thread
            entries = await asyncio.to_thread(
                lambda: [p.name for p in target.iterdir()]
            )
            return f"""
ListDir at {file_path}:
{", ".join(entries)}
"""
        except Exception as exc:
            logger.error(f"Failed to list directory at {file_path}: {exc}")
            return f"Failed to list directory at {file_path}: {exc}"
