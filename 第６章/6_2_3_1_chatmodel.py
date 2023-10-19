from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# ChatModelの作成
chat_model = ChatOpenAI(
    max_tokens=300, openai_api_key="API KEY")

# メッセージを生成する
system_message = SystemMessage(content="文章を英語に翻訳してください")
human_message = HumanMessage(content="私はPythonを勉強しています")
print(chat_model([system_message, human_message]))
# AIMessage(content='I am studying Python.', additional_kwargs={}, example=False)

# ChatModelを実行する
chat_response = chat_model([system_message, human_message])
print(chat_response.content)  # I am studying Python. # 返り値にアクセスする

# ChatModelを実行する
chat_response = chat_model.generate([
    [
        SystemMessage(content="文章を英語に翻訳してください"),
        HumanMessage(content="ChatGPTの本を読んでいます")
    ],
    [
        SystemMessage(content="文章を英語に翻訳してください"),
        HumanMessage(content="第５章までは読みました")
    ],
])
print(chat_response.generations[0][0])
# text='I am reading a book about ChatGPT.' generation_info={'finish_reason': 'stop'} message=AIMessage(content='I am reading a book about ChatGPT.', additional_kwargs={}, example=False)

print(chat_response.generations[0][0].text)
# I am reading a book about ChatGPT.
print(chat_response.llm_output)
# {'token_usage': {'prompt_tokens': 66, 'completion_tokens': 19, 'total_tokens': 85}, 'model_name': 'gpt-3.5-turbo'}

# プロンプトのトークン数を取得する
print(chat_model.get_num_tokens_from_messages([
    SystemMessage(content="文章を英語に翻訳してください"),
    HumanMessage(content="ChatGPTの本を読んでいます")
]))  # 36

openai_llm = OpenAI(
    max_tokens=100, openai_api_key="API KEY")
# LLMとChatModelでpredictを実行する
openai_llm.predict("こんにちは")  # お元気ですか？
chat_model.predict("こんにちは")  # こんにちは！どのようなご用件でしょうか？

system_message = SystemMessage(content="文章を英語に翻訳してください")
human_message = HumanMessage(content="私はPythonを勉強しています")

# LLMとChatModelでpredict_messagesを実行する
openai_llm.predict_messages([system_message, human_message])
# AIMessage(content='\n\nSystem: I am studying Python.', additional_kwargs={}, example=False)
chat_model.predict_messages([system_message, human_message])
# AIMessage(content='I am studying Python.', additional_kwargs={}, example=False)
