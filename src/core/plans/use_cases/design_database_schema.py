from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Design a production-ready database schema from requirements, including entity modeling, indexing strategy, migrations, and scalability considerations.",
    steps=[
        StepModel(
            description="Gather requirements: entities, relationships, access patterns, read/write ratios, constraints, and scalability needs."
        ),
        StepModel(
            description="Model entities and relationships: identify primary keys, foreign keys, cardinality (1:1, 1:N, N:M)."
        ),
        StepModel(
            description="Normalize schema to avoid redundant data while considering denormalization for read-heavy access patterns."
        ),
        StepModel(
            description="Choose data types carefully, length limits, nullability, and default values to ensure storage efficiency and correctness."
        ),
        StepModel(
            description="Design indexes based on WHERE clauses, JOINs, and ORDER BY; consider composite and covering indexes."
        ),
        StepModel(
            description="Design constraints, transactions, and referential integrity rules; create migration scripts or DDL statements."
        ),
        StepModel(
            description="Consider partitioning, sharding, or replication for large datasets; create archiving strategy for old data."
        ),
        StepModel(
            description="Document the schema with ER diagrams and sample queries for common access patterns."
        ),
        StepModel(
            description="Review and iterate with stakeholders, then implement migrations and test with realistic data volumes."
        ),
    ],
)
