import csv
import nltk
import sys

with open(sys.argv[1]) as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        print(row['resumo_em_portugues'])
