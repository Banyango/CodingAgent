from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Author CI/CD pipeline configurations (GitHub Actions, GitLab CI, CircleCI) to build, test, and deploy with secure secrets and caching.",
    steps=[
        StepModel(
            description="Decide pipeline goals: run tests, linters, build artifacts, run migrations, and deploy targets."
        ),
        StepModel(
            description="Choose CI provider supported by the team and repository hosting; find reusable templates if available."
        ),
        StepModel(
            description="Author workflow jobs: checkout, install deps, run tests, build artifacts, and upload/cache dependencies."
        ),
        StepModel(
            description="Add matrix builds for multiple versions or platforms if compatibility is required."
        ),
        StepModel(
            description="Secure secrets via provider's secrets management and ensure least-privilege for deploy keys."
        ),
        StepModel(
            description="Add caching to speed up builds and artifacts to pass between jobs when needed."
        ),
        StepModel(
            description="Add deployment job with safe promotion steps (manual approvals, canary strategies)."
        ),
        StepModel(
            description="Add monitoring and notifications for pipeline failures and key metrics (build times, flakiness)."
        ),
        StepModel(
            description="Document how to run pipelines locally and how to add new jobs or workflows."
        ),
    ],
)
