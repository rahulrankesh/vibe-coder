# core/coder.py
from core.llm import call_llm
from core.memory import load_memory

SYSTEM_PROMPT = "..."  # from above

def vibe_coder(user_input, chat_history):
    memory = load_memory()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": f"User memory: {memory}"},
    ] + chat_history

    return call_llm(messages)
