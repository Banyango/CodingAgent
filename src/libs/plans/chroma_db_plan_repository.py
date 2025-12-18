from asyncer import asyncify
from chromadb.api.models.Collection import Collection
from chromadb.utils.embedding_functions.sentence_transformer_embedding_function import (
    SentenceTransformerEmbeddingFunction,
)
from loguru import logger
from wireup import service

from core.interfaces.plan import PlanRepository
from core.plans.models import PlanModel, StepModel
from core.plans.use_cases import ALL_PLANS as all_plans

from libs.chromadb.client import ChromaClient
from libs.plans.models import ResultModel

PROMPTS = "prompts"


@service
class ChromaDbPlanRepository(PlanRepository):
    def __init__(self, client: ChromaClient):
        self.client = client

    async def init_collection(self):
        """Initialize the ChromaDB collection for plans."""
        collection: Collection = await asyncify(
            self.client.connection.create_collection
        )(
            name=PROMPTS,
            get_or_create=True,
            embedding_function=SentenceTransformerEmbeddingFunction(
                model_name="mixedbread-ai/mxbai-embed-xsmall-v1"
            ),  # type: ignore
        )

        documents = []
        steps = []
        ids = []

        total_plans = len(all_plans)
        logger.info(f"Indexing {total_plans} plans into ChromaDB collection...")

        for i, plan in enumerate(all_plans):
            logger.info(f"Indexing plan: {i + 1}/{total_plans}")
            ids.append(f"id{i}")
            documents.append(plan.name)
            steps.append({"steps": "\n".join(step.description for step in plan.steps)})

        await asyncify(collection.upsert)(  # type: ignore
            documents=documents, metadatas=steps, ids=ids
        )

    async def search_plans(self, query: str) -> PlanModel:
        """Search for plans matching the given query.

        Args:
            query (str): The search query.

        Returns:
            PlanModel: A plan matching the query.
        """
        collection = await asyncify(self.client.connection.get_collection)(PROMPTS)
        results = await asyncify(collection.query)(
            query_texts=[query],
        )

        model = ResultModel.model_validate(results)

        if not model.documents or not model.documents[0]:
            return PlanModel(name="", steps=[])

        steps = (
            model.metadatas[0][0]["steps"].split("\n")
            if model.metadatas and model.metadatas[0]
            else []
        )

        return PlanModel(
            name=model.documents[0][0]
            if model.documents and model.documents[0]
            else "",
            steps=[StepModel(description=step) for step in steps],
        )
