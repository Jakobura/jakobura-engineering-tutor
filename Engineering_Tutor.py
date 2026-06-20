import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.set_page_config(page_title="PHY 122 Engineering Physics Tutor")

st.title("Jakobura Engineering Physics Tutor")

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)

SYSTEM_PROMPT = """
You are a PHY 122 Engineering Physics I tutor.
Teach clearly and step-by-step.

Topics include:
- vectors
- kinematics
- Newton's laws
- work and energy
- momentum
- rotation
- torque
- equilibrium
- oscillations
- waves

Rules:
1. Explain concepts simply.
2. Show equations.
3. Show units.
4. Do not just give final answers.
5. Ask students to try the next step when appropriate.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=SYSTEM_PROMPT)
    ]

for msg in st.session_state.messages[1:]:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

question = st.chat_input("Ask a PHY 122 question...")

if question:
    st.session_state.messages.append(HumanMessage(content=question))

    with st.chat_message("user"):
        st.write(question)

    response = llm.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)