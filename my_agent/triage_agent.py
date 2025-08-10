from agents import Agent
from .skill_agent import skill_agent
from .job_agent import job_agent
from .career_agent import career_agent

triage_agent = Agent(
    name="TriageAgent",
    instructions="""
    You must detect the user's intent from their message and handoff to the correct agent.

    Rules:
    - If the message contains words like "skill", "skills", "roadmap", "learn", "learning path", "how to become", or "requirements" → handoff to skill_agent.
    - If the message contains words like "job", "jobs", "roles", "positions", "titles", or "opportunities" → handoff to job_agent.
    - If the message talks about personal interests without mentioning jobs or skills, or asks for career suggestions → handoff to career_agent.
    - Do not ask clarifying questions. Always choose the most relevant agent directly.
    """,
    handoffs=[skill_agent, job_agent, career_agent]
)
