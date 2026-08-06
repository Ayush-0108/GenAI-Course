import os

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36"
)

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

model = ChatGroq(model= "llama-3.3-70b-versatile")
parser = StrOutputParser()

url = "https://www.amazon.in/Apple-2024-MacBook-Laptop-chip/dp/B0DLHFSR9S/ref=sr_1_4?crid=3J44YKN0HOYDC&dib=eyJ2IjoiMSJ9.ppENzF8W_dgGBLrPMTPG3wxrBZv-wd_SA5oGTRCRqE7BUfcmA3jj4Nuln-0ExJVMvT6tnDZJVsyPGmb3VlxIrJPLcwzBsVwyp2vtIT-DfMUIsABhIesbmOrxS4Y4fQQpAYFzs1m8fIsJ4TOoXxaI2LeSp-I0AfQyp02nvYXZ7kwaaYnbuXEngO28FeDkHajx.AXX0SXL4APaWaNM__3sbyvd2JayH7uvhvzu61Pv8eYA&dib_tag=se&keywords=macbook&qid=1786013998&s=kitchen&sprefix=macbook%2Ckitchen%2C283&sr=1-4"
loader = WebBaseLoader(url)

docs = loader.load()
scrapped_data = docs[0].page_content
prompt = PromptTemplate(template="answer the {question} using the following"f"{scrapped_data}",
                        input_variables=["question"])
chain = prompt | model | parser
print(chain.invoke({"question":"what is the name of this product"}))
# print(docs[0].page_content)
# print(len(docs))

