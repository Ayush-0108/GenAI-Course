from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv()

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(template= "write a detailed description about {topic}",
                         input_variables = ["topic"])


prompt2 = PromptTemplate(template= "write 5 lines on the text {text}",
                         input_variables = ["text"])

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":"titan watches"})

print(result)

chain.get_graph().print_ascii()