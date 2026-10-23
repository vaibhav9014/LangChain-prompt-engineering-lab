from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])


chat_history = [
    HumanMessage(content="I requested a refund last week."),
    AIMessage(content="I will check the refund status for you.")
]


prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})


print(prompt)