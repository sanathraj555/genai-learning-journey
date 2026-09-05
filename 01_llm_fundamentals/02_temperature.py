import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPEN_ROUTER_API_KEY")

# OpenRouter API endpoint
url = "https://openrouter.ai/api/v1/chat/completions"

# Request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}


# Function to ask the LLM a question
def ask_llm(temperature):
    response = requests.post(
        url=url,
        headers=headers,
        json={
            "model": "nvidia/nemotron-3.5-lightning:free",
            "messages": [
                {
                    "role": "user",
                    "content": "Write a short description about India",
                }
            ],
            "temperature": temperature,
        },
    )

    response.raise_for_status()

    response_data = response.json()

    return response_data["choices"][0]["message"]["content"]


# Test with low temperature
print("===== Temperature: 0.1 =====")
print(ask_llm(0.1))

print()


# Test with medium temperature
print("===== Temperature: 0.7 =====")
print(ask_llm(0.7))

print()


# Test with high temperature
print("===== Temperature: 1.0 =====")
print(ask_llm(1.0))