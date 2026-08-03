import spacy

nlp = spacy.load('en_core_web_sm')

s = "He told Dr. Lovato that he was done with the tests and would post the results shortly."
doc = nlp(s)

#stop word list
# print(nlp.Defaults.stop_words)
# print(len(nlp.Defaults.stop_words))


print([t for t in doc if not t.is_stop])