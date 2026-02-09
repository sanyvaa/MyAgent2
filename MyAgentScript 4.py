from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
import asyncio
import random
import DefineModel

@function_tool
def generate_random_number():
    i = random.randint(1, 100)
    return i
     
async def AgentsCall():
    with trace("Parallel random agent runs"):
        results = await asyncio.gather(
            Runner.run(agent1, message),
            Runner.run(agent2, message),
            Runner.run(agent3, message),
        )
        return results

load_dotenv(override=True)
DefineModel.InitModel()

instructions="You are a random number generator"
message = "generate a random number using generate_random_number tool. Respond with only the number."

agent1 = Agent(
        name="randomizer agent 1",
        instructions=instructions,
        tools=[generate_random_number],
        model=DefineModel.MyModel
)

agent2 = Agent(
        name="randomizer agent 2",
        instructions=instructions,
        tools=[generate_random_number],
        model=DefineModel.MyModel
)

agent3 = Agent(
        name="randomizer agent 3",
        instructions=instructions,
        tools=[generate_random_number],
        model=DefineModel.MyModel
)

agentSelectBigger = Agent(
        name="select maximum",
        instructions="You are an agent that selects the biggest number from a list of numbers provided to you. You must respond with only the number.",
        model=DefineModel.MyModel
)

result2 = Runner.run_sync(agent1, "generate random number using generate_random_number tool. Respond with only the number.")

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