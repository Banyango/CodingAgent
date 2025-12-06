from typing import List, Dict, Any

from pydantic import BaseModel
from wireup import service

from core.interfaces.chat import ChatClient
from core.chat.models import ChatMessageModel, ChatOptionsModel


class Step(BaseModel):
    completed: bool
    description: str


class Plan(BaseModel):
    steps: List[Step]


@service
class AgentPlanService:
    def __init__(self, chat_client: ChatClient):
        self.chat_client = chat_client

    async def create_plan(
        self, message_input: str, system_prompt: str, context: Dict[str, Any]
    ) -> Plan:
        """
        Create a plan based on the given message_input.

        Args:
            message_input (str): The input string to process.
            system_prompt (str): The system prompt to guide the plan creation.
            context (Dict[str, Any]): Additional context for the agent that will be passed to all tools.
        """
        response = await self.chat_client.chat(
            messages=[
                ChatMessageModel(
                    role="system",
                    content=system_prompt,
                ),
                ChatMessageModel(
                    role="user",
                    content=f"Create a multi-step plan to address the following request: {message_input}",
                ),
            ],
            tools=None,
            options=ChatOptionsModel(temperature=0.7, format=Plan.model_json_schema()),
        )

        if response.content:
            return Plan.model_validate_json(response.content)

        return Plan(steps=[])
