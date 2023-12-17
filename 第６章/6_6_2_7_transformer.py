from langchain.embeddings import OpenAIEmbeddings
from langchain.document_transformers.embeddings_redundant_filter import EmbeddingsRedundantFilter
from langchain.document_loaders import TextLoader
import os
from langchain_core.documents import Document

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "embedding_list.txt"), autodetect_encoding=True)
loaded_documents = loader.load()

# 区切り文字で分割してリストにする
content_list = loaded_documents[0].page_content.split()
meta_data = loaded_documents[0].metadata

# 分割した文字列をDocumentに変換
documents = [Document(page_content=document, metadata=meta_data) for document in content_list]

embeddings_model = OpenAIEmbeddings(
    openai_api_key="your-api-key")  # API KEYを設定

embedding_filter = EmbeddingsRedundantFilter(
    embeddings=embeddings_model,
    similarity_threshold=0.95,
)
filtered_documents = embedding_filter.transform_documents(documents)

print([d.page_content for d in filtered_documents])
