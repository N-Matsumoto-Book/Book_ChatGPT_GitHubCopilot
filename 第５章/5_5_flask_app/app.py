from flask import Flask, render_template, request
from openai import OpenAI
import tiktoken

app = Flask(__name__)

client = OpenAI(
    api_key="your-api-key",
)
MODEL_NAME = "gpt-3.5-turbo"
MAX_INPUT_TOKENS = 1000
ENCODING = tiktoken.encoding_for_model(MODEL_NAME)

def summarize_text(input_text): # APIを呼び出して、文章を要約する関数
    num_input_tokens = len(ENCODING.encode(input_text))
    if num_input_tokens > MAX_INPUT_TOKENS: # トークン数が大きい場合
        return "文字数が多すぎます。"
    # APIを呼び出す
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
                {"role": "system", "content": "userが入力した文書を箇条書きで改行してまとめてください"},
                {"role": "user", "content": input_text},
        ],
        max_tokens=1000
    )
    summarized_text = completion.choices[0].message.content
    return summarized_text

@app.route('/', methods=['GET', 'POST']) # URLを設定
def render_summary_page(): # 要約を表示する画面
    input_text = ""
    summarized_text = "" # 要約されたテキスト
    if request.method == 'POST': # POSTメソッドで呼び出された場合には、要約を実行する
        input_text = request.form['input_text']
        summarized_text = summarize_text(input_text) # 要約を実行する関数
        summarized_text = summarized_text.split('\n') # 改行で分割する
    return render_template('summary.html', input_text=input_text, summary=summarized_text)


def send_email(to_address, email_body):
    # メール送信処理をここに書きます
    print(f"{to_address}宛にメールを送信しました。")
    print(email_body)

def prepare_email_summary(input_text):
    # 入力テキストのトークン数を計算
    num_input_tokens = len(ENCODING.encode(input_text))

    # トークン数が最大限を超えた場合の処理
    if num_input_tokens > MAX_INPUT_TOKENS:
        return "文字数が多すぎます。"

    # ChatCompletion APIを使用して処理
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "メールの宛先を抽出してto_addressに、内容のまとめをemail_bodyに設定してください。"},
            {"role": "user", "content": input_text},
        ],
        functions=[
            {
                "name": "send_email",
                "description": "メールを送る処理",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_address": {
                            "type": "string",
                            "description": "メールの宛先",
                        },
                        "email_body": {
                            "type": "string",
                            "description": "メールの内容",
                        },
                    },
                    "required": ["to_address", "email_body"],
                }
            }
        ],
        function_call="auto",
        max_tokens=1000
    )

    # 処理結果を返す
    return completion.choices[0]


import json
@app.route("/send_email", methods=["GET", "POST"])
def render_send_email_page(): # メール送信画面
    input_text = ""
    email_body = ""
    to_address = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        model_response = prepare_email_summary(input_text) # API呼び出し
        if model_response.finish_reason == "function_call":
            function_call = model_response.message.function_call
            if function_call.name == "send_email":
                arguments = json.loads(function_call.arguments)
                to_address = arguments.get("to_address", "")
                email_body = arguments.get("email_body", "")
                send_email(to_address, email_body) # メール送信（モック）
    return render_template("send_email.html", input_text=input_text, email_body=email_body, to_address=to_address)

@app.route("/create_image", methods=["GET", "POST"])
def render_create_image_page(): # イメージ作成
    input_text = ""
    image_url = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        response = client.images.generate(
            model="dall-e-3",
            prompt=input_text,
            size="1024x1024",
            quality="hd",
            style="vivid",
        )
        image_url = response.data[0].url
    return render_template("create_image.html", input_text=input_text, image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
