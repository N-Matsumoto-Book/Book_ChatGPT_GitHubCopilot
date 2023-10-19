from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "index.txt"))
documents = loader.load()
print(documents)
