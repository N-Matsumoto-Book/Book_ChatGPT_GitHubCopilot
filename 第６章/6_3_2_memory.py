from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage,  SystemMessage
from langchain.memory import ConversationBufferWindowMemory

# ConversationBufferMemoryインスタンスを初期化
memory = ConversationBufferWindowMemory(return_messages=True, k=1)
memory.chat_memory.add_user_message("こんにちは")
memory.chat_memory.add_ai_message("どうしましたか？")
memory.chat_memory.add_user_message("太陽系の惑星は何個ありますか？")
memory.chat_memory.add_ai_message("8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。")

# メモリを表示
print(memory.load_memory_variables({}))

# return_messages=Trueを指定すると、Messageのリストを返す
memory = ConversationBufferWindowMemory(return_messages=True, k=1)
memory.chat_memory.add_message(SystemMessage(content="メッセージを要約して下さい"))
memory.chat_memory.add_message(HumanMessage(content="太陽系の惑星は何個ありますか？"))
memory.chat_memory.add_message(
    AIMessage(content="8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。"))
print(memory.load_memory_variables({}))

# メモリを引数にとってChatModelを実行する
response = chat_model.generate([
    memory.load_memory_variables({})['history']
])
print(response)
