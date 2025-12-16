from typing import List

from app.pydantic import BaseSchema


class StepModel(BaseSchema):
    description: str
    is_complete: bool = False


class PlanModel(BaseSchema):
    name: str
    steps: List[StepModel]
