from langchain.chat_models.openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

# ConversationChainのインスタンスを作成
chat = ChatOpenAI(max_tokens=500, openai_api_key="your-api-key")
conversation_memory = ConversationBufferWindowMemory(return_messages=True, k=2)
chain = ConversationChain(llm=chat, memory=conversation_memory)
question_count = 0

# ユーザーの質問が10回になるまでループして、チャットを行う
while question_count < 10:
    user_input = input("質問内容を入力してください: ")
    chain.run(user_input)
    print(conversation_memory.load_memory_variables({})['history'])  # 会話履歴を表示
    question_count += 1
