import asyncio
from pathlib import Path

from loguru import logger
from wireup import service

from core.agent.interfaces import Tool
import os
import tempfile

from core.code.models import CodeContext, ToolErrorModel
from core.code.services import FileService


@service
class ModifyFile(Tool):
    description = "Modify a file."

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    @staticmethod
    def _write_atomic(path: Path, new_content: str) -> None:
        parent = path.parent
        # Create a temp file in the same directory so os.replace is atomic
        fd, tmp_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(parent))
        try:
            # Write text using the file descriptor and ensure it's flushed to disk
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(new_content)
                f.flush()
                os.fsync(f.fileno())

            # Atomically replace the target file with the temp file
            os.replace(tmp_path, str(path))
        finally:
            # If something went wrong and the temp still exists, try to remove it
            if os.path.exists(tmp_path):
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass

    async def execute_async(
        self, file_path: str, new_content: str, context: CodeContext
    ) -> str | ToolErrorModel:
        """Atomically replace the contents of `file_path` with `new_content`.

        Args:
            file_path (str): The full path to the file to be modified.
            new_content (str): The new content to write to the file.
            context (CodeContext): Additional context for the operation.
        """
        error = self.file_service.validate_file_path(
            tool_name="ModifyFile",
            file_path=file_path,
            project_root=context["project_root"],
        )
        if error:
            return error

        path = Path(context["project_root"]) / Path(file_path)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)

            await asyncio.to_thread(self._write_atomic, path, new_content)

            return f"ModifyFile - file_path = {file_path} updated to {new_content}"
        except Exception as exc:
            logger.error(f"Failed to modify file {file_path}: {exc}")
            return f"Failed to modify file {file_path}: {exc}"
