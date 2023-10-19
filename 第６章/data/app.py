import json
from flask import Flask, render_template, request
import openai
import tiktoken

app = Flask(__name__)
MODEL_NAME = "gpt-3.5-turbo"
openai.api_key = "your-api-key"
MAX_INPUT_TOKENS = 1000
ENCODING = tiktoken.encoding_for_model(MODEL_NAME)


def send_email(to_address, email_body):
    # メール送信処理をここに書きます
    print(f"{to_address}宛にメールを送信しました。")
    print(email_body)


def summarize_text(input_text):  # APIを呼び出して、文章を要約する関数
    num_input_tokens = len(ENCODING.encode(input_text))
    if num_input_tokens > MAX_INPUT_TOKENS:  # トークン数が大きい場合
        return "文字数が多すぎます。"
    # APIを呼び出す
    completion = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "userが入力した文書を箇条書きで改行してまとめてください"},
            {"role": "user", "content": input_text},
        ],
        max_tokens=1000
    )
    summarized_text = completion.choices[0].message.content
    return summarized_text


@app.route("/",  methods=["GET", "POST"])
def render_summary_page():
    input_text = ""
    summarized_text = ""
    if request.method == "POST":  # POSTメソッドで呼び出された場合には、要約を実行する
        input_text = request.form["input_text"]
        summarized_text = summarize_text(input_text)
        summarized_text = summarized_text.split("\n")  # 改行で分割する
    return render_template("summary.html", input_text=input_text, summary=summarized_text)


def prepare_email_summary(input_text):
    num_input_tokens = len(ENCODING.encode(input_text))
    if num_input_tokens > MAX_INPUT_TOKENS:
        return "文字数が多すぎます。"
    completion = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system",
                "content": "メールの宛先を抽出してto_addressに、内容のまとめをemail_bodyに設定してください。"},
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
                },
            }
        ],
        function_call="auto",
        max_tokens=1000
    )
    return completion.choices[0]


@app.route("/send_email", methods=["GET", "POST"])
def render_send_email_page():  # 翻訳画面
    input_text = ""
    email_body = ""
    to_address = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        model_response = prepare_email_summary(input_text)  # API呼び出し
        if model_response.finish_reason == "function_call":
            function_call = model_response.message.function_call
            if function_call["name"] == "send_email":
                arguments = json.loads(function_call["arguments"])
                to_address = arguments.get("to_address", "")
                email_body = arguments.get("email_body", "")
                send_email(to_address, email_body)  # メール送信（モック）
    return render_template("send_email.html", input_text=input_text, email_body=email_body, to_address=to_address)


def fetch_model_response(user_query):  # Fine-tunedモデルを呼び出す関数
    FINE_TUNED_MODEL_NAME = 'ada:ft-personal-2023-08-16-10-38-11'
    formatted_query = user_query.rstrip("。")
    model_response = openai.Completion.create(
        model=FINE_TUNED_MODEL_NAME,
        prompt=f"{formatted_query}\n\n###\n\n",
        temperature=0,
        max_tokens=1,  # logprobsについて確認しよう
        logprobs=3,
    )
    print(model_response)
    response_number = model_response.choices[0].text.strip()
    response_messages = {
        1: "標準語ですね",
        2: "あなたは関西人ですね",
        3: "あなたは九州の人ですね"
    }
    try:
        response_number = int(response_number)
        return response_messages.get(response_number, "判定に失敗しました。")
    except ValueError:
        return "判定に失敗しました。"


@app.route("/dialect_check", methods=["GET", "POST"])
def render_dialect_check_page():  # 方言チェック画面
    user_query = ""
    response_message = ""
    if request.method == "POST":
        user_query = request.form["user_query"]
        response_message = fetch_model_response(user_query)
    return render_template("dialect_check.html", user_query=user_query, response_message=response_message)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
