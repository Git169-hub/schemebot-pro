import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

CHROMA_PATH = "chroma_db"
SQLITE_PATH = "memory.db"
MODEL_NAME = "llama-3.1-8b-instant"