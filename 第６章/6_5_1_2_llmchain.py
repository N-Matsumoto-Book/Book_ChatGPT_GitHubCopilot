from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm_model = OpenAI(
    openai_api_key=your-api-key, temperature=0.9)
output_parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate.from_template(
   "{business}を行う会社名を5つ考えてください?\n{format_instructions}",
)

chain = LLMChain(llm=llm_model, prompt=prompt, output_parser=output_parser)
response = chain.run({"business": "ソフトウェア開発", "format_instructions": output_parser.get_format_instructions()})
print(response)  # ['Microsoft', 'Google', 'Apple', 'Oracle', 'SAP']
print(type(response))  # <class 'list'>
