import csv, re
from inflector import Inflector

# Primary result: matches only title
# Secondary result: matches title and keywords
# Tertiary result: matches everything
    
SEARCH_COLUMNS = [['titulo_em_portugues',
                   'titulo_em_ingles',
                   'titulo_em_espanhol',
                   'titulo_em_frances'],
                      
                  ['palavras_chave_em_portugues',
                   'palavras_chave_em_ingles',
                   'palavras_chave_em_espanhol',
                   'palavras_chave_em_frances'],
                  
                  ['resumo_em_portugues',
                   'resumo_em_ingles',
                   'resumo_em_espanhol',
                   'resumo_em_frances']]
NOT_FOUND = 100

def preprocess(row):
    for level in range(3):
        for column in SEARCH_COLUMNS[level]:
            row[column + '_processed'] = re.split('[\s.,;"\'!()?]', row[column].lower())
    return row

with open('../data/compsci_com_cc_e_resumo.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    data = []
    for row in spamreader:
        data.append(preprocess(row))


def get_match_level(query_word, row):
    for level in range(3):
        for column in SEARCH_COLUMNS[level]:
            for word in row[column + '_processed']:
                if query_word == word:
                    return level
    return NOT_FOUND

def get_search_results(query, data, exact_match):    
    query = [query] if exact_match else query.split()
    results = [[], [], []]
    for row in data:
        query_match_level = 0
        for query_word in query:
            search_list = [query_word] if exact_match else [query_word, Inflector.pluralize(query_word), Inflector.singularize(query_word)]
            word_match_level = NOT_FOUND
            for word in search_list:
                word_match_level = min(word_match_level, get_match_level(word, row))
            query_match_level = max(query_match_level, word_match_level)
        if query_match_level != NOT_FOUND:
            results[query_match_level].append(row)
    return results[0] + results[1] + results[2]

while True:
    query = input()
    results = get_search_results(query.lower(), data, False)
    print('Found %d matches:' % len(results))
    for result in results:
        print('%s: %s' % (result['nome_completo'], result['titulo_em_portugues']))
