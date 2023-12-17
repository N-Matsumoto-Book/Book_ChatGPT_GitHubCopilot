from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "programming.txt"))
documents = loader.load_and_split()
text_splitter = TokenTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    encoding_name="cl100k_base",
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)

# ChromaにCollectionを指定してで格納する
db = Chroma.from_documents(
    splitted_documents, persist_directory=os.path.join(
        BASE_DIR, "chroma_db"), collection_name="my_collection", embedding=OpenAIEmbeddings(openai_api_key="your-api-key"))

db = Chroma(persist_directory=os.path.join(
    BASE_DIR, "chroma_db"), collection_name="my_collection", embedding_function=OpenAIEmbeddings(openai_api_key="your-api-key"))
query = "オブジェクト思考とは何ですか？"
docs = db.similarity_search(query)

print(docs)

db.delete_collection()
