# filename: app.py (your backend)
from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

# Your Gemini API Key
genai.configure(api_key="AIzaSyC4WNLxuUtA3DCy7QO1zZrsUIMYspwDJq0")

@app.route('/genai', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    client = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = client.generate_content(prompt)
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
