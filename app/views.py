# from flask import jsonify
from flask import render_template

from app import app
from app import process_data


@app.route('/')
def index():
    return render_template("Welcome to CryptoSite")


@app.route('/cryptoSymbol/<cryptoSymbol>', methods=['GET'])
def cryptoSymbol(cryptoSymbol):
    return render_template("index.html", data=process_data.process(cryptoSymbol))
