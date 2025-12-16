from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Profile the codebase to identify performance hotspots and provide measurable optimization proposals (benchmarks, profiling, and regression tests).",
    steps=[
        StepModel(
            description="Define performance goals and metrics (latency p99, throughput, memory footprint)."
        ),
        StepModel(
            description="Add benchmarks and representative load tests to reproduce performance characteristics."
        ),
        StepModel(
            description="Use profilers (CPU, memory, allocation) suitable for the runtime and collect traces."
        ),
        StepModel(
            description="Identify hotspots, inefficient algorithms, excessive allocations, and blocking I/O."
        ),
        StepModel(
            description="Propose targeted optimizations: algorithmic improvements, caching, batching, and parallelism."
        ),
        StepModel(
            description="Implement optimizations incrementally and benchmark after each change to quantify gains."
        ),
        StepModel(
            description="Add monitoring to catch regressions and document trade-offs between complexity and performance."
        ),
    ],
)
