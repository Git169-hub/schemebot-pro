\# 🏛️ SchemeBot Pro



A bilingual (English + Telugu) agentic AI system that helps Indian citizens discover and apply for government welfare schemes.



\*\*Live Demo:\*\* https://schemebot-pro-tpsstw8czm8re65hvdnit8.streamlit.app



\---



\## What It Does



\- Detects whether the user is typing in English or Telugu

\- Assesses eligibility for Indian government schemes (PM Kisan, MGNREGA, Ayushman Bharat, PM Awas Yojana, Atal Pension Yojana)

\- Searches the web for latest scheme deadlines and updates

\- Generates a step-by-step application plan in the user's language

\- Saves session history to a local SQLite database



\---



\## Architecture



```

User Input

&#x20;   │

&#x20;   ▼

\[Node 1] Language Detector

&#x20;   │     Unicode-based Telugu/English detection

&#x20;   ▼

\[Node 2] Eligibility Assessor

&#x20;   │     Groq LLaMA 3.1 8b

&#x20;   ▼

\[Node 3] Web Search

&#x20;   │     Tavily API (3 results)

&#x20;   ▼

\[Node 4] Plan Generator

&#x20;   │     Groq LLaMA 3.1 8b

&#x20;   ▼

\[Node 5] Memory Writer

&#x20;         SQLite persistence

```



\---



\## Tech Stack



| Component | Tool |

|-----------|------|

| Agent Framework | LangGraph (StateGraph) |

| LLM | Groq LLaMA 3.1 8b Instant |

| Web Search | Tavily API |

| Memory | SQLite |

| Frontend | Streamlit |

| Language | Python 3.13 |



\---



\## Project Structure



```

schemebot\_pro/

├── app/

│   ├── config.py      # API key loading (env + Streamlit secrets)

│   ├── graph.py       # LangGraph StateGraph definition

│   ├── nodes.py       # All 5 node functions

│   └── main.py        # Streamlit UI

├── .env               # Local API keys (never push)

├── .gitignore

├── .streamlit/

│   └── secrets.toml   # Local Streamlit secrets (never push)

└── requirements.txt

```



\---



\## Setup



```bash

git clone https://github.com/Git169-hub/schemebot-pro.git

cd schemebot-pro

pip install -r requirements.txt

```



Create a `.env` file:

```

GROQ\_API\_KEY=your\_groq\_key

TAVILY\_API\_KEY=your\_tavily\_key

```



Run locally:

```bash

streamlit run app/main.py

```



\---



\## Example Queries



\*\*English:\*\*

> I am a farmer with 2 acres of land in Andhra Pradesh



\*\*Telugu:\*\*

> నేను ఆంధ్రప్రదేశ్‌లో 2 ఎకరాల భూమి ఉన్న రైతును



\---



\## Author



\*\*Razak\*\* — AI/ML Engineer  

GitHub: \[Git169-hub](https://github.com/Git169-hub) | HuggingFace: \[RazakAIhub](https://huggingface.co/RazakAIhub)

