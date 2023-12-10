from openai import OpenAI
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
client = OpenAI(api_key="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")

conversation_history = []
MAX_ALLOWED_TOKENS = 100
total_tokens = 0
iteration_count = 0

while iteration_count < 10:
    user_input = input("質問内容を入力してください: ")
    user_input_tokens = len(tokenizer.encode(user_input)) # 入力のトークンを数える
    if user_input_tokens > MAX_ALLOWED_TOKENS:
        print(f'入力文字列が長いです。{MAX_ALLOWED_TOKENS}トークン以下にしてください。')
        continue # 再ループ

    conversation_history.append({"role": "user", "content": user_input})
    total_tokens += user_input_tokens
    
    chatbot_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.7, # 出力の多様性
        max_tokens=100, # 出力トークンの最大値
    )
    assistant_response = chatbot_response.choices[0].message.content
    assistant_tokens = len(tokenizer.encode(assistant_response))
    conversation_history.append({"role": "assistant", "content": assistant_response})
    total_tokens += assistant_tokens
    
    while total_tokens > MAX_ALLOWED_TOKENS: # トークンの合計が制限を超えた場合に一部削除
        removed_message = conversation_history.pop(0) # リストから最初のメッセージを削除
        removed_tokens = len(tokenizer.encode(removed_message['content']))
        total_tokens -= removed_tokens # 削除されたトークン数を差し引く
    print(assistant_response)
    iteration_count += 1
