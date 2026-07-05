from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, jsonify
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

prompt = ChatPromptTemplate.from_messages([

    ("system", """
You are an intelligent information extraction assistant.

Your task is to analyze the given text and extract useful information in a clean, readable format.

Rules:
- Extract only information present in the text.
- Do NOT hallucinate missing information.
- If information is unavailable, write "Not Mentioned".
- Ignore repeated information and remove duplicates.
- Generate a short summary at the end.

Extract:

Movie Name:
Category:
Genre:
Director/Creator:
Cast:
Main Characters:
Themes:
Key Topics:
Scientific Concepts:
Technologies:
Locations:
Important Events:
Story/Plot:
Tone:
Notable Features:
Keywords:
Quick Summary:
"""),

("human", """
Analyze the following text and extract useful information:

{text}
""")

])

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# AI processing
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    paragraph = data["text"]

    final_prompt = prompt.invoke(
        {"text": paragraph}
    )

    response = model.invoke(final_prompt)

    return jsonify({
        "result": response.content
    })


if __name__ == "__main__":
    app.run(debug=True)