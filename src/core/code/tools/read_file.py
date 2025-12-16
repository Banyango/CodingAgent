import asyncio
from pathlib import Path

from loguru import logger
from wireup import service

from core.interfaces.tool import Tool
from core.code.models import ToolErrorModel, CodeContext
from core.code.services import FileService


@service
class ReadFile(Tool):
    description = "Reads the contents of a specified file. file_path must be relative to project_root."

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    async def execute_async(
        self, file_path: str, context: CodeContext
    ) -> str | ToolErrorModel:
        """Read and return the contents of the specified file.

        Args:
            file_path (str): The file path to read (absolute or relative to project_root).
            context (CodeContext): Additional context for the operation.
        """
        error = self.file_service.validate_file_path(
            tool_name="ReadFile",
            file_path=file_path,
            project_root=context["project_root"],
        )
        if error:
            return error

        target = Path(context["project_root"]) / Path(file_path)

        try:
            content = await asyncio.to_thread(target.read_text, encoding="utf-8")
            return f"""
ReadFile - file_path: {file_path}
{content}"""
        except Exception as exc:
            logger.error(f"Failed to read file {file_path}: {exc}")

            return ToolErrorModel(
                tool_name="ReadFile",
                error_message=f"Failed to read file {file_path}: {exc}",
            )
