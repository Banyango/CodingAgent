from typing import List

from app.pydantic import BaseSchema


class Step(BaseSchema):
    description: str
    completed: bool
    is_complete: bool


class Plan(BaseSchema):
    name: str
    description: str
    steps: List[Step]

    @property
    def is_complete(self) -> bool:
        """Check if all steps in the plan are complete.

        Returns:
            bool: True if all steps are complete; False otherwise.
        """
        return all(step.is_complete for step in self.steps)

    def __len__(self) -> int:
        """Return the number of steps in the plan.

        Returns:
            int: The number of steps.
        """
        return len(self.steps)

    def mark_step_completed(self, step_index: int) -> None:
        """Mark a specific step as completed.

        Args:
            step_index (int): The index of the step to mark as completed.
        """
        if 0 <= step_index < len(self.steps):
            self.steps[step_index].completed = True
        else:
            raise IndexError("Step index out of range.")
