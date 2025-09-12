def calculator_tool(expression: str) -> str:
    try:
        # WARNING: Using eval can be dangerous if you're evaluating untrusted input.
        # In a production environment, consider using a safer alternative.
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: could not compute result - {str(e)}"

def summarize_tool(text: str) -> str:
    sentences = text.split(".")
    return sentences[0].strip() + "." if sentences else "No text to summarize."

def search_tool(query: str) -> str:
    if "ada lovelace" in query.lower():
        return "Ada Lovelace was a pioneering computer scientist."
    return "Search not implemented in demo."

