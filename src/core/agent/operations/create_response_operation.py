from typing import Any, Dict

from wireup import AsyncContainer

from core.agent.agent import Agent
from core.interfaces.memory import AgentMemoryService
from core.agent.providers import ToolsProvider

from core.interfaces.chat import ChatClient

from core.code.tools.add_file import AddFile
from core.code.tools.list_dir import ListDir
from core.code.tools.modify_file import ModifyFile
from core.code.tools.read_file import ReadFile


class CreateAgentResponseOperation:
    def __init__(
        self,
        client: ChatClient,
        container: AsyncContainer,
        memory_service: AgentMemoryService,
    ):
        self.client = client
        self.container = container
        self.memory_service = memory_service

    async def execute_async(self, message: str, context: Dict[str, Any]) -> str:
        """
        Execute the operation to create an agent response.

        Args:
            message (str): The input message for the agent.
            context (Dict[str, Any]): Additional context for the agent that will be passed to all tools.
        """
        system_prompt = """
        You are a helpful coding assistant. You have access to tools that can help you manage and manipulate code files within a project.
        Use the provided tools to assist with file operations as needed.
        
        Available tools:
        1. AddFile: Adds a file to the specified directory.
        2. ModifyFile: Modifies the contents of a specified file.
        3. ReadFile: Reads the contents of a specified file.
        4. ListDir: Lists the contents of a specified directory.
        
        All paths are relative to the project root provided in the context. so strip leading slashes from paths.
        
        Plan:
        1. Understand the user's request.
        2. Determine which tools to use based on the request.
        3. Call the appropriate tools with the necessary arguments.
        4. Return a summary of the actions taken or the requested information.
        
        Evaluate the tool calls and stop when you have run enough tools to answer the user's question or complete the task.
        """

        agent = Agent(
            chat_client=self.client,
            container=self.container,
            tools=ToolsProvider([AddFile, ModifyFile, ReadFile, ListDir]),
            system_prompt=system_prompt,
            memory=self.memory_service,
        )

        return await agent.run_async(message, context=context)
