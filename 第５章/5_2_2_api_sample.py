import openai
openai.api_key = "your-api-key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたはアシスタントです."},
        {"role": "user", "content": "こんにちは"},
        {"role": "assistant", "content": "はじめまして"},
    ],
    temperature=0.7,
    max_tokens=100
)

print(completion)
