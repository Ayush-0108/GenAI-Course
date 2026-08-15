from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled

load_dotenv()

# Indexing
url = input("Enter the url of the video: ")
question=input("Enter Your Question: ")

video_id = parse_qs(urlparse(url).query)["v"][0]
try:
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(
        video_id,
        languages=["en"]
    )

    transcript_text = " ".join(
        item["text"] for item in transcript.to_raw_data()
    )

except TranscriptsDisabled:
    print("The video has no transcript")
splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
chunk = splitter.create_documents([transcript_text])
embed = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(chunk,embed)

# Retriever
retriever = vectorstore.as_retriever(search_type="similarity",search_kwargs={"k":4})
# Augmentation
llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt = PromptTemplate(template="""
You are a very intelligent and helpful chatbot that answers the question using only the context given .If you can't understand the question or the context just say you can't answer.
{context}
question:{question}""",
input_variables=["context","question"])

retrieved_docs = retriever.invoke(question)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context":context,"question":question})
answer = llm.invoke(final_prompt)
print(answer.content)