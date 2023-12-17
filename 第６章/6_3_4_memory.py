from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI

# ChatOpenAIインスタンスを初期化
chat_model = ChatOpenAI(
    max_tokens=300, openai_api_key=your-api-key)

# ConversationSummaryMemoryインスタンスを初期化
memory = ConversationSummaryMemory(llm=chat_model)
memory.save_context({"input": "こんにちは"}, {"output": "どうも"})
print(memory.load_memory_variables({}))

# ConversationSummaryMemoryインスタンスにデータを格納
memory.save_context({"input": "明日の天気はどうなるのかな？"}, {
                    "output": "申し訳ございませんが、私はリアルタイムの天気情報を持っていません。"})
print(memory.load_memory_variables({}))
