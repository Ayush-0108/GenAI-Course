from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
topic = input("Enter topic:")
model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = StrOutputParser()

template = PromptTemplate(template="Write a detailed explanation on {topic}",
                          input_variables = ["topic"])

chain = template | model | parser

result = chain.invoke({"topic":topic})

print(result)