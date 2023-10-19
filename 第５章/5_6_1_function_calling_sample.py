import json
import openai


def get_current_weather(location, unit="fahrenheit"):
    """指定した場所の現在の天気を取得"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": "sunny",
    }
    return weather_info


openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": "東京の現在の天気を押しててください"}],
    functions=[
        {
            "name": "get_current_weather",
            "description": "指定した場所の現在の天気を取得",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "都市名と国の名前、例：東京, 日本",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                "required": ["location"],
            },
        },
        {
            "name": "send_email",
            "description": "メールを送る処理",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "to": {
                            "type": "string",
                            "description": "メールの宛先",
                        },
                        "body": {
                            "type": "string",
                            "description": "メールのの中身",
                        },
                    },
                "required": ["to", "body"],
            },
        }
    ],
    function_call="auto",
)
print(response.choices[0].message.function_call.arguments)  # レスポンスメッセージ
