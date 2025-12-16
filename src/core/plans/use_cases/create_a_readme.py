from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Write a clear, structured README for the project including quickstart, usage, development, and contribution guidelines.",
    steps=[
        StepModel(
            description="Consult Agents.md or list the file directories for style and overall structure."
        ),
        StepModel(
            description="""Follow a good template to create a comprehensive README.md file for your project:"""
        ),
    ],
)
