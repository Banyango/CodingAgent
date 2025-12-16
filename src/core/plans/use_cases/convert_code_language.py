from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Plan and execute conversion of code from one language to another with tests, idiomatic translation, and documentation of semantic differences.",
    steps=[
        StepModel(
            description="Clarify the scope: single module, library, or whole application; identify runtime constraints and external dependencies."
        ),
        StepModel(
            description="Create a compatibility and feature map: language idioms, error handling, concurrency model, and type system differences."
        ),
        StepModel(
            description="Write tests or examples in the source language that define expected behavior and outputs (reproducers)."
        ),
        StepModel(
            description="Translate algorithmic logic first into clear, idiomatic constructs of the target language (types, ownership)."
        ),
        StepModel(
            description="Implement data structures and error handling idioms native to the target language; prefer safety and correctness."
        ),
        StepModel(
            description="Wire up external integrations (DB, network) via target language libraries and adapt configuration and build tooling."
        ),
        StepModel(
            description="Run tests and compare outputs to the original implementation; iterate on edge cases and numeric differences."
        ),
        StepModel(
            description="Benchmark critical code paths and tune idiomatic performance options in the target language."
        ),
        StepModel(
            description="Document differences, migration notes, and any behavior that cannot be exactly reproduced due to language semantics."
        ),
    ],
)
