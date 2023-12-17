from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import get_buffer_string
from langchain.chains.llm import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory

CUSTOM_DEFAULT_SUMMARIZER_TEMPLATE = """履歴と最新の会話を要約してください。
    # 履歴
    {summary}

    # 最新の会話
    Human: {new_lines}

    出力:
    """

CUSTOM_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summary", "new_lines"], template=CUSTOM_DEFAULT_SUMMARIZER_TEMPLATE
)


class CustomConversationSummaryBufferMemory(ConversationSummaryBufferMemory):
    prompt=CUSTOM_SUMMARY_PROMPT


# ChatOpenAIインスタンスを初期化
chat_model = ChatOpenAI(
    max_tokens=200, openai_api_key=your-api-key)
memory = CustomConversationSummaryBufferMemory(
    llm=chat_model, max_token_limit=60)
memory.save_context({"input": "今日の天気はどうなるのかな？"}, {
                    "output": "申し訳ございませんが、私はリアルタイムの天気情報を持っていません。"})
memory.save_context({"input": "明日の天気を教えてください。"}, {
                    "output": "申し訳ございませんが、私はリアルタイムの天気情報を持っていません。"})
print(memory.load_memory_variables({}))
