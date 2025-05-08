import spacy
nlp = spacy.load("en_core_web_sm")

text = """
I tell you that very senior CEOs at major American car companies shook my hand
and quickly turned away.
"""

doc = nlp(text)

# phrase‑level (noun chunks come pre‑grouped)
# noun_phrases = [chunk.text for chunk in doc.noun_chunks]
# print("Noun phrases:", noun_phrases)

# token‑level
nouns       = [tok.text   for tok in doc if tok.pos_ in {"NOUN", "PROPN", "PRON"}]
print("Nouns:      ", nouns)
verbs       = [tok.lemma_ for tok in doc if tok.pos_ == "VERB"]
print("Verbs:      ", verbs)
adjectives  = [tok.text   for tok in doc if tok.pos_ == "ADJ"]
print("Adjectives: ", adjectives)
adverbs     = [tok.text   for tok in doc if tok.pos_ == "ADV"]
print("Adverbs:    ", adverbs)
