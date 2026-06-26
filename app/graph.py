from langgraph.graph import StateGraph, END
from nodes import (
    detect_language,
    assess_eligibility,
    web_search,
    generate_plan,
    write_memory
)
from typing import TypedDict, List

class AgentState(TypedDict):
    user_input: str
    language: str
    eligibility: str
    search_results: List[dict]
    plan: str

def build_graph():
    graph = StateGraph(AgentState)
    
    graph.add_node("language_detector", detect_language)
    graph.add_node("eligibility_assessor", assess_eligibility)
    graph.add_node("web_search", web_search)
    graph.add_node("plan_generator", generate_plan)
    graph.add_node("memory_writer", write_memory)
    
    graph.set_entry_point("language_detector")
    graph.add_edge("language_detector", "eligibility_assessor")
    graph.add_edge("eligibility_assessor", "web_search")
    graph.add_edge("web_search", "plan_generator")
    graph.add_edge("plan_generator", "memory_writer")
    graph.add_edge("memory_writer", END)
    
    return graph.compile()

agent = build_graph()
