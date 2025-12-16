from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Create a safe, tested data migration script with backups, transactional steps, and a rollback strategy; include tests and runbook.",
    steps=[
        StepModel(
            description="Plan the migration and identify data invariants, required backups, and performance considerations."
        ),
        StepModel(
            description="Create a migration script that can be run idempotently and in small batches if needed."
        ),
        StepModel(
            description="Add tests or a dry-run mode to validate transformations against sample data."
        ),
        StepModel(
            description="Prepare monitoring and alerts for the migration to detect failures or long-running steps."
        ),
        StepModel(
            description="Document rollback procedures and how to restore from backups if problems occur."
        ),
        StepModel(
            description="Schedule the migration during a maintenance window and notify stakeholders as needed."
        ),
    ],
)
