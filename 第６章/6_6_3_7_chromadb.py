from langchain.schema import Document
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import WebBaseLoader


BASE_DIR = os.path.dirname(__file__)
# ChromaのCollectionを指定して読み込む
db = Chroma(persist_directory=os.path.join(BASE_DIR, "chroma_db"), collection_name="wikipedia",
            embedding_function=OpenAIEmbeddings(openai_api_key=your-api-key))


# Retrieverの作成
retriever = db.as_retriever()

# 作成したRetrieverをChainに設定する

qa_chain = RetrievalQA.from_llm(llm=OpenAI(
    openai_api_key=your-api-key),  retriever=retriever)

# Chainを実行して、回答を得る。
query = "What is Langchain?"
print(qa_chain.run(query))


texts = ["apple", "grape", "banana"]
metadatas = [
    {'source': 'apple.txt'},
    {'source': 'grape.txt'},
    {'source': 'banana.txt'},
]
documents = [Document(page_content=text, metadata=metadata)
             for text, metadata in zip(texts, metadatas)]
retriever.vectorstore.add_documents(documents)
