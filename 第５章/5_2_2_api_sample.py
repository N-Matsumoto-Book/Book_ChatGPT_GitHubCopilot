from openai import OpenAI

client = OpenAI(api_key="your-api-key") # 5-1-1で発行したAPIキーを貼り付けてください
completion = client.chat.completions.create(
   messages=[
       {"role": "system", "content": "あなたはアシスタントです."},
       {"role": "user", "content": "こんにちは"},
       {"role": "assistant", "content": "はじめまして"},
   ],
   model="gpt-3.5-turbo",
   temperature=0.7,
   max_tokens=100
)

print(completion)

