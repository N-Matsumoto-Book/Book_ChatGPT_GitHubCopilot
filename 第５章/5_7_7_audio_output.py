from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

speech_file_path = Path(__file__).parent / "speech_shimmer.mp3"
prompt = "私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。"

response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input=prompt
)

response.stream_to_file(speech_file_path)
