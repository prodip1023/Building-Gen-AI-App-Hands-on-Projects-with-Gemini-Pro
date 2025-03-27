from crewai import Agent,LLM
from tools import tool
import os
from dotenv import load_dotenv


load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"
# Correct
llm = LLM(model="openai/gpt-4-0125-preview")




# Create a senior blog content reseacher

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic {topic} from Yt channel',
    verbose=True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science , Machine Learning and GEN AI and providing suggestion"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a senior blog writer with YT tool
writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about the video {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
