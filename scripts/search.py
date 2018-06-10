import csv, re, join_bigrams, consts
from inflector import Inflector
from collections import OrderedDict

bigrams = join_bigrams.bigramas()

with open('data/search_data.txt', 'r') as data_file:
    data = eval(data_file.read())

def get_match_level(query_word, row):
    for level in range(3):
        for column in consts.SEARCH_COLUMNS[level]:
            for word in row[column + '_processed']:
                if query_word == word:
                    return level
    return consts.NOT_FOUND

def get_search_results(query, data, exact_match = False):
    query = join_bigrams.bigramar(query, bigrams)
    query = [query] if exact_match else query.split()
    results = [[], [], []]
    for row in data:
        query_match_level = 0
        for query_word in query:
            search_list = [query_word] if exact_match else [query_word, Inflector.pluralize(query_word), Inflector.singularize(query_word)]
            word_match_level = consts.NOT_FOUND
            for word in search_list:
                word_match_level = min(word_match_level, get_match_level(word, row))
            query_match_level = max(query_match_level, word_match_level)
        if query_match_level != consts.NOT_FOUND:
            results[query_match_level].append(row)
    return results[0] + results[1] + results[2]

while True:
    query = join_bigrams.bigramar(input().lower(), bigrams)
    results = get_search_results(query, data, False)
    print('Found %d matches:' % len(results))
    for result in results:
        print('%s: %s' % (result['nome_completo'], result['titulo_em_portugues']))
