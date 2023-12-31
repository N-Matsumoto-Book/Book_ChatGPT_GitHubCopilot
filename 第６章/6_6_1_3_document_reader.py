from langchain.document_loaders import DirectoryLoader, PythonLoader, TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = DirectoryLoader(BASE_DIR, glob="*.txt",
                         recursive=True, loader_cls=TextLoader, loader_kwargs={"autodetect_encoding": True})
docs = loader.load()

print(docs)


loader = DirectoryLoader(BASE_DIR, glob="*.py",
                         recursive=True, loader_cls=PythonLoader)
docs = loader.load()
print(docs)
