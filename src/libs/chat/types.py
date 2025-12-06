from dataclasses import dataclass
from typing import Optional, Sequence, Mapping, Any


class Function:
    """
    Tool call function.
    """

    name: str
    "Name of the function."

    arguments: Mapping[str, Any]
    "Arguments of the function."

    def __init__(self, name: str, arguments: Mapping[str, Any]):
        self.name = name
        self.arguments = arguments


class ToolCall:
    """
    Model tool calls.
    """

    id: Optional[str] = None

    function: Function
    "Function to be called."

    def __init__(self, function: Function, id: Optional[str] = None):
        self.function = function
        self.id = id


@dataclass
class Message:
    """
    Chat message.
    """

    role: str
    "Assumed role of the message. Response messages has role 'assistant' or 'tool'."

    content: Optional[str] = None
    "Content of the message. Response messages contains message fragments when streaming."

    thinking: Optional[str] = None
    "Thinking content. Only present when thinking is enabled."

    tool_name: Optional[str] = None
    "Name of the executed tool."

    tool_calls: Optional[Sequence[ToolCall]] = None
    "Tool calls made by the model."


@dataclass
class TokenLogprob:
    token: str
    "Token text."

    logprob: float
    "Log probability for the token."


@dataclass
class Logprob(TokenLogprob):
    top_logprobs: Optional[Sequence[TokenLogprob]] = None
    "Most likely tokens and their log probabilities."


@dataclass
class ChatResponse:
    """
    Response returned by chat requests.
    """

    message: Message
    "Response message."

    logprobs: Optional[Sequence[Logprob]] = None
    "Log probabilities for generated tokens if requested."

    done: Optional[bool] = None
    "Indicates if the response is complete."
