from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = 'https://api.example.com/sentiment'  # Replace with your actual API endpoint
    response = requests.post(url, headers={'Authorization': f'Bearer {api_key}'}, json={'text': text})
    result = response.json()
    return result['sentiment']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.form['text']
    sentiment = analyze_sentiment(user_text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
