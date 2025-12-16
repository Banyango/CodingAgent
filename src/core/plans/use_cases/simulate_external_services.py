from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Simulate external services for local development and testing by providing deterministic mocks, failure modes, and performance characteristics.",
    steps=[
        StepModel(
            description="Identify external dependencies to simulate and the behaviors (success, timeouts, errors) to model."
        ),
        StepModel(
            description="Choose simulation strategy: in-process mocks, local stub servers, or service virtualization tools."
        ),
        StepModel(
            description="Implement deterministic responses with configurable delays and error injection for testing resilience."
        ),
        StepModel(
            description="Provide scripts or docker-compose services for running the simulated services locally."
        ),
        StepModel(
            description="Add integration tests that exercise the simulated services and verify retry/backoff logic."
        ),
        StepModel(
            description="Document how to extend or replace simulators with real endpoints for staging tests."
        ),
    ],
)
