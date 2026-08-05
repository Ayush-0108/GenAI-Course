from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path = r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\Books",
    glob = "*.pdf",
    loader_cls= PyPDFLoader
)

docs  = loader.load()

for document in docs:
    print(document.metadata)
# this would present the result all at once 

docs = loader.lazy_load()
for document in docs:
    print(document.metadata)
# this would produce the result one at a time and not keep u waiting