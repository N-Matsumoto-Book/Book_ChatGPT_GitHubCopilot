from openai import OpenAI
from pathlib import Path
import os

DIR_PATH = Path(__file__).resolve().parent
client = OpenAI(api_key="your-api-key")
original_image = "5_7_7_dog_cat.png"

response = client.images.create_variation(
    model="dall-e-2",
    image=open(os.path.join(DIR_PATH, original_image), "rb"),
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url
print(image_url)
