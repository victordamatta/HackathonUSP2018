import csv
import nltk
from nltk.collocations import *
import sys

stopwords_file = open('data/stopwords.txt')
stopwords = list(map(lambda x: x.strip(), stopwords_file.readlines()))

bigram_measures = nltk.collocations.BigramAssocMeasures()

text = open(sys.argv[1]).read()
words = nltk.word_tokenize(text)
finder = BigramCollocationFinder.from_words(words)
finder.apply_freq_filter(10)
# finder.apply_word_filter(lambda w: w.lower() in stopwords)
# bgs = finder.nbest(bigram_measures.likelihood_ratio, 300)
bgs = finder.nbest(bigram_measures.pmi, 500)
bgs_no_stop = list(filter(lambda x: x[0].lower() not in stopwords and x[1].lower() not in stopwords, bgs))
for (w1, w2) in bgs_no_stop:
    print(w1, w2)
