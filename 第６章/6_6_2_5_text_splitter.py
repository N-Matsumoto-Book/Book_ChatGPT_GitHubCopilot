from langchain.text_splitter import PythonCodeTextSplitter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "app.py"), autodetect_encoding=True)
documents = loader.load_and_split()
text_splitter = PythonCodeTextSplitter(
chunk_size=1000,
chunk_overlap=200,
add_start_index=True,
)
splitted_documents = text_splitter.transform_documents(documents)