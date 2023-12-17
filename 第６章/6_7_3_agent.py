from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.agents import AgentType
from langchain.llms import OpenAI
llm = OpenAI(
    openai_api_key="your-api-key")

agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run("15のフィボナッチ数を計算してください")
