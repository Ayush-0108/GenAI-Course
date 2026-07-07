from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional , Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

class Review(TypedDict):
    key_themes : Annotated[list[str], "tell the key themes of the destination in a list"]
    summary : Annotated[str, "Detailed description of the review"]
    pros : Annotated[Optional[list[str]],"write all the pros inside a list "]
    cons : Annotated[Optional[list[str]],"Write down all the cons in a list"]
    sentiment : Annotated[Literal["pos","neg","mid"],"Tell the sentiment of the review either positive , negative or neutral"]
    name : Annotated[Optional[str],"Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently had the opportunity to visit Japan, and it was one of the most memorable trips I've ever taken. From the bustling streets of Tokyo to the peaceful temples of Kyoto, every city offered a unique blend of modern innovation and rich cultural heritage. The public transportation system was incredibly efficient, making it easy to travel between destinations with minimal hassle.

One of the highlights of my trip was experiencing Japanese cuisine. Whether it was fresh sushi from local markets, steaming bowls of ramen, or traditional matcha desserts, every meal felt like a new adventure. I was also impressed by how clean and organized the cities were. Even in crowded places, everything seemed calm and well-managed.

The locals were polite and welcoming, always willing to help despite the language barrier. Visiting famous landmarks such as Mount Fuji and the historic shrines was an unforgettable experience. During spring, the cherry blossoms added a magical atmosphere that made every walk feel like a postcard come to life.

However, the trip wasn't without its challenges. Japan can be quite expensive, especially in major cities where accommodation and transportation costs add up quickly. English is not widely spoken in some rural areas, which occasionally made communication difficult. Popular tourist attractions were also very crowded, particularly during peak travel seasons.

Overall, Japan is a fantastic destination for anyone interested in culture, history, technology, and food. The combination of breathtaking scenery, efficient infrastructure, and warm hospitality makes it a country worth visiting at least once in a lifetime.

Highlights:
- Beautiful blend of traditional culture and modern technology
- World-class public transportation system
- Delicious and diverse cuisine
- Safe, clean, and well-organized cities
- Friendly and respectful local people

Travel Experience by Ananya Mehta
""")

print(result)