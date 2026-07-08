from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

schema = [
    ResponseSchema(name = "topic",description ="the topic of the explanation given"),
    ResponseSchema(name = "list",description ="the list of lines explained ")
]

parser= StructuredOutputParser.from_response_schemas(schema)

prompt = PromptTemplate(template = "write 5 lines on {topic} \n {format_instruction}",
                        input_variables= ["topic"],
                        partial_variables= {"format_instruction":parser.get_format_instructions()})

chain = prompt | model | parser

result = chain.invoke({"topic":"human"})

print(result)
print(type(result))