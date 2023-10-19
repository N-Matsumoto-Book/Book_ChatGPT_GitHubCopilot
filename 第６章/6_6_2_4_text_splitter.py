from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "summary.html"))
documents = loader.load_and_split()

# HTML向けの設定
text_splitter = RecursiveCharacterTextSplitter.from_language(
    Language.HTML,
    chunk_size=100,
    chunk_overlap=10,
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)
print([d.page_content for d in splitted_documents])
