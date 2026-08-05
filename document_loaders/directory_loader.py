from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path = r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\Books",
    glob = "*.pdf",
    loader_cls= PyPDFLoader
)

docs  = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)