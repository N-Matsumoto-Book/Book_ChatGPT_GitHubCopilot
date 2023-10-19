from langchain.chains.router.multi_prompt import MultiPromptChain
from langchain.chains.router.embedding_router import EmbeddingRouterChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains import ConversationChain
from langchain.llms import OpenAI


llm_model = OpenAI(
    max_tokens=1023, openai_api_key="API KEY", temperature=0.9)

names_and_descriptions = [
    ("designer", ["デザインに関する質問に答える"]),
    ("engineer", ["技術に関する質問に答える"]),
]
router_chain = EmbeddingRouterChain.from_names_and_descriptions(
    names_and_descriptions, Chroma, OpenAIEmbeddings(openai_api_key="API KEY"), routing_keys=["input"]
)

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

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["input"])
    chain = LLMChain(llm=llm_model, prompt=prompt)
    destination_chains[name] = chain
default_chain = ConversationChain(llm=llm_model, output_key="text")

chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)
chain.run("Pythonとはなんですか？")
