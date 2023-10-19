from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Modelの作成
llm_model = OpenAI(
    openai_api_key="API KEY", temperature=0.9)
memory = ConversationBufferWindowMemory(
    memory_key="chat_history", return_messages=True, k=1)
prompt = PromptTemplate(
    template="{chat_history}\nHuman: {question}\n",
    input_variables=["chat_history", "question"],
)

# Chainの作成
chain = LLMChain(llm=llm_model, prompt=prompt, memory=memory)

print(chain.run("京都の有名な観光地をおしえて下さい"))
print(chain.run("1つ目について詳しくおしえて下さい"))
print(memory.load_memory_variables({})['chat_history'])
