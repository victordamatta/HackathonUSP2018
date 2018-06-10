# HackathonUSP2018

## INSTALAÇÃO

#### 1. Clonar o repositório

#### 2. Instalar pip

$ sudo python -m pip install -U pylint

#### 3. Instalar Flask

$ pip3 install flask

#### 4. Instalar nltk

$ pip3 install nltk

$ python3

    >>> import nltk

    >>> nltk.download()

    Downloader> d

#### 5. localhost

$ flask run

ou

$ python3 server/poswebserver.py

## API

#### Request para Lista de publicações

Requisição para obter a lista de publicações relacionadas a SUA_PESQUISA

GET localhost:500/server/SUA_PESQUISA

#### Response para Lista de publicações
[
    {
        "file": "string",
        "area_do_conhecimento": "string",
        "autor": "string",
        "banca_examinadora": "string",
        "data_de_defesa": "string",
        "data_de_publicacao": "string",
        "documento": "string",
        "doi": "string",
        "imprenta": "string",
        "nome_completo": "string",
        "orientador": "string",
        "palavras_chave_em_ingles": "string",
        "palavras_chave_em_portugues": "string",
        "resumo_em_ingles": "string",
        "resumo_em_portugues": "string",
        "titulo_em_ingles": "string",
        "titulo_em_portugues": "string",
        "unidade_da_usp": "string",
        "v1": "string",
        "e_mail": "E-mail",
        "data_de_liberacao": "string",
        "palavras_chave_em_espanhol": "string",
        "resumo_em_espanhol": "string",
        "titulo_em_espanhol": "string",
        "palavras_chave_em_frances": "string",
        "resumo_em_frances": "string",
        "titulo_em_frances": "string"
    },
    {
        ...
    },
    ...
]

#### Request para Grafo

Requisição para obter o grafo relacionado a SUA_PESQUISA

#### Response para Lista de publicações

 {
     ...
 }

