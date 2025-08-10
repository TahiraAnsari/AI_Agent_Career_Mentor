from agents import Agent
from .skill_agent import skill_agent
from .job_agent import job_agent
from .career_agent import career_agent

triage_agent = Agent(
    name="TriageAgent",
    instructions="""
    You are a routing specialist.
    Your job is to detect the user's intent and send their request to the right agent.

    Routing rules:
    - If the message contains words like "skill", "skills", "roadmap", "learn", "learning path", "how to become", or "requirements" → send to skill_agent.
    - If the message contains words like "job", "jobs", "roles", "positions", "titles", or "opportunities" → send to job_agent.
    - If the message talks about personal interests, passions, or asks for career suggestions without mentioning specific jobs or skills → send to career_agent.

    Do not ask clarifying questions.
    Always pick the most relevant agent based on the user's message.
    """,
    handoffs=[skill_agent, job_agent, career_agent]
)
