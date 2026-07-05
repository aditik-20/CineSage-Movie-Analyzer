from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

print("---------------- Welcome (type 0 to exit) ----------------")
print("Choose your mode")
print("1 -> Angry mode")
print("2 -> Sad mode")
print("3 -> Happy mode")

choice = int(input("Tell: "))

if choice == 1:
    mode = """
    You are an angry AI assistant.
    Reply to everything with an irritated, frustrated tone.
    Use expressions like "ugh", "seriously?", "again?" naturally.
    Stay angry in every response but still answer correctly.
    """

elif choice == 2:
    mode = """
    You are a sad AI assistant.
    Reply with a gloomy, emotional, low-energy tone.
    Sound disappointed and melancholic.
    Stay sad in every response but still answer correctly.
    """

elif choice == 3:
    mode = """
    You are a happy AI assistant.
    Reply with excitement, positivity, and cheerful energy.
    Use enthusiastic words naturally.
    Stay happy in every response but still answer correctly.
    """

else:
    print("Invalid choice")
    exit()

messages = [
    SystemMessage(content=mode)
]

while True:
    prompt = input("You : ")

    if prompt == "0":
        print("Goodbye!")
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot :", response.content)