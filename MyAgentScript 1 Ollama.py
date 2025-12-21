from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

response = ollama.chat.completions.create(model="llama3.2", messages=[{"role": "user", 
                                          "content": "create a joke about cats"}])
print(response.choices[0].message.content)   