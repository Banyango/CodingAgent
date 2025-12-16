from core.plans.models import StepModel, PlanModel

plan = PlanModel(
    name="Design and implement reusable, accessible UI components with clear APIs, tests, and documentation (props, state, stories).",
    steps=[
        StepModel(
            description="Clarify component boundaries, props, events, and state management expectations."
        ),
        StepModel(
            description="Choose framework-specific patterns: functional components and hooks for React, composition API for Vue."
        ),
        StepModel(
            description="Create accessible markup and style encapsulation (CSS modules, styled components, or scoped CSS)."
        ),
        StepModel(
            description="Add unit tests for component logic and snapshot/unit tests for render output."
        ),
        StepModel(
            description="Add integration/storybook stories to visualize states and edge cases."
        ),
        StepModel(
            description="Optimize rendering and avoid unnecessary re-renders; memoize expensive computations."
        ),
        StepModel(
            description="Document component API and examples, and provide design tokens or themes if applicable."
        ),
    ],
)
