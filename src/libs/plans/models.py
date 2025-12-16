from typing import List

from pydantic import BaseModel


class ResultModel(BaseModel):
    ids: List[List[str]]
    documents: List[List[str]]
    metadatas: List[List[dict]]

    class Config:
        extra = "allow"
