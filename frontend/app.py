import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/run_agent"

st.set_page_config(page_title="Agentic Multi-Tool Assistant")
st.title("🤖 Agentic Multi-Tool Assistant (LangChain + Groq)")

query = st.text_input("Ask me anything (calculation, summary, question):", "")
prefer_tool = st.selectbox("Prefer a particular tool? (optional)", ["auto", "calculator", "wikipedia", "tavily_search", "Groq AI"]) # Add auto instead of "" in list

if st.button("Run Agent"):
    with st.spinner("Thinking..."):
        prefer_tool = None if prefer_tool == "auto" else prefer_tool
        payload = {"query": query, "prefer_tool": prefer_tool}
        resp = requests.post(BACKEND_URL, json=payload, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            if not data["tool_used"]:
                st.error("oops! Agent could not use any tool. Try Auto.")
            else:
                st.success(f"Final answer: {data['answer']}")
                st.divider()
                st.subheader("Agent Steps:")
                st.info(f"Tool used: {', '.join(data['tool_used'])}")
            
        else:
            st.error(f"Error: {resp.status_code} - {resp.text}")