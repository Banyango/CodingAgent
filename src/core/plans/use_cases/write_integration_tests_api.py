from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Write reliable API integration tests including environment setup, dependency mocking or staging services, and CI integration.",
    steps=[
        StepModel(
            description="Define test scenarios that cover important API flows, error paths, authentication, and edge cases."
        ),
        StepModel(
            description="Set up test fixtures for the environment: test DB, seeded data, and mocks for external services."
        ),
        StepModel(
            description="Write integration tests that exercise real endpoints and validate responses, side effects, and DB state."
        ),
        StepModel(
            description="Add retry/backoff logic in tests for flaky external dependencies or use mocks to avoid flakiness."
        ),
        StepModel(
            description="Run integration tests in CI with proper secrets and isolation; ensure tests are hermetic where possible."
        ),
        StepModel(
            description="Document how to run integration tests locally and in the CI environment."
        ),
    ],
)
