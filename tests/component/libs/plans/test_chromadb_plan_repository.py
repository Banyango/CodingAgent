import pytest
import wireup

import core
import libs
from core.interfaces.plan import PlanRepository


@pytest.mark.asyncio
async def test_search_plans_should_return_result():
    # Arrange
    headless_app = wireup.create_async_container(
        service_modules=[
            core,
            libs,
        ]
    )

    repository = await headless_app.get(PlanRepository)
    await repository.init_collection()

    # Act
    response = await repository.search_plans("create a react project")

    # Assert
    assert response is not None


@pytest.mark.asyncio
async def test_search_plans_evaluate_results():
    # Arrange
    headless_app = wireup.create_async_container(
        service_modules=[
            core,
            libs,
        ]
    )

    repository = await headless_app.get(PlanRepository)
    await repository.init_collection()

    # Act
    responses = []

    queries = [
        "create focused unit tests for a function",
        "build a RESTful API with authentication",
        "design a responsive web page layout",
        "implement a caching mechanism for a web application",
        "optimize database queries for performance",
        "set up continuous integration and deployment (CI/CD) pipeline",
        "develop a mobile app with offline capabilities",
        "create a data visualization dashboard",
        "Figure out what's wrong here",
    ]

    for query in queries:
        response = await repository.search_plans(query)
        responses.append(response.name)

    # output the responses for manual verification
    for query, response in zip(queries, responses):
        print(f"Query: {query}\nResponse: {response}\n")
