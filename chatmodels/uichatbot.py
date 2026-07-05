import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ---------------- MODEL ----------------
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

# ---------------- UI TITLE ----------------
st.title("🤖 Simple AI Chatbot")
st.write("Type your message below and chat with AI")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are funny ai agent")
    ]

# ---------------- DISPLAY CHAT HISTORY ----------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# ---------------- INPUT BOX ----------------
prompt = st.chat_input("Type your message...")

if prompt:
    # show user message
    st.chat_message("user").write(prompt)

    # keep same logic
    st.session_state.messages.append(HumanMessage(content=prompt))

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    # show bot response
    st.chat_message("assistant").write(response.content)