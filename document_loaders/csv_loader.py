from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path=r"D:\Ayush_Files\Users\kumar\GenAI-Course\document_loaders\Social_Network_Ads.csv")
docs = loader.load()
print(len(docs))
print(docs[0].page_content)