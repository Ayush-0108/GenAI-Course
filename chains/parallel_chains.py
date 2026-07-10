from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGroq(model = "llama-3.3-70b-versatile")

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct",
                          task = "text-generation")

model2 = ChatHuggingFace(llm=llm)
# model2 might take more time than usual to load please keep patience, thank you
parser = StrOutputParser()

prompt1 = PromptTemplate(template = "write a detailed notes on the {topic}",
                          input_variables=["topic"])
prompt2 = PromptTemplate(template = "give 5 mcq questions on the {topic}",
                          input_variables=["topic"])
prompt3 = PromptTemplate(template = "merge the text from the two sources as notes ->{notes} and quiz ->{quiz}",
                         input_variables=["notes","quiz"]
)

parallel_chain= RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"topic":"linear regression"})

print(result)

chain.get_graph().print_ascii()