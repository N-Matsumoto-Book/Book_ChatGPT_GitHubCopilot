from langchain.memory import ConversationTokenBufferMemory
from langchain.chat_models import ChatOpenAI

# ChatOpenAIインスタンスを初期化
chat_model = ChatOpenAI(max_tokens=300, openai_api_key="API KEY")

# ConversationBufferMemoryインスタンスを初期化
memory = ConversationTokenBufferMemory(llm=chat_model, max_token_limit=20)
memory.save_context({"input": "こんにちは"}, {"output": "どうも"})  # トークン数のチェック
memory.save_context({"input": "元気ですか？"}, {"output": "まあまあですね"})  # トークン数のチェック
print(memory.load_memory_variables({}))
