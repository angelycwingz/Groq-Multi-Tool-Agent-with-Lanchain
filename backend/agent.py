import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

from tools import calculator, wikipedia, tavily_search

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

tools = [calculator, wikipedia, tavily_search]
llm = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct", model_provider="groq", temperature=0)


def pick_tool_and_run(query: str, prefer_tool: str = None):

    if prefer_tool == "Groq AI":
        messages = [
            SystemMessage("""you are a helpful AI assistant, Provice concise and accurate answers with a maximum of 700 characters. 
                          If you don't know the answer, just say that you don't know, don't try to make up an answer.
                          If you notice multiple parts in the question, suggest using a tool to answer the question."""),
            HumanMessage(content=query)
        ]
        res_llm = llm.invoke(messages)
        return ["Used Groq without any tool"], f"Sure! I am a Groq LLM. {res_llm.content}"

    llm_with_tools = llm.bind_tools(tools)
    
    messages = [HumanMessage(content=query)]
    ai_msg = llm_with_tools.invoke(messages)

    messages.append(ai_msg)

    tool_used =[]
    
    # First, run preferred tool(s) if
    try:
        if prefer_tool:
            for tool_call in ai_msg.tool_calls:
                tool_name = tool_call["name"].lower()
                if tool_name == prefer_tool.lower():
                    tool_used.append(f"Used {tool_name} with {tool_call['args']}")
                    selected_tool = {
                        "calculator": calculator,
                        "wikipedia": wikipedia,
                        "tavily_search": tavily_search
                    }[tool_name]
                    tool_msg = selected_tool.invoke(tool_call)
            
                    messages.append(tool_msg)

        # Then run remaining tools (if any)
        for tool_call in ai_msg.tool_calls:
            tool_name = tool_call["name"].lower()
            if prefer_tool and tool_name == prefer_tool.lower():
                continue  # already ran
            tool_used.append(f"Used {tool_name} with {tool_call['args']}")
            selected_tool = {
                "calculator": calculator,
                "wikipedia": wikipedia,
                "tavily_search": tavily_search
            }[tool_name]
            tool_msg = selected_tool.invoke(tool_call)
            print("tool msg:", [tool_msg])
            messages.append(tool_msg)

        response = llm_with_tools.invoke(messages)
    
        return tool_used, response.content
    
    except Exception as e:
        print("Error during tool execution:", str(e))
        return [], f"Error: could not compute result - {str(e)}"