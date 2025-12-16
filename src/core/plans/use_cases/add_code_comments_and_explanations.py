from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Create comprehensive inline code comments and explanations for algorithms, invariants, and non-obvious implementations — include rationale, assumptions, and minimal examples where helpful.",
    steps=[
        StepModel(
            description="Identify complex or non-obvious code paths that benefit from explanation (algorithms, invariants, math)."
        ),
        StepModel(
            description="Add concise comments explaining the why, not the what; include references to design docs or papers if applicable."
        ),
        StepModel(
            description="Add inline examples or small usage snippets where helpful; avoid duplicating obvious code behavior."
        ),
        StepModel(
            description="Keep comments up-to-date: add tests or linters that detect stale or missing docstrings for public APIs."
        ),
        StepModel(
            description="Encourage PR reviewers to require clarification comments for complex changes."
        ),
    ],
)
