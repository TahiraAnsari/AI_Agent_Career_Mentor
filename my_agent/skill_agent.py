from agents import Agent
from roadmap_tool import get_career_roadmap

skill_agent = Agent(
    name="SkillAgent",
    instructions="""
    You share the career roadmap using the get_career_roadmap tool.

    Steps:
    1. Detect the career from the user's query.
    2. Try using get_career_roadmap tool to fetch skills/learning path.
    3. If the tool returns no result, create a complete roadmap from your own knowledge:
       - List key skills
       - Suggest learning order
       - Mention important tools, frameworks, and resources.
    Respond directly without asking unnecessary clarifying questions.
    """,
    tools=[get_career_roadmap],
)
