from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.schema import StrOutputParser

llm_model = OpenAI(
    max_tokens=500, openai_api_key="your-api-key")
prompt_1 = PromptTemplate.from_template(
    template="{question}について、カンマ区切りで出力して下さい\n一覧: ",
)
prompt_2 = PromptTemplate.from_template(
    template="{subjects}についてそれぞれ詳細を教えて下さい。\n詳細: ",
)

chain = (
    {"subjects": prompt_1 | llm_model}
    | prompt_2
    | llm_model
)
response = chain.invoke({"question": "日本のおすすめの観光地"})
print(response)
"""
京都：京都は、日本の首都である東京から約500km南東に位置しています。京都は、古くから文化や歴史を残してきた街で、近代の日本の文化や歴史が育まれた場所として重要な役割を果たしました。世界遺産にも数多く指定されており、世界中から多くの観光客が訪れています。

東京：東京は、日本の首都であり、日本最大の都市です。東京は、多様な文化や経済活動が行われている多くの地域を持ち、他の都市とは一線を画す異なる存在です。東京は、日本という国の象徴として、多くの日本人の心をつなぐ場所として、また世界中の人々にも愛されています。

北海道：北海道は、日本の北海道本島を中心とする、日本本土最北部の地域です。北海道は、山々や原生林や森林、多様な動植物
"""