from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation",
    pipeline_kwargs = {"temperature": 0.7, "max_new_tokens": 256}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the mass of moon")

print(result.context)
