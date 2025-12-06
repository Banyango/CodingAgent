from abc import ABC, abstractmethod
from typing import Any

from wireup import abstract

from core.agent.providers import Tool
from core.code.models import CodeOutputModel


@abstract
class PythonExecutor(ABC):
    @abstractmethod
    def send_tools(self, tools: dict[str, Tool]) -> None: ...

    @abstractmethod
    def send_variables(self, variables: dict[str, Any]) -> None: ...

    @abstractmethod
    def __call__(self, code_action: str) -> CodeOutputModel: ...
