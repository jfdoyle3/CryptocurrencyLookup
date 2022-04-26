from flask import jsonify

from app import app
from app import process_data


@app.route('/')
def index():
    return "Welcome to CryptoSite"


@app.route('/cryptoSymbol/<cryptoSymbol>', methods=['GET'])
def cryptoSymbol(cryptoSymbol):
    return jsonify(process_data.process(cryptoSymbol))
