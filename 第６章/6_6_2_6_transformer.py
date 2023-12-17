from langchain.text_splitter import CharacterTextSplitter
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://ja.wikipedia.org/wiki/")
data = loader.load()
print(data)

# HTMLをテキストに変換
html2text = Html2TextTransformer()
transformed_data = html2text.transform_documents(data)
print(transformed_data)

# 文字で分割
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=10,
    add_start_index=True,
    separator="\n",
)
splitted_data = text_splitter.transform_documents(transformed_data)
print(splitted_data)
