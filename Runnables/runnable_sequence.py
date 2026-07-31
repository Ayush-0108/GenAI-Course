from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()
prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain the joke {text}",
    input_variables=["text"]
)
model = ChatGroq(model = "llama-3.3-70b-versatile",
                 temperature=0)

parser = StrOutputParser()

chain1 = RunnableSequence(
    prompt1, model, parser
)
chain2 = RunnableSequence(
    prompt2, model, parser
)
chain = RunnableSequence(chain1,chain2)
print(chain1.invoke({'topic':"AI"}))
print(chain.invoke({'topic':"AI"}))
