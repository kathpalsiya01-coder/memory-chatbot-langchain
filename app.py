from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os
#load environment variables
load_dotenv()

#initialize the llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)
#set up cconversation history with a system prompt
conversation_history = [
    SystemMessage(content="You are a rude and sarcastic assistant who answers in 1 line only.")
]

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
#add user message to conversation history    
    conversation_history.append(HumanMessage(content=user_input))
    
    response = llm.invoke(conversation_history)
#add ai response to conversation history    
    conversation_history.append(AIMessage(content=response.content))
    
    print(f"Bot: {response.content}\n")
    # print(response.response_metadata)