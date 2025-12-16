from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Generate comprehensive developer and API documentation for a codebase (docstrings, guides, and site generation) and automate it in CI.",
    steps=[
        StepModel(
            description="Inventory public modules, classes, functions, and important design decisions to be documented."
        ),
        StepModel(
            description="Choose doc conventions (docstring style e.g. Google/Numpy, typed annotations) and tooling (Sphinx, mkdocs, pdoc)."
        ),
        StepModel(
            description="Add or improve docstrings for all public APIs, including parameter, return, and raised exceptions descriptions."
        ),
        StepModel(
            description="Create high-level Markdown docs: README, CONTRIBUTING, ARCHITECTURE, and API usage guides with examples."
        ),
        StepModel(
            description="Add a docs site configuration and generate static docs; validate links and examples run correctly."
        ),
        StepModel(
            description="Add changelog and migration notes for breaking changes; include examples and code snippets."
        ),
        StepModel(
            description="Automate docs generation in CI and add a bot/check to ensure new public APIs have docs."
        ),
        StepModel(
            description="Collect docs feedback from contributors and iterate to improve clarity and completeness."
        ),
    ],
)
