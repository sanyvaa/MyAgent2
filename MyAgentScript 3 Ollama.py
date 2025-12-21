from dotenv import load_dotenv
from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, AsyncOpenAI
import asyncio


load_dotenv(override=True)

# Configure the model
model = OpenAIChatCompletionsModel( 
    model="llama3.2",
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1"))

async def AgentsCall():
    with trace("Parallel random agent runs"):
        results = await asyncio.gather(
            Runner.run(agent1, message),
            Runner.run(agent2, message),
            Runner.run(agent3, message),
        )
        return results

instructions="You are a random number generator"
message = "generate a random number between 1 and 100. Respond with only the number."

agent1 = Agent(
        name="randomizer agent 1",
        instructions=instructions,
        model=model
)

agent2 = Agent(
        name="randomizer agent 2",
        instructions=instructions,
        model=model
)

agent3 = Agent(
        name="randomizer agent 3",
        instructions=instructions,
        model=model
)

agentSelectBigger = Agent(
        name="select maximum",
        instructions="You are an agent that selects the biggest number from a list of numbers provided to you. You must respond with only the number.",
        model=model
)

results = asyncio.run(AgentsCall())
outputs = [result.final_output for result in results]

numbers = ""
for output in outputs:
    print(output)
    numbers += output + " "
print(numbers)

with trace("Select maximum number"):
        maximum = asyncio.run(Runner.run(agentSelectBigger, numbers))

print(f"Maximum: {maximum.final_output}")