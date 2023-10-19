import openai
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
openai.api_key = "your-api-key"

conversation_history = []
total_tokens = 0
max_allowed_tokens = 300
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

    if total_tokens > max_allowed_tokens:
        # conversation_historyの内容を要約
        summarizing_message = [
            message for message in conversation_history
        ]
        summarizing_message.append(
            {"role": "system", "content": "これまでの会話を全て要約して下さい。"}
        )
        summary = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=summarizing_message,
            temperature=0.7,
            max_tokens=200
        )
        summary_message = summary.choices[0].message.content
        # 要約結果をsystemメッセージとしてconversation_historyに設定
        conversation_history = [
            {"role": "system", "content": f"過去の要約: {summary_message}"}]
        # total_tokensをリセット
        total_tokens = len(tokenizer.encode(summary_message))

    print(conversation_history)
    question_count += 1
