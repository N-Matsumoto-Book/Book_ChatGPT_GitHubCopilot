from langchain.embeddings import OpenAIEmbeddings
from langchain.document_transformers.embeddings_redundant_filter import EmbeddingsRedundantFilter
from langchain.document_loaders import TextLoader
import os

BASE_DIR = os.path.dirname(__file__)
loader = TextLoader(os.path.join(BASE_DIR, "data", "embedding_list.txt"))
documents = loader.load()
embeddings_model = OpenAIEmbeddings(
    openai_api_key="your-api-key")  # API KEYを設定

embedding_filter = EmbeddingsRedundantFilter(
    embeddings=embeddings_model,
    similarity_threshold=0.95,
)
filtered_documents = embedding_filter.transform_documents(documents)

print([d.page_content for d in filtered_documents])
