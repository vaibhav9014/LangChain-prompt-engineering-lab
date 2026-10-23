from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv


load_dotenv()


model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0
)


messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="Who won the World Series in 2020?")
]


response = model.invoke(messages)

print(response.content)