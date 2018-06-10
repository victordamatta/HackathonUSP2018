import csv
import nltk
from nltk.collocations import *
import sys

def context(tokens, i):
    c = []
    for j in range(1, 5):
        if(i - j < 0 or i + j >= len(tokens)): break
        left = tokens[i-j].lower()
        right = tokens[i+j].lower()
        c.append(left)
        c.append(right)
    c.append('*START*')
    c.append('*END*')
    return tuple(c)

tokens = open("data/tokens.txt").readlines()
text = nltk.word_tokenize(open(sys.argv[1]).read())
ci = nltk.ContextIndex(text, context_func=context)

for token in tokens:
    token = token.strip()
    sw = ci.similar_words(token, n=10)
    if not len(sw) == 0:
        print(token, ' '.join(sw))
