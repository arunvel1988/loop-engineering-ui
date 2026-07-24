from ollama import Client

client = Client(host="http://ollama:11434")

response = client.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Say Hello"
        }
    ]
)

print(response["message"]["content"])
