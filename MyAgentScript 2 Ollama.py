from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import DefineModel

load_dotenv(override=True)

DefineModel.InitModel()

# Create the agent
agent = Agent( name="Assistant",    instructions="You are a joke teller",  model=DefineModel.MyModel)

# Run the agent synchronously
result = Runner.run_sync(agent, "Tell a joke about cats. also, return the name of LLM used.")

print(result.final_output)