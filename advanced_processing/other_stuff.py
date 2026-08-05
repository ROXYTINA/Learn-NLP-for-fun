import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

# We initialize the Matcher with the spaCy vocab object, which contains words along with their labels and entities.
matcher = Matcher(nlp.vocab)
s = "I want to book a hotel room."
doc = nlp(s)

# Patterns are expressed as an ordered sequence. Here, we're looking
# to match occurrences starting with a 'book' string followed by
# a determiner (DET) POS tag, then a noun POS tag.
# The OP key marks the match as optional in some way.

# Here, the DET POS (marked with '?') will match 0 or 1 times, and
# the NOUN POS (marked with '+') will match 1 or more times.
# See this link for more information:
# https://spacy.io/usage/rule-based-matching#quantifiers
pattern = [
  {'TEXT': 'book'},
  {'POS': 'DET', 'OP': '?'},
  {'POS': 'NOUN', 'OP': '+'},
]

# We give our pattern a label and pass it to the matcher.
matcher.add('USER_INTENT', [pattern])

# Run the matcher over the doc.
matches = matcher(doc)

# For each match, the matcher returns a tuple specifying a match id, start,
# and end of the match.
print("Matches:", [doc[start:end].text for match_id, start, end in matches])


