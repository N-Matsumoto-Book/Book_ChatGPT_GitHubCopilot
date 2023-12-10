import requests

# 使用例
image_url = "your-image-url"  # ダウンロードしたい画像のURL
file_path = "downloaded_image.jpg"           # 保存するファイル名

response = requests.get(image_url)
with open(file_path, 'wb') as file:
    file.write(response.content) # 画像を作業ディレクトリに保存
