import json



def get_current_weather(location, unit="fahrenheit"):
    """指定した場所の現在の天気を取得"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": "sunny",
    }
    return weather_info


from openai import OpenAI
client = OpenAI(
    api_key="your-api-key",
)

response = client.chat.completions.create(
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

import json

func = response.choices[0] # choicesの0番目の要素を取得する。中には、関数呼び出しのための引数が入っている。
if func.finish_reason == "function_call": # 条件がfunction_callの場合の処理
    function_call = func.message.function_call # argumentsとnameが入っている
    if function_call.name == "get_current_weather": # nameがget_current_weatherの場合
        arguments = function_call.arguments
        arguments = json.loads(arguments) # json形式の文字列をpythonで扱いやすいように型変換
        location = arguments.get("location", "") # locationの値を取得（存在しない場合は空文字）
        unit = arguments.get("unit", "fahrenheit") # unitの値を取得（存在しない場合は「fahrenheit」）
        current_weather = get_current_weather(location, unit) # 関数get_current_weatherの呼び出し
        print(current_weather) # 出力: {'location': '東京, 日本', 'temperature': '72','unit': 'fahrenheit', 'forecast': 'sunny'}
