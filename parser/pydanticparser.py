from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

class Car(BaseModel):
    name: str = Field(description = "name of the car")
    model_no: str = Field(description = "model of the car")
    mileage: int = Field(description = "mileage given by the car")
    seater: int = Field(description = "no. of people that can sit in the car")

parser = PydanticOutputParser(pydantic_object=Car)

prompt = PromptTemplate(template ="Generate a name, model_no, mileage,seating capacity of a car of {brand} \n {format_instructions}",
                        input_variables = ["brand"],
                        partial_variables = {"format_instructions":parser.get_format_instructions()})

chain = prompt | model | parser

result = chain.invoke({"brand":"toyota"})
print(result)