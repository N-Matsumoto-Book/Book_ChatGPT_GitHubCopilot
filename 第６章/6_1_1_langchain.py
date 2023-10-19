from langchain.llms import OpenAI

# Modelを実行する
llm = OpenAI(openai_api_key="API KEY")
response = llm("こんにちは")
print(response)

# Modelを変更する
llm = OpenAI(openai_api_key="API KEY", model_name="gpt-3.5-turbo")

# temperatureを変更する
llm = OpenAI(temperature=2.0, model_name="gpt-3.5-turbo", max_tokens=100,
             openai_api_key="API KEY")
response = llm("何か面白いことを話して下さい")
print(response)  # 「数字よabric367ふ」以下意味不明な出力がされる
