# 📄 Text Summarizer (Flask + SpaCy + NLTK)

A simple web app that summarizes long English paragraphs into concise summaries using NLP techniques powered by **SpaCy** and **NLTK**.

---

## 🚀 Features

- Extractive text summarization using word frequency scoring.
- Built with Python, Flask, SpaCy, and NLTK.
- Clean and responsive HTML UI.
- No page reload — uses AJAX for a smooth experience.

---

## 📷 Demo

*(Include screenshots or demo link here if applicable)*

---

## 🧠 Technologies Used

- Flask  
- SpaCy  
- NLTK  
- HTML5, CSS3, JavaScript (Fetch API)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/text-summarizer-flask.git
cd text-summarizer-flask
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Download SpaCy model & NLTK data
```bash
python -m spacy download en_core_web_sm
```
NLTK data (punkt, stopwords) will download automatically when you run the app the first time.

4. ▶️ Run the App
```bash
python app.py
```
Open your browser and go to: http://127.0.0.1:5000

📁 Project Structure
```bash

text_summarizer/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

## ✍️ Example
### Input:

Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language.

Summary Output:

Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language.

