from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-7B-Instruct",
#     task="text-generation",

# )

# model = ChatHuggingFace(llm=llm)

chat_history = [SystemMessage(content="you are a helpful agent")]

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(chat_history)