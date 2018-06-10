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
