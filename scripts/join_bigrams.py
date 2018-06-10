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
    for line in texto:
        words = nltk.word_tokenize(line)
        past_word = ""
        for word in words:
            if past_word in bgs and word.lower() == bgs[past_word].lower():
                print("{}_{}".format(past_word, word), end=' ')
                past_word = ""
            else:
                print(past_word, end=' ')
                past_word = word
        print()

if __name__ == '__main__':
    bgs = bigramas()
    text = open(sys.argv[1]).readlines()
    bigramar(text, bgs)
