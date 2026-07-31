from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")
prompt = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()
def wordcounter(text):
    return len(text.split())

joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "wordcounter": RunnableLambda(wordcounter)
})

final_chain = RunnableSequence(joke_chain,parallel_chain)
print(final_chain.invoke({"topic":"AI"}))