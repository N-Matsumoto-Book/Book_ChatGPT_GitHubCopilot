from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

chat = ChatOpenAI(max_tokens=100,openai_api_key="your-api-key")
conversation = ConversationChain(
    llm=chat, memory=ConversationBufferMemory(), verbose=True
)
conversation.run("代表的なPythonライブラリ一覧を出力して")
conversation.run("それぞれについて詳細に")
conversation.run("続きは？")
