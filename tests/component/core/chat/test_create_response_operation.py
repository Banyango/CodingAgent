import os

import pytest
import wireup

import core
import libs

from core.interfaces.memory import AgentMemoryService
from core.interfaces.chat import ChatClient
from core.agent.operations.create_response_operation import CreateAgentResponseOperation
from core.interfaces.plan import PlanRepository


@pytest.mark.asyncio
async def test_create_response_operation():
    # Arrange
    headless_app = wireup.create_async_container(
        service_modules=[
            core,
            libs,
        ]
    )

    chat_client = await headless_app.get(ChatClient)
    memory_service = await headless_app.get(AgentMemoryService)
    plan_repository = await headless_app.get(PlanRepository)
    await plan_repository.init_collection()

    _sut = CreateAgentResponseOperation(
        client=chat_client,
        container=headless_app,
        memory_service=memory_service,
        plan_repository=plan_repository,
    )

    # Act
    response = await _sut.execute_async(
        """
        Create a unit test for src/libs/disk/services.py it should go into tests/unit/libs/disk/test_services.py
        """,
        context={"project_root": os.path.abspath(".")},
    )

    # Assert
    assert response is not None
    print(response)
