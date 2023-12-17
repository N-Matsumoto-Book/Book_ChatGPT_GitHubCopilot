from langchain.chains import SequentialChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.llms import OpenAI

output_parser = CommaSeparatedListOutputParser()
llm_model = OpenAI(
    max_tokens=1023, openai_api_key="your-api-key", temperature=0.9)

prompt_1 = PromptTemplate(
    template="{location}の{topic}について、カンマ区切りで出力して下さい\n{format_instructions}\n一覧: ",
    input_variables=["location", "topic"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()}
)
prompt_2 = PromptTemplate(
    template="{location}の{topic}の{output_1}についてそれぞれ詳細を教えて下さい。\n詳細: ",
    input_variables=["location", "topic", "output_1"],
)


llm_chain_1 = LLMChain(llm=llm_model, prompt=prompt_1,
                       output_parser=output_parser, output_key="output_1")
llm_chain_2 = LLMChain(llm=llm_model, prompt=prompt_2, output_key="output_2")

overall_chain = SequentialChain(
    chains=[llm_chain_1, llm_chain_2],
    input_variables=["location", "topic"],
    output_variables=["output_1", "output_2"],
    verbose=True
)

response = overall_chain({"location": "京都", "topic": "観光地"})
print(response)
