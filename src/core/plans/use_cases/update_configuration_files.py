from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Update and standardize project configuration files (env, YAML, TOML) across environments and document recommended practices for secrets and overrides.",
    steps=[
        StepModel(
            description="Inventory current configuration files and differences between environments (dev, staging, prod)."
        ),
        StepModel(
            description="Consolidate configuration keys and document defaults, environment overrides, and secure secrets handling."
        ),
        StepModel(
            description="Add validation and schema checks for critical configuration values and integrate into CI."
        ),
        StepModel(
            description="Provide sample .env templates and instructions for rotating secrets and managing multi-environment configs."
        ),
        StepModel(
            description="Document how to apply configuration changes and rollback safely."
        ),
    ],
)
