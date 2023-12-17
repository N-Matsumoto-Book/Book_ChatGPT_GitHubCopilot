import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# ChatOpenAIインスタンスを初期化
chat_llm = ChatOpenAI(max_tokens=500, openai_api_key=your-api-key)
summarize_llm = ChatOpenAI(max_tokens=200, openai_api_key=your-api-key)

# 会話の履歴を保存するリスト
conversation_history = []
max_allowed_tokens = 100
question_count = 0

# ユーザーの質問が10回になるまでループ
while question_count < 10:
    user_input = input("質問内容を入力してください: ")
    human_message = HumanMessage(content=user_input)

    # ユーザー入力のトークン数を取得
    user_input_tokens = chat_llm.get_num_tokens_from_messages([human_message])

    # トークン数が制限を超えていれば警告を出力
    if user_input_tokens > max_allowed_tokens:
        print(f'入力文字列が長いです。{max_allowed_tokens}トークン以下にしてください。')
        continue  # 最初からループをやり直し

    # ユーザー入力を会話履歴に追加
    conversation_history.append(human_message)

    # チャットボットからの返答
    chatbot_response = chat_llm.predict_messages(conversation_history)
    conversation_history.append(chatbot_response)

    # トークン数が制限を超えていれば、会話を要約
    total_tokens = chat_llm.get_num_tokens_from_messages(conversation_history)
    if total_tokens > max_allowed_tokens:
        conversation_history.append(
            SystemMessage(content="これまでの会話を全て要約して下さい。")
        )
        summary = summarize_llm.predict_messages(conversation_history)
        summary_message = summary.content

        # 会話履歴を要約だけにする
        conversation_history = [
            SystemMessage(content=f"過去の要約: {summary_message}")
        ]

    print(conversation_history)  # 会話履歴を表示
    question_count += 1
