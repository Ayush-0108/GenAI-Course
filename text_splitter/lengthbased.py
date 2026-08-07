from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"D:\Ayush_Files\Users\kumar\GenAI-Course\text_splitter\dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= "",
)

result = splitter.split_documents(docs)
print(result[0].page_content)