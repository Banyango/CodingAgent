from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Create focused unit tests for a function or method, covering typical behavior and edge cases with deterministic assertions and fixtures.",
    steps=[
        StepModel(description="Identify the function or method to be tested."),
        StepModel(description="Query any supporting files that might be needed."),
        StepModel(description="Focus on cyclomatic complexity to cover edge cases."),
        StepModel(
            description="Follow the style guidelines for the project and add the unit test."
        ),
        StepModel(description="Verify the unit test works as expected."),
    ],
)
