from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Provide example API client implementations across multiple languages demonstrating authentication, requests, error handling, and usage patterns.",
    steps=[
        StepModel(
            description="Identify the public API endpoints to demonstrate and auth patterns (API key, OAuth, JWT)."
        ),
        StepModel(
            description="Choose target languages (e.g., Python, JavaScript, Ruby, Go) that are relevant to consumers."
        ),
        StepModel(
            description="Create minimal client examples that show auth, making a request, handling errors, and parsing responses."
        ),
        StepModel(
            description="Use idiomatic libraries in each language (requests/axios/faraday/http.Client) and show installation steps."
        ),
        StepModel(
            description="Add unit/integration tests or scripts that exercise the example clients against a staging API or mocked responses."
        ),
        StepModel(
            description="Publish examples under a clear folder structure and add README for each client with code snippets."
        ),
        StepModel(
            description="Optionally generate clients from OpenAPI/Swagger specs and show how to use them."
        ),
        StepModel(
            description="Document versioning and compatibility notes for each client and how to run examples locally."
        ),
    ],
)
