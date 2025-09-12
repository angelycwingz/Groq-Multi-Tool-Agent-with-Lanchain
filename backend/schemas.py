from pydantic import BaseModel, Field
from typing import List

class ToolCall(BaseModel):
    name: str = Field(..., examples=["calculator"])
    input: str = Field(..., examples=["2 + 2"])

class AgentStep(BaseModel):
    description: str = Field(..., examples=["Ran calculator on Input '2 + 2'"])
    result: str = Field(..., examples=["4"])

class TaskRequest(BaseModel):
    query: str = Field(..., examples=["What is 2 + 2?"])
    prefer_tool: str | None = Field(None, examples=["calculator"])

class AgentResponse(BaseModel):
    steps: List[AgentStep]
    answer: str
    tool_used: str
