from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template="write a report on the following {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="summarize the following {text}",
    input_variables=["variables"]
)

parser = StrOutputParser()

report_chain = prompt1|model|parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain,branch_chain)
print(final_chain.invoke({"topic":"AI"}))

final_chain.get_graph().print_ascii()