from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()
chat_history = [SystemMessage(content="you are a helpful agent")]
url = input("Enter the url of the video: ")
chat_history = [HumanMessage(content=url)]
while True:
    question=input("Enter Your Question: ")
    if question == "exit":
        break
    chat_history.append(HumanMessage(content=[question]))
    def context(url,question):
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
        splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
        chunk = splitter.create_documents([transcript_text])
        embedding = HuggingFaceEmbeddings()
        vectorstore = Chroma.from_documents(chunk,embedding)
        retriever = vectorstore.as_retriever(search_type="similarity",search_kwargs = {"k":4})
        retrieved = retriever.invoke(question)
        context =  "\n\n".join(doc.page_content for doc in retrieved)
        return context

    parallel_chain = RunnableParallel({
        "context":RunnableLambda(lambda x: context(x["url"],x["question"])),
        "question":RunnableLambda(lambda x: x["question"]),
        "chat_history": RunnableLambda(lambda x: x["chat_history"])
    })

    parser = StrOutputParser()
    prompt = PromptTemplate(template="""
    You are a very intelligent and helpful chatbot that answers the question using only the context given and the chat history .If you can't understand the question or the context just say you can't answer.
    {context}
    chat history:{chat_history}
    question:{question}""",
    input_variables=["context","chat_history","question"])
    llm = ChatGroq(model = "llama-3.3-70b-versatile")

    final_chain = parallel_chain | prompt | llm | parser

    chat_history.append(AIMessage(content=final_chain.invoke({
        "url": url,
        "chat_history":chat_history,
        "question": question
    })))
print(chat_history)