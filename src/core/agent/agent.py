import inspect
from typing import Dict, Any, List

from loguru import logger
from wireup import AsyncContainer

from core.code.models import ToolErrorModel
from core.interfaces.memory import AgentMemoryService
from core.agent.providers import ToolsProvider
from core.interfaces.chat import ChatClient
from core.chat.models import ChatMessageModel, ChatOptionsModel


class Agent:
    def __init__(
        self,
        chat_client: ChatClient,
        container: AsyncContainer,
        memory: AgentMemoryService,
        tools: ToolsProvider,
        system_prompt: str,
        max_iterations: int = 15,
    ):
        self.chat_client = chat_client
        self.container = container
        self.tools = tools
        self.memory = memory
        self.system_prompt = system_prompt
        self.max_iterations = max_iterations
        self.iteration = 0

    async def run_async(self, message_input: str, context: Dict[str, Any]) -> str:
        """
        Run the agent with the given message_input.

        Args:
            message_input (str): The input string to process.
            context (Dict[str, Any]): Additional context for the agent that will be passed to all tools.
        """
        messages = await self.memory.load_messages()
        if messages is None:
            messages = [
                ChatMessageModel(role="system", content=self.system_prompt),
                ChatMessageModel(role="user", content=message_input),
            ]

        self.iteration = 0
        while self.iteration < self.max_iterations:
            await self.memory.save_messages(messages)

            response = await self.chat_client.chat(
                messages=messages,
                tools=self.tools.get_tools(),
                options=ChatOptionsModel(
                    temperature=0.7,
                ),
            )

            if response is None:
                break

            if response.tool_calls is not None:
                for tool_call in response.tool_calls:
                    function_name = tool_call.name
                    function_args = tool_call.arguments

                    klass_name = self.tools.get_tool_by_name(function_name)
                    if klass_name is None:
                        messages.append(
                            ChatMessageModel(
                                tool_call_id=tool_call.id,
                                role="tool",
                                content=f"Tool {function_name} not found.",
                                tool_name=function_name,
                            )
                        )
                        continue

                    klass = await self.container.get(klass_name)

                    sig = inspect.signature(klass.execute_async)
                    parameters = sig.parameters
                    filtered_function_args = {}
                    for arg_name, arg_value in function_args.items():
                        if arg_name in parameters.keys():
                            filtered_function_args[arg_name] = arg_value

                    missing_params = False
                    for key in parameters.keys():
                        if key not in filtered_function_args and key != "context":
                            missing_params = True
                            break
                    if missing_params:
                        messages.append(
                            ChatMessageModel(
                                tool_call_id=tool_call.id,
                                role="tool",
                                content=f"Tool {function_name} missing required arguments.",
                                tool_name=function_name,
                            )
                        )
                        continue

                    tool_response = await klass.execute_async(
                        context=context, **filtered_function_args
                    )

                    if tool_response is None:
                        tool_response = ""

                    logger.info(
                        "Tool {function_name} executed with response: {tool_response}",
                        function_name=function_name,
                        tool_response=tool_response,
                    )

                    messages.append(
                        ChatMessageModel(
                            role="tool",
                            tool_call_id=tool_call.id,
                            thinking=response.thinking,
                            content=tool_response.error_message
                            if isinstance(tool_response, ToolErrorModel)
                            else tool_response,
                            tool_name=function_name,
                        )
                    )
            else:
                logger.info(
                    "Assistant responded: {content}", content=response.content
                )
                messages.append(
                    ChatMessageModel(
                        role="assistant",
                        content=response.content or "",
                        thinking=response.thinking,
                    )
                )

            is_done = await self.check_if_request_is_done(messages)
            if is_done:
                return await self.generate_final_response(messages)
            else:
                self.iteration += 1

        return "No response generated."

    async def check_if_request_is_done(self, messages: List[ChatMessageModel]) -> bool:
        is_done_system_prompt = (
            "$messages\n"
            "Based on the previous conversation, has the user's request been fully addressed? Respond with 'yes' or 'no'."
            "\n".join([f"{m.content}" for m in messages])
        )

        response = await self.chat_client.chat(
            messages=[
                ChatMessageModel(
                    role="system",
                    content=is_done_system_prompt,
                )
            ],
            options=ChatOptionsModel(
                temperature=0.0,
            ),
            tools=None,
        )

        if response is not None and response.content is not None:
            content = response.content.strip().lower()
            return content == "yes"

        return False

    async def generate_final_response(self, messages: List[ChatMessageModel]) -> str:
        """
        Generate a final response based on the conversation so far.

        Args:
            messages (List[ChatMessageModel]): The conversation messages.

        Returns:
            str: The final response content.
        """
        response = await self.chat_client.chat(
            messages=messages
            + [
                ChatMessageModel(
                    role="system",
                    content="Generate a concise final response to the user's original request based on the conversation so far.",
                )
            ],
            options=ChatOptionsModel(
                temperature=0.7,
            ),
            tools=None,
        )

        if response is not None and response.content is not None:
            return response.content.strip()

        return "No final response generated."
