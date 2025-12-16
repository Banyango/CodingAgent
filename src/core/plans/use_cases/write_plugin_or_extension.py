from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Develop a plugin or extension scaffold with clear lifecycle hooks, API surface, tests, and packaging instructions for distribution.",
    steps=[
        StepModel(
            description="Identify extension points and required APIs or hooks the host exposes."
        ),
        StepModel(
            description="Design the plugin API and configuration surface; define lifecycle events and error handling."
        ),
        StepModel(
            description="Implement the plugin core and add tests for lifecycle and edge cases."
        ),
        StepModel(
            description="Package and document installation and configuration steps for consumers."
        ),
        StepModel(
            description="Provide examples and an integration test showcasing the plugin in the host environment."
        ),
    ],
)
