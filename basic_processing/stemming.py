from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import TreebankWordTokenizer

s = "He told Dr. Lovato that he was done with the tests and would post the results shortly."

stemmer = SnowballStemmer("english")

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(s)

stems = [stemmer.stem(token) for token in tokens]

print(stems)