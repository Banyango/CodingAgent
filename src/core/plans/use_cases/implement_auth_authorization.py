from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Implement secure authentication and authorization (JWT, OAuth, RBAC), including safe storage of credentials, token lifecycle, and tests.",
    steps=[
        StepModel(
            description="Clarify auth requirements: who, how, and what permissions are needed; decide token types and flows."
        ),
        StepModel(
            description="Choose libraries and frameworks that fit the security model and integrate with existing identity providers if needed."
        ),
        StepModel(
            description="Implement authentication flows and secure credential storage; add token refresh and revocation paths."
        ),
        StepModel(
            description="Implement authorization checks (RBAC/ABAC) and unit tests to validate permission boundaries."
        ),
        StepModel(
            description="Add logging and monitoring for suspicious auth activity and implement rate-limiting where necessary."
        ),
        StepModel(
            description="Document auth flows, configuration, and rotation/runbooks for secrets."
        ),
    ],
)
