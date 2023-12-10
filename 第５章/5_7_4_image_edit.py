from openai import OpenAI
from pathlib import Path
import os


DIR_PATH = Path(__file__).resolve().parent # 実行ファイルを格納しているフォルダ
client = OpenAI(api_key="your-api-key")
original_image = "5_7_4_photo.png" # オリジナルの画像ファイル
masked_image = "5_7_5_photo.png" # マスクした画像ファイル

response = client.images.edit(
   model="dall-e-2",
   image=open(os.path.join(DIR_PATH, original_image), "rb"),
   mask=open(os.path.join(DIR_PATH, masked_image), "rb"),
   prompt="道路に大きな白い猫",
   n=1,
   size="1024x1024"
)

image_url = response.data[0].url
print(image_url)
