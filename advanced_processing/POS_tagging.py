import spacy

nlp = spacy.load('en_core_web_sm')
s = "John watched an old movie at the cinema."
doc = nlp(s)


#To get a description for a POS tag, we can use spacy.explain.
print(spacy.explain("JJ"))
print(spacy.explain("NNP"))
print(spacy.explain("DT"))


print([(t.text, t.pos_) for t in doc])
print([(t.text, t.tag_) for t in doc])