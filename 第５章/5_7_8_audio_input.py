from pathlib import Path
from openai import OpenAI

client = OpenAI(
  api_key="your-api-key",
)

audio_file_path = Path(__file__).parent / "5_7_10_speech.mp3"
audio_file = open(audio_file_path, "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text",
    language="ja",
)
print(transcript) # 私はその人を常に先生と呼んでいた。 だからここでもただ先生と書くだけで本命は打ち明けない。
