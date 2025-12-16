from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Generate deterministic and randomized mock data or test fixtures aligned with schemas and privacy constraints for unit and integration tests.",
    steps=[
        StepModel(
            description="Identify schemas and constraints for the data you need to generate (types, lengths, relationships)."
        ),
        StepModel(
            description="Choose tooling for fixtures: factory_boy, pytest fixtures, faker, or custom generators."
        ),
        StepModel(
            description="Create reusable factories and fixtures that can produce deterministic and randomized data."
        ),
        StepModel(
            description="Provide small and large dataset generators to support unit tests and performance tests."
        ),
        StepModel(
            description="Add fixtures for common scenarios and edge cases (empty sets, max sizes, invalid records)."
        ),
        StepModel(
            description="Store seed snapshots for integration tests and document how to refresh them."
        ),
        StepModel(
            description="Ensure sensitive fields are obfuscated and that generated data conforms to privacy rules."
        ),
    ],
)
