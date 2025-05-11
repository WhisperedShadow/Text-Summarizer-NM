from flask import Flask, render_template, request, jsonify
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import heapq

nltk.download('punkt')
nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    word_freq = {}

    for sent in sentences:
        words = word_tokenize(sent.lower())
        for word in words:
            if word not in stop_words:
                word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                if len(sent.split(' ')) < 30:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarize_text(text) if text.strip() else "No text provided."
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
