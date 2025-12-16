from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Design and implement a caching layer (Redis, in-memory, or file-based) with clear key schema, invalidation, eviction strategy, and monitoring.",
    steps=[
        StepModel(
            description="Identify caching targets: expensive computations, DB queries, or external API calls and access patterns."
        ),
        StepModel(
            description="Choose cache backend and eviction strategy (LRU, TTL, LFU) based on consistency and scale requirements."
        ),
        StepModel(
            description="Define cache keys and namespaces carefully to avoid collisions and support invalidation."
        ),
        StepModel(
            description="Implement read-through, write-through, or write-back caching patterns where appropriate."
        ),
        StepModel(
            description="Add cache invalidation, expiration, and fallback logic for cache misses or stale data."
        ),
        StepModel(
            description="Add metrics for cache hit/miss rates and monitor for thundering herd or stale data issues."
        ),
        StepModel(
            description="Document cache behavior and operational runbooks for scaling and failure scenarios."
        ),
    ],
)
