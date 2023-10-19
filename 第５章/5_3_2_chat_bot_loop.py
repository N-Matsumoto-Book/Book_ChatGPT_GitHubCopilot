import openai
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
openai.api_key = "your-api-key"

conversation_history = []
total_tokens = 0
max_allowed_tokens = 100
question_count = 0

while question_count < 10:
    user_input = input("質問内容を入力してください: ")
    user_input_tokens = len(tokenizer.encode(user_input))  # 入力のトークンを数える
    if user_input_tokens > max_allowed_tokens:
        print(f'入力文字列が長いです。{max_allowed_tokens}トークン以下にしてください。')
        continue  # 再ループ

    conversation_history.append({"role": "user", "content": user_input})
    total_tokens += user_input_tokens

    chatbot_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=100
    )
    assistant_message = chatbot_response.choices[0].message.content
    assistant_tokens = len(tokenizer.encode(assistant_message))
    conversation_history.append(
        {"role": "assistant", "content": assistant_message})
    total_tokens += assistant_tokens

    while total_tokens > max_allowed_tokens:
        removed_message = conversation_history.pop(0)  # リストから最初のメッセージを削除
        removed_tokens = len(tokenizer.encode(removed_message['content']))
        total_tokens -= removed_tokens  # 削除されたトークン数を差し引く

    print(assistant_message)
    question_count += 1
