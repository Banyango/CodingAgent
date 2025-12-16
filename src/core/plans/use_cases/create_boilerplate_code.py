from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Generate a complete project boilerplate tailored to the chosen language/framework, including entrypoint, routing, tests, and basic CI hints.",
    steps=[
        StepModel(
            description="Gather requirements: language/framework (e.g., FastAPI, Express, Rails), API endpoints, auth, DB, and config preferences."
        ),
        StepModel(
            description="Choose project layout and folder structure following framework best practices."
        ),
        StepModel(
            description="Initialize project (venv/npm bundle/rails new), create package manifests and lockfiles."
        ),
        StepModel(
            description="Add core dependencies and dev-dependencies (framework, router, testing, linting)."
        ),
        StepModel(
            description="Create app entrypoint (main.py or index.js) and basic server startup code."
        ),
        StepModel(
            description="Create routing modules, controllers, and request/response schemas or serializers."
        ),
        StepModel(
            description="Add data access layer: database client, models/ORM scaffolding, and migrations folder."
        ),
        StepModel(
            description="Add basic auth middleware and error handling middleware."
        ),
        StepModel(
            description="Wire up configuration management (env, config files) and logging setup."
        ),
        StepModel(
            description="Add tests for server startup and a sample endpoint, plus linting and formatting config."
        ),
        StepModel(
            description="Create README with run, develop, test, and deploy instructions; include example requests."
        ),
        StepModel(
            description="Optional: add Dockerfile, CI config, and healthcheck endpoint."
        ),
    ],
)
