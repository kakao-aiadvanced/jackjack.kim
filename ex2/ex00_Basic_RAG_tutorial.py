import os

from openaikey import openai_key
from langchain import hub
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = openai_key
llm = ChatOpenAI(model="gpt-4o-mini")



prompt = hub.pull("rlm/rag-prompt")
example_messages = prompt.invoke(
    {"context": "filler context", "question": "filler question"}
).to_messages()

print(example_messages)
print(example_messages[0].content)