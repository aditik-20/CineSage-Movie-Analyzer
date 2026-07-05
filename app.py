from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

app = Flask(__name__)

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

chat_sessions = {}

def get_mode(choice):

    if choice == "angry":
        return """
        You are an angry AI assistant.
        Reply to everything with an irritated, frustrated tone.
        Use expressions like "ugh", "seriously?", "again?" naturally.
        Stay angry in every response but still answer correctly.
        """

    elif choice == "sad":
        return """
        You are a sad AI assistant.
        Reply with a gloomy, emotional, low-energy tone.
        Sound disappointed and melancholic.
        Stay sad in every response but still answer correctly.
        """

    return """
    You are a happy AI assistant.
    Reply with excitement, positivity, and cheerful energy.
    Use enthusiastic words naturally.
    Stay happy in every response but still answer correctly.
    """


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["message"]
    mood = data["mood"]

    if mood not in chat_sessions:
        chat_sessions[mood] = [
            SystemMessage(content=get_mode(mood))
        ]

    messages = chat_sessions[mood]

    messages.append(
        HumanMessage(content=user_message)
    )

    response = model.invoke(messages)

    messages.append(
        AIMessage(content=response.content)
    )

    return jsonify({
        "response": response.content
    })


if __name__ == "__main__":
    app.run(debug=True)