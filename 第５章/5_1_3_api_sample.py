from openai import OpenAI


client = OpenAI(api_key="your-api-key") # 5-1-1で発行したAPIキーを貼り付けてください

response = client.chat.completions.create(
   messages=[
       {
           "role": "user",
           "content": "こんにちは",
       }
   ],
   model="gpt-3.5-turbo",
)

generated_text = response.choices[0].message.content
print(generated_text)
