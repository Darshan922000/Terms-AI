from fastapi import FastAPI
import os
from pydantic import BaseModel
from langgraph.graph.message import MessagesState
import uvicorn
from IPython.display import Markdown
from terms_ai.graph import orchestrator_worker
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

# call APIs
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH__PROJECT")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Terms AI", page_icon="🤖", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #1f77b4;
        }
        .stTextInput input {
            border: 2px solid #1f77b4;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown('<h1 class="title">🤖 Terms AI</h1>', unsafe_allow_html=True)

# Input Box
user_input = st.text_input("🔍 Enter the topic:")

# Function to simulate processing (Replace with AI logic)
def process_query(query):
    response = orchestrator_worker.invoke({"topic": query})
    explaination = response.get("final_report", "No response received.")  # Extract text
    return explaination

# Search Button
if st.button("Search"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response = process_query(user_input)
            st.success("TERMS AI:")
            st.write(response)
    else:
        st.warning("⚠️ Please enter a query before searching.")

# app = FastAPI()

# class MessagesState(BaseModel):
#     messages: str

# @app.post("/chat")
# async def chat(request: MessagesState):
#     """
#     Receives user messages, processes them through the RAG system, and returns a response.
#     """
#     try:
#         response = orchestrator_worker.invoke({"topic": request.messages})
#         explaination = Markdown(response["final_report"])


#         return {"response": explaination}

#     except Exception as e:
#         print(f"Error in chat endpoint: {str(e)}")
#         return {"response": "I'm sorry, I couldn't process your request right now!! Internal Server Error"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)

