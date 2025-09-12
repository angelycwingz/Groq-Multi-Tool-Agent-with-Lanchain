from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import TaskRequest, AgentResponse, AgentStep
from agent import pick_tool_and_run

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
    print(request.prefer_tool)
    tool, steps, final = pick_tool_and_run(request.query, request.prefer_tool)
    return AgentResponse(
        steps=[AgentStep(**step) for step in steps],
        answer=final,
        tool_used=tool
    )