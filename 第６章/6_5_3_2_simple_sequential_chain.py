from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains.llm import LLMChain
from langchain.chains import SimpleSequentialChain

llm_model = OpenAI(
    max_tokens=1023, openai_api_key="API KEY", temperature=0.9)
to_english_prompt = PromptTemplate(
    template="```{question}```を、英語にしてください\n出力: ",
    input_variables=["question"],
)
english_query = PromptTemplate(
    template="Tell me about ```{english_question}```\nAnswer: ",
    input_variables=["english_question"],
)
to_japanese_prompt = PromptTemplate(
    template="```{english_answer}```を、日本語にしてください\n出力: ",
    input_variables=["english_answer"],
)
to_english_chain = LLMChain(llm=llm_model, prompt=to_english_prompt)
query_chain = LLMChain(llm=llm_model, prompt=english_query)
to_japanese_chain = LLMChain(llm=llm_model, prompt=to_japanese_prompt)
overall_chain = SimpleSequentialChain(
    chains=[to_english_chain, query_chain, to_japanese_chain], verbose=True)
response = overall_chain.run("デラウェア州について教えてください")
