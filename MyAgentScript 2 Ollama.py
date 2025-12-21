from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# https://blog.stackademic.com/openai-agents-sdk-with-ollama-fc85da11755d

load_dotenv(override=True)

# Configure the model
model = OpenAIChatCompletionsModel( 
    model="llama3.2",
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1"))

# Create the agent
agent = Agent( name="Assistant",    instructions="You are a joke teller",  model=model)

# Run the agent synchronously
result = Runner.run_sync(agent, "Tell a joke about cats")

print(result.final_output)