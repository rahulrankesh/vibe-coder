# core/utils.py
import os, re

def extract_and_write_files(text, base="workspace"):
    pattern = r"FILE:\s*(.*?)\n```[\s\S]*?\n```"
    matches = re.findall(pattern, text)

    for path in matches:
        full_path = os.path.join(base, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
