from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm_model = OpenAI(
    openai_api_key=your-api-key, temperature=0.9)
prompt = PromptTemplate.from_template(
    "{business}を手がける会社の会社名を1つ考えてください?",
)

chain = LLMChain(llm=llm_model, prompt=prompt)
print(chain.run({"business": "ソフトウェア開発"}))
