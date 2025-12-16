from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Implement a feature end-to-end from a user story or spec: clarify acceptance criteria, design, implement, test, and roll out safely.",
    steps=[
        StepModel(
            description="Clarify the user story: acceptance criteria, success metrics, error cases, and UX expectations."
        ),
        StepModel(
            description="Break the feature into tasks: backend, frontend, DB, API, tests, and deployment steps."
        ),
        StepModel(
            description="Design API contract and data model changes needed; get design approval if necessary."
        ),
        StepModel(
            description="Implement backend changes with tests and API routes; keep changes small and testable."
        ),
        StepModel(
            description="Implement frontend components or CLI changes and wire them to the new API or local mocks."
        ),
        StepModel(
            description="Write unit and integration tests covering acceptance criteria and edge cases."
        ),
        StepModel(
            description="Run end-to-end or manual QA against staging; capture bug reports and iterate."
        ),
        StepModel(
            description="Update documentation, release notes, and migration scripts if applicable."
        ),
        StepModel(
            description="Deploy behind a feature flag or canary rollout, monitor metrics and roll back if regressions occur."
        ),
    ],
)
