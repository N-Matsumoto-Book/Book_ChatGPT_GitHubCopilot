import openai

openai.api_key = 'your-api-key' # 5-1-1で発行したAPIキーを貼り付けてください

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= [
   {"role": "user", "content":  "こんにちは"}
  ]
)

generated_text = response.choices[0].message.content
print(generated_text) # コンソールに出力