from openai import OpenAI
from openaikey import openai_key
import os

os.environ["OPENAI_API_KEY"] = openai_key
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "바나나를 영어로 써줘."
        }
    ]
)

print(completion.choices[0].message)