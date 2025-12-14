# core/llm.py
from openai import OpenAI
client = OpenAI()

def call_llm(messages, model="gpt-4.1"):
    return client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
    ).choices[0].message.content
