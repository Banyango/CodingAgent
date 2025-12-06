from dataclasses import dataclass
from typing import Any, TypedDict


@dataclass
class CodeOutputModel:
    output: Any
    logs: str
    is_final_answer: bool


@dataclass
class ToolErrorModel:
    tool_name: str
    error_message: str


class CodeContext(TypedDict):
    project_root: str
