import spacy


nlp = spacy.load('en_core_web_sm')
nlp.vocab["told"].is_stop = True



