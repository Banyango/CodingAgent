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
from core.interfaces.plan import PlanRepository


class CreateAgentResponseOperation:
    def __init__(
        self,
        client: ChatClient,
        container: AsyncContainer,
        memory_service: AgentMemoryService,
        plan_repository: PlanRepository,
    ):
        self.client = client
        self.container = container
        self.memory_service = memory_service
        self.plan_repository = plan_repository

    async def execute_async(self, message: str, context: Dict[str, Any]) -> str:
        """
        Execute the operation to create an agent response.

        Args:
            message (str): The input message for the agent.
            context (Dict[str, Any]): Additional context for the agent that will be passed to all tools.
        """
        plan = await self.plan_repository.search_plans(query=message)

        plan_text = f"'{plan.name}':\n"
        for step in plan.steps:
            plan_text += f"- {step.description}\n"

        system_prompt = f"""
        You are a helpful coding assistant. You have access to tools that can help you manage and manipulate code files within a project.
        Use the provided tools to assist with file operations as needed.
        
        Available tools:
        1. AddFile: Adds a file to the specified directory.
        2. ModifyFile: Modifies the contents of a specified file.
        3. ReadFile: Reads the contents of a specified file.
        4. ListDir: Lists the contents of a specified directory.
        
        All paths are relative to the project root provided in the context. so strip leading slashes from paths.
        
        {plan_text}
        
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
