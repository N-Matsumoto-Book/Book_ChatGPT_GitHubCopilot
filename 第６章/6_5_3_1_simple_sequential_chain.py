from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.llms import OpenAI

llm_model = OpenAI(
    max_tokens=500, openai_api_key="API KEY")
prompt_1 = PromptTemplate(
    template="{question}について、カンマ区切りで出力して下さい\n一覧: ",
    input_variables=["question"],
)
prompt_2 = PromptTemplate(
    template="{subjects}についてそれぞれ詳細を教えて下さい。\n詳細: ",
    input_variables=["subjects"],
)

llm_chain_1 = LLMChain(llm=llm_model, prompt=prompt_1)
llm_chain_2 = LLMChain(llm=llm_model, prompt=prompt_2)
overall_chain = SimpleSequentialChain(
    chains=[llm_chain_1, llm_chain_2], verbose=True)
response = overall_chain.run("日本のおすすめの観光地")
