from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from schemas import TaskRequest, AgentResponse, AgentStep
from schemas import TaskRequest, AgentResponse
from dotenv import load_dotenv

from agent import pick_tool_and_run

load_dotenv()

app = FastAPI(title="Agentic Multi-Tool Assistant")

"""advance this app to use simple calc tool, weather tool, web search tool, and a groq llm rest of the task"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/run_agent", response_model=AgentResponse)
def run_agent(request: TaskRequest):

    tool, answer = pick_tool_and_run(request.query, request.prefer_tool)
    return AgentResponse(
        tool_used= tool,
        answer= answer
    )