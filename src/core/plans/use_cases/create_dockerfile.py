from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Create a production-ready Dockerfile and image build strategy (multi-stage builds, caching, minimal runtime image, and security best practices).",
    steps=[
        StepModel(
            description="Gather runtime and build requirements: language, package manager, build steps, ports, environment variables."
        ),
        StepModel(
            description="Choose base images optimized for size and compatibility (e.g., python:3.12-slim, node:18-alpine)."
        ),
        StepModel(
            description="Create a multi-stage Dockerfile if the app requires a build step to keep final image small."
        ),
        StepModel(
            description="Add instructions to copy only necessary files and leverage dependency caching (copy lockfiles first)."
        ),
        StepModel(
            description="Install runtime dependencies, build the app, and remove build-only artifacts in final stage."
        ),
        StepModel(
            description="Set working directory, expose ports, configure environment variables, and add a non-root user where appropriate."
        ),
        StepModel(
            description="Add a healthcheck and make ENTRYPOINT/CMD idempotent and signal-friendly (exec form)."
        ),
        StepModel(
            description="Document how to build and run the image locally and in CI; include example docker run commands."
        ),
        StepModel(
            description="Add a small .dockerignore to avoid adding unnecessary files into the build context."
        ),
        StepModel(
            description="Optional: add a docker-compose file and a lightweight CI step to build/push the image."
        ),
    ],
)
