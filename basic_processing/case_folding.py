import spacy

nlp = spacy.load('en_core_web_sm')

s = "He told Dr. Lovato that he was done with the tests and would post the results shortly."
doc = nlp(s)

print([t.lower_.upper() for t in doc])

print([t.lower_.title() for t in doc])

print([t.lower_ if not t.is_sent_start else t for t in doc])

print([t.lower_.title() if not t.is_sent_start else t.lower_.upper() for t in doc])

print([t.lower_.upper() if not t.is_sent_start else t.lower_ for t in doc])
