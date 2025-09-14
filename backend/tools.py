import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_tavily import TavilySearch

load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", "YOUR_TAVILY_API_KEY_HERE")

@tool
def calculator(expression: str) -> str:
    """Simple mathematical calculator tool that evaluates '+', '-', '*', '/' operations."""
    try:
        # WARNING: Using eval can be dangerous if you're evaluating untrusted input.
        # In a production environment, consider using a safer alternative.
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: could not compute result - {str(e)}"

# Change it to inbuilt langchain wikipedia tool
api_wrapper = WikipediaAPIWrapper(doc_content_chars_max=700)
api_wrapper = WikipediaAPIWrapper(doc_content_chars_max=700)
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper)
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper)

# change it to inbuilt langchain tavily search tool

tavily_search = TavilySearch(max_results=1, topic="general")
tavily_search = TavilySearch(max_results=1)

api_wrapper = WikipediaAPIWrapper(doc_content_chars_max=700)
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper)

# ✅ Tavily tool as a proper LangChain Tool

