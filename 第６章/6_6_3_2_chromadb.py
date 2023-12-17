import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import TextLoader

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "programming.txt"), autodetect_encoding=True)
documents = loader.load_and_split()
text_splitter = TokenTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    encoding_name="cl100k_base",
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)

# ChromaにInMemoryで格納する

BASE_DIR = os.path.dirname(__file__)
db = Chroma.from_documents(splitted_documents, persist_directory=os.path.join(
    BASE_DIR, "chroma_db"), embedding=OpenAIEmbeddings(openai_api_key="your-api-key"))
query = "オブジェクト思考とは何ですか？"
docs = db.similarity_search(query)
