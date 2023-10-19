from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm_model = OpenAI(
    openai_api_key="API KEY", temperature=0.9)
prompt = PromptTemplate(
    template="{business}を行う会社名を考えて下さい?",
    input_variables=["business"],
)

chain = LLMChain(llm=llm_model, prompt=prompt)
print(chain.run({"business": "ソフトウェア開発"}))
