from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.memory import ConversationBufferWindowMemory

# ChatOpenAIインスタンスを初期化
chat_llm = ChatOpenAI(
    max_tokens=500, openai_api_key="your-api-key")

# 会話の履歴を保存するMemory
conversation_memory = ConversationBufferWindowMemory(return_messages=True, k=2)

question_count = 0
# ユーザーの質問が10回になるまでループ
while question_count < 10:
    user_input = input("質問内容を入力してください: ")
    human_message = HumanMessage(content=user_input)

    # ユーザー入力をMemoryに追加
    conversation_memory.chat_memory.add_message(human_message)
    print(type(conversation_memory.load_memory_variables({})['history']))
    print(conversation_memory.load_memory_variables({})['history'])
    # チャットボットからの返答（このとき、Memoryから過去の2回の対話を取り出す）
    chatbot_response = chat_llm.predict_messages(
        conversation_memory.load_memory_variables({})['history'],
    )

    conversation_memory.chat_memory.add_message(chatbot_response)

    print(conversation_memory.load_memory_variables({}))
    question_count += 1
