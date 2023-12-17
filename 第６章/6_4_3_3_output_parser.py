from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser


# OutputParserの作成
output_parser = DatetimeOutputParser()
print(output_parser.get_format_instructions())


prompt = PromptTemplate(
    template="{query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()}
)
llm_model = OpenAI(
    max_tokens=100, openai_api_key="your-api-key")
output = llm_model(prompt.format(query="ブロックチェーンが発表されたのはいつですか？"))
print(output)

print(output_parser.parse(output))
