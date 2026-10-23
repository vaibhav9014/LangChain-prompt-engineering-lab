from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()


model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0,
    timeout=30,
    max_retries=0
)


chat_history = [
    SystemMessage(
        content=(
            "You are a helpful AI assistant. "
            "Answer clearly and briefly unless the user asks for detail."
        )
    )
]


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    chat_history.append(HumanMessage(content=user_input))

    print("AI is thinking...", flush=True)

    try:
        result = model.invoke(chat_history)
        chat_history.append(result)
        print("AI:", result.content, flush=True)

    except Exception as e:
        print("Error:", type(e).__name__, flush=True)
        print(e, flush=True)