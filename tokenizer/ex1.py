#
# EXERCISE:
# 1) Tokenize the following text
# 2) Iterate through the tokens to check whether there's a currency symbol.
# 3) If there is, and the currency label is followed by a number, print
#    both the symbol and the number.
#
# Look through https://spacy.io/api/token#attributes on how to check whether
# a token is a currency symbol or a number.
#
# Expected output: "$20".


import spacy

nlp = spacy.load('en_core_web_sm')

s = "He didn't want to pay $20 for this book."
doc = nlp(s)

for i, tokens in enumerate(doc):
    if tokens.is_currency:
        if i+1 < len(doc) and doc[i+1].like_num:
            print(tokens.text + doc[i + 1].text)