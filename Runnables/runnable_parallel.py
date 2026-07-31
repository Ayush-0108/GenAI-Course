from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGroq(model = "llama-3.3-70b-versatile")
prompt1 = PromptTemplate(
    template="Write a tweet on the {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="write a linkedin post on the {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1,model,parser),
    "linkedin": RunnableSequence(prompt2,model,parser)
})
result = parallel_chain.invoke({'topic':"ai"})
print(result["tweet"])
print("-"*100)
print(result["linkedin"])