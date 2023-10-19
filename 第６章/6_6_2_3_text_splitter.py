from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "kokoro.txt"))
documents = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=15,
    chunk_overlap=10,
    add_start_index=True,
    separators=["、", "。"],
)
splitted_documents = text_splitter.transform_documents(documents)
# page_contentだけ表示
print([d.page_content for d in splitted_documents])
