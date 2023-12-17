from langchain.chains import LLMMathChain
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.llms import OpenAI


def fetch_weather(location):
    return "Sunny"


llm = OpenAI(
    openai_api_key="your-api-key")

weather_tool = Tool(
    name="天気",
    func=fetch_weather,
    description="場所の情報を元に天気の情報を取得する",
)
tools = [weather_tool]

agent_executor = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)
agent_executor.run("東京の今日の天気を教えて")

# 数値計算をするAgent
llm_math = LLMMathChain(llm=llm)
math_tool = Tool(
    name="計算機",
    func=llm_math,
    description="数学の計算をするのに使います",
)
tools = [math_tool]
agent_executor = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)
agent_executor.run("4.5 * 2.3 / 3.5 = ?")


llm_tool = Tool(
    name="一般的な回答",
    func=llm.predict,
    description="一般的な質問に対して答えを得られます",
)
tools = [math_tool, llm_tool]
agent_executor = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)
agent_executor.run("日本の首都はどこですか？")
