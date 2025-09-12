import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

from tools import calculator_tool, summarize_tool, search_tool

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

llm = init_chat_model("llama-3.1-8b-instant", model_provider="groq", temperature=0)

def pick_tool_and_run(query: str, prefer_tool: str = None):
    print(prefer_tool)
    # Naive pattern matching to pick tool
    if prefer_tool:
        tool = prefer_tool.lower()
    elif any(word in query.lower() for word in ["add", "plus", "times", "+", "-", "*", "/", "calculate", "sqrt", "square"]):
        tool = "calculator"
    elif "summarize" in query.lower():
        tool = "summarizer"
    elif "search" in query.lower() or "who is" in query.lower() or "what is" in query.lower():
        tool = "search"
    else:
        tool = "llm"

    steps = []
    if tool == "calculator":
        expr = query.replace("What is", "").replace("?", "").strip()
        print(expr)
        result = calculator_tool(expr)
        steps.append({"description": f"Ran calculator on '{expr}'", "result": result})
    elif tool == "summarizer":
        result = summarize_tool(query)
        steps.append({"description": f"Ran summarizer", "result": result})
    elif tool == "search":
        result = search_tool(query)
        steps.append({"description": f"Ran search", "result": result})
    else:
        # Fallback: Use Groq LLM with chat prompt
        prompt = [
            SystemMessage(content="You are a general assistant."),
            HumanMessage(content=query)
        ]
        response = llm.invoke(prompt)
        result = response.content
        steps.append({"description": f"Ran Groq LLM", "result": result})
    return tool, steps, steps[-1]["result"]