from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI

# ChatOpenAIインスタンスを初期化
chat_model = ChatOpenAI(
    max_tokens=200, openai_api_key=your-api-key)

# ConversationSummaryBufferMemoryインスタンスを初期化
memory = ConversationSummaryBufferMemory(llm=chat_model, max_token_limit=60)
memory.save_context({"input": "今日の天気はどうなるのかな？"}, {
                    "output": "申し訳ございませんが、私はリアルタイムの天気情報を持っていません。"})
print(memory.load_memory_variables({}))


memory.save_context({"input": "明日の天気を教えてください。"}, {
                    "output": "申し訳ございませんが、私はリアルタイムの天気情報を持っていません。"})
print(memory.load_memory_variables({}))
