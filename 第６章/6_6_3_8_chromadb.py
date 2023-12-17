from langchain.document_loaders import WebBaseLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os

BASE_DIR = os.path.dirname(__file__)

index_creater = VectorstoreIndexCreator(
    embedding=OpenAIEmbeddings(openai_api_key=your-api-key),
    text_splitter=CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=10,
        add_start_index=True,
        separator="\n",
        keep_separator=True,
    ),
    vectorstore_kwargs={
        "persist_directory": os.path.join(BASE_DIR, "chroma_db"),
        "collection_name": "wikipedia",
    },
)


# index_creater.from_documents(documents)

loader = WebBaseLoader("https://en.wikipedia.org/wiki/LangChain")
index_creater.from_loaders([loader])
