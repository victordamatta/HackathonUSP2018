
from flask import Flask, jsonify, request

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

if __name__ == '__main__':
    app.run(debug=True)
