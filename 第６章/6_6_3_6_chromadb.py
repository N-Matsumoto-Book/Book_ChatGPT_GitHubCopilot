import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/LangChain")
data = loader.load()


html2text = Html2TextTransformer()
transformed_data = html2text.transform_documents(data)
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    add_start_index=True,
    separator="\n",
    keep_separator=True,
)
splitted_data = text_splitter.transform_documents(transformed_data)


BASE_DIR = os.path.dirname(__file__)
db = Chroma.from_documents(splitted_data, persist_directory=os.path.join(
    BASE_DIR, "chroma_db"),
    collection_name="wikipedia", embedding=OpenAIEmbeddings(openai_api_key=your-api-key))

db.similarity_search("What is Langchain?", k=1)

# ChromaのCollectionを指定して読み込む
db = Chroma(persist_directory=os.path.join(BASE_DIR, "chroma_db"), collection_name="wikipedia",
            embedding_function=OpenAIEmbeddings(openai_api_key=your-api-key))
response = db.get(where={"source": "https://en.wikipedia.org/wiki/LangChain"})

print(response)
