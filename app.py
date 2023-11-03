from flask import Flask, render_template, request, send_from_directory
import openai
from dotenv import load_dotenv
import os
import csv
import prompt
import json

# API load
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# New flask instance
app = Flask(__name__)

# main route
@app.route('/')
def index():
    return render_template('index.html')

# ユーザーの入力に対して、続きを生成する
@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form['text']
    
    # トークン数が上限に達するかどうかをチェックし、達する場合は要約とタイトルを更新します
    if count_tokens(input_text) + count_tokens(summary) >= TOKEN_THRESHOLD:
        summary = generate_gpt_summary(prompts)
        title = generate_gpt_title(prompts)
        prompts = [summary]
    
    prompts.append(input_text)
    
    with open('story.csv', 'w', newline='', encoding='utf-8') as csvfile:
        story_writer = csv.writer(csvfile)
        story_writer.writerow([title, summary] + prompts)
    
    generated_text = generate_gpt_response(input_text)
    prompts.append(generated_text)
    
    return jsonify({"input_text": input_text, "generated_text": generated_text, "summary": summary, "title": title})

# 障害対策（立ち上げた時にcsvを読み込む）
@app.route('/load_story')
def load_story():
    if not os.path.exists('story.csv'):
        return jsonify({"story": [], "title": ""})

    with open('story.csv', 'r', newline='', encoding='utf-8') as csvfile:
        story_reader = csv.reader(csvfile)
        title, summary, *story_data = next(story_reader)

    elements = [{"text": x, "type": "user" if i % 2 == 0 else "gpt"} for i, x in enumerate(story_data)]
    return jsonify({"story": elements, "title": title})

# entry point
if __name__ == '__main__':
    app.run(debug=True)