from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate

# ChatPromptTemplateインスタンスを作成
template = ChatPromptTemplate.from_messages([
    ("system", "あなたはAIのボットです。名前は{name}です"),
    ("human", "こんにちは"),
    ("ai", "こんにちは！何か質問があれば、お気軽にどうぞ。"),
    ("human", "{question}について教えて下さい。"),
])
messages = template.format_messages(
    name="ChatAI",
    question="LangChain"
)
print(messages)


# MessageTemplateを作成する
system_message = SystemMessagePromptTemplate.from_template(
    "あなたはAIのボットです。名前は{name}です")
human_message_1 = HumanMessagePromptTemplate.from_template("こんにちは")
ai_message = AIMessagePromptTemplate.from_template("こんにちは！何か質問があれば、お気軽にどうぞ。")
human_message_2 = HumanMessagePromptTemplate.from_template(
    "{question}について教えて下さい。")

# ChatPromptTemplateを作成する
chat_prompt = ChatPromptTemplate.from_messages([
    system_message, human_message_1, ai_message, human_message_2
])
print(chat_prompt.format_prompt(name="ChatAI", question="LangChain").to_messages())
# [SystemMessage(content='あなたはAIのボットです。名前はChatAIです', additional_kwargs={}),
# HumanMessage(content='こんにちは', additional_kwargs={}, example=False),
# AIMessage(content='こんにちは！何か質問があれば、お気軽にどうぞ。', additional_kwargs={}, example=False),
# HumanMessage(content='LangChainについて教えて下さい。', additional_kwargs={}, example=False)]


# chat_modelを実行する
chat_model = ChatOpenAI(
    max_tokens=300, openai_api_key=your-api-key)
print(chat_model(chat_prompt.format_prompt(name="ChatAI",
      question="LangChain").to_messages()))
print(chat_prompt.input_variables)
