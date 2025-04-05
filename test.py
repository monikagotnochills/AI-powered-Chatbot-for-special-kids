import requests
import json

OPENROUTER_API_KEY = "sk-or-v1-"

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json", 
        "HTTP-Referer": "https://yourdomain.com",  
        "X-Title": "MyCoolApp",  
    },
    json={ 
        "model": "openchat/openchat-7b:free", 
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ]
    }
)

if response.status_code == 200:
    print("AI Response:", response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}:", response.text)
