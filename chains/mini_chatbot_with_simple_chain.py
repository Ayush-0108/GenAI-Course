from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
topic = input("enter input:")

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt = PromptTemplate(template = "You are a very helpful agent for {topic}",
                        input_variables = ["topic"])

chain = prompt | model | parser

result = chain.invoke({"topic":topic})

print(result)

chain.get_graph().print_ascii()