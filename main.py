
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

external_client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL_KEY")
)

llm_model = OpenAIChatCompletionsModel(
    model="poolside/laguna-s-2.1:free",
    openai_client=external_client
)

agent = Agent(
    name="Maths solver",
    instructions="You are a maths tutor",
    model=llm_model
)

result = Runner.run_sync(
    starting_agent=agent,
    input="788+667=?"
)

print(result.final_output)

