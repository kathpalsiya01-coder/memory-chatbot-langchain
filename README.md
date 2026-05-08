# Memory Chatbot using LangChain + Groq

## Overview

This project is a conversational AI chatbot with memory support built using LangChain and Groq LLM APIs.  
The chatbot maintains conversation history and generates context-aware responses for more natural and engaging interactions.

It demonstrates how conversational memory can improve chatbot intelligence by allowing the model to remember previous user inputs during a session.

---

## Features

- Conversational memory support
- Context-aware responses
- Real-time terminal interaction
- LangChain integration
- Groq LLM API integration
- Message history handling
- Lightweight and beginner-friendly architecture

---

## Tech Stack

- Python
- LangChain
- Groq API
- dotenv
- VS Code

---

## Project Structure


memory-chatbot-langchain/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── conversation.png


### Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/memory-chatbot-langchain.git

### 2. Navigate to the project folder

cd memory-chatbot-langchain

### 3. Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the root directory and add your Groq API key:


GROQ_API_KEY=your_api_key_here


---

## Run the Project


python app.py


---

## Example Conversation


You: My favorite programming language is Python.

Bot: Interesting choice. Another Python enthusiast joins the crowd.

You: What is my favorite programming language?

Bot: Python. Your memory may fail, mine unfortunately doesn't.
```

---

## Memory Demonstration


You: I am preparing for AI internships.

Bot: Brave decision. The competition is only slightly terrifying.

You: What am I preparing for?

Bot: AI internships. Try not to panic before the interviews.

---

## Future Improvements

- Streamlit web interface
- Persistent memory storage
- Voice-enabled interaction
- Vector database integration
- Multi-user support
- Long-term memory handling
- Deployment on cloud platforms

---

## Learning Outcomes

Through this project, I learned:

- How conversational memory works in LLM applications
- LangChain message handling
- Prompt engineering basics
- API integration with Groq
- Context-aware response generation
- Structuring AI projects for GitHub

---

## Author

Siya Kathpal

---

## Topics

`langchain`, `llm`, `chatbot`, `groq`, `python` ,`generative-ai` ,`memory-chatbot`, `ai-project`
