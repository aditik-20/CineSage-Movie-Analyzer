import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mood AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom,#111827,#1f2937);
}

.main-title{
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:bold;
}

.sub{
    text-align:center;
    color:#d1d5db;
    margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.markdown(
    '<p class="main-title">🤖 Mood AI Chatbot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub">Choose a mood and start chatting</p>',
    unsafe_allow_html=True
)


# ---------------- MODEL ----------------
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🎭 Select Mood")

    choice = st.radio(
        "Choose chatbot personality",
        ["😡 Angry", "😢 Sad", "😄 Happy"]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()



# ---------------- MODES ----------------
if choice == "😡 Angry":
    mode = """
    You are an angry AI assistant.
    Reply to everything with an irritated, frustrated tone.
    Use expressions like "ugh", "seriously?", "again?" naturally.
    Stay angry in every response but still answer correctly.
    """

elif choice == "😢 Sad":
    mode = """
    You are a sad AI assistant.
    Reply with a gloomy, emotional, low-energy tone.
    Sound disappointed and melancholic.
    Stay sad in every response but still answer correctly.
    """

else:
    mode = """
    You are a happy AI assistant.
    Reply with excitement, positivity, and cheerful energy.
    Use enthusiastic words naturally.
    Stay happy in every response but still answer correctly.
    """


# ---------------- SESSION ----------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]


# Reset if mood changes
if (
    len(st.session_state.messages) > 0
    and st.session_state.messages[0].content != mode
):

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]


# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)



# ---------------- INPUT ----------------
prompt = st.chat_input("Type your message...")


if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.write(response.content)


    st.session_state.messages.append(
        AIMessage(content=response.content)
    )