from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(max_tokens=100,
             openai_api_key="API KEY")
conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
)
conversation.run("代表的なPythonライブラリ一覧を出力して")
conversation.run("それぞれについて詳細に")
conversation.run("続きは？")
