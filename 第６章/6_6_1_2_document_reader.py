import os
from langchain.document_loaders import PyPDFLoader

BASE_DIR = os.path.dirname(__file__)
loader = PyPDFLoader(os.path.join(BASE_DIR, "data", "itpassport_syllabus.pdf"))
pages = loader.load_and_split()
print(pages)
