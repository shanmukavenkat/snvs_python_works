from openai import OpenAI

client = OpenAI(
    api_key="31cffb73739b4d95a854c0d2bfff5793",
    base_url="https://api.aimlapi.com",
)

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {
            "role": "user",
            "content": "Tell me about the rollsRoyce and it's features?"
        },
    ],
)

message = response.choices[0].message.content
print(f"Assistant: {message}")