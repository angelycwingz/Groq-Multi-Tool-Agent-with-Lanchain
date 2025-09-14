from pydantic import BaseModel, Field
from typing import List

class TaskRequest(BaseModel):
    query: str = Field(..., examples=["What is 2 + 2?"])
    prefer_tool: str | None = Field(None, examples=["calculator"])

class AgentResponse(BaseModel):
    # steps: str
    tool_used: List[str]
    answer: str
