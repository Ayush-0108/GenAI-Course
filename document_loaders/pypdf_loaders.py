# from langchain_community.document_loaders import PyPDFLoader

# loader  = PyPDFLoader(r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\dl-curriculum.pdf")

# docs = loader.load()

# print(docs)
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

# from llama_index.core import SimpleDirectoryReader
# from langchain_core.documents import Document
# path_file = r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\dl-curriculum.pdf"
# llama_docs = SimpleDirectoryReader(input_files=[path_file]).load_data()

# docs = [Document(page_content=doc.text,metadata=doc.metadata)
#         for doc in llama_docs]

# print(docs[0].page_content)
