from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Design and implement a small, well-tested CLI tool with clear argument parsing, dry-run options, and packaging for distribution.",
    steps=[
        StepModel(
            description="Define the CLI goals, commands, flags, and expected behaviors and error modes."
        ),
        StepModel(
            description="Choose a language and CLI framework (Python: click/argparse, Node: yargs, Go: cobra)."
        ),
        StepModel(
            description="Create project skeleton, add argument parsing, help text, and input validation."
        ),
        StepModel(
            description="Implement core functionality in small functions and add unit tests for those functions."
        ),
        StepModel(
            description="Add logging, dry-run mode, and a --yes/--force flag for destructive operations."
        ),
        StepModel(
            description="Package the tool (pip entry-point, npm package, or single static binary) and add packaging config."
        ),
        StepModel(
            description="Add usage examples, README, and basic integration tests or smoke tests."
        ),
        StepModel(
            description="Optional: add shell completion scripts and a lightweight installer script."
        ),
    ],
)
