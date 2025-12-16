from wireup import AsyncContainer

from libs.plans.chroma_db_plan_repository import ChromaDbPlanRepository


async def on_app_startup(container: AsyncContainer):
    repo = await container.get(ChromaDbPlanRepository)
    await repo.init_collection()
    pass
