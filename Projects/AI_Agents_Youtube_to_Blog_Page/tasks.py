from crewai import Task
from agents import blog_researcher, writer
from tools import tool



# Research task
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[tool],
  agent=blog_researcher,
)
# Writing task with language model configuration
write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic}',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)
