import os
from dotenv import load_dotenv
from agents import Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load Agents
from my_agent.career_agent import career_agent
from my_agent.skill_agent import skill_agent
from my_agent.job_agent import job_agent
from my_agent.triage_agent import triage_agent

load_dotenv()

# Create client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Apply model to agents
career_agent.model = model
skill_agent.model = model
job_agent.model = model
triage_agent.model = model

config = RunConfig(
    model=model,
    tracing_disabled=True
)

def main():
    print("\U0001F393 Career Master Agent\n")

    while True:
        interest = input("What are your interests? (type 'quit' to exit): ").strip()
        if interest.lower() == 'quit':
            print("Goodbye, take care!")
            break

        result = Runner.run_sync(triage_agent, interest, run_config=config)
        print("\n" + result.final_output + "\n" + "-"*50)

if __name__ == "__main__":
    main()
