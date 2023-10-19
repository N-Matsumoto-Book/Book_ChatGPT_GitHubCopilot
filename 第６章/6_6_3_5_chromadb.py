from langchain.schema.document import Document
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

texts = ["apple", "grape", "banana"]
metadatas = [
    {'source': 'apple.txt'},
    {'source': 'grape.txt'},
    {'source': 'banana.txt'},
]
documents = [Document(page_content=text, metadata=metadata)
             for text, metadata in zip(texts, metadatas)]
db = Chroma(embedding_function=OpenAIEmbeddings(
    openai_api_key="API KEY"))
db.add_documents(documents)

# 類似度検索
print(db.similarity_search("ぶどう", k=1))

# ドキュメントの取得
print(db.get(where={"source": "banana.txt"}))


# 更新
response = db.get(where={"source": "banana.txt"})
id = response['ids'][0]  # idを取得
new_document = Document(page_content="バナナ", metadata={
                        "source": "banana.txt"})  # Documentの再作成
db.update_document(id, new_document)  # idのものに対して、page_contentを変更

print(db.similarity_search("バナナ", k=1))

# 削除
ids = response['ids']
db.delete(ids)
