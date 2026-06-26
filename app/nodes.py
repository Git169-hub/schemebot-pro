import re
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, TAVILY_API_KEY, MODEL_NAME
from tavily import TavilyClient

llm = ChatGroq(api_key=GROQ_API_KEY, model=MODEL_NAME)
tavily = TavilyClient(api_key=TAVILY_API_KEY)

def detect_language(state: dict) -> dict:
    text = state["user_input"]
    telugu_pattern = re.compile(r'[\u0C00-\u0C7F]')
    if telugu_pattern.search(text):
        state["language"] = "telugu"
    else:
        state["language"] = "english"
    print(f"[Node 1] Language detected: {state['language']}")
    return state

def assess_eligibility(state: dict) -> dict:
    user_input = state["user_input"]
    language = state["language"]
    prompt = f"""
    User query: {user_input}
    Language: {language}
    
    Based on the query, identify which Indian government welfare schemes 
    the user may be eligible for from this list:
    - PM Kisan (farmers)
    - Ayushman Bharat (health coverage)
    - MGNREGA (rural employment)
    - PM Awas Yojana (housing)
    - Atal Pension Yojana (pension)
    
    Return a brief eligibility assessment in {language}.
    """
    response = llm.invoke(prompt)
    state["eligibility"] = response.content
    print(f"[Node 2] Eligibility assessed")
    return state

def web_search(state: dict) -> dict:
    query = f"Indian government scheme application deadline 2025 {state['eligibility'][:100]}"
    results = tavily.search(query=query, max_results=3)
    state["search_results"] = results["results"]
    print(f"[Node 3] Web search done")
    return state

def generate_plan(state: dict) -> dict:
    language = state["language"]
    eligibility = state["eligibility"]
    search_results = state.get("search_results", [])
    search_text = "\n".join([r["content"] for r in search_results[:2]])
    
    prompt = f"""
    Eligibility assessment: {eligibility}
    Recent information: {search_text}
    
    Create a clear step-by-step application plan for the user.
    Respond in {language}.
    """
    response = llm.invoke(prompt)
    state["plan"] = response.content
    print(f"[Node 4] Plan generated")
    return state

def write_memory(state: dict) -> dict:
    import sqlite3
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            language TEXT,
            eligibility TEXT,
            plan TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        INSERT INTO sessions (user_input, language, eligibility, plan)
        VALUES (?, ?, ?, ?)
    """, (
        state["user_input"],
        state["language"],
        state["eligibility"],
        state["plan"]
    ))
    conn.commit()
    conn.close()
    print(f"[Node 5] Memory written to SQLite")
    return state
