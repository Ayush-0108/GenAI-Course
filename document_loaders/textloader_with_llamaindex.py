from llama_index.core import SimpleDirectoryReader
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
model = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()
prompt = PromptTemplate(template="write the summary of following {text}",
                        input_variables=["text"])

llama_docs = SimpleDirectoryReader(input_files=[r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\text.txt"]).load_data()

docs = [Document(page_content=doc.text,metadata = doc.metadata)
        for doc in llama_docs
        ]
print(docs)
print(len(docs))

chain = prompt | model | parser

print(chain.invoke({"text":docs[0].page_content}))