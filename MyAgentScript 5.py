from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
import asyncio
import random

@function_tool
def generate_random_number():
    return random.randint(1, 100)
     
load_dotenv(override=True)
instructions="You are a random number generator"
message = "generate five random numbers using generate_random_number tool. " \
"Respond with string contains only numbers multiplied to 2 and separated by spaces."

agent1 = Agent(
        name="randomizer agent 1",
        instructions=instructions,
        tools=[generate_random_number],
        model="gpt-4o-mini"
)

with trace("generate numbers"):
        random_numbers_result = asyncio.run(Runner.run(agent1, message))

print(random_numbers_result.final_output)

agentSelectBigger = Agent(
        name="select maximum",
        instructions="You are an agent that selects the biggest number from a list of numbers provided to you. You must respond with only the number.",
        model="gpt-4o-mini"
)



with trace("Select maximum number"):
        maximum = asyncio.run(Runner.run(agentSelectBigger, random_numbers_result.final_output))

print(f"Maximum: {maximum.final_output}")