from openai import OpenAI


client = OpenAI(
    api_key="your-api-key",
)

message = input("質問内容を入力してください: ")
completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": message}
    ],
    temperature=0.7,
    max_tokens=1000,
    model="gpt-3.5-turbo",
)

response_message = completion.choices[0].message.content
print(response_message)

new_message = input("再度、質問内容を入力してください: ")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message},
        {"role": "assistant", "content": response_message},
        {"role": "user", "content": new_message}
    ],
    temperature=0.7,
    max_tokens=1000
)
print(completion.choices[0].message.content)
