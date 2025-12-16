from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Detect and remediate security vulnerabilities in dependencies and codebase, add CI checks, and document security policies and remediation steps.",
    steps=[
        StepModel(
            description="Run dependency scanners (e.g., safety, npm audit, GitHub Dependabot) and static analyzers (Snyk, Bandit)."
        ),
        StepModel(
            description="Prioritize findings by severity and exploitability and identify quick wins vs. complex fixes."
        ),
        StepModel(
            description="Update dependencies carefully, run tests, and pin versions or add overrides for vulnerable transitive deps."
        ),
        StepModel(
            description="Fix code issues flagged by linters/static analyzers: injection risks, unsafe deserialization, improper auth checks."
        ),
        StepModel(
            description="Add CI checks that fail the build on high-severity vulnerabilities or dangerous lints."
        ),
        StepModel(
            description="Document security policies, rotation schedules for secrets, and secure coding guidelines for contributors."
        ),
        StepModel(
            description="Plan periodic audits and dependency upgrade windows; monitor for new advisories."
        ),
    ],
)
