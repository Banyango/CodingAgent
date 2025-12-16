from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Set up structured logging, distributed tracing, and metrics collection for the application (OpenTelemetry, Prometheus) — instrument requests, expose a metrics endpoint, and configure dashboards, alerts, and log forwarding.",
    steps=[
        StepModel(
            description="Inventory what to observe: request rates, error rates, latency, resource usage, and business metrics."
        ),
        StepModel(
            description="Choose libraries and exporters (OpenTelemetry SDK, Prometheus client) compatible with the runtime."
        ),
        StepModel(
            description="Instrument code for structured logging and attach relevant context (request-id, user-id, trace id)."
        ),
        StepModel(
            description="Instrument metrics: counters, histograms, gauges for request latency, DB calls, cache hits/misses."
        ),
        StepModel(
            description="Add distributed tracing (span around major operations) and connect tracing backend."
        ),
        StepModel(
            description="Expose metrics endpoint (e.g., /metrics) and configure scraping or push gateway."
        ),
        StepModel(
            description="Configure log forwarding and retention in production (e.g., JSON logs to ELK or Splunk)."
        ),
        StepModel(
            description="Add dashboards and alerts for critical SLOs and error thresholds; document how to interpret them."
        ),
    ],
)
