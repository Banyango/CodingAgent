from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Create a reproducible local development environment with scripts or Docker compose, environment templates, and developer documentation.",
    steps=[
        StepModel(
            description="Document prerequisites: runtime versions, package managers, system packages, and credentials."
        ),
        StepModel(
            description="Provide a quickstart script or Makefile that sets up virtualenv, installs deps, runs DB migrations, and seeds dev data."
        ),
        StepModel(
            description="Provide docker-compose or scripts to bring up dependent services (DB, cache, message broker) locally."
        ),
        StepModel(
            description="Add a sample .env file and instructions to securely obtain or create local secrets."
        ),
        StepModel(
            description="Add helper commands for common developer tasks: run tests, lint, format, and run the app in dev mode."
        ),
        StepModel(
            description="Document debugging tips and how to attach debuggers or hot-reload in development."
        ),
    ],
)
