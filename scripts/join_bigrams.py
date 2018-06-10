import csv
import nltk
from nltk.collocations import *
import sys

def bigramas():
    raw_bgs = open("data/bigramas.txt")
    bgs = {}
    for line in raw_bgs:
        w1, w2 = line.strip().split()
        bgs[w1] = w2
    return bgs

def bigramar(texto, bgs):
    bigrammed_words = []
    # for line in texto:
    words = nltk.word_tokenize(texto)
    past_word = ""
    for word in words:
        if past_word in bgs and word.lower() == bgs[past_word].lower():
            bigrammed_words.append('%s_%s' % (past_word, word))
            past_word = ""
        else:
            bigrammed_words.append(past_word)
            past_word = word
    bigrammed_words.append(past_word)
    return ' '.join(filter(lambda x: x != '', bigrammed_words))

if __name__ == '__main__':
    bgs = bigramas()
    text = open(sys.argv[1]).readlines()
    bigramar(text, bgs)
