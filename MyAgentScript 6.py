from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
import asyncio
import random
import datetime
import time

@function_tool
def generate_random_number():
    r = random.randint(1, 100)
    time.sleep(1)
    #print(datetime.datetime.now() + " : Generated number: " + str(r))
    return r
     
load_dotenv(override=True)

instructions = "generate five random numbers using generate_random_number tool. " \
"Respond with string contains only numbers multiplied to 2 and separated by spaces."

agent1 = Agent(
        name="randomizer agent 1",
        instructions=instructions,
        tools=[generate_random_number],
        model="gpt-4o-mini"
)

tool1 = agent1.as_tool(tool_name="generate_random_numbers", 
                       tool_description="generate some numbers")

agentSelectBigger = Agent(
        name="select maximum",
        tools=[tool1],
        instructions="You are an agent that uses the generate_random_numbers tool to generate numbers. " \
        "You must respond with string contans all generated numbers and the biggest number from the generated numbers.",
        model="gpt-4o-mini"
)


with trace("Select maximum number"):
        result = asyncio.run(Runner.run(agentSelectBigger, "select the biggest number"))

print(f"{result.final_output}")