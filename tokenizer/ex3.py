#
# EXERCISE: Look up how to tokenize the sentence below using NLTK. The imports
# are done for you. Does the NLTK tokenizer handle "N.Y.C." correctly?
#

import nltk
from nltk.tokenize import TreebankWordTokenizer


s = "Let's go to N.Y.C. for the weekend."

tokenizer = TreebankWordTokenizer() #Penn Treebank tokenization rules by NLTK traceback
tokens = tokenizer.tokenize(s)

print(tokens)

