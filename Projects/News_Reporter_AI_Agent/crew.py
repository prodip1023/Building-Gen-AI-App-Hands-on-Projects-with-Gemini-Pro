from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

crew = Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
)

# Starting the task execution process
result = crew.kickoff(inputs={'topic':'AI in healthcare'})

# Printing the final result
print(result)