from langchain.cache import SQLiteCache
from langchain.cache import InMemoryCache
from langchain.llms import OpenAI
from langchain.globals import set_llm_cache

set_llm_cache(InMemoryCache())

# Modelを実行する
openai_llm = OpenAI(
    max_tokens=100, openai_api_key=your-api-key)
response = openai_llm.generate(["面白いことを話して下さい"])
print(response.generations[0][0].text)
print(response.llm_output)

# 2回目の実行、キャッシュが効いている
response = openai_llm.generate(["面白いことを話して下さい"])
print(response.generations[0][0].text)
print(response.llm_output)  # {}

# キャッシュを無効にする
openai_llm = OpenAI(
    openai_api_key=your-api-key, cache=False, max_tokens=100)

# キャッシュが利用されない
response = openai_llm.generate(["面白いことを話して下さい"])
print(response.generations[0][0].text)
print(response.llm_output)

# SQLiteのキャッシュ
set_llm_cache(SQLiteCache(database_path=".langchain.db"))
response = openai_llm.generate(["面白いことを話して下さい"])

# キャッシュを無効にする
set_llm_cache(None)
