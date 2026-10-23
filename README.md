<<<<<<< HEAD
# LangChain Prompt Engineering Lab

A beginner-friendly learning project for understanding prompt engineering, messages, prompt templates, placeholders, chat history, and model invocation with LangChain.

This repository follows a practical, step-by-step learning path. Each Python file focuses on one LangChain concept so that learners can run the examples, inspect the output, and understand how the pieces connect.

> This is a learning project, not a production chatbot.

---

## Table of Contents

- [Demo](#demo)
- [Project Goal](#project-goal)
- [Problem Statement](#problem-statement)
- [What It Does](#what-it-does)
- [Features](#features)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Example Output](#example-output)
- [Core Concepts](#core-concepts)
- [Current Status](#current-status)
- [Milestones](#milestones)
- [Roadmap](#roadmap)
- [Known Limitations](#known-limitations)
- [Data and Privacy](#data-and-privacy)
- [Deploying to Render](#deploying-to-render)
- [Contributing](#contributing)
- [License](#license)
- [Connect](#connect)

---

## Demo

The project contains small runnable programs that demonstrate:

- Basic chat model invocation.
- Single-message prompts.
- Lists of system, human, and AI messages.
- Dynamic prompt variables.
- Chat prompt templates.
- Message placeholders.
- Conversation history.
- A terminal-based chatbot.

Run the interactive chatbot:

```bash
python chatbot.py
```

Then enter a message after:

```text
You:
```

To stop the chatbot:

```text
exit
```

---

## Project Goal

The goal of this project is to build a strong foundation in LangChain prompt engineering through small, understandable examples.

The project focuses on learning how to:

1. Create messages.
2. Combine different message types.
3. Build reusable prompt templates.
4. Insert dynamic values into prompts.
5. Insert chat history at runtime.
6. Invoke a chat model.
7. Maintain a simple conversation history.
8. Understand the flow from prompt to model response.

---

## Problem Statement

Beginners often see complete LangChain applications before understanding the smaller building blocks behind them.

This project solves that learning problem by separating the concepts into simple Python files. Each file demonstrates one idea and can be executed independently.

Instead of learning one large application at once, learners can follow this flow:

```text
Messages
   ↓
Prompt Templates
   ↓
Dynamic Variables
   ↓
Message Placeholders
   ↓
Model Invocation
   ↓
Conversation History
   ↓
Interactive Chatbot
```

---

## What It Does

This repository demonstrates how LangChain can be used to:

- Define system instructions.
- Send human questions to a chat model.
- Represent model responses as AI messages.
- Create reusable chat prompt templates.
- Pass dynamic values into prompts.
- Insert previous messages into a prompt.
- Call a model through OpenRouter.
- Build a simple command-line chatbot.

---

## Features

- Beginner-friendly LangChain examples.
- OpenRouter model integration.
- Environment-variable-based API key management.
- Message-based chat history.
- Dynamic prompt variables.
- `MessagesPlaceholder` demonstration.
- Interactive terminal chatbot.
- Small files that can be tested independently.
- Step-by-step learning structure.
- No API key stored in source code.

---

## How It Works

The project has two main stages.

### Stage 1: Create the prompt

A prompt is created from messages and templates.

```python
prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Doosra"
})
```

The template receives values and creates structured chat messages.

### Stage 2: Invoke the model

The model receives the messages:

```python
response = model.invoke(messages)
```

The response is an AI message:

```python
print(response.content)
```

For a chatbot, the process repeats:

```text
User input
   ↓
HumanMessage
   ↓
Chat history
   ↓
model.invoke(chat history)
   ↓
AIMessage
   ↓
Display response
```

---

## Architecture

```text
User
 │
 ▼
Terminal Input
 │
 ▼
HumanMessage
 │
 ▼
Chat History
 │
 ▼
ChatPromptTemplate or Direct Messages
 │
 ▼
ChatOpenRouter
 │
 ▼
OpenRouter API
 │
 ▼
AIMessage
 │
 ▼
Terminal Output
```

The project uses LangChain as the interface between the Python application and the chat model provider.

---

## Tech Stack

- Python
- LangChain
- LangChain Core
- LangChain OpenRouter
- OpenRouter API
- python-dotenv
- Git
- GitHub

---

## Quick Start

### 1. Clone the repository

```bash
git clone [https://github.com/YOUR_USERNAME/langchain-prompt-engineering-lab.git](https://github.com/YOUR_USERNAME/langchain-prompt-engineering-lab.git)
cd langchain-prompt-engineering-lab
```

### 2. Create a virtual environment

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -U langchain langchain-core langchain-openrouter python-dotenv
```

### 4. Create the environment file

Create a file named `.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Never commit `.env` to GitHub.

### 5. Run the examples

```bash
python chat_prompt_template.py
python message_placeholder.py
python messages.py
python chatbot.py
```

---

## Environment Variables

The project uses the following environment variable:

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | API key used to access OpenRouter models |

Example:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

The `.env` file is intentionally excluded through `.gitignore`.

---

## API Documentation

### OpenRouter

OpenRouter provides access to multiple chat models through a unified API.

The project uses the LangChain integration:

```python
from langchain_openrouter import ChatOpenRouter
```

Example:

```python
model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0,
    timeout=30,
    max_retries=0
)
```

### LangChain Model Invocation

A model is invoked with:

```python
response = model.invoke(messages)
```

The returned response is an `AIMessage`.

To print only the response text:

```python
print(response.content)
```

---

## Project Structure

```text
.
├── .env.example
├── .gitignore
├── README.md
├── chat_history.txt
├── chat_prompt_template.py
├── chatbot.py
├── message_placeholder.py
├── messages.py
└── requirements.txt
```

The `.venv` folder may exist locally, but it should not be committed to GitHub.

### `chat_prompt_template.py`

Demonstrates a reusable `ChatPromptTemplate` with dynamic variables.

Example variables:

```python
{domain}
{topic}
```

The template is invoked with:

```python
prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Doosra"
})
```

### `message_placeholder.py`

Demonstrates `MessagesPlaceholder`.

It inserts a list of messages into a prompt at runtime.

```python
MessagesPlaceholder(variable_name="chat_history")
```

### `messages.py`

Demonstrates direct model invocation using a list of messages.

### `chatbot.py`

Demonstrates an interactive terminal chatbot with conversation history.

### `chat_history.txt`

Reserved for experimenting with external chat-history storage. The current chatbot stores history in memory while it is running.

---

## Core Concepts

### 1. Model Invocation

Model invocation means sending input to a chat model and receiving a response.

```python
response = model.invoke(messages)
```

The response can be printed with:

```python
print(response.content)
```

There are two common input styles.

#### Single-message input

A model can receive one message or one simple text input:

```python
response = model.invoke("Explain LangChain simply")
```

This is useful for simple requests without a manually constructed conversation.

#### List-of-messages input

A model can receive a list of structured messages:

```python
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain LangChain simply.")
]

response = model.invoke(messages)
```

This is useful when you want to control roles and conversation history.

---

### 2. Message Types

LangChain commonly uses three message roles.

#### `SystemMessage`

Defines instructions or behavior for the model.

```python
SystemMessage(
    content="You are a helpful customer support agent."
)
```

#### `HumanMessage`

Represents the user’s message.

```python
HumanMessage(
    content="Where is my refund?"
)
```

#### `AIMessage`

Represents the model’s response.

```python
AIMessage(
    content="I will check your refund status."
)
```

---

### 3. Static and Dynamic Prompt Content

Prompt templates usually contain static and dynamic content.

#### Static content

Static content remains the same each time the template is used.

```python
("system", "You are a helpful cricket expert")
```

#### Dynamic content

Dynamic content changes at runtime through variables.

```python
("system", "You are a helpful {domain} expert")
("human", "Explain {topic}")
```

Values are supplied during invocation:

```python
prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Doosra"
})
```

---

### 4. `ChatPromptTemplate`

`ChatPromptTemplate` creates a reusable structure for chat messages.

```python
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain {topic} in simple terms")
])
```

It separates the prompt design from the values supplied later.

---

### 5. `MessagesPlaceholder`

`MessagesPlaceholder` is a special placeholder used inside a chat prompt template to insert a list of messages at runtime.

```python
MessagesPlaceholder(
    variable_name="chat_history"
)
```

Example:

```python
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])
```

The history is supplied during invocation:

```python
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})
```

This is useful for:

- Conversation history.
- Previous human messages.
- Previous AI responses.
- Multi-turn chat.
- Reusable prompt structures.

---

### 6. Message History

The chatbot stores previous messages in a list:

```python
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]
```

Each user message is added:

```python
chat_history.append(
    HumanMessage(content=user_input)
)
```

Each model response is also added:

```python
chat_history.append(result)
```

The complete history is sent on the next invocation:

```python
result = model.invoke(chat_history)
```

This gives the model context from earlier turns.

---

## Example Output

### Chat prompt template

```text
System: You are a helpful cricket expert
Human: Explain in simple terms, what is Doosra
```

### Message placeholder

```text
System: You are a helpful customer support agent
Human: I requested a refund last week.
AI: I will check the refund status for you.
Human: Where is my refund?
```

### Chatbot

```text
You: Hi
AI: Hi! How can I help you today?

You: Explain LangChain
AI: LangChain is a framework for building applications powered by language models.

You: exit
```

The exact model response may vary.

---

## Current Status

Completed:

- Basic message examples.
- System, human, and AI messages.
- Direct model invocation.
- Dynamic chat prompt templates.
- Message placeholders.
- In-memory conversation history.
- Terminal chatbot.
- OpenRouter integration.
- Environment-variable configuration.

---

## Milestones

### Milestone 1: Message Fundamentals

- Learn message roles.
- Create message lists.
- Invoke a model with messages.

### Milestone 2: Prompt Templates

- Create reusable chat templates.
- Add dynamic variables.
- Invoke templates with runtime values.

### Milestone 3: Conversation History

- Store human messages.
- Store AI responses.
- Insert history with `MessagesPlaceholder`.

### Milestone 4: Interactive Chatbot

- Read terminal input.
- Call the model.
- Print responses.
- Stop with the `exit` command.

### Milestone 5: Better Application Design

- Separate configuration from application logic.
- Add error handling.
- Add persistent history.
- Add tests.
- Add a user interface.

---

## Roadmap

- [ ] Add a `requirements.txt` file.
- [ ] Add `.env.example`.
- [ ] Add error handling for unavailable models.
- [ ] Add conversation-history persistence.
- [ ] Add streaming responses.
- [ ] Add prompt templates for multiple use cases.
- [ ] Add automated tests.
- [ ] Add a web interface.
- [ ] Explore LangGraph.
- [ ] Add retrieval-augmented generation.
- [ ] Add document loading and embeddings.
- [ ] Deploy a web version.

---

## Known Limitations

- Free OpenRouter models may be slow or temporarily unavailable.
- Free model limits may change.
- Chat history currently exists only in memory.
- Restarting the chatbot clears the conversation.
- The project is intended for learning, not production.
- Responses depend on the selected model.
- There is no authentication or web interface.
- Error handling is basic.
- Python 3.14 may show compatibility warnings with some dependencies.

---

## Data and Privacy

- Never commit `.env` or API keys.
- Do not include private or sensitive information in prompts.
- Requests are sent to the selected model provider.
- Review the provider’s privacy and data-retention policies before using sensitive data.
- Delete and rotate an API key immediately if it is accidentally exposed.

---

## Deploying to Render

This project currently runs as a command-line application and is not directly suitable for a normal Render web service.

To deploy it to Render, first add a web framework such as Flask or FastAPI.

A future web version may use:

```text
Browser
   ↓
FastAPI or Flask
   ↓
LangChain
   ↓
OpenRouter
```

General deployment steps:

1. Add a web application entry point.
2. Add a `requirements.txt` file.
3. Add a start command.
4. Push the changes to GitHub.
5. Create a Render Web Service.
6. Connect the GitHub repository.
7. Add `OPENROUTER_API_KEY` as a Render environment variable.
8. Deploy the service.

Never place the API key directly in source code.

A possible future start command is:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

This command applies only after adding a FastAPI application named `app.py`.

---

## Contributing

Contributions are welcome.

### Basic contribution process

1. Fork the repository.
2. Create a branch:

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Test your changes.
5. Commit your changes:

```bash
git add .
git commit -m "Add your change description"
```

6. Push the branch:

```bash
git push origin feature/your-feature
```

7. Open a pull request.

Please keep examples beginner-friendly and explain new LangChain concepts clearly.

---

## License

This project is intended for educational use.

You may add an MIT License if you want others to reuse and modify the code. Create a file named `LICENSE` and select the MIT License through GitHub’s license options.

---

## Connect

Created by **Vaibhav Singh**

- GitHub: `hhttps://github.com/vaibhav9014`
- LinkedIn: `ADD_YOUR_LINKEDIN_URL`
- Portfolio: `ADD_YOUR_PORTFOLIO_URL`

If this repository helps you learn LangChain, consider starring it and sharing suggestions.
=======
# Langchain-prompt-engineering-lab
A beginner-friendly LangChain prompt engineering lab covering messages, prompt templates, placeholders, chat history, and model invocation.
>>>>>>> 26d414a9396820833bb2c5bf27c4303637d5dcd9
