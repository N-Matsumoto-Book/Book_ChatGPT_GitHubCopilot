import openai
openai.api_key = "your-api-key"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": 'ITで注目する技術の話をしてください。'},
    ],
    frequency_penalty=2.0,
    max_tokens=300
)
print(completion.choices[0].message.content)
