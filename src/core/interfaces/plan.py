from abc import ABC, abstractmethod

from wireup import abstract

from core.plans.models import PlanModel


@abstract
class PlanRepository(ABC):
    @abstractmethod
    async def init_collection(self):
        """Initialize the plan collection in the repository."""
        pass

    @abstractmethod
    async def search_plans(self, query: str) -> PlanModel:
        """Search for plans matching the given query.

        Args:
            query (str): The search query.
        Returns:
            PlanModel: The plan that matches the query.
        """
        pass
