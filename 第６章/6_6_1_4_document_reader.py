from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://ja.wikipedia.org/wiki/")
data = loader.load()
print(data)
# [Document(page_content='\n\n\n\nWikipedia\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nコンテンツにスキップ', metadata={'source': 'https://ja.wikipedia.org/wiki/', 'title': 'Wikipedia', 'language': 'ja'})]

# 複数読み込み
loader = WebBaseLoader(
    ["https://ja.wikipedia.org/wiki/", "https://google.com"])
docs = loader.load()
print(docs)
