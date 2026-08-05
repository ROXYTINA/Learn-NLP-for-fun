import spacy

nlp = spacy.load('en_core_web_sm')
s = "Volkswagen is developing an electric sedan which could potentially come to America next fall."
doc = nlp(s)

print(spacy.explain("GPE"))


print([(t.text, t.ent_type_) for t in doc if t.ent_type != 0])  #check if the token is an entity and check ent_type is non-zero

print([(t.text, t.ent_type_) for t in doc]) #accessed name attribute through ent_type

print([(ent.text, ent.label_) for ent in doc.ents])

print([(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents])   #access the position of the entity in the text


#we visualize the entities in our sample sentence.

from spacy import displacy

# We need to set the 'jupyter' variable to True to output the visualization directly. Otherwise, you'll get raw HTML.
displacy.render(doc, style='ent', jupyter=True)