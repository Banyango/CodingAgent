from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Produce example data visualizations and dashboards for key metrics, including data preparation, charting, and alerting guidance.",
    steps=[
        StepModel(
            description="Define the key metrics and the target audience for the dashboards or visualizations."
        ),
        StepModel(
            description="Prepare and shape the data with aggregation queries or ETL to match visualization needs."
        ),
        StepModel(
            description="Choose visualization tools (Grafana, Metabase, matplotlib, D3) and design mockups for charts."
        ),
        StepModel(
            description="Implement charts and dashboards, add filters and drill-downs for exploratory analysis."
        ),
        StepModel(
            description="Add automated jobs to refresh data or connect live data sources for near-real-time dashboards."
        ),
        StepModel(
            description="Document how to interpret the visualizations and add alerts for key thresholds."
        ),
    ],
)
