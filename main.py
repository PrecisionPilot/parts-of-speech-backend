from flask import Flask, jsonify, request
from flask_cors import CORS
import test
import spacy

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def return_pos():
    data = request.get_json()
    text = data['text']

    # NLP code
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    nouns       = [tok.text   for tok in doc if tok.pos_ == "NOUN"]
    propns       = [tok.text   for tok in doc if tok.pos_ == "PROPN"]
    prons       = [tok.text   for tok in doc if tok.pos_ == "PRON"]
    verbs       = [tok.lemma_ for tok in doc if tok.pos_ == "VERB"]
    adjectives  = [tok.text   for tok in doc if tok.pos_ == "ADJ"]
    adverbs     = [tok.text   for tok in doc if tok.pos_ == "ADV"]

    # Send back data
    return jsonify({
        'errMsg': "",
        'nouns': nouns,
        'propns': propns,
        'prons': prons,
        'verbs': verbs,
        'adjectives' : adjectives,
        'adverbs' : adverbs,
    })

if __name__ == "__main__":
    app.run(debug=False, port=8080)