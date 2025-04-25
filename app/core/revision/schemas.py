from pydantic import BaseModel
from typing import List

class RevisionResult(BaseModel):
    query_prompt: str
    generated_query: str
    retrieved_results: List[str]
    final_prompt: str
    revised_passage: str