from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Explain what a piece of code does, identify potential bugs, and propose minimal reproducible fixes with tests and annotations.",
    steps=[
        StepModel(
            description="Collect the file(s) and a minimal reproduction or example inputs to run the code if possible."
        ),
        StepModel(
            description="Read code top-to-bottom, noting data flow, side effects, external dependencies, and implicit assumptions."
        ),
        StepModel(
            description="Summarize the high-level goal of the code in plain language and list its inputs/outputs."
        ),
        StepModel(
            description="Annotate tricky areas with comments: invariants, preconditions, return value expectations, and performance notes."
        ),
        StepModel(
            description="Run the code with representative inputs, capture outputs, and compare with expected behavior."
        ),
        StepModel(
            description="Look for common bug patterns: off-by-one, mutable default args, race conditions, unhandled exceptions, and incorrect resource cleanup."
        ),
        StepModel(
            description="Identify edge cases not covered by tests and propose fixes or guard clauses."
        ),
        StepModel(
            description="Propose minimal, behavior-preserving fixes and unit tests demonstrating the bug and the fix."
        ),
        StepModel(
            description="Document the explanation and suggested fixes in comments and/or a short report with reproducer steps."
        ),
        StepModel(
            description="Optional: suggest further refactors or performance optimizations if complexity or inefficiency is observed."
        ),
    ],
)
