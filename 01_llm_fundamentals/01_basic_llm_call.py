import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Get OpenRouter API key from .env
api_key = os.getenv("OPEN_ROUTER_API_KEY")

# OpenRouter API endpoint
url = "https://openrouter.ai/api/v1/chat/completions"

# Request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# Send request to the free model
response = requests.post(
    url=url,
    headers=headers,
    json={
        "model": "nvidia/nemotron-3.5-lightning:free",
        "messages": [
            {
                "role": "user",
                "content": "Explain what a large language model in simple sentences.",
            }
        ],
    },
)

# Check if request was successful
response.raise_for_status()

# Convert JSON response into Python dictionary
response_data = response.json()

# Extract model name
model_used = response_data["model"]

# Extract assistant's response
answer = response_data["choices"][0]["message"]["content"]

print("Model used:", model_used)
print()
print("Response:")
print(answer)