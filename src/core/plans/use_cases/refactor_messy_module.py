from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Refactor a messy module into clearer, well-tested functions and classes while preserving behavior and adding documentation and typings.",
    steps=[
        StepModel(
            description="Create a safety-first plan: add or update unit tests to cover current behavior (baseline tests)."
        ),
        StepModel(
            description="Run tests and record failing behavior to ensure tests are valid; add regression tests for edge cases."
        ),
        StepModel(
            description="Read and document the module's responsibilities, inputs/outputs, side effects, and global state usage."
        ),
        StepModel(
            description="Identify logical groups of code that can be extracted into pure functions or classes."
        ),
        StepModel(
            description="Extract small functions with clear names and single responsibilities; keep original signatures temporarily via adapters."
        ),
        StepModel(
            description="Introduce classes only when there is coherent state or behavior to encapsulate (constructors, invariants)."
        ),
        StepModel(
            description="Preserve public API: add deprecation shims if method/argument names change, maintain backward compatibility."
        ),
        StepModel(
            description="Refactor incrementally: run tests after each refactor step and fix issues immediately."
        ),
        StepModel(
            description="Improve documentation and add docstrings and typing for new functions/classes."
        ),
        StepModel(
            description="Remove dead code and inline trivial helpers; keep a changelog entry describing behavior-preserving changes."
        ),
        StepModel(
            description="Run integration tests and a small smoke test in the running app to ensure behavior is preserved."
        ),
        StepModel(
            description="Optional: improve performance hotspots identified during refactor and benchmark critical paths."
        ),
    ],
)
