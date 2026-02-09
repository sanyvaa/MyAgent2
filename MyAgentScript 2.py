from dotenv import load_dotenv
from agents import Agent, Runner, trace
import asyncio
import DefineModel

load_dotenv(override=True)
DefineModel.InitModel()

agent = Agent(name="Jokester", instructions="You are a joke teller", model=DefineModel.MyModel)
 
async def main(): 
    with trace("Telling a joke"): #https://platform.openai.com/logs?api=traces
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
        print(result.final_output)

asyncio.run(main())