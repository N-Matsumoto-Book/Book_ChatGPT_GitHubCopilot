from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator


class User(BaseModel):
    name: str = Field(description="人の名前")
    age: int = Field(description="年齢")

    @validator('age')
    def age_constraints(cls, age):
        if age < 20 or age > 60:
            raise ValueError("年齢が正しくありません")
        return age


parser = PydanticOutputParser(pydantic_object=User)
# formatを表示
print(parser.get_format_instructions())

# PromptTemplateの作成
prompt = PromptTemplate(
    template="ユーザーデータを出力してください\n{format_instructions}\n",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
llm_model = OpenAI(
    max_tokens=100, openai_api_key="API KEY")

output = llm_model(prompt.format_prompt().to_string())
print(output)
print(parser.parse(output))
