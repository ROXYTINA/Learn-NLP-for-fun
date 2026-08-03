# EXERCISE: Learn how the spaCy tokenizer works and how to customize it:
import re

import spacy
from spacy.symbols import ORTH
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer



##### CASE 1
nlp = spacy.load('en_core_web_sm')

#sample doc
s1 = "Gimme those"
s2 = "lemme in"

doc = nlp(s1)
doc = nlp(s2)


print([t.text for t in doc])

#special case rule for gimme
nlp.tokenizer.add_special_case("gimme", [{ORTH: "gim"}, {ORTH: "me"}])
nlp.tokenizer.add_special_case("lemme", [{ORTH: "lem"}, {ORTH: "me"}])

print([t.text for t in nlp("lemme in")])


##### CASE 2
nlp = English()
text = '''"Let's go!"'''

doc = nlp(text)

tok_exp = nlp.tokenizer.explain(text)
assert[t.text for t in doc if not t.is_space] == [t[1] for t in tok_exp]
for t in tok_exp:
    print(t[1])


##### CASE 3

nlp = spacy.blank("en")

special_cases = {"😂😂": [{ORTH: "😂😂"}]}

prefix_re = re.compile(r'^[@]') #if tokens start with these, split it
suffix_re = re.compile(r'[!?]$') #if tokens end with these, split it
phone_re = re.compile(r'^\d{3}-\d{3}-\d{3}$')   #regex format for phone number

tokenizer = Tokenizer(
    nlp.vocab,
    rules=special_cases,
    prefix_search=prefix_re.search,
    suffix_search=suffix_re.search,
    token_match=phone_re.match
)

nlp.tokenizer = tokenizer

doc = nlp("@សុខ សួស្តី! 012-345-678 😂😂")

print([t.text for t in doc])