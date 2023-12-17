from langchain.llms import OpenAI

# Modelを実行する
llm = OpenAI(openai_api_key="your-api-key")
response = llm.invoke("こんにちは")
print(response)

# Modelを変更する
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key="your-api-key")

# temperatureを変更する
llm = OpenAI(temperature=2.0, model_name="gpt-3.5-turbo-instruct", max_tokens=100,
             openai_api_key="your-api-key")
response = llm.invoke("何か面白いことを話して下さい")
print(response)  # 「数字よabric367ふ」以下意味不明な出力がされる
