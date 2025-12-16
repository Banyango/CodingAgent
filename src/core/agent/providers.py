from typing import (
    List,
    Dict,
    Type,
    Optional,
    get_origin,
    get_args,
    Union as TypingUnion,
)
import types
import inspect

from core.interfaces.tool import Tool
from core.chat.models import (
    FunctionCallReqeustModel,
    FunctionModel,
    ParametersModel,
    PropertyModel,
)


def get_json_type_from_python_type(kind: str) -> str:
    """
    Map Python types to JSON schema types.

    Args:
        kind (str): The Python type.

    Returns:
        str: The corresponding JSON schema type.
    """
    if kind is int:
        return "integer"
    elif kind is float:
        return "number"
    elif kind is str:
        return "string"
    elif kind is bool:
        return "boolean"
    elif kind is list:
        return "array"
    elif kind is dict:
        return "object"
    elif kind is types.NoneType:
        return "null"
    else:
        raise ValueError(f"Unsupported parameter type: {kind}")


def get_union_types(tp) -> tuple:
    """
    Return a tuple of member types for a Union (including PEP 604 `A | B`).
    Returns an empty tuple if `tp` is not a union.
    """
    origin = get_origin(tp)
    if (
        origin is TypingUnion
        or origin is types.UnionType
        or isinstance(tp, types.UnionType)
    ):
        return get_args(tp)
    return ()


def serialize_tool(tool: Type[Tool]) -> FunctionCallReqeustModel:
    """Serialize a Tool into a FunctionCallToolModel.

    Args:
        tool (Tool): The tool to serialize.

    Returns:
        FunctionCallReqeustModel: The serialized tool.
    """
    signature = inspect.signature(tool.execute_async)

    params = {}
    required = []
    for name, parameter in signature.parameters.items():
        name = parameter.name
        kind = parameter.annotation

        if name == "self" or name == "context":
            continue

        if parameter.default == inspect.Parameter.empty:
            required.append(name)

        types_or_type: str | List[str] = []
        if isinstance(kind, types.UnionType):
            members = get_union_types(kind)
            types_or_type = [get_json_type_from_python_type(m) for m in members]
        else:
            types_or_type = get_json_type_from_python_type(kind)

        params[name] = PropertyModel(
            type=types_or_type,
            description=f"The {name} parameter",
        )

    return FunctionCallReqeustModel(
        type="function",
        function=FunctionModel(
            name=tool.__name__,
            description=tool.description,
            parameters=ParametersModel(
                type="object", required=required, properties=params
            ),
        ),
    )


class ToolsProvider:
    def __init__(self, tools: List[Type[Tool]]):
        self._str_to_tool_map: Dict[str, Type[Tool]] = {
            tool.__name__: tool for tool in tools
        }
        self._serialized_tools: List[FunctionCallReqeustModel] = [
            serialize_tool(tool) for tool in tools
        ]

    def get_tools(self) -> List[FunctionCallReqeustModel]:
        """Get the serialized tools.

        Returns:
            List[FunctionCallReqeustModel]: The list of serialized tools.
        """
        return self._serialized_tools

    def get_tool_by_name(self, name: str) -> Optional[Type[Tool]]:
        """Get a tool class by its name

        Args:
            name (str): The name of the tool.

        Returns:
            Optional[Type[Tool]]: The tool class if found, else None.
        """
        if name not in self._str_to_tool_map:
            return None

        return self._str_to_tool_map[name]
