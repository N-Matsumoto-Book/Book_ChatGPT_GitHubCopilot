from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.images.generate(
   model="dall-e-3",
   prompt="アニメのような白猫の絵",
   size="1024x1024",
   quality="standard",
   style="natural",
)

image_url = response.data[0].url
print(image_url)
