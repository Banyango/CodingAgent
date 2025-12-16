from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Perform a thorough code review focusing on correctness, style, security, maintainability, and provide actionable suggestions and rationale.",
    steps=[
        StepModel(
            description="Analyze the code changes to understand their purpose and impact."
        ),
        StepModel(
            description="Check for adherence to coding standards and best practices."
        ),
        StepModel(
            description="Identify potential bugs, security vulnerabilities, and performance issues."
        ),
        StepModel(
            description="Provide constructive feedback and suggestions for improvement."
        ),
        StepModel(description="Create a markdown file of the changes."),
    ],
)
