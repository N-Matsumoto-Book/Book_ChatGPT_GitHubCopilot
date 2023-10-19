from langchain.memory import ConversationBufferMemory
from langchain import SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain

llm = OpenAI(
    openai_api_key="API KEY")

search = SerpAPIWrapper(serpapi_api_key="API KEY")

memory = ConversationBufferMemory()
search_tool = Tool(
    name="検索",
    func=search.run,
    description="最新の情報を得たい場合に用います",
)

llm_math = LLMMathChain(llm=llm)
math_tool = Tool(
    name="計算機",
    func=llm_math,
    description="数値演算の内容を文字列で与えて正確な数値演算を行います",
)

tools = [search_tool, math_tool]
agent_executor = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    memory=memory,
    max_iterations=4
)
agent_executor.run("GPT-3.5とGPT-4の最大入力トークン数の差を計算してください。")
