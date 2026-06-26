import streamlit as st
import sys
sys.path.insert(0, r"C:\Users\Razak\schemebot_pro")
from graph import agent

st.set_page_config(page_title="SchemeBot Pro", page_icon="🏛️")
st.title("🏛️ SchemeBot Pro")
st.subheader("Indian Government Welfare Scheme Advisor")
st.caption("Ask in English or Telugu | ఆంగ్లంలో లేదా తెలుగులో అడగండి")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input(
    "Enter your situation:",
    placeholder="e.g. I am a farmer with 2 acres of land in AP"
)

if st.button("Get My Scheme Plan") and user_input:
    with st.spinner("Analyzing your eligibility..."):
        result = agent.invoke({
            "user_input": user_input,
            "language": "",
            "eligibility": "",
            "search_results": [],
            "plan": ""
        })
    
    st.session_state.history.append({
        "input": user_input,
        "language": result["language"],
        "eligibility": result["eligibility"],
        "plan": result["plan"]
    })

if st.session_state.history:
    latest = st.session_state.history[-1]
    
    st.markdown("---")
    st.markdown(f"**Language detected:** {latest['language'].capitalize()}")
    
    with st.expander("Eligibility Assessment", expanded=True):
        st.markdown(latest["eligibility"])
    
    with st.expander("Your Application Plan", expanded=True):
        st.markdown(latest["plan"])
    
    if len(st.session_state.history) > 1:
        st.markdown("---")
        st.markdown("**Previous queries this session:**")
        for item in st.session_state.history[:-1]:
            st.markdown(f"- {item['input']}")
