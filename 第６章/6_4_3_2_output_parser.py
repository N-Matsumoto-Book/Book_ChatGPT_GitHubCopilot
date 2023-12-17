from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

# CommandSeparatedListOutputParserの作成
output_parser = CommaSeparatedListOutputParser()
print(output_parser.get_format_instructions())

# PromptTemplateの作成
prompt = PromptTemplate(
    template="5つ{subject}を表示してください\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()}
)
llm_model = OpenAI(
    max_tokens=100, openai_api_key="your-api-key")

# Modelの実行
output = llm_model(prompt.format(subject="アイスクリームの味"))
print(output)  # '\n\nストロベリー, チョコレート, バニラ, マンゴー, ピスタチオ'

print(output_parser.parse(output))
