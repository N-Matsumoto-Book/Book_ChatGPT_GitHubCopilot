from langchain.chains import SimpleSequentialChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType, initialize_agent, Tool
import os
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader, PythonLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, PythonCodeTextSplitter, Language
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

API_KEY = "API KEY"
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

llm_model = OpenAI(max_tokens=1023, openai_api_key=API_KEY, temperature=0.9)
to_english_prompt = PromptTemplate(
    template="```{question}```を、英語にしてください\n出力: ",
    input_variables=["question"],
)

to_japanese_prompt = PromptTemplate(
    template="```{english_answer}```を、日本語にしてください\n出力: ",
    input_variables=["english_answer"],
)
to_english_chain = LLMChain(llm=llm_model, prompt=to_english_prompt)
to_japanese_chain = LLMChain(llm=llm_model, prompt=to_japanese_prompt)
overall_chain = SimpleSequentialChain(
    chains=[to_english_chain, agent_executor, to_japanese_chain], verbose=True)
response = overall_chain.run(
    "restaurantsテーブルのモデルのソースコードを全て教えて下さい")
print(response)

# response = code_chain.run("レストラン詳細画面のViewのコードを、レストラン一覧画面のソースコードを参考に作成してください")
# print(response)
