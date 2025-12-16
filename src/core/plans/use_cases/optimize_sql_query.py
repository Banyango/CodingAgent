from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Optimize a slow SQL query, document the changes, and explain why the new version improves performance (EXPLAIN/ANALYZE, indexing, and rewrites).",
    steps=[
        StepModel(
            description="Collect the slow query, its execution plan (EXPLAIN/EXPLAIN ANALYZE), and sample data statistics."
        ),
        StepModel(
            description="Identify the bottleneck: full table scan, missing index, poor join order, or expensive sorts/aggregations."
        ),
        StepModel(
            description="Rewrite query to use indexes-friendly constructs: avoid leading wildcards, prefer joins with indexed keys, and select needed columns."
        ),
        StepModel(
            description="Add or adjust indexes (single-column, composite, or covering indexes) based on predicates and JOIN conditions."
        ),
        StepModel(
            description="Consider rewriting joins as exists/IN, using CTEs, or pushing filters earlier to reduce row counts."
        ),
        StepModel(
            description="Test the new query with EXPLAIN ANALYZE and compare timing, I/O, and rows processed."
        ),
        StepModel(
            description="Explain why the optimized version is faster: reduced scanned rows, index seeks instead of scans, less sorting, better join algorithms."
        ),
        StepModel(
            description="If necessary, consider schema changes (normalization/denormalization), partitioning, or materialized views for heavy aggregations."
        ),
        StepModel(
            description="Add monitoring queries and alerting for regressions; document the change and its trade-offs."
        ),
    ],
)
