import base64
import requests
from pathlib import Path
import os

DIR_PATH = Path(__file__).resolve().parent

api_key = "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"

# イメージをbase64エンコードする
def encode_image(image_path):
 with open(image_path, "rb") as image_file:
   return base64.b64encode(image_file.read()).decode('utf-8')


image_name = "5_7_9_cuba.jpg"
base64_image = encode_image(os.path.join(DIR_PATH, image_name))
prompt = "この画像には何が映っていますか？"

# api_keyをヘッダーに含める
headers = {
 "Content-Type": "application/json",
 "Authorization": f"Bearer {api_key}"
}

payload = {
 "model": "gpt-4-vision-preview",
 "messages": [
   {
     "role": "user",
     "content": [
       {
         "type": "text",
         "text": prompt
       },
       {
         "type": "image_url",
         "image_url": {
           "url": f"data:image/jpeg;base64,{base64_image}"
         }
       }
     ]
   }
 ],
 "max_tokens": 300
}

# リクエストを送信する
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
