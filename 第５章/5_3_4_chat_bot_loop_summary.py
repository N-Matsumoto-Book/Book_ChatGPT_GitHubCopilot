from openai import OpenAI
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
client = OpenAI(api_key="your-api-key")

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
    
    if total_tokens > MAX_ALLOWED_TOKENS:
        # conversation_historyの内容を要約
        conversation_history.append(
            {"role": "system", "content": "これまでの会話をすべて要約してください。"}
        )
        summary = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=100 # 出力の最大トークン数
        )
        summary_message = summary.choices[0].message.content
        # conversation_historyに要約結果をsystemメッセージとして設定して初期化
        conversation_history = [
            {"role": "system", "content": f"過去の要約: {summary_message}"}
        ]
        # total_tokensをリセット
        total_tokens = len(tokenizer.encode(summary_message))
    print(assistant_response)
    iteration_count += 1
