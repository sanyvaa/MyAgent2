from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

openai = OpenAI()
response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": "create a joke about cats"}], max_tokens=100)
print(response.choices[0].message.content)   