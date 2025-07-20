import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from roadmap_tool import get_career_roadmap

gemini_key = ""

load_dotenv()
client = AsyncOpenAI(
    api_key=gemini_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=client)
config = RunConfig(
    model=model, 
    tracing_disabled=True
)

career_agent = Agent(
    name="CareerAgent",
    instructions="You ask about interests and suggest a career field.",
    model=model
)

skill_agent = Agent(
    name="SkillAgent",
    instructions="You share the roadmap using the get_career_roadmap tool.",
    model=model,
    tools=[get_career_roadmap]
)

job_agent = Agent(
    name="JobAgent",
    instructions="you suggest job titles in the choosen career",
    model=model
)

def main():
    print("\U0001F393 Career Master Agent\n")
    interest = input("What are your Interest?")

    result1 = Runner.run_sync(career_agent,interest,run_config=config)
    field = result1.final_output.strip()
    print("\nSuggested Career:",field)

    result2 = Runner.run_sync(skill_agent,field,run_config=config)
    print("\nRequired Skill:",result2.final_output)

    result3 = Runner.run_sync(job_agent,field,run_config=config)
    print("\nPossible Jobs:",result3.final_output)

if __name__ == "__main__":
    main()