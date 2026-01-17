from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)

# AIの鍵（APIキー）を環境から読み込む設定
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    description = data.get('description')
    
    try:
        # AIに「販売コピーを作って」と依頼する
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは優秀なECコピーライターです。商品の特徴を捉え、売れる紹介文を日本語で作成してください。"},
                {"role": "user", "content": description}
            ]
        )
        return jsonify({"copy": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
