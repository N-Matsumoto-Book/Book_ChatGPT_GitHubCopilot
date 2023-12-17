from langchain.llms import OpenAI

# Modelを実行する
openai_llm = OpenAI(max_tokens=100, openai_api_key="your-api-key")
response = openai_llm.invoke("日本の首都はどこですか？")
print(response)  # 日本の首都は東京です。

# プロンプトを複数渡す
response = openai_llm.generate(["日本の首都はどこですか？", "アメリカの首都はどこですか？"])
print(type(response.generations))  # <class 'list'>
print(response.generations)
print(response.generations[0][0].text)  # \n\n日本の首都は東京都です。
# \n\nワシントンD.C.print(response.llm_output)
print(response.generations[1][0].text)

# レスポンスのトークン数を取得する
print(response.llm_output)
# {'token_usage': {'total_tokens': 70, 'completion_tokens': 32, 'prompt_tokens': 38}, 'model_name': 'text-davinci-003'}
print(response.llm_output.get("token_usage").get("total_tokens"))  # 70

# プロンプトのトークン数を取得する
print(openai_llm.get_num_tokens("日本の首都はどこですか。"))  # 17
