from crewai import Crew,Process
from tasks import research_task, write_task
from agents import blog_researcher, writer


crew = Crew(
  agents=[blog_researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

# start the task execution process with enhanced feedback
# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)