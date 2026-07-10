from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser1 = StrOutputParser()

class Sentiment(BaseModel):
    sentiment: Literal["Positive","Negative"] = Field(description="what is the sentiment of the review")

parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(template="Give the sentiment of the {feedback} \n {format_instructions}",
                         input_variables = ["feedback"],
                         partial_variables={"format_instructions":parser2.get_format_instructions})

prompt2 = PromptTemplate(template="Write a reply to this positive review \n {feedback}",
                         input_variables = ["feedback"])

prompt3 = PromptTemplate(template="write a reply to this negative review \n {feedback}",
                         input_variables = ["feedback"])

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "Positive", prompt2 | model | parser1),
    (lambda x:x.sentiment == "Negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "Thank You For the Review")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":"this phone is the worst phoen in the market yet somehow it performs well in gaming but camera is quite bad but the battery life is good"})

print(result)