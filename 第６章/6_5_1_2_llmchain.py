from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm_model = OpenAI(
    openai_api_key="API KEY", temperature=0.9)
output_parser = CommaSeparatedListOutputParser()

prompt = PromptTemplate(
    template="{business}を行う会社名を5つ考えて下さい?\n{format_instructions}",
    input_variables=["business"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()}
)
chain = LLMChain(llm=llm_model, prompt=prompt, output_parser=output_parser)
response = chain.run({"business": "ソフトウェア開発"})
print(response)  # ['Microsoft', 'Google', 'Apple', 'Oracle', 'SAP']
print(type(response))  # <class 'list'>
