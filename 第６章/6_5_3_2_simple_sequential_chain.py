from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains.llm import LLMChain
from langchain.chains import SimpleSequentialChain

llm_model = OpenAI(max_tokens=1023, openai_api_key="your-api-key", temperature=0.9)
to_english_prompt = PromptTemplate.from_template(
    "```{question}```を、英語にしてください\n出力: ",
)
english_query = PromptTemplate.from_template(
    "Tell me about ```{english_question}```\nAnswer: ",
)
to_japanese_prompt = PromptTemplate.from_template(
    "```{english_answer}```を、日本語にしてください\n出力: ",
)
to_english_chain = LLMChain(llm=llm_model, prompt=to_english_prompt)
query_chain = LLMChain(llm=llm_model, prompt=english_query)
to_japanese_chain = LLMChain(llm=llm_model, prompt=to_japanese_prompt)
overall_chain = SimpleSequentialChain(
    chains=[to_english_chain, query_chain, to_japanese_chain], verbose=True)
response = overall_chain.run("デラウェア州について教えてください")
