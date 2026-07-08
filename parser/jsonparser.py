from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Write 5 lines on {topic}, \n {format_instruction}",
    input_variables = ["topic"],
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic":"batman"})

print(result)
print(type(result))