import csv, re, join_bigrams, consts, json

bigrams = join_bigrams.bigramas()

def preprocess(row):
    for level in range(3):
        for column in consts.SEARCH_COLUMNS[level]:
            row[column + '_processed'] = re.split('[\s.,;"\'!()?]',
                                                  join_bigrams.bigramar(row[column].lower(), bigrams))
    return row

with open('data/compsci_com_cc_e_resumo.csv') as csvfile:
    print('Preprocessing...')
    spamreader = csv.DictReader(csvfile)
    data = []
    for row in spamreader:
        data.append(preprocess(row))
    f = open('data/search_data.txt', 'w')
    f.write(json.dumps(data))
    print('done!')
