from langchain.chains.llm import LLMChain
from langchain.agents import AgentType, initialize_agent, Tool
import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

API_KEY = "your-api-key"
# ドキュメントを読み込む
BASE_DIR = os.path.dirname(__file__)
docs_db = Chroma(persist_directory=os.path.join(BASE_DIR, "chroma_db"), collection_name="docs",
                 embedding_function=OpenAIEmbeddings(openai_api_key=API_KEY))
code_db = Chroma(persist_directory=os.path.join(BASE_DIR, "chroma_db"), collection_name="code",
                 embedding_function=OpenAIEmbeddings(openai_api_key=API_KEY))

# Retrieverの作成
docs_retriever = docs_db.as_retriever()
code_retriever = code_db.as_retriever()

llm = OpenAI(
    openai_api_key=API_KEY)
# 検索用のChainを作成
docs_chain = RetrievalQA.from_llm(llm=llm, retriever=docs_retriever)
code_chain = RetrievalQA.from_llm(llm=llm, retriever=code_retriever)

# docs_chainとcode_chainでAgentを作成する

docs_tool = Tool(
    name="ドキュメント",
    func=docs_chain.run,
    description="設計書などドキュメント情報を得たい場合に用います",
)

code_tool = Tool(
    name="コード",
    func=code_chain.run,
    description="実際に記述したソースコードを参考にしたい場合に用います",
)

tools = [docs_tool, code_tool]

memory = ConversationBufferMemory()
agent_executor = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    memory=memory,
    max_iterations=4
)
response = agent_executor.run("レストラン詳細画面はどんな画面ですか？")
print(response)

response = agent_executor.run("restaurantsテーブルのモデルのソースコードをすべて教えてください")
print(response)
