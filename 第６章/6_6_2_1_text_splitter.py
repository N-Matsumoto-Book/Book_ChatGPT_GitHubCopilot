from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "kokoro.txt"), autodetect_encoding=True)
documents = loader.load_and_split()

# 文字で分割
text_splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    add_start_index=True,
    separator="。",
)
splitted_documents = text_splitter.transform_documents(documents)
print([d.page_content for d in splitted_documents])

print(splitted_documents[0])
