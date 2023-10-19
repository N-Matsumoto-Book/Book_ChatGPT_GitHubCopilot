from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage,  SystemMessage
from langchain.memory import ConversationBufferMemory

# ConversationBufferMemoryインスタンスを初期化
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("こんにちは")
memory.chat_memory.add_ai_message("どうしましたか？")
memory.chat_memory.add_user_message("太陽系の惑星は何個ありますか？")
memory.chat_memory.add_ai_message("8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。")

# メモリを表示
print(memory.load_memory_variables({}))
memory.load_memory_variables({})['history']

# return_messages=Trueを指定すると、Messageのリストを返す
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("こんにちは")
memory.chat_memory.add_ai_message("どうしましたか？")
print(memory.load_memory_variables({}))

# メモリをクリアする
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_message(SystemMessage(content="メッセージを要約して下さい"))
memory.chat_memory.add_message(HumanMessage(content="太陽系の惑星は何個ありますか？"))
memory.chat_memory.add_message(
    AIMessage(content="8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。"))
print(memory.load_memory_variables({}))


# メモリをクリアする
memory = ConversationBufferMemory(return_messages=True)
memory.save_context({"input": "太陽系の惑星は何個ありますか？"}, {
                    "output": "8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。"})
print(memory.load_memory_variables({}))
# {'history': [HumanMessage(content='太陽系の惑星は何個ありますか？', additional_kwargs={}, example=False), AIMessage(content='8個あります。水星、金星、地球、火星、木星、土星、天王星、および海王星です。', additional_kwargs={}, example=False)]}

# メモリをクリアする
memory.clear()
print(memory.load_memory_variables({}))  # {'history': []}

# ChatModelの作成
chat_model = ChatOpenAI(
    max_tokens=300, openai_api_key="API KEY")
memory.chat_memory.add_message(HumanMessage(content="こんにちは"))

# メモリを引数にとってChatModelを実行する
response = chat_model.generate([
    memory.load_memory_variables({})['history']
])
print(response)
