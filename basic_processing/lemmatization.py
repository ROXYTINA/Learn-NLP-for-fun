import spacy

nlp = spacy.load('en_core_web_sm')

s = "He told Dr. Lovato that he was done with the tests and would post the results shortly."
doc = nlp(s)



print([(t.text, t.lemma_) for t in doc])