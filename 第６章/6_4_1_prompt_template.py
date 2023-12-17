from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# PromptTemplateインスタンスを作成
prompt_template = PromptTemplate.from_template(
    "{subject}の{content}について教えて下さい。"
)
print(prompt_template.format(subject="給料", content="増やし方"))
# 給料の増やし方について教えて下さい。

# PromptTemplateインスタンスをの実行
llm_model = OpenAI(
    max_tokens=100, openai_api_key=your-api-key)
print(llm_model.predict(prompt_template.format(subject="給料", content="増やし方")))
print(prompt_template.input_variables)  # ['content', 'subject']
