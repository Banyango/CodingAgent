from fastapi import APIRouter
from wireup import Injected

from app.apis.v1.conversations.requests import ConversationRequest
from app.container import container
from core.agent.operations.create_response_operation import CreateAgentResponseOperation
from core.interfaces.chat import ChatClient
from core.interfaces.memory import AgentMemoryService
from core.interfaces.plan import PlanRepository

router = APIRouter()


@router.post("/conversations", tags=["conversations"])
async def create_conversation(
    request: ConversationRequest,
    chat_client: Injected[ChatClient],
    memory_service: Injected[AgentMemoryService],
    plan_repository: Injected[PlanRepository],
):
    create_conversation_operation = CreateAgentResponseOperation(
        client=chat_client,
        container=container,
        memory_service=memory_service,
        plan_repository=plan_repository,
    )

    response = await create_conversation_operation.execute_async(
        request.message,
        context={"project_root": request.project_root},
    )

    return response
