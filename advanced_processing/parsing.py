import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm')
s = "She enrolled in the course at the university."
doc = nlp(s)

# Note the 'style' argument is assigned a 'dep' flag this time around.
displacy.render(doc, style='dep', jupyter=True)

print(spacy.explain("nsubj"))

print([(t.text, t.dep_) for t in doc])

print([(t.text, t.dep_, t.head.text) for t in doc])    #see head of each words