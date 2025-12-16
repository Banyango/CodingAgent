"""Chat-related data models.

This module contains the small data models used by the chat and agent
subsystems. Models include message shapes, chat options, and function
schemas used for function-calling/tool-invocation flows.

Notes:
- Types are implemented mostly as dataclasses for simple interchange.
- Some schema-like types inherit from `BaseModel` (a pydantic wrapper)
  to enable JSON schema generation when needed.
"""

from typing import Literal, Optional, Dict, Any, List, Union

from pydantic import BaseModel
from pydantic.json_schema import JsonSchemaValue

Role = Literal["system", "user", "assistant", "tool"]


class ChatOptionsModel(BaseModel):
    """Options that control model generation and behavior.

    Attributes:
        temperature: sampling temperature for generation.
        max_tokens: maximum number of tokens to generate.
        top_p: nucleus sampling parameter.
        presence_penalty: penalty for new tokens based on whether they
            appear in the text so far.
        frequency_penalty: penalty for new tokens based on their
            existing frequency in the text so far.
        format: optional JSON schema or named format hint used to request
            structured output (e.g. "json").
        think: whether "thinking" traces should be requested from the
            model (if supported by the adapter).
        stop: optional list of stop token strings.
    """

    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    format: Optional[Union[Literal["", "json"], JsonSchemaValue]] = None
    think: Optional[bool] = None
    stop: Optional[List[str]] = None


class PropertyModel(BaseModel):
    """Describes a single JSON-schema-like property used in function parameters.

    Fields mirror a pared-down JSON Schema property definition and are
    used when generating a parameters schema for function calling.
    """

    type: str | List[str]
    description: Optional[str]


class ParametersModel(BaseModel):
    """Object describing the parameters accepted by a callable function.

    This mirrors the structure of a JSON Schema 'object' with a set of
    required fields and property definitions.
    """

    type: Literal["object"]
    required: List[str]
    properties: Dict[str, PropertyModel]


class FunctionModel(BaseModel):
    """Definition of a callable function for model-driven tooling.

    Contains a name, an optional description and a `ParametersModel`
    describing its expected arguments.
    """

    name: str
    description: Optional[str]
    parameters: ParametersModel


class FunctionCallReqeustModel(BaseModel):
    """Wrapper model representing a request to call a function.

    The `type` field is set to "function" and `function` holds the
    `FunctionModel` describing the function to invoke.
    """

    type: Literal["function", "object"]
    function: FunctionModel


class FunctionCallResponseModel(BaseModel):
    """Model representing a function call response (name + arguments).

    This is used to capture the name of the function called and the
    parsed arguments that should be passed to the tool implementation.
    """

    id: Optional[str] = None
    name: str
    arguments: Dict[str, Any]


class ChatMessageModel(BaseModel):
    """Represents a chat message exchanged with the model.

    Attributes:
        role: the role of the message sender (e.g. 'user', 'assistant').
        content: the textual content of the message.
        tool_call_id: optional id associated with a tool call.
        tool_name: optional tool name when the message originated from a tool.
        tool_calls: optional list of function call responses discovered in the message.
        thinking: optional "thinking" trace text when supported.
        name: optional human-readable name for the sender.
        metadata: optional free-form metadata dictionary.
    """

    role: Role
    """The role of the message sender."""

    content: str
    """The content of the message."""

    tool_call_id: Optional[str] = None
    """The ID of the tool call associated with this message, if any."""

    tool_name: Optional[str] = None
    """The name of the tool used, if any."""

    tool_calls: Optional[List[FunctionCallResponseModel]] = None
    """The list of tool calls made in this message, if any."""

    thinking: Optional[str | bytes] = None
    """The thinking content of the message, if any."""

    name: Optional[str] = None
    """The name of the message sender, if applicable."""

    metadata: Optional[Dict[str, Any]] = None
    """Additional metadata associated with the message."""
