from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Write comprehensive unit tests for an existing module or class, covering public API, edge cases, and ensuring deterministic CI runs.",
    steps=[
        StepModel(
            description="Identify the module/class public API and important behaviors to test (happy path, edge cases, error conditions)."
        ),
        StepModel(
            description="Choose a test framework and conventions used by the project (pytest, unittest, jest, etc.)."
        ),
        StepModel(
            description="Create test files mirroring module structure and name test cases clearly and deterministically."
        ),
        StepModel(
            description="Write unit tests for typical inputs and expected outputs (assertions on return values and state changes)."
        ),
        StepModel(
            description="Add tests for boundary cases, invalid inputs, and exception handling; include property and paramized tests where helpful."
        ),
        StepModel(
            description="Use mocks/stubs for external dependencies to keep tests fast and isolated."
        ),
        StepModel(
            description="Add fixture setup/teardown and reusable helper functions for repeated test scaffolding."
        ),
        StepModel(
            description="Run tests locally and in watch mode; ensure deterministic results and fix flakiness."
        ),
        StepModel(
            description="Add tests to CI and enforce coverage gates if desired; document how to run tests."
        ),
        StepModel(
            description="Optional: add mutation or contract tests to increase confidence in critical logic."
        ),
    ],
)
