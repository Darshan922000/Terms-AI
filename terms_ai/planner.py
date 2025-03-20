from langchain_groq import ChatGroq
from terms_ai.schema import Sections

llm = ChatGroq(model="gemma2-9b-it")

# Augment the LLM with schema for structured output
planner = llm.with_structured_output(Sections)