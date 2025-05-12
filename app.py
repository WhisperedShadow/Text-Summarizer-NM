from flask import Flask, render_template, request, jsonify
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import heapq

nltk.download('punkt')
nltk.download('stopwords')

# Load SpaCy's legal-capable model (use en_core_web_sm if you don't have legal-specific)
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def summarize_legal_text(text, num_sentences=5):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    word_freq = {}

    # Calculate word frequencies ignoring stopwords
    for sent in sentences:
        words = word_tokenize(sent.lower())
        for word in words:
            if word not in stop_words and word.isalpha():
                word_freq[word] = word_freq.get(word, 0) + 1

    # Named entity importance scoring using SpaCy
    doc = nlp(text)
    named_entities = [ent.text.lower() for ent in doc.ents]
    named_entity_weight = 2  # boost score if a named entity is found

    sentence_scores = {}
    for sent in sentences:
        sent_lower = sent.lower()
        words = word_tokenize(sent_lower)
        for word in words:
            if word in word_freq:
                if len(sent.split(' ')) < 60:  # Allow longer sentences for legal text
                    score = word_freq[word]
                    if word in named_entities:
                        score *= named_entity_weight
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + score

    # Pick top N sentences
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
    summary = summarize_legal_text(text) if text.strip() else "No text provided."
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
