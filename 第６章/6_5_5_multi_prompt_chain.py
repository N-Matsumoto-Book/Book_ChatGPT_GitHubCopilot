from langchain.chains.router.llm_router import RouterOutputParser, LLMRouterChain
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router.multi_prompt import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
designer_template = """あなたはデザイナーです\
デザインについて、箇条書きでわかりやすく説明して、論拠も示して下さい。 
質問:
{input}"""

engineer_template = """あなたはITエンジニアです\
技術やプログラミングについて、箇条書きでわかりやすく説明して、論拠も示して下さい。 
質問:
{input}"""
prompt_infos = [
    {
        "name": "designer",
        "description": "デザインに関する質問に答える",
        "prompt_template": designer_template,
    },
    {
        "name": "engineer",
        "description": "技術に関する質問に答える",
        "prompt_template": engineer_template,
    },
]

llm_model = OpenAI(
    max_tokens=1023, openai_api_key="API KEY", temperature=0.9)

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["input"])
    chain = LLMChain(llm=llm_model, prompt=prompt)
    destination_chains[name] = chain

default_chain = ConversationChain(llm=llm_model, output_key="text")
destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)


router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(llm_model, router_prompt)
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

chain.run("Figmaとはなんですか？")
