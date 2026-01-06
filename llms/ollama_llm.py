import requests
import json


def ask_ollama(prompt, model="llama2"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
    )
    return response.json()["response"]


# Usage
result = ask_ollama("Explain quantum computing in simple terms")
print(result)
