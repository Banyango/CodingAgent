import json
from typing import List

import aiofiles
from wireup import service

from core.interfaces.memory import AgentMemoryService
from core.chat.models import ChatMessageModel


@service
class DebuggingAgentMemoryService(AgentMemoryService):
    async def load_messages(self) -> List[ChatMessageModel]:
        try:
            async with aiofiles.open("agent_memory.json", "r", encoding="utf-8") as f:
                content = await f.read()
                memory = json.loads(content)
                messages = [
                    ChatMessageModel(**message_dict)
                    for message_dict in memory.get("messages", [])
                ]
                return messages
        except FileNotFoundError:
            return []

    async def save_messages(self, messages: List[ChatMessageModel]):
        memory = {"messages": [message.__dict__ for message in messages]}

        async with aiofiles.open("agent_memory.json", "w", encoding="utf-8") as f:
            # json.dumps is synchronous but small; write asynchronously
            serialized = json.dumps(memory, ensure_ascii=False, indent=2) + "\n"
            await f.write(serialized)
