from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Produce comprehensive OpenAPI/Swagger documentation for the API including schemas, examples, interactive docs, and client generation guidance.",
    steps=[
        StepModel(
            description="Inventory endpoints, request/response schemas, status codes, and auth mechanisms."
        ),
        StepModel(
            description="Choose how to author OpenAPI: code-first annotations, schema-first YAML, or generator from routes."
        ),
        StepModel(
            description="Add descriptive summaries, examples, and schema models for inputs/outputs and errors."
        ),
        StepModel(
            description="Generate interactive docs (Swagger UI or Redoc) and validate the spec against test requests."
        ),
        StepModel(
            description="Add client generation step (OpenAPI generator) and example clients for common languages."
        ),
        StepModel(
            description="Integrate docs generation into CI and publish to a docs host or the repository."
        ),
    ],
)
