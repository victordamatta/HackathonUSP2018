import sys
sys.path.append('scripts/')

from flask import Flask, jsonify, request
from search import get_search_results


app = Flask(__name__)

@app.route("/")
def index():
    return "Oi"

# GET /lista
@app.route('/lista/<string:search>')
def lista(search):
#    return jsonify({'autor': 'lista', 'titulo': 'aaa aaa aaa'})
    return search


# GET /grafo
@app.route('/grafo/<string:search>')
def grafo(search):
#    return jsonify({'autor': 'grafo', 'titulo': 'aaa aaa aaa'})
    return search

# GET /search
@app.route('/search/<string:query>')
def search(query):
    return get_search_results(query)

if __name__ == '__main__':
    app.run(debug=True)
