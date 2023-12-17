from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "kokoro.txt"), autodetect_encoding=True)
documents = loader.load_and_split()


text_splitter = TokenTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    encoding_name="cl100k_base",
    add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)

# page_contentだけ表示
print([d.page_content for d in splitted_documents])
