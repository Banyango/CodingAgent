from dataclasses import dataclass


@dataclass
class ConversationRequest:
    """Request to create a new conversation."""

    message: str
    project_root: str
