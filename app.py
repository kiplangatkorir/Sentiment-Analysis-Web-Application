import os
from flask import Flask, request, jsonify, send_from_directory
from textblob import TextBlob

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    return app

def analyze_sentiment(text):
    try:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    except Exception as e:
        app.logger.error(f"Error in sentiment analysis: {str(e)}")
        return 'error'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': 'Invalid input. Please provide text to analyze.'}), 400
        
        text = data['text']
        sentiment = analyze_sentiment(text)
        
        if sentiment == 'error':
            return jsonify({'error': 'An error occurred during analysis.'}), 500
        
        return jsonify({'sentiment': sentiment})
    except Exception as e:
        app.logger.error(f"Error in analyze route: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)