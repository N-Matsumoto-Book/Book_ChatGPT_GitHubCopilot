import os
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader, PythonLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, PythonCodeTextSplitter, Language
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# ドキュメントを読み込む
BASE_DIR = os.path.dirname(__file__)
loader = DirectoryLoader(os.path.join(BASE_DIR, "source_code", "docs"), glob="*.md",
                         recursive=True, loader_cls=UnstructuredMarkdownLoader, loader_kwargs={"autodetect_encoding": True})
documents = loader.load()
# 文字で分割
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
    add_start_index=True,
    keep_separator=True,
    separators=["#", "\n"],
)
splitted_documents = text_splitter.transform_documents(documents)

# collection_nameをdocsにして、Chromaに保存
Chroma.from_documents(
    splitted_documents, persist_directory=os.path.join(
        BASE_DIR, "chroma_db"), collection_name="docs", embedding=OpenAIEmbeddings(openai_api_key="your-api-key"))

# Pythonファイルを読み込む
BASE_DIR = os.path.dirname(__file__)
loader = DirectoryLoader(os.path.join(BASE_DIR, "source_code"), glob="*.py",
                         recursive=True, loader_cls=PythonLoader)
documents = loader.load()
# 文字で分割
text_splitter = PythonCodeTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)

# collection_nameをcodeにして、Chromaに保存
Chroma.from_documents(
    splitted_documents, persist_directory=os.path.join(
        BASE_DIR, "chroma_db"), collection_name="code", embedding=OpenAIEmbeddings(openai_api_key="your-api-key"))

# HTMLファイルを読み込む
BASE_DIR = os.path.dirname(__file__)
loader = DirectoryLoader(os.path.join(BASE_DIR, "source_code"), glob="*.html",
                         recursive=True, loader_cls=TextLoader, loader_kwargs={"autodetect_encoding": True})
documents = loader.load()
# 文字で分割
text_splitter = RecursiveCharacterTextSplitter.from_language(
    Language.HTML,
    chunk_size=500,
    chunk_overlap=20,
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)

# collection_nameをcodeにして、Chromaに保存
Chroma.from_documents(
    splitted_documents, persist_directory=os.path.join(
        BASE_DIR, "chroma_db"), collection_name="code", embedding=OpenAIEmbeddings(openai_api_key="your-api-key"))
