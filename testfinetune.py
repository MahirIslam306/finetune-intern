import os
from openai import OpenAI

MY_KEY = '<ADD_IT>'
client = OpenAI(api_key = MY_KEY)

question = input("Ask me anything: ")

response = client.chat.completions.create(
  messages=[
    {
      "role": "system",
      "content": "You are a helpful assistant who is an expert in Kubernetes troubleshooting and can help developers with step by step suggestions about how to investigate and solve Kubernetes problems."
    },
    {
      "role": "user",
      "content": question
    }
  ],
  #model="ft:gpt-3.5-turbo-0613:personal::8UXexX8R",
  model='ft:gpt-3.5-turbo-0125:personal::9uCoSac6',
  temperature=0,
  max_tokens=1024,
  n=1,
  stop=None
)

print(response)
