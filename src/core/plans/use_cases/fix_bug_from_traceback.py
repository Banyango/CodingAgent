from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Diagnose and fix a bug using the provided error message and stack trace; produce a minimal reproducer, apply a regression test, and document the fix/postmortem.",
    steps=[
        StepModel(
            description="Collect the exact error message, stack trace, input data, and steps to reproduce the failure."
        ),
        StepModel(
            description="Map stack frames to the source code and identify the failing module, function, and line."
        ),
        StepModel(
            description="Read the nearby code and variables to infer the root cause (e.g., None value, wrong type, missing key)."
        ),
        StepModel(
            description="Add logging or a focused unit test that reproduces the stack trace deterministically."
        ),
        StepModel(
            description="Implement a minimal fix that addresses the root cause and add tests covering the regression."
        ),
        StepModel(
            description="Run the full test suite and integration tests to ensure no other areas regress."
        ),
        StepModel(
            description="Review the fix with peers, add comments explaining the change, and add monitoring for recurrence."
        ),
        StepModel(
            description="If a hotfix was applied, schedule a proper patch and post-mortem documenting the root cause and mitigation."
        ),
    ],
)
