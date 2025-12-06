from pydantic_settings import BaseSettings
from wireup import service


class GeminiAISettings(BaseSettings):
    model_config = {"env_prefix": "GEMINI_"}

    api_key: str = "abc123"
    model: str = "gemini-2.5-flash"


@service
def get_gemini_ai_settings() -> GeminiAISettings:
    return GeminiAISettings()
