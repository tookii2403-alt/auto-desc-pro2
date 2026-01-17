from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import openai

# static_url_path='' と設定することで、HTMLファイルを直接読み込めるようにします
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

# URLにアクセスしたときに、自動で index.html を表示する設定
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    description = data.get('description')
    
    try:
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
