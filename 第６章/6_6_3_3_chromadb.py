import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

BASE_DIR = os.path.dirname(__file__)

db = Chroma(persist_directory=os.path.join(
    BASE_DIR, "chroma_db"), embedding_function=OpenAIEmbeddings(openai_api_key=your-api-key))
query = "オブジェクト思考とは何ですか？"
docs = db.similarity_search(query)
print(docs)
