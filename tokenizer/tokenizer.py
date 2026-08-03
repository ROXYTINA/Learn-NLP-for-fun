import spacy

nlp = spacy.load('en_core_web_sm')
type(nlp)

# Sample sentence.
s = "He didn't want to pay $20 for this book."
doc = nlp(s)

print([t.text for t in doc])
print(doc.text)


#sample paragraph
s = """Either the well was very deep, or she fell very slowly, for she 
had plenty of time as she went down to look about her and to wonder what 
was going to happen next. First, she tried to look down and make out what 
she was coming to, but it was too dark to see anything; then she looked at 
the sides of the well, and noticed that they were filled with cupboards and 
book-shelves; here and there she saw maps and pictures hung upon pegs."""

doc = nlp(s)

# Look at individual sentences (there should be two 'Span' objects).
print([sent for sent in doc.sents])