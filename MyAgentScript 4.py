from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
import asyncio
import random

@function_tool
def generate_random_number():
    return random.randint(1, 100)
     
async def AgentsCall():
    with trace("Parallel random agent runs"):
        results = await asyncio.gather(
            Runner.run(agent1, message),
            Runner.run(agent2, message),
            #Runner.run(agent3, message),
        )
        return results

load_dotenv(override=True)
instructions="You are a random number generator"
message = "generate a random number using generate_random_number tool. Respond with only the number."

agent1 = Agent(
        name="randomizer agent 1",
        instructions=instructions,
        tools=[generate_random_number],
        model="gpt-4o-mini"
)

agent2 = Agent(
        name="randomizer agent 2",
        instructions=instructions,
        tools=[generate_random_number],
        model="gpt-4o-mini"
)

agent3 = Agent(
        name="randomizer agent 3",
        instructions=instructions,
        tools=[generate_random_number],
        model="gpt-4o-mini"
)

agentSelectBigger = Agent(
        name="select maximum",
        instructions="You are an agent that selects the biggest number from a list of numbers provided to you. You must respond with only the number.",
        model="gpt-4o-mini"
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